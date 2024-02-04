from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes name field for testing our APIVIew"""
    name = serializers.CharField(max_length=20)