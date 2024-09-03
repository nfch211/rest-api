from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import datetime
import pytz
from res_api import models

class NickSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'ProductName', 'ProductDescription', 'ProductCategory', 'ProductPrice', 'ProductLink')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        # Define the Hong Kong timezone
        hong_kong_tz = pytz.timezone('Asia/Hong_Kong')

        # Get the current UTC time and convert it to Hong Kong time
        created_at_utc = datetime.utcnow()
        created_at_hk = created_at_utc.replace(tzinfo=pytz.utc).astimezone(hong_kong_tz)

        # Calculate the expiration time and convert it to Hong Kong time
        expires_at_utc = created_at_utc + refresh.access_token.lifetime
        expires_at_hk = expires_at_utc.replace(tzinfo=pytz.utc).astimezone(hong_kong_tz)

        data['token_info'] = {
            'created_at': created_at_hk.isoformat(),
            'expires_at': expires_at_hk.isoformat()
        }
        return data
