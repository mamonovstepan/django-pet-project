from django.shortcuts import render


def home(request):
    template_name = 'crm/home.html'
    context = {
        'title': 'CRM-Система',
        'text': 'just a text'
    }
    return render(request, template_name, context)
