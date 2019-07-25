from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='problems'),
    path('add/', views.add_problem, name='add_problem'),
    path('<slug:slug_text>/', views.problem, name='problem')
]
