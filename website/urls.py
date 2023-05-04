from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('info/', views.account_info, name='info'),
    path('method/', views.method, name='method'),
    path('gcash/', views.gcash, name='gcash'),
    path('credit/', views.credit, name='credit'),
]