from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def w1(request)
    template = loader.get_template('w1.html')
    return HttpResponse(template.render())
def w2(request)
    template = loader.get_template('w2.html')
    return HttpResponse(template.render())
