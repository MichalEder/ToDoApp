from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ToDoApp_api import serializers

class HelloApiView(APIView):
    """TEst APIView"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns list of APIView features"""
        an_api_view = [
            'Uses HTTP methods as function',
            'IS similat to DjangoView',
            'Gives you the most control over aplication logic',
        ]

        return Response({'message': 'Hello', 'an_api_view': an_api_view})

    def post(self, request):
        """Hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})