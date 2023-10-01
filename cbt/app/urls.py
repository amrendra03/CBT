from django.urls import path

from app import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("forgetpassword/", views.forgetPassword, name="forgetpassword"),
    path("singup/", views.singup, name="singup"),
]
