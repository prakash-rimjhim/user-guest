from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('user-list/', views.user_list, name="user-list"),
    path('user-create/', views.user_create, name="user-create"),
    path('user-update/<str:pk>/', views.user_update, name="user-update"),
    path('user-delete/<str:pk>/', views.user_delete, name="user-delete"),
]