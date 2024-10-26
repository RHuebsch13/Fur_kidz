from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),  # Ensure this line is present
]
