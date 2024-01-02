from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    template_name = 'crm/home.html'
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            message = 'Вы успешно вошли в систему'
            messages.success(request, message)
            return redirect('home')
        else:
            message = 'Ошибка входа'
            messages.error(request, message)
            return redirect('home')
    else:
        return render(request, template_name)


def logout_user(request):
    pass
