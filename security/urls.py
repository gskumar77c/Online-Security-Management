from django.contrib import admin
from django.urls import path,include
from .import views as sec_views

urlpatterns = [
    #path('admin/', admin.site.urls),
   path('',sec_views.home)
]
