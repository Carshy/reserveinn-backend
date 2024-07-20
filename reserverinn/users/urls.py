from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RegisterViewSet, LoginView, LogoutViewSet, ProfileViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'registers', RegisterViewSet, basename='registers')
router.register(r'profiles', ProfileViewSet)
router.register(r'logout', LogoutViewSet, basename='logout')

urlpatterns = [
  path('', include(router.urls)),
  path('login/', LoginView.as_view(), name='token_obtain_pair'),
  path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
