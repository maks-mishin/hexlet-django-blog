from django.urls import path

from categories import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='categories_index'),
    path('<int:id>/', views.CategoryView.as_view(), name='categories_detail'),
    path('create/', views.CategoryFormCreateView.as_view(), name='categories_create'),
]
