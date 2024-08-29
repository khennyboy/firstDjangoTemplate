from django.urls import path
from .views import *

urlpatterns = [
    path("", todo_view, name="todo"),
    path("<int:id>/delete/", delete_todo, name="delete_todo"),
    path("<int:id>/update/", mark_done, name="update_todo"),
    path("<int:id>/edit/", todo_edit, name='edit_todo')
]