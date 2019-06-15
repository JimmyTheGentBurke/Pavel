from django.shortcuts import render
def index(request):
    return render(request, 'vedmed/home.html')
def contact(request):
    return render(request, 'vedmed/basic.html', {'values':['Звоните по телефну', '911']})


# Create your views here.
