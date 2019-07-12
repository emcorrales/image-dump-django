from rest_framework import generics
from .models import Photo
from .serializers import PhotoSerializer


class ListPhotoView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
