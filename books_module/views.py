from django_rest.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book,Book_Category
from.serializers import Books_Serializer,Category_Serializer
from .forms import Add_Book_Form
from .pagination_classes import Book_Pagination

class All_Books(ListAPIView):
    http_method_names = ['get']
    pagination_class = Book_Pagination
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = Books_Serializer


class Add_Book(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self,request):
        frm=Add_Book_Form(request.POST)
        print(request.POST)
        if frm.is_valid():
            frm.save()
            return Response(data={'message':'book was added successfully'},status=200)
        else:
            errors=''
            for field in frm.errors:
                errors+=frm.errors[field]

            return Response(data={'message': 'book could not be added','error':errors}, status=400)


class Get_Book_Categories(ListAPIView):
    http_method_names = ['get']
    queryset = Book_Category.objects.all()
    serializer_class = Category_Serializer
