from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            msg = f'Welcome {username}, your account is created.'
            messages.success(request, msg)
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
