from django.urls import path

from articles import views

urlpatterns = [
    path('/<str:tags>/<int:article_id>', views.index, name='article'),
]
