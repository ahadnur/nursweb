from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='problems'),
    path('add/', views.add_problem, name='add_problem'),
    path('<int:problem_id>/', views.problem, name='problem')
]
