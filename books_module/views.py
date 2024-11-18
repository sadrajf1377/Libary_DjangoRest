from django.db.models import Case, When, Value, IntegerField
from django_rest.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book,Book_Category
from.serializers import Books_Serializer,Category_Serializer,Create_Book_Serializer
from .forms import Add_Book_Form
from .pagination_classes import Book_Pagination

class All_Books(ListAPIView):
    http_method_names = ['get']
    pagination_class = Book_Pagination
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = Books_Serializer


class Add_Book(CreateAPIView):
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class =Create_Book_Serializer



class Get_Book_Categories(ListAPIView):
    http_method_names = ['get']
    queryset = Book_Category.objects.all()
    serializer_class = Category_Serializer


class Update_Book(UpdateAPIView):
    serializer_class = None
    queryset = None