from django.urls import path
from . import views

urlpatterns = [
    path('api/routes/', views.getRoutes, name='routes'),
    path('api/list/', views.getList, name='list'),
    path('api/note/<pk>', views.getNote, name='note'), 
    path('api/create/', views.addNote, name='add')
]
