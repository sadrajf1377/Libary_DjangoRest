from django.contrib import admin
from .models import Book,Book_Category,Book_Comment

class comment_display(admin.ModelAdmin):
    list_display = ['id','author','rating','date']


admin.site.register(Book)
admin.site.register(Book_Category)
admin.site.register(Book_Comment,comment_display)
# Register your models here.
