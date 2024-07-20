from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from .models import Profile

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
    )
  
  password = serializers.CharField(
    required=True,
    write_only=True,
    validators=[validate_password]
    )
  
  password2 = serializers.CharField(required=True, write_only=True)
  
  class Meta:
    model = User
    fields = ['id', 'username', 'password', 'password2', 'email', 'first_name', 'last_name']

    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True},
    }
  
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError({"password": "Password fields didn't Match!"})
    return attrs
  
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
    )

    user.set_password(validated_data['password'])

    user.save()

    return user


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class ProfileSerializer(serializers.ModelSerializer):

  class Meta:
    model = Profile
    fields = ['id', 'bio', 'profile_picture', 'created_at', 'updated_at', 'user']
    read_only_fields = ['user', 'created_at', 'updated_at']
  
  def create(self, validated_data):
    user = self.context['request'].user
    validated_data['user'] = user
    return Profile.objects.create(**validated_data)