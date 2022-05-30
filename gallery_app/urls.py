from django.contrib import path 
from gallery_app.views import landingpage

urlpatterns = [
    path('', landingpage, name='home'),
]