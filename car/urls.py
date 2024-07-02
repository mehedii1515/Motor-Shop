from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddCarCreateView.as_view(), name='add_car'),
    path('edit/<int:id>/', views.EditCarView.as_view(), name='edit_car'),
    path('delete/<int:id>/', views.DeleteCarView.as_view(), name='delete_car'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car'),
]