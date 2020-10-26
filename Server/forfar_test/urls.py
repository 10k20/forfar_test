from django.contrib import admin
from django.urls import path, include
from checks import views

api_patterns = [
    path('', include('checks.urls')),
]

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
]