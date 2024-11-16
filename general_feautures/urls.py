from django.urls import path
from .views import generate_token,test_page
urlpatterns=[path('get_token',generate_token,name='generate_token')
             ,path('test',test_page,name='test')

             ]