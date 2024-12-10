from django.urls import path
from .views import Log_in,Who_Am_I,Logout
urlpatterns=[
    path('login',Log_in.as_view(),name='log_in'),
    path('who_am_i',Who_Am_I.as_view(),name='who_am_i'),
    path('logout',Logout.as_view(),name='logout')
]