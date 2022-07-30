from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about_us/', views.about_us),
    path('our_solutions/', views.our_solutions),
    path('our_products/', views.our_products),
    path('our_clients/', views.our_clients),
    path('blogs/', views.blogs),
]
