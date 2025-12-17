from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('about/', views.about, name='about'),
]