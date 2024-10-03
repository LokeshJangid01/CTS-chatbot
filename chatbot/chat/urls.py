from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Chat interface
    path('get_response/', views.get_response, name='get_response'),  # Bot response
]
