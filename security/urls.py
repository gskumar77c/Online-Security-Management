from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('',auth_views.LoginView.as_view(template_name='security/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='security/logout.html'),name='logout'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('home/',include('allotment.urls'))
    
]


