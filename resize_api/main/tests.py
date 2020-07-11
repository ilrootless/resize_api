import io
from unittest import mock

from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.core.files import File

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Resize


class ResizeTest(APITestCase):

    def test_create_invalid_resize(self):
        image = io.BytesIO()
        Image.new('RGB', (1080, 720)).save(image, 'JPEG')
        image.seek(0)

        image_file = SimpleUploadedFile('image.jpg', image.getvalue())

        response = self.client.post(reverse('main:resize'), {
            'height': 10000,
            'width': 0,
            'format': 'pdf',
            'original': image_file
        }, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_resize(self):
        image = io.BytesIO()
        Image.new('RGB', (1080, 720)).save(image, 'JPEG')
        image.seek(0)

        image_file = SimpleUploadedFile('image.jpg', image.getvalue())

        response = self.client.post(reverse('main:resize'), {
            'height': 9999,
            'width': 9999,
            'format': 'jpg',
            'original': image_file
        }, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fail_resize_detail(self):
        response = self.client.get(reverse('main:resize_detail', kwargs={'pk': 50}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_resize_detail(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'photo.jpg'

        resize = Resize.objects.create(
            height=200,
            width=200,
            format='png',
            original=file_mock.name,
            result=file_mock.name
        )
        response = self.client.get(reverse('main:resize_detail', kwargs={'pk': resize.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('height'), 200)
        self.assertEqual(response.json().get('width'), 200)
        self.assertEqual(response.json().get('format'), 'png')
