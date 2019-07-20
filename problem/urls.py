from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='problems'),
    path('<int:problem_id>/', views.problem, name='problem')
]
