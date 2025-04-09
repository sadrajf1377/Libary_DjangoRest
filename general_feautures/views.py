from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
@api_view(['GET'])
@csrf_protect
def generate_token(request):
    if request.method=="GET":
      token=get_token(request)
      print('generated token is',token)
      return JsonResponse({"token":token},status=200)
    else:
        pass

def show_headers(func):
    def to_do(*args):
        print('sdsd')
        print(args[0].headers)
        func(*args)
    return to_do

def test_page(request):
    return render(request,'test.html')

class Service_Info(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        data={'service_name':'book_manager','description':'this service allows you to create your own book management system',
              'functions':{
                  'books_manager':['add_book','delete_book','update_book','get_books_list','show_books_details'],
                  'books_comment_manager':['write_comment','delete_comment'],
                  'authentication':['login','logout','sign_up','delete_account'],

              }
              }
        return Response(data=data,status=200)
