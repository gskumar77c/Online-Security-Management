from django.urls import path,include
from .import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('set_up/',views.set_up,name='set_up'),
    path('schedule',views.schedule_duties,name='schedule-duties'),
    
    
]


