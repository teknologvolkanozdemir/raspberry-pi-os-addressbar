import unittest

from addressbar import resolve_address


class ResolveAddressTests(unittest.TestCase):
    def test_keeps_http_and_https_urls(self):
        self.assertEqual(
            resolve_address("https://example.com/path"),
            "https://example.com/path",
        )
        self.assertEqual(
            resolve_address("http://example.com"), "http://example.com"
        )

    def test_adds_https_to_domain_and_local_addresses(self):
        self.assertEqual(resolve_address("example.com"), "https://example.com")
        self.assertEqual(resolve_address("localhost:8000"), "https://localhost:8000")
        self.assertEqual(resolve_address("192.168.1.2"), "https://192.168.1.2")

    def test_searches_for_terms(self):
        self.assertEqual(
            resolve_address("raspberry pi"),
            "https://duckduckgo.com/?q=raspberry+pi",
        )
        self.assertEqual(
            resolve_address("weather"),
            "https://duckduckgo.com/?q=weather",
        )

    def test_rejects_unsupported_schemes_and_empty_input(self):
        with self.assertRaises(ValueError):
            resolve_address("javascript:alert(1)")
        with self.assertRaises(ValueError):
            resolve_address(" ")


if __name__ == "__main__":
    unittest.main()
