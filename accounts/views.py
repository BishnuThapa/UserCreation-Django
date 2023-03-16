from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def index(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "User created Successfully")
        return redirect('index')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'register.html', context)
