from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from npo_user.models import NPOUser
from npo_user.serializers import NPOUserSerializer


class RegisterAPIView(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        user = NPOUser.objects.create(username=username,
                                      password=password,
                                      email=email,
                                      is_active=True)
        user.save()
        return Response(data=NPOUserSerializer(user).data,
                        status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def get(self, request):
        user = authenticate(
            email=request.data['email'],
            password=request.data['password'])
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'User not found or does not exist'})
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return Response(data={'token': token.key},
                            status=status.HTTP_200_OK)
