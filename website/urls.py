from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('info/', views.account_info, name='info'),
    path('method/', views.payment_method, name='payment_method'),
    path('success/', views.success, name='success'),
]