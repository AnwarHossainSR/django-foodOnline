from django.urls import path

from . import views

urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashbord/', views.dashbord, name='dashbord'),
    path('forgot_password/', views.forgotPassword, name='forgotPassword'),
]