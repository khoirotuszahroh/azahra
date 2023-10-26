from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def h1(request)
    template = loader.get_template('h1.html')
    return HttpResponse(template.render())
def h2(request)
    template = loader.get_template('h2.html')
    return HttpResponse(template.render())


# 
