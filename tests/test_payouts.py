import unittest
from lomi import LomiClient

class TestPayoutsService(unittest.TestCase):
    def setUp(self):
        self.client = LomiClient(api_key="test_key")

    def test_service_initialized(self):
        self.assertIsNotNone(self.client.payouts)
        
    # TODO: Add mock tests for Payouts methods
