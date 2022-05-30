from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landingpage(request):
    html = '<h1>Home</h1>'
    return HttpResponse(html)
