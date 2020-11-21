from django.urls import path
from . import views


urlpatterns = [

    path('homepage/', views.homepage),
    path('templates/', views.templates),
    path('value/', views.ginger),
    path('home/', views.Home_extends_base),
]