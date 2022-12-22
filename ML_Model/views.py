from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')