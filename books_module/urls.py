from django.urls import path
from django.urls import re_path
from .views import All_Books,Add_Book,Get_Book_Categories,View_Book_Details,Update_Book,Add_Comment,Delete_Comment,Search_Books


urlpatterns=[
path('',All_Books.as_view(),name='show_all_books'),
    path('add_book',Add_Book.as_view(),name='add_new_book'),
    path('get_categories',Get_Book_Categories.as_view(),name='get_book_caregories'),
path('view_book_Details/<pk>',View_Book_Details.as_view(),name='get_book_details'),
path('view_book_Details/<pk>/<page_number>',View_Book_Details.as_view(),name='get_book_details'),
path('add_comment',Add_Comment.as_view(),name='add_book_comment'),
path('delete_comment/<pk>',Delete_Comment.as_view(),name='delete_book_comment'),
re_path(r'^search_books/(?P<min_year>)/(?P<max_year>)\w+?$',Search_Books.as_view(),name='search_books')
]