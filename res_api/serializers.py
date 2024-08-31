from rest_framework import serializers


class NickSerializer(serializers.Serializer):
    """Serializers a field for testing our APIView"""
    text = serializers.CharField(max_length=10)
