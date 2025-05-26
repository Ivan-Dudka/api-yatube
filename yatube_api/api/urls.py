from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet


v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(
    r'posts/(?P<id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

v1_urls = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(v1_router.urls)),
]

urlpatterns = [
    path('v1/', include(v1_urls)),
]
