from django.urls import path     
from . import views
urlpatterns = [
    path('admin/admin-page/add-item/', views.add_item),
    path('admin/admin-page/edit-item/<int:item_id>/', views.edit_item, name="edit_item"),
    path('admin/admin-page/edit-item/<int:item_id>/update-item/<int:same_item_id>/', views.update_item),
    path('admin/admin-page/delete-item/<int:id>/', views.delete_item),
    path('marketplace/buy-items/<int:item_id>/<int:user_id>/', views.buy_items),
    path('admin/admin-page/add-category/', views.add_category)
]
