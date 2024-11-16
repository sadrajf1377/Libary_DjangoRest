from django.urls import path

from .views import All_Books,Add_Book


urlpatterns=[
path('',All_Books.as_view(),name='show_all_books'),
    path('add_book',Add_Book.as_view(),name='add_new_book')

]