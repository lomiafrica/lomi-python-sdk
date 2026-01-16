import unittest
from lomi import LomiClient

class TestSubscriptionsService(unittest.TestCase):
    def setUp(self):
        self.client = LomiClient(api_key="test_key")

    def test_service_initialized(self):
        self.assertIsNotNone(self.client.subscriptions)
        
    # TODO: Add mock tests for Subscriptions methods
