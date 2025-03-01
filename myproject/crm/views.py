from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import myform  # Adjust according to your model import


def register(request):
    if request.method == "POST":
        # Getting data from the body
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if the email already exists
        if myform.objects.filter(Email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")  # Redirect to the register page

        try:
            # Hash the password using Django's built-in hashing function
            hashed_password = make_password(password)

            # Create the user object and save it
            user = myform(
                Uname=uname, Email=email, Password=hashed_password
            )  # Store the hashed password
            user.save()

            messages.success(request, "Registration successful. Please log in.")
            return redirect("login")  # Redirect to the login page after registration

        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, "An error occurred during registration.")
            return redirect(
                "register"
            )  # Redirect back to the registration page in case of error

    return render(request, "crm/register.html")


def login(request):
    if request.method == "POST":
        # Getting data from the body
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if the email exists
        try:
            user = myform.objects.get(Email=email)  # Fetch the user by email

            # Use Django's check_password function to verify the entered password
            if check_password(password, user.Password):
                # Password is correct, redirect to the homepage or dashboard

                return HttpResponse(
                    f"Welcome! {user.Uname}"
                )  # Replace with your actual homepage URL or dashboard

            else:
                # Password is incorrect
                messages.error(request, "Invalid password")
                return redirect("login")

        except myform.DoesNotExist:
            # User not found
            messages.error(request, "Email not registered")
            return redirect("/register")

    return render(request, "crm/login.html")  # The login page template
