from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='programming'),
    path('python/', views.python, name='python'),
    path('python/<int:python_id>/', views.python_post, name='python_post'),
    path('<int:program_id>/', views.programming_post, name='programming_post'),
]
