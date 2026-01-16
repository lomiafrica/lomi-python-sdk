import unittest
from lomi import LomiClient

class TestWebhooksService(unittest.TestCase):
    def setUp(self):
        self.client = LomiClient(api_key="test_key")

    def test_service_initialized(self):
        self.assertIsNotNone(self.client.webhooks)
        
    # TODO: Add mock tests for Webhooks methods
