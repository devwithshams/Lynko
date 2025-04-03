from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  # Use cleaned_data for password
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/dashboard/')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})
