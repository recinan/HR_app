from django.shortcuts import render
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer, ChangePasswordSerializer, UpdateUserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg import openapi




# Create your views here.
@swagger_auto_schema(
        method='post',
        request_body=RegisterSerializer,
        responses={201:RegisterSerializer},
        operation_summary='Register'
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


@swagger_auto_schema(
        method='put',
        request_body=ChangePasswordSerializer,
        responses={201:ChangePasswordSerializer},
        operation_summary='Change Password'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    serializer = ChangePasswordSerializer(instance=user,data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
        method='put',
        request_body=UpdateUserSerializer,
        responses={201:UpdateUserSerializer},
        operation_summary='Change Password'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    serializer = UpdateUserSerializer(instance=user,data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


refresh_token_param = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["refresh_token"],
    properties={
        'refresh_token': openapi.Schema(type=openapi.TYPE_STRING)
    }
)

@swagger_auto_schema(
    method='post',
    request_body=refresh_token_param,
    operation_description="Log out user by blacklisting refresh token",
    responses={
        205: 'Token blacklisted successfully',
        400: 'Bad Request - Invalid token or missing field'
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    print("Request data:", request.data)  
    refresh_token = request.data.get("refresh_token")

    if not refresh_token:
        return Response({"detail": "refresh_token is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)