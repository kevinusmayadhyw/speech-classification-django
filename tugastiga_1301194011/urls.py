from django.urls import path

from . import views

app_name = 'tugastiga_1301194011'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('save/', views.save, name='save'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
]