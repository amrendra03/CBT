from django.urls import path

from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("forgetpassword/", views.forgetPassword, name="forgetpassword"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("exam/", views.exam, name="exam"),
    path("candidate/", views.candidate, name="candidate"),
    path("question/", views.question, name="question"),
    path("result/", views.result, name="result"),
    path("setting/", views.setting, name="setting"),
    path("about/", views.about, name="about"),
]
