from django.urls import path
from .views import ListPhotosView


urlpatterns = [
    path('photos/', PhotosView.as_view(), name="photos-all")
]
