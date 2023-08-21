"""rentals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from offerspage.views import *
from indexpage.views import *
from indexloginpage.views import *
from aboutpage.views import *
from contactpage.views import *
from leasepage.views import *
from registrationpage.views import *
from bikeselection.views import *
from availability.views import *
from loginPage.views import *
from fleetpage.views import *
from reservation.views import *
from payment.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('offerspage/',offerspage),
    path('indexpage/',indexpage),
    path('indexloginpage/',indexloginpage),
    path('aboutpage/',aboutpage),
    path('contactpage/',contactpage),
    path('leasepage/',leasepage),
    path('registrationpage/',registrationpage),
    path('availability/',availability, name='availability'),
    path('loginPage/',loginPage),
    path('fleetpage/',fleetpage),
    path('bikeselection/', bikeselection, name='bikeselection'),
    path('reservation/',reservation, name='reservation'),
    path('payment/',payment, name='payment')

]
