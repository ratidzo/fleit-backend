from .serializers import DestinationSerializer
from .models import Destination
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

