from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField()
