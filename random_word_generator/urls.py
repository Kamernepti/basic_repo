from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_word),
    path('reset', views.reset)
]