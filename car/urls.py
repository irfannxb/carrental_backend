from django.urls import path, include

from .views import CarViewSet

urlpatterns = [
    path(
        'cars/', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car-list'),
    path('cars/<int:pk>/',
         CarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='car-detail'),
    path('cars/by-user/<int:user_id>/',
         CarViewSet.as_view({'get': 'by_user'}), name='car-by-user'),
]
