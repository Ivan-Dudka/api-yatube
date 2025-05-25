from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]
