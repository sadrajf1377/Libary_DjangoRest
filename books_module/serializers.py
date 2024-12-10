
from rest_framework import serializers
from .models import Book,Book_Category,Book_Comment
class Books_Serializer(serializers.ModelSerializer):
    rate_status=serializers.CharField(read_only=True,max_length=100)
    rating=serializers.IntegerField(read_only=True)
    class Meta:
        model=Book
        fields=['title','price','id','rate_status','rating']



class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Book_Category
        fields=['title','id']


class Create_Book_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['title','book_category','price','author','publish_date']

class Comments_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Book_Comment
        fields=['content','rating','parent_book']

class Create_Comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Book_Comment
        fields=['content','rating','parent_book']