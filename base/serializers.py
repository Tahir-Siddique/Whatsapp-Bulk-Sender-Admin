from rest_framework import serializers
from .models import SoftwareLicenseKey, User

# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    software_license_key = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('id', 'email',
                  'password', 'software_license_key')
        extra_kwargs = {
            'password': {'write_only': True},
            'software_license_key': {'required': True},
        }

    def create(self, validated_data):
        software_license_key = validated_data['software_license_key']
        user = None
        if (SoftwareLicenseKey.objects.get(key=software_license_key) != None):

            user = User.objects.create_user(
                validated_data['email'], validated_data['password'])
            user.software_license_key = validated_data['software_license_key']

        return user
