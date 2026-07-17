
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.home, name='home'),
    path("download-pdf/", views.download_pdf, name="download_pdf"),
    path(
    "send-email/",
    views.send_pdf_email,
    name="send_pdf_email",
    
),
    path('download/jpeg/', views.download_jpeg, name='download_jpeg'),
    path('privacy-policy/', TemplateView.as_view(template_name='privacy-policy.html'), name='privacy_policy'),
]