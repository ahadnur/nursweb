from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='posts'),
    path('<slug:slug_text>/', views.post, name='post'),
]
