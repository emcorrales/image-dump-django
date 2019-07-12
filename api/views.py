from rest_framework import generics
from .models import Photo
from .serializers import PhotoSerializer


class PhotosView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
