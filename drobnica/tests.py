from django.test import TestCase
from .models import Package
from django.urls import reverse

class PackageModelTest(TestCase):

    def test_empty_package(self):
        package = Package()
        self.assertIs(len(package.pack_type)!=3,True)

def create_pacakge(pack_type, desc, width, length,height):
        return Package.objects.create(pack_type=pack_type, description = desc, width= width, length = length, height = height)

class PackageViewTest(TestCase):
    
    
    def test_package_creation(self):
        create_pacakge('FAB','opis','123','321','333')
        response = self.client.get(reverse('package_list'))
        self.assertEqual(response.status_code,200)
