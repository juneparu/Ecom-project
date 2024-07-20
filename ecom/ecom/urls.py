from django.contrib import admin
<<<<<<< HEAD
from django.urls import path ,include
from . import settings
=======
from django.urls import path ,include 
from django.conf import settings
>>>>>>> f5d05fd35d7a467215f6d2e0008bbd1bf1f7dbd2
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
<<<<<<< HEAD

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
>>>>>>> f5d05fd35d7a467215f6d2e0008bbd1bf1f7dbd2

