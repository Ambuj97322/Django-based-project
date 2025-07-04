"""
URL configuration for rms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from myapp import views
# urlpatterns = [
#     path('hello',views.app),
#     path('dyn_res/<str:string>',views.dynamic_response),
#     path('fact/<int:no>',views.factvw),
#     path('length/<str:string>',views.length),
#     path('find/<str:string>/<str:char>',views.find),
#     path('index/<int:a>',views.indexvw),
#     path('a',views.avw),
# ]

from django.urls import path
from myapp import views
urlpatterns = [
   path('index',views.indexVw,name='index'),
   path('contact',views.ContactVw,name='contact'),
]
