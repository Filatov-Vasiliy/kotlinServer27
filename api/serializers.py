from rest_framework import serializers
from .models import *


class NewsChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsChannels
        depth = 1
        fields = ['id', 'name', 'sections']


class NewsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSection
        fields = ['id', 'name', 'newsChannel', 'headers']


class NewsHeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsHeaders
        fields = '__all__'
