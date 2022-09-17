from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.decorators import api_view

# Create your views here.


def index(request):
    return render(request, 'base/index.html', {})


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })


@api_view(["POST"])
def login_view(request):
    if ('email' not in request.data or 'password' not in request.data):
        return Response({
            'success': False,
            'message': "Email and Passwords are the required fields",
        })
    else:
        email = request.data.email
        password = request.data.password

        user = login(email, password)
        if user is not None:
            return Response({
                'success': True,
                "message": "User logged in succesfully.",
                'user': user
            })
        else:
            return Response({
                'success': False,
                "message": "Invalid email or password.",
            })
