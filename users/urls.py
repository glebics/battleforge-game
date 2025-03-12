# users/urls.py

from django.urls import path
from django.http import HttpResponse


def hello_view(request):
    return HttpResponse('hello')


urlpatterns = [
    path('', hello_view, name='hello'),
]
