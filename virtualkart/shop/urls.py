from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  
  path('shop/', views.shop, name='shop'),
  path('shop/<slug:category_slug>/', views.shop, name='products_by_category'),
  path('shop/<slug:category_slug>/<slug:sub_category_slug>/', views.shop, name='products_by_sub_category'),
  path('shop_filter/', views.shop, name='shop_filter'),
  path('shop_price_sort/', views.shop, name='shop_price_sort'),
  path('shop_name_sort/', views.shop, name='shop_name_sort'),


  
  path('shop/<slug:category_slug>/<slug:sub_category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),
  
  path('price_change/', views.price_change, name='price_change'),
  
  
  path('search/', views.search, name='search'),
  
  path('sub_category/', views.sub_category, name='sub_category'),
  
  path('contact/', views.contact, name='contact'),
]