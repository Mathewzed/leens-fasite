from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('order/<int:product_id>/', views.order, name='order'),
    path('rate/<int:product_id>/', views.rate_product, name='rate_product'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]