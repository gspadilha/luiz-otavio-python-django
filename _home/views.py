# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):  # request é sempre obrigatório
    # return HttpResponse('Home!')
    return render(request, '_home/index.html')
