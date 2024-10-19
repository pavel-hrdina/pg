import unittest
from unittest.mock import patch

from first import sude_nebo_liche  # Import the function from first.py


class TestSudeNeboLiche(unittest.TestCase):

    @patch('builtins.print')  # Patch the print function
    def test_sude(self, mock_print):
        sude_nebo_liche(1000)
        mock_print.assert_called_once_with("1000 je sudé.")

    @patch('builtins.print')  # Patch the print function
    def test_liche(self, mock_print):
        sude_nebo_liche(5)
        mock_print.assert_called_once_with("5 je liché.")


if __name__ == "__main__":
    unittest.main()
