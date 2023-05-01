from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('info/', views.account_info, name='info'),
]