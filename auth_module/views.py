from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user_module.models import User
from rest_framework.authtoken.models import Token

from .serializers import User_Serializer
# Create your views here.

class Log_in(APIView):

    permission_classes = [AllowAny]
    def post(self,request):
        for us in User.objects.all():
            print('user=',us.username, us.password)
        try:
           username=request.POST.get('username')
           password=request.POST.get('password')

           us=User.objects.get(username=username)
           print(us)
           user=us if us.check_password(password) else None
           print(user)
           if user != None:
               print('user valid')
               tok,tk = Token.objects.get_or_create(user=user)
               return Response(data={'message':'user was valid','token':str(tok.key)},status=200)
           else:
               print('user not valid')
               return Response(data={'message':'user not found'}, status=404)


        except Exception as exc:
            print(exc.args)
            return Response(data={'message':'internal error happend'},status=500)


class Who_Am_I(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        return Response(data={'username':request.user.username},status=200)


class Logout(APIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        Token.objects.get(user=request.user).delete()
        return Response(data={'message':'user logged out successfully'},status=200)