from django.shortcuts import render
from django.shortcuts import render

# Create your views here.


def login(req):
    print("tet---")
    print(req.method)
    if req.method == "POST":
        print(req.POST.get("username"))
    return render(req, "login.html")


def signup(req):
    return render(req, "signup.html")


def forgetPassword(req):
    return render(req, "forgetPassword.html")


def index(req):
    return render(req, "index.html")


def profile(req):
    return render(req, "profile.html")


def exam(req):
    return render(req, "exam.html")


def candidate(req):
    return render(req, "candidate.html")


def question(req):
    return render(req, "question.html")


def result(req):
    return render(req, "result.html")


def setting(req):
    return render(req, "setting.html")


def about(req):
    return render(req, "about.html")
