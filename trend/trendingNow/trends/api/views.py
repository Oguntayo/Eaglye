from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from trends.models import Message
from .serializers import MessageSerializer


@api_view(['GET'])
def ApiDocs(request):
    routes = [
        'GET /api',
        'GET /api/message',
        'GET /api/message/:id'
    ]
    return Response(routes)


class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all()
        return queryset


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
