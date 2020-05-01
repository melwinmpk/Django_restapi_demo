from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class AuthView(APIView):
    authentication_classes = []
    permission_classes     = [permissions.AllowAny] # permissions.AllowAny
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail':'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        qs = User.objects.filter(
                                    Q(username__iexact=username)|
                                    Q(email__iexact=username)
                                ).distinct()
        if qs.count() == 1:
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