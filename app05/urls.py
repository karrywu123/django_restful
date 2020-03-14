from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('users/', views.user_list, name='user-list'),
    path('carts/', views.CartView.as_view(), name='cart-list'),
    path('login/',views.LoginView.as_view(),name='login')

]