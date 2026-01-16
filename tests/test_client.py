import unittest
from lomi import LomiClient

class TestLomiClient(unittest.TestCase):
    def test_init(self):
        client = LomiClient(api_key="test_key")
        self.assertEqual(client.api_key, "test_key")
        self.assertEqual(client.base_url, "https://api.lomi.africa")

    def test_sandbox(self):
        client = LomiClient(api_key="test_key", environment="test")
        self.assertEqual(client.base_url, "https://sandbox.api.lomi.africa")

if __name__ == '__main__':
    unittest.main()
