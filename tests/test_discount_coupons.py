import unittest
from lomi import LomiClient

class TestDiscountCouponsService(unittest.TestCase):
    def setUp(self):
        self.client = LomiClient(api_key="test_key")

    def test_service_initialized(self):
        self.assertIsNotNone(self.client.discount_coupons)
        
    # TODO: Add mock tests for DiscountCoupons methods
