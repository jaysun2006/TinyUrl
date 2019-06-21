from rest_framework import serializers


class URLSerializer(serializers.Serializer):
    url = serializers.CharField(required=True)
