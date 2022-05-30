from django.urls import path 
from gallery_app.views import landingpage

urlpatterns = [
    path('gallery/', landingpage, name="landingpage"),
]