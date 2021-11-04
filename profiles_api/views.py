from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_api_view = [
            "Uses HTTP methods as functions (get, post, patch, put, delete)",
            "Is similar to a traditional Django view",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs."
        ]

        return Response({"message": "Hello", "an_api_view": an_api_view})

    def post(self, requests):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=requests.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, requests, pk=None):
        """Handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, requests, pk=None):
        """Handle partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, requests, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})

