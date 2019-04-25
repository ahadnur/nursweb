from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='programming'),
    path('<int:program_id>/', views.programming_post, name='programming_post'),
]
