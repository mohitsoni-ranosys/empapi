from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from .views import EmpList


class TestEmpList(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = EmpList.as_view()
        self.uri = 'emp_list'
        self.uri2 = 'http://127.0.0.1:8000/employees/emp_list'
        self.user = self.setup_user()
        self.client = APIClient()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test_user',
            email='test_user@yopmail.com',
            password='test_user123*',
        )

    def test_list(self):
        request = self.factory.get(self.uri)
        request.user = self.user
        response = self.view(request)
        print(response)
        self.assertEqual(
            response.status_code,
            200,
            'Expected 200, received {0} instead'.format(response.status_code))

    # def test_list_from_client_side(self):
    #     # self.client.login(email='test_user', password='test_user123*')
    #     response = self.client.get(self.uri)
    #     self.assertEqual(
    #         response.status_code,
    #         200,
    #         'Expected 200, received {0} instead'.format(response.status_code))

    def test_list2(self):
        self.client.login(username='test_user', password='test_user123*')
        response = self.client.get(self.uri2)
        print(response)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        
