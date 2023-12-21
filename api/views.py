from rest_framework import generics
from .models import *
from .serializers import *


class NewsChannelsList(generics.ListCreateAPIView):
    queryset = NewsChannels.objects.all()
    serializer_class = NewsChannelsSerializer


class NewsChannelsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsChannels.objects.all()
    serializer_class = NewsChannelsSerializer


class NewsSectionsList(generics.ListCreateAPIView):
    queryset = NewsSection.objects.all()
    serializer_class = NewsSectionSerializer


class NewsSectionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsSection.objects.all()
    serializer_class = NewsSectionSerializer


class NewsHeadersList(generics.ListCreateAPIView):
    queryset = NewsHeaders.objects.all()
    serializer_class = NewsHeadersSerializer


class NewsHeadersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsHeaders.objects.all()
    serializer_class = NewsHeadersSerializer
