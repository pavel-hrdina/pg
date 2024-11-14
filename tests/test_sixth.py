import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

from sixth import download_url_and_get_all_hrefs


class TestDownloadUrlAndGetAllHrefs(unittest.TestCase):

    @patch('requests.get')
    def test_successful_download_and_href_extraction(self, mock_get):
        # Simulating a successful response with status code 200
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'<html><body><a href="https://example.com/page1">Link 1</a><a href="https://example.com/page2">Link 2</a></body></html>'
        mock_get.return_value = mock_response

        url = "https://example.com"
        expected_hrefs = ["https://example.com/page1", "https://example.com/page2"]

        result = download_url_and_get_all_hrefs(url)

        self.assertEqual(result, expected_hrefs)

    @patch('requests.get')
    def test_unsuccessful_download(self, mock_get):
        # Simulating an unsuccessful response with status code 404
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        url = "https://example.com"

        # Capture printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = download_url_and_get_all_hrefs(url)
            self.assertEqual(result, [])
            self.assertIn("Chyba pri stahovani stranky", mock_stdout.getvalue())

    @patch('requests.get')
    def test_no_hrefs_found(self, mock_get):
        # Simulating a page with no <a href=...> tags
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'<html><body>No links here!</body></html>'
        mock_get.return_value = mock_response

        url = "https://example.com"
        expected_hrefs = []

        result = download_url_and_get_all_hrefs(url)

        self.assertEqual(result, expected_hrefs)

    @patch('requests.get')
    def test_multiple_hrefs(self, mock_get):
        # Simulating a page with multiple <a href=...> tags
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'<html><body><a href="https://example.com/page1">Link 1</a><a href="https://example.com/page2">Link 2</a><a href="https://example.com/page3">Link 3</a></body></html>'
        mock_get.return_value = mock_response

        url = "https://example.com"
        expected_hrefs = ["https://example.com/page1", "https://example.com/page2", "https://example.com/page3"]

        result = download_url_and_get_all_hrefs(url)

        self.assertEqual(result, expected_hrefs)

    @patch('requests.get')
    def test_empty_response(self, mock_get):
        # Simulating an empty page with no content
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b''
        mock_get.return_value = mock_response

        url = "https://example.com"
        expected_hrefs = []

        result = download_url_and_get_all_hrefs(url)

        self.assertEqual(result, expected_hrefs)


if __name__ == '__main__':
    unittest.main()
