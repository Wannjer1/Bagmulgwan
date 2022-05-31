from django.urls import path 
from gallery_app.views import landingpage,gallery
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',landingpage, name='home'),
    path('gallery/', gallery, name="gallery"),
    # path('location/(?P<locale>\w+)/', gallery, name='location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)