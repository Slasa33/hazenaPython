"""hazena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import HazenaIS.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kluby/',HazenaIS.views.kluby, name='kluby'),
    path('soupiska/<int:klub_id>',HazenaIS.views.soupiska, name='soupiska'),
    path('zapasy/',HazenaIS.views.zapasy, name='zapasy'),
    path('zapasydetail/<int:zapasy_id>',HazenaIS.views.zapasydetail, name='zapasydetail'),
    path('soupiska/<int:hrac_id>/edit',HazenaIS.views.hrac_edit, name='hrac_edit'),
    path('kluby/add',HazenaIS.views.klub_add, name='klub_add'),
    path('zapasy/add',HazenaIS.views.zapasy_add, name='zapasy_add'),
    path('tabulka/',HazenaIS.views.tabulka, name='tabulka'),
    path('hraci/',HazenaIS.views.hraci, name='hraci'),
    path('hraci/add',HazenaIS.views.hraci_add, name='hraci_add'),
    path('kariera/',HazenaIS.views.kariera, name='kariera'),
    path('rozhodci/',HazenaIS.views.rozhodci, name='rozhodci'),
    path('soupiska/<int:hrac_id>/delete',HazenaIS.views.end_kariera, name='kariera_delete'),
]
