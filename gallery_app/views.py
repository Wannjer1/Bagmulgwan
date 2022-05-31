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

# function to enable users to search by category
def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        res = Images.search_image(search_term)
        message = f'{search_term}'

        return render (request, 'gallery/search.html', {'message': message, 'results': res})
    
    else:
        message = 'You have not searched any term'
        return render(request, 'search.html', {'message':message})

def location(request,locale):
    '''Method to filter images by location'''
    images = Images.filter_by_location(locale)
    return render (request, 'location.html', {'results': images})


