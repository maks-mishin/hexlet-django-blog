from django.contrib import admin
from django.urls import path
from hexlet_django_blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('', views.index, name='index')
]
