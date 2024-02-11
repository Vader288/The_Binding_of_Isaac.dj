

from django.urls import path
from . import views


urlpatterns = [

    path('', views.category),
    path('azazel/', views.category_1),
    path('3dkub/', views.kub),
    path('isaac/<int:cat_id>/', views.category_2),
    path('magdalene/', views.category_3),
    path('cain/<slug:cat_slug>/', views.category_slug),
    path('keeper/', views.category_4),
    path('lilith0/', views.category_5),
    path('lilith1/', views.category_5_1),



]
