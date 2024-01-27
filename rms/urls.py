"""
URL configuration for rmshotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rmsapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.home,name='login'),
    path('accountsreport',views.account, name='accountsreport'),
    path('registration', views.registration,name='registration' ),
    path('hotelbooking', views.hotelbooking, name='hotelbooking'),
    path('hotelreport', views.hotelreport, name='hotelreport'),
    path('roommaintenance/', views.roommaintenance, name='roommaintenance'),
    path('roomcancellation/', views.roomcancellation, name='roomcancellation'),
    path('reception/', views.reception, name='reception'),
    path('bar/', views.bar, name='bar'),
    path('bill/', views.bill, name='bill'),
    path('foodreport', views.food, name='foodreport'),
    path('Food_Mastry/', views.Food_Mastry, name='Food_Mastry'),
    path('dining/', views.dining, name='dining'),
    path('parcel/', views.parcel, name='parcel'),
    path('online/', views.online, name='online'),
    path('Expenses_Entry/', views.Expenses_Entry, name='Expenses_Entry'),
    path('Groceries_Entry/', views.Groceries_Entry, name='Groceries_Entry'),
    path('Gas_Maintenance/', views.Gas_Maintenance, name='Gas_Maintenance'),
    path('Income_Entry/', views.Income_Entry, name='Income_Entry'),
    path('Advertisement/', views.Advertisement, name='Advertisement'),
    path('workersapplication/', views.workersapplication, name='workersapplication'),
    path('veseelmaintenance/', views.veseelmaintenance, name='veseelmaintenance'),
    path('workersattendance/', views.workersattendance, name='workersattendance'),
    path('workerssalary/', views.workerssalary, name='workerssalary'),
    path('stockentry/', views.stockentry, name='stockentry'),
    path('Parking/', views.Parking, name='Parking'),
    path('log', views.home, name='Login_Page'),
    path('signin/', views.signin, name='signin'),
    
    path("",auth_views.LoginView.as_view(template_name='signin.html'),name="Login"),
    path("login/",auth_views.LoginView.as_view(template_name='signin.html'),name="Logout"),
    path('register/',views.reg,name="Register"), 
]
