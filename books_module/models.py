from user_module.models import User
from django.db import models

class Book_Category(models.Model):
    title=models.CharField(max_length=15,verbose_name='title of category',null=False,blank=False)


# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=20,verbose_name='title of this book',null=False,blank=False,unique=True)
    author=models.CharField(max_length=30,verbose_name='who wrote this book',null=False,blank=False)
    price=models.DecimalField(max_digits=8,decimal_places=4,default=0000.0000)
    book_category=models.ForeignKey(Book_Category,on_delete=models.SET_NULL,null=True,blank=True,db_index=True)
    publish_date=models.DateField(null=False,blank=False,verbose_name='date of publishment')
    copies_count = models.PositiveIntegerField(default=0, verbose_name='how many copies of this book are available',
                                               null=False, blank=False)


    def can_borrow(self):
        result=self.borrowed_users.all().count()<self.copies_count
        return result

    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['title','author'],name='check replication')
        ]

def rating_validator(value):
    if value>10 or value<0:
        raise ValueError('rating can only be between 0 to 10')


class Book_Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False,verbose_name='writter of comment',related_name='comments')
    date=models.DateTimeField(auto_now_add=True,verbose_name='time of comment creation')
    content=models.TextField(max_length=2000,verbose_name='main content of comment',null=False,blank=False)
    parent_book=models.ForeignKey(Book,on_delete=models.CASCADE,null=False,blank=False,related_name='comments',db_index=True)
    rating=models.IntegerField(verbose_name='rating of this book',validators=[rating_validator],default=0)







class Borrow_History(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False,related_name='borrowed_books')
    borrowed_book=models.ForeignKey(Book,on_delete=models.CASCADE,null=False,blank=False,db_index=True,related_name='borrowed_users')
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['user','borrowed_book'],name='make sure each user can only borrowed one copy of each book')
        ]

