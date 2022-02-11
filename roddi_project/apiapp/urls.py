from rest_framework import routers
from . import views
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'status', views.StatusViewSet)
router.register(r'belonging', views.BelongingViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'estate', views.EstateViewSet)
router.register(r'comment', views.CommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

