from .models import Car
from .serializers import CarSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    parser_classes = (MultiPartParser, FormParser)
    # permission_classes = [IsAuthenticated]  # Require authentication

    # def create(self, request, *args, **kwargs):
    #     # Log files to see if the image is coming through
    #     print("FILES:", request.FILES)
    #     # This is automatically set from JWT token
    #     print("USER:", request.user)
    #     print("USER ID:", request.user)  # Get user ID from JWT

    #     # The serializer will automatically set the user via perform_create
    #     return super().create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     # Automatically set the user from the JWT token
    #     serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='by-user/(?P<user_id>[^/.]+)')
    def by_user(self, request, user_id=None):
        cars = Car.objects.filter(user_id=user_id)
        serializer = self.get_serializer(cars, many=True)
        return Response(serializer.data)
