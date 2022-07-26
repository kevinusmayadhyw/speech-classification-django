from django.urls import path

from . import views

app_name = 'tugasdua_1301194011'

urlpatterns = [
    path('', views.index, name='index'),
]