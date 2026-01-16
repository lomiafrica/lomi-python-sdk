import unittest
from lomi import LomiClient

class TestBeneficiaryPayoutsService(unittest.TestCase):
    def setUp(self):
        self.client = LomiClient(api_key="test_key")

    def test_service_initialized(self):
        self.assertIsNotNone(self.client.beneficiary_payouts)
        
    # TODO: Add mock tests for BeneficiaryPayouts methods
