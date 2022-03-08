from django.urls import path
from .views import *

urlpatterns = [
    path('', all_users, name='all_users'),
    path('create/', create, name="create"),
    path('<str:id>/', specific_users, name='specific_users'),
    path('update/<str:id>/', update, name='update'),
    path('delete/<str:id>/', delete, name='delete'),
]