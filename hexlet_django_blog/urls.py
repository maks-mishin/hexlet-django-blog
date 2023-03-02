from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('articles/', include('articles.urls')),
    path('categories/', include('categories.urls')),
    path('', views.index, name='index')
]
