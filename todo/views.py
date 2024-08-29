from django.shortcuts import render, redirect
from .models import Todo
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages

# Create your views here.
@csrf_protect
def todo_view(request):
    if request.method == "POST":
        item = request.POST.get("item")
        if item.strip() == "":
            messages.error(request, "Todo Field cannot be empty!")
            return redirect("todo")
        Todo.objects.create(title=item)
        # new_todo = Todo(title=item)
        # new_todo.save()
        messages.success(request, "Todo list added successfully!")
        return redirect("todo")
    todo_list = Todo.objects.all()
    context = {
        "todo_list": todo_list,
        "count": todo_list.count()
    }
    return render(request, "todo.html", context)

@csrf_protect
def delete_todo(request, id):
    if request.method == "POST":
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            messages.success(request, f"{todo.title} deleted successfully")
            return redirect("todo")
        except Exception as e:
            messages.error(request, f"Error occured: {e}")
            return redirect("todo")
    else:
        return HttpResponseBadRequest(f"Method {request.method} not allowed.")
    
    
@csrf_protect
def mark_done(request, id):
    if request.method == "POST":
        try:
            todo = Todo.objects.get(id=id)
            if(todo.done == True):
                  todo.done = False
                  todo.save()
            else:
                todo.done = True
                todo.save()
            messages.success(request, f"{todo.title} mark successfully")
            return redirect("todo")
        except Exception as e:
            messages.error(request, f"Error occured: {e}")
            return redirect("todo")
    else:
        return HttpResponseBadRequest(f"Method {request.method} not allowed.")

@csrf_protect 
def todo_edit(request, id):
    context =''
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=id)
            context = todo.title
            return render(request, 'todo_edit.html', {
                'title' : context,
                 "id": id
            })
        except Exception as e:
            return HttpResponse('Error gettin the task')
    elif request.method =='POST':
        try:
            todo = Todo.objects.get(id = id)
            todo.title  = request.POST.get('title')
            if todo.title.strip() == "":
                messages.error(request, "Todo Field cannot be empty!")
                return redirect("edit_todo", id)
            todo.save()
            messages.success(request, f"{todo.title} updated successfully")
            return redirect('todo')
        except Exception as e:
            messages.error(request, f"Error occured: {e}")
            return redirect('edit_todo', id)
