
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dojo_table', views.dojo_table),
    path('ninja_table', views.ninja_table),
]