from django.urls import path
from . import views

urlpatterns = [
    path("user/profile/", views.profile, name="profile"),
    path("user/<username>/", views.user, name="user"),
    path("hello/<string>", views.hello, name="hello")
]