from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls', namespace='app')),
]

urlpatterns += [
    path('api/sensor/auth/', include('rest_framework.urls')),
]
