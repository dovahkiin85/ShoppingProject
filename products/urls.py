from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/add', views.addProducts, name='addProducts'),
    path('products/edit', views.editProducts, name='editProducts'),
    path('products/edit/<int:id>/', views.edit_post, name='product-edit'),

]