from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('info/<int:record_id>/', views.account_info, name='info'),
    path('method/', views.payment_method, name='payment_method'),
    path('success/', views.success, name='success'),
]