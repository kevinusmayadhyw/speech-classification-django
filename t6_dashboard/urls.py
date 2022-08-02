from django.urls import path

from . import views

app_name = 't6_dashboard'

urlpatterns = [
    path('', views.index, name='index'),
]