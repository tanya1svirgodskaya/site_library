
from django.contrib import admin
from django.conf.urls import include,url


urlpatterns = [
    # Examples:
   url(r'^', include('TNBooks.urls')),
    url(r'^admin/', admin.site.urls),
   
]
