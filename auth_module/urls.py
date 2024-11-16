from django.urls import path
from .views import Log_in
urlpatterns=[
    path('log_in',Log_in.as_view(),name='log_in')
]