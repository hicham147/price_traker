from django.contrib import admin
from django.urls import path
from . import views
from .views import ihrab_update_prices,amazon_update_prices,nicone_update_prices,AmazonDeleteViwes

urlpatterns = [
    path('',views.home,name='home-app'),
    path('About',views.about,name='about-app'),
    path('ihreb/',views.ihreb,name='ihreb'),
    path('nicone/',views.nicone,name='nicone'),
    path('amazon/',views.amazon,name='amazon'),
    path('xcite/',views.xcite,name='xcite'),
    path('update/',views.ihrab_update_prices,name='update-prices'),
    path('update_price/',views.amazon_update_prices,name='amazon-update-prices'),
    path('update_prices/',views.nicone_update_prices,name='niceone-update-prices'),
    path('update_prices/',views.xcite_update_prices,name='xcite-update-prices'),

]
