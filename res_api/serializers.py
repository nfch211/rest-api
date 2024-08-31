from rest_framework import serializers


class NickSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
