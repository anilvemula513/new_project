from django.urls import path
from . import views

urlpatterns = [
    path('', views.static_page, name='static_page'),
]