from django.contrib import admin
from django.urls import path, include
from django.conf.urls import *
from wkhtmltopdf.views import PDFTemplateView
from checks import views

api_patterns = [
    path('', include('checks.urls')),
]

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
    url(r'^pdf/$', PDFTemplateView.as_view(template_name='my_template.html',
                                           filename='my_pdf.pdf'), name='pdf'),
]