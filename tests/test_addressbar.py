import unittest

from addressbar import address_to_url


class AddressToUrlTests(unittest.TestCase):
    def test_empty_input_does_not_open_a_page(self):
        self.assertIsNone(address_to_url(" \t"))

    def test_keeps_http_and_https_addresses(self):
        self.assertEqual(address_to_url("http://example.com"), "http://example.com")
        self.assertEqual(address_to_url("HTTPS://example.com"), "HTTPS://example.com")

    def test_adds_https_to_a_domain(self):
        self.assertEqual(address_to_url("example.com/path"), "https://example.com/path")

    def test_uses_http_for_localhost(self):
        self.assertEqual(address_to_url("localhost:8000"), "http://localhost:8000")

    def test_searches_for_plain_text(self):
        self.assertEqual(
            address_to_url("raspberry pi os"),
            "https://www.google.com/search?q=raspberry+pi+os",
        )


if __name__ == "__main__":
    unittest.main()
