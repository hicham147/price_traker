"""amazon_price_tarker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp.views import AmazonDeleteViwes,NiceonedeletViews,IhrebdeletViews,XcitedeletViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path("amazon/delete/<int:pk>/",AmazonDeleteViwes.as_view(),name='amz-dell'),
    path("nicone/delete/<int:pk>/",NiceonedeletViews.as_view(),name='nic-dell'),
    path("ihreb/delete/<int:pk>/",IhrebdeletViews.as_view(),name='ihr-dell'),
    path("xcite/delete/<int:pk>/",XcitedeletViews.as_view(),name='xci-dell'),


    
]
