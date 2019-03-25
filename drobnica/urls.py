from django.urls import path
from . import views

urlpatterns = [
    path('opakowania/', views.package_list, name = 'package_list'),
    path('consignees/', views.consignee_list, name = 'consignee_list'),
    path('order/<int:pk>/', views.order_detail, name = 'order_detail'),
    path('order/new/', views.order_new, name = 'order_new'),
    path('order/<int:pk>/edit', views.order_edit, name = 'order_edit'),
]