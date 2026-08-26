"""Smoke test: generated services attach to client."""
import unittest


class TestSurface(unittest.TestCase):
    def test_client_services(self):
        from lomi import LomiClient

        c = LomiClient(api_key="test")

        attrs = sorted(
            a
            for a in dir(c)
            if not a.startswith("_") and callable(getattr(c, a, None)) is False
        )
        # spot-check newly added surfaces
        self.assertTrue(hasattr(c, "charges"))
        self.assertTrue(hasattr(c, "payment_intents"))

        expected = sorted(
            name
            for name in attrs
            if name
            not in ("api_key", "base_url", "session")
        )

        services = sorted(
            a
            for a in attrs
            if not a.startswith('_')
            and getattr(c, a).__class__.__name__.endswith("Service")
        )
        assert len(expected) >= 10
        print("services:", services)


if __name__ == "__main__":
    unittest.main()
