import unittest
from lomi import LomiClient

class TestCustomersService(unittest.TestCase):
    def setUp(self):
        self.client = LomiClient(api_key="test_key")

    def test_service_initialized(self):
        self.assertIsNotNone(self.client.customers)
        
    # TODO: Add mock tests for Customers methods
