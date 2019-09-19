from django.conf.urls import url
from .views import *


app_name = "libraryApplication"

urlpatterns = [
    url(r'^$', book_list, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^$', library_list, name='home'),
    url(r'^libraries$', library_list, name='libraries'),
]
