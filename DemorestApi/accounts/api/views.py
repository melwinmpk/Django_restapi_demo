from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .permissions import AnonPermissionOnly
# models.User

User = get_user_model()

class AuthAPIView(APIView):
    # authentication_classes = []
    permission_classes     = [permissions.AllowAny] # permissions.AllowAny
    def post(self, request, *args, **kwargs):
        print(str(request.user))
        if request.user.is_authenticated:
            return Response({'detail':'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        # user = authenticate(username=username, password=password)
        qs = User.objects.filter(
                                    Q(username__iexact=username)|
                                    Q(email__iexact=username)
                                ).distinct()
        if qs.count() > 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                print(user)
                refresh = RefreshToken.for_user(user)
                result = {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                          }
                return Response(result)
        return Response({"detail":"Invalid credentials "}, status=401)

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AnonPermissionOnly]

'''
class RegisterAPIView(APIView):
    # authentication_classes = []
    permission_classes = [permissions.AllowAny]  # permissions.AllowAny

    def post(self, request, *args, **kwargs):
        print(str(request.user))
        if request.user.is_authenticated:
            return Response({'detail': 'You are already registered and authenticated'}, status=400)
        data        = request.data
        username    = data.get('username')
        email       = data.get('email')
        password    = data.get('password')
        password2   = data.get('password2')
        # user = authenticate(username=username, password=password)
        qs = User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact=username)
        )
        if password != password2:
            return Response({"detail": "Password should match"}, status=402)
        if qs.exists():
            return Response({"detail": "This user already exist"}, status=401)
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            # user.set_passowrd(password)
            user.save()
            refresh = RefreshToken.for_user(user)
            result = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response({"detail": "New User Got registered and please Verify the email "}, status=201)
        return Response({"detail": "Invalid Request "}, status=400)
'''