import unittest
from lomi import LomiClient

class TestWebhookDeliveryLogsService(unittest.TestCase):
    def setUp(self):
        self.client = LomiClient(api_key="test_key")

    def test_service_initialized(self):
        self.assertIsNotNone(self.client.webhook_delivery_logs)
        
    # TODO: Add mock tests for WebhookDeliveryLogs methods
