from rest_framework import viewsets, status
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Profile
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action

from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class RegisterViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer
  permission_classes = [AllowAny]

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

class ProfileViewSet(viewsets.ModelViewSet):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class LogoutViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token or token expired."}, status=status.HTTP_400_BAD_REQUEST)
