from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response


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