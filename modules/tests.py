from rest_framework.test import APITestCase, APIClient
from modules.models import Modules
from modules.serializers import ModuleSerializer
from django.urls import reverse
from rest_framework import status


class ModuleSerializerTestCase(APITestCase):
    def setUp(self):
        self.module_data = {'number': 1, 'title': 'Test Title', 'description': 'Test Description'}
        self.serializer = ModuleSerializer(data=self.module_data)

    def test_serializer_with_valid_data(self):
        self.assertTrue(self.serializer.is_valid())
        module = self.serializer.save()
        self.assertEqual(module.number, 1)
        self.assertEqual(module.title, 'Test Title')
        self.assertEqual(module.description, 'Test Description')

    def test_serializer_with_invalid_data(self):
        invalid_data = {'number': 1, 'title': 'крипта', 'description': 'dfbdbgbfgdb'}
        serializer = ModuleSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())


class ModulesAPITestCase(APITestCase):
    def setUp(self):
        self.module = Modules.objects.create(number=1, title='Test Title', description='Test Description')

    def test_module_update(self):
        url = f'http://127.0.0.1:8000/module/update/{self.module.pk}/'
        data = {'number': 2, 'title': 'Updated Title', 'description': 'Updated Description'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.module.refresh_from_db()
        self.assertEqual(self.module.number, 2)
        self.assertEqual(self.module.title, 'Updated Title')
        self.assertEqual(self.module.description, 'Updated Description')

    def test_module_read(self):
        url = f'http://127.0.0.1:8000/module/{self.module.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['number'], self.module.number)
        self.assertEqual(response.data['title'], self.module.title)
        self.assertEqual(response.data['description'], self.module.description)

    def test_module_delete(self):
        url = f'http://127.0.0.1:8000/module/delete/{self.module.pk}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Modules.objects.filter(pk=self.module.pk).exists())

    def test_module_creation(self):
        client = APIClient()
        data = {
            'number': 1,
            'title': 'Test Title',
            'description': 'Test Description'
        }
        response = client.post('http://127.0.0.1:8000/module/create/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        modules = Modules.objects.filter(title='Test Title')
        self.assertEqual(modules.count(), 2)
        module = modules.first()
        self.assertEqual(module.number, 1)
        self.assertEqual(module.description, 'Test Description')

