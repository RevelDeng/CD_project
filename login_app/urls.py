from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('add-user/', views.add_user),
    path('login/', views.login),
    path('marketplace/logout/', views.logout),
    path('marketplace/', views.marketplace, name="marketplace"),
    path('admin/', views.admin_index, name="admin_index"),
    path('admin/add-admin/', views.add_admin),
    path('admin/admin-login/', views.admin_login),
    path('admin/admin-page/', views.admin_page, name="admin_page"),
    path('admin/admin-page/admin-logout/', views.admin_logout)
]
