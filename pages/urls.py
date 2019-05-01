from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('comment-policy/', views.comment_policy, name='comment-policy'),
]
