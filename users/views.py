from rest_framework.views import APIView, Response, Request, status
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsUserOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
class UserDatailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOnly]

    def get(self, request:Request, user_id):
        userValidate = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, userValidate)
        serializer = UserSerializer(userValidate)
        return Response(serializer.data)
    
    def patch(self, request:Request, user_id):
        userValidate = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, userValidate)
        serializer = UserSerializer(userValidate ,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
    
