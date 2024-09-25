from django.urls import path
from .views import *


app_name = 'transactions'

urlpatterns = [
    path('', transaction_list, name='listCreate'),
    path('create/', transactionCreate, name='transactionCreate'),
    path('update/<int:pk>/', transaction_update, name='transactionUpdate'),
    path('delete/<int:pk>/', transaction_delete, name='transactionDelete'),
    path('api/transaction/', postListAPIView.as_view(), name='listCreate'),
    path('api/transaction/<int:pk>/', postDetailAPIView.as_view(), name='detailCreate'),
    path('api/users/', postListAPIView.as_view(), name='userList'),
    path('api/users/<int:pk>/', postDetailAPIView.as_view(), name='userDetail'),
    path('api/reports/', postListAPIView.as_view(), name='reportList'),

] 