from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.
from .models import Employee


class ModelTestCase(TestCase):
    """
    This class define the test suite for the Employee model.
    """

    def setUp(self):
        """
        Define test client and other test variables
        :return: 
        """
        self.employee_name = "avi"
        self.employee = Employee(full_name=self.employee_name)

    def test_model_can_create_model(self):
        """Test if Employee model can create a employee model"""
        old_count = Employee.objects.count()
        self.employee.save()
        new_count = Employee.objects.count()
        self.assertNotEquals(old_count, new_count)


class ViewTestCase(TestCase):
    """ Test for api view"""

    def setUp(self):
        """Defining the test client and other test variable"""
        self.client = APIClient()
        self.employee_data = {'full_name': "Michel"}
        self.response = self.client.post(
            reverse('create'),
            self.employee_data,
            format="json"
        )

    def test_api_can_create_employee(self):
        """ Testing the capability of api, to create employee """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
