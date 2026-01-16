import unittest
from lomi import LomiClient

class TestRefundsService(unittest.TestCase):
    def setUp(self):
        self.client = LomiClient(api_key="test_key")

    def test_service_initialized(self):
        self.assertIsNotNone(self.client.refunds)
        
    # TODO: Add mock tests for Refunds methods
