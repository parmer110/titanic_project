from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:id>/edit/', views.post_update, name='post_update'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),
]
