from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """TEst APIView"""
    def get(self, request, format=None):
        """Returns list of APIView features"""
        an_api_view = [
            'Uses HTTP methods as function',
            'IS similat to DjangoView',
            'Gives you the most control over aplication logic',
        ]

        return Response({'message': 'Hello', 'an_api_view': an_api_view})
        # Create your views here.
