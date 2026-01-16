import unittest
from lomi import LomiClient

class TestPaymentRequestsService(unittest.TestCase):
    def setUp(self):
        self.client = LomiClient(api_key="test_key")

    def test_service_initialized(self):
        self.assertIsNotNone(self.client.payment_requests)
        
    # TODO: Add mock tests for PaymentRequests methods
