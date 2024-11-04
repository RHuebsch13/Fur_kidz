from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('save-for-later/<int:product_id>/', views.save_for_later, name='save_for_later'),
    path('move-to-bag/<int:product_id>/', views.move_to_bag, name='move_to_bag'),
    path('remove-saved-item/<int:item_id>/', views.remove_saved_item, name='remove_saved_item'),
]