import unittest
from lomi import LomiClient

class TestAccountsService(unittest.TestCase):
    def setUp(self):
        self.client = LomiClient(api_key="test_key")

    def test_service_initialized(self):
        self.assertIsNotNone(self.client.accounts)
        
    # TODO: Add mock tests for Accounts methods
