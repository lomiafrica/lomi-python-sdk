import unittest
from lomi import LomiClient

class TestPaymentLinksService(unittest.TestCase):
    def setUp(self):
        self.client = LomiClient(api_key="test_key")

    def test_service_initialized(self):
        self.assertIsNotNone(self.client.payment_links)
        
    # TODO: Add mock tests for PaymentLinks methods
