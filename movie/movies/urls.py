"""
URL configuration for movie project.

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

from django.urls import path
from movies import views
app_name='movies'

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('add1/',views.add1,name='add1'),
    path('mdetails/<int:p>',views.mdetails,name='mdetails'),
    path('editmoviebyid/<int:p>',views.editmoviebyid,name="editmoviebyid"),
    path('deletemoviebyid/<int:p>',views.deletemoviebyid,name="deletemoviebyid"),


]

