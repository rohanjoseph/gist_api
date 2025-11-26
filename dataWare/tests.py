from django.test import TestCase

# Create your tests here.
class DataWareTests(TestCase):
    def test_data_view(self):
        response = self.client.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)