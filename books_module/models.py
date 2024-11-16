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
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['title','author'],name='check replication')
        ]


