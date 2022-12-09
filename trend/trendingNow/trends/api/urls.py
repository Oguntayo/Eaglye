from django.urls import path
from .views import MessageList, MessageDetail, ApiDocs

urlpatterns = [
    path('',  ApiDocs),
    path('message/', MessageList.as_view()),
    path('message/<str:pk>/', MessageDetail.as_view()),
]
