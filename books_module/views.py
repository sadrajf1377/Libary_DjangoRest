import json
from collections import OrderedDict

from django.db.models import Case, When, Value, IntegerField, Sum, Q, CharField, Avg
from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_rest.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book,Book_Category,Book_Comment,Borrow_History
from .serializers import Books_Serializer, Category_Serializer, Create_Book_Serializer, Comments_Serializer,Create_Comment_Serializer
from .forms import Add_Book_Form
from .pagination_classes import Book_Pagination




class All_Books(ListAPIView):
    http_method_names = ['get']
    pagination_class = Book_Pagination
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = Books_Serializer
    def get_queryset(self):
        query_set=super().get_queryset().prefetch_related('comments').annotate(rating=Avg('comments__rating',distinct=True,default=0)).annotate(rate_status=
           Case(When(rating__gt=8,then=Value('excellent')),
                When(Q(Q(rating__gt=4),Q(rating__lt=8)),then=Value('good')),
                  When(Q(Q(rating__gte=0) ,Q(rating__lte=4)),then=Value('average')),
                   When(rating__lt=0,then=Value('bad')),
                output_field=CharField()

        )).filter(id__in=range(0,1000))

        return query_set


class Add_Book(CreateAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class =Create_Book_Serializer
    def post(self,request):
        print(request.POST)
        return super().post(request)



class Get_Book_Categories(ListAPIView):
    http_method_names = ['get']
    permission_classes = [AllowAny]
    queryset = Book_Category.objects.all()
    serializer_class = Category_Serializer


class Update_Book(UpdateAPIView):
    serializer_class =Create_Book_Serializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class View_Book_Details(APIView):
    http_method_names = ['get']
    permission_classes = [AllowAny]
    def get(self,request,pk,page_number=None):
        book=Book.objects.get(id=pk)
        comments=book.comments.all()

        if page_number:
            page_number=int(page_number)
            start=page_number-1+1 if page_number>0 else 0
            comments=comments[start:start+1]
        else:
            comments=comments[0:1]
        return Response(data={'commments':Comments_Serializer(comments,many=True).data,'book':Books_Serializer(book,many=False).data})


class Add_Comment(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    http_method_names = ['post','get']
    def post(self,request):
        ser=Create_Comment_Serializer(data=request.data)
        if ser.is_valid():
            dat=ser.validated_data
            com=Book_Comment(content=dat.get('content'),rating=int(dat.get('rating')),parent_book=dat.get('parent_book'),author=request.user)
            com.save()
            return Response({'message':'comment added successfully','comment':Comments_Serializer(com,many=False).data},status=200)
        else:
            return Response({'message': 'invalid data structure'}, status=400)


class Delete_Comment(DestroyAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Comments_Serializer


    def get_object(self):
        object=Book_Comment.objects.get(author=self.request.user,id=self.kwargs['pk'])
        return object
    def post(self,request):
        try:
            return super().post(request)
        except:
            return Response({'message':'comment not found'},status=404)



class Borrow_Book(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['post']
    def post(self,request):
        data=json.loads(request.data)
        book_id=data['book_id']
        try:
           book=Book.objects.get(id=book_id)
           if book.can_borrow():
              history=Borrow_History(user=request.user,borrowed_book=book)
              history.save()
              return Response({'message':f'borrowed book was {book.title} and user who borrowed this book was {request.user.username}'},status=200)
           else:
              return Response({
                                'message': f'not enough copies of this book left to borrow'},
                             status=401)
        except Book.DoesNotExist:
            return Response({'message':'Couldnt find such book'},status=404)

class Return_Book(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']
    def post(self,request):
        book_id=json.loads(request.data)['book_id']
        try:
            hist=Borrow_History.objects.get(borrowed_book_id=book_id,user_id=request.user)
            book_title=hist.borrowed_book.title
            hist.delete()
            return Response({'message':f'user :{request.user.username} returned the book {book_title} successfully'},status=201)

        except Borrow_History.DoesNotExist:
            return Response({'book or user not found!'},status=404)


class Search_Books(ListAPIView):
    serializer_class = Books_Serializer
    permission_classes = [AllowAny]
    pagination_class = Book_Pagination
    queryset = Book.objects.all()
    def get_queryset(self):
        min_year=self.kwargs['min_year']
        max_year=self.kwargs['max_year']
        print('max_year'+min_year,'min_year'+max_year)

        query_set=super().get_queryset()

        return query_set






