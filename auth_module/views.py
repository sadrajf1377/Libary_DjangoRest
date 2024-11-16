from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views import View
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user_module.models import User
from rest_framework.authtoken.models import Token
# Create your views here.

class Log_in(APIView):

    permission_classes = [AllowAny]
    def post(self,request):
        print('i was called')
        try:
           username=request.POST.get('username')
           password=request.POST.get('password')

           us=User.objects.get(username=username)
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

