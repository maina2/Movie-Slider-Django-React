from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUserView(APIView):

    permission_classes=[permissions.AllowAny]

    def post (self,request):
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid():
            user= serializer.save()
            refresh=RefreshToken.for_user(user)
            response = {
                "message": "User registered successfully",
                "data": serializer.data,
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    