from django.shortcuts import render
from django.http import HttpResponse
from .models import Images,Location,Category

# Create your views here.
def landingpage(request):
   
    return render(request, 'gallery/home.html')

def gallery(request):
    pictures = Images.get_all()
    location = Location.get_all()
   
    return render(request, 'gallery/gallery.html')

def location(request,locale):
    images = Images.filter_by_location(locale)
    return render (request, 'location.html', {'results': images})


