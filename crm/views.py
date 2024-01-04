from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .models import Lead


def home(request):
    leads = Lead.objects.all()

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
        return render(request, template_name, {'leads': leads})


def logout_user(request):
    logout(request)
    message = 'Вы успешно покинули систему'
    messages.success(request, message)
    return redirect('home')


def register_user(request):
    template_name = 'crm/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)

            message = 'Вы успешно зарегистрировались'
            messages.success(request, message)

            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, template_name, {'form': form})
