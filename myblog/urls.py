from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('posts/', include('posts.urls')),
    path('programming/', include('programming.urls')),
    path('problems/', include('problem.urls')),
]

handler404 = 'pages.views.error_404_view'
