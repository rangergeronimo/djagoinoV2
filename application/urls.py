from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.chart, name='chart'),
    path('sensor/', views.sensor, name='sensor'),
    path('api/sensor/', views.SensorList.as_view(), name='list'),
    path('api/sensor/<int:pk>/', views.SensorDetail.as_view(), name='detail'),
]
