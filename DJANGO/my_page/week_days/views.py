from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def monday (request,):
    return HttpResponse('1. Бегит <br>2. Анжианя')

def tuesday (request,):
    return HttpResponse('1. Прес качат <br>2. Бегит')