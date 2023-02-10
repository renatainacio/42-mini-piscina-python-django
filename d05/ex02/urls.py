from django.urls import path

from . import views

urlpatterns = [
    path('ex02/init/', views.init, name='init'),
    path('ex02/populate/', views.init, name='populate'),
    path('ex02/display/', views.init, name='display'),
]