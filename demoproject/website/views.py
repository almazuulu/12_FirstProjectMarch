from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = "Askar"
    title = "Домашняя страница"
    age = 10
    list_pages = ['О Нас', 'Контакты', 'Логин', 'Выход']
    
    
    context = {
        'nametemp': name, 
        'titlenews': title, 
        'pages': list_pages, 
        'age': age}
    #return render(request, 'website/index.html', context={'nametemp': name, 'titlenews': title, 'pages': list_pages, 'age': age})
    return render(request, 'website/index.html', context)

def about_us(request):
    addresses = {
        'filial 1': 'Чуй 123',
        'filial 2': 'Чуй 66',
        'filial 3': 'Чуй 45',
    }
    
    context = {
        'addresses': addresses,
    }
    
    
    
    return render(request, 'website/about.html', context)

def contact_us(request):
    return render(request, 'website/contact.html')
    
