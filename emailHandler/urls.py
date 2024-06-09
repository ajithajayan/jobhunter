from django.urls import path
from emailHandler.views import *

urlpatterns = [
    path('', index , name='index_page'),

    path('jobs', update_company , name='jobs'),


]


