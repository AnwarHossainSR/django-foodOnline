from django.shortcuts import render

# Create your views here.


def registerUser(request):
    return render(request, "accounts/registerUser.html")
