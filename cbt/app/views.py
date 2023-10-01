from django.shortcuts import render
from django.shortcuts import render

# Create your views here.


def login(req):
    print("tet---")
    print(req.method)
    if req.method == "POST":
        print(req.POST.get("username"))
    return render(req, "login.html")


def singup(req):
    return render(req, "singup.html")


def forgetPassword(req):
    return render(req, "forgetPassword.html")
