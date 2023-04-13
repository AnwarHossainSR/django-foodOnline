from django.shortcuts import redirect
from django.shortcuts import render

from .forms import UserForm
from .models import User

# Create your views here.


def registerUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user with the form data

            # user = form.save(commit=False)
            # user.set_password(form.cleaned_data["password"])
            # user.role = User.CUSTOMER
            # user.save()

            # Create the user with crate_user method
            user = User.objects.create_user(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            user.role = User.CUSTOMER
            user.save()

            return redirect("registerUser")
        else:
            print(form.errors)
    else:
        form = UserForm()
    context = {"form": form}
    return render(request, "accounts/registerUser.html", context)
