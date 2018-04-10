from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ourwork/',views.ourwork,name='ourwork'),
    path('testimonials/',views.testimonials,name='testimonials'), 
    path('projects/',views.projects,name='projects'), 
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
]