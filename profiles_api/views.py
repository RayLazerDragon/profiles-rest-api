from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializer, models, permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializer.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'automatically maps to URLs using Routers',
            'provide more functionality with less code',
        ]
        return Response({'message': "Hello", 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}!"
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http method': "GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http method': "PUT"})

    def partial_update(self, request, pk=None):
        return Response({'http method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http method': "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


