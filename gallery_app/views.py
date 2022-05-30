from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landingpage(request):
   
    return render(request, 'gallery/home.html')

def landingpage2(request):
   
    return render(request, 'gallery/gallery.html')


