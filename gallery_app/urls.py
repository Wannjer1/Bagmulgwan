from django.urls import path 
from gallery_app.views import landingpage,landingpage2

urlpatterns = [
    path('',landingpage, name='home'),
    path('gallery/', landingpage2, name="home"),
]