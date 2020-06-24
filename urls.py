"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .import views
from .import one


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyze',views.analyze,name='analyze'),
    path('AboutUs/',views.AboutUs,name='AboutUs'),
    path('ContactUs/',views.ContactUs, name='ContactUs'),

   # path('about/',views.about,name='about'),
    #path('one/',one.one,name='one'),
    #path('ones/',one.ones,name='ones'),
    #path('personal/',views.personal, name = 'personal'),
    #path('personals/',views.personals, name = 'personals'),
]
