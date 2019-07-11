from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Photo
from .serializers import PhotoSerializer

# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_photo(name=""):
        if title != "" and artist != "":
            Photo.objects.create(photo=photo)

    def setUp(self):
        # add test data
        self.create_photo("Horse")
        self.create_photo("Cow")
        self.create_photo("Whale")


class GetAllPhotoTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("photo-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Photo.objects.all()
        serialized = PhotoSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
# Create your tests here.
