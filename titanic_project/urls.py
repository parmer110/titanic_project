from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('titanic/', include('titanic.urls')),
    path('api/', include('blog.urls')),
]
