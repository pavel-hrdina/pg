import os
import unittest
from tempfile import NamedTemporaryFile

from fifth import read_header, is_jpeg, is_gif, is_png


class TestImageTypeChecker(unittest.TestCase):
    def setUp(self):
        # Create temporary test files for each image type
        self.test_files = []

        # Create a JPEG test file
        self.jpeg_file = NamedTemporaryFile(delete=False)
        self.jpeg_file.write(b'\xff\xd8\xff\xe0some jpeg content')
        self.jpeg_file.close()
        self.test_files.append(self.jpeg_file.name)

        # Create a GIF87a test file
        self.gif87_file = NamedTemporaryFile(delete=False)
        self.gif87_file.write(b'GIF87asome gif content')
        self.gif87_file.close()
        self.test_files.append(self.gif87_file.name)

        # Create a GIF89a test file
        self.gif89_file = NamedTemporaryFile(delete=False)
        self.gif89_file.write(b'GIF89asome gif content')
        self.gif89_file.close()
        self.test_files.append(self.gif89_file.name)

        # Create a PNG test file
        self.png_file = NamedTemporaryFile(delete=False)
        self.png_file.write(b'\x89PNG\r\n\x1a\nsome png content')
        self.png_file.close()
        self.test_files.append(self.png_file.name)

        # Create an invalid image file
        self.invalid_file = NamedTemporaryFile(delete=False)
        self.invalid_file.write(b'invalid content')
        self.invalid_file.close()
        self.test_files.append(self.invalid_file.name)

    def tearDown(self):
        # Clean up temporary files after tests
        for file_name in self.test_files:
            try:
                os.unlink(file_name)
            except:
                pass

    def test_read_header(self):
        """Test if read_header correctly reads specified number of bytes"""
        test_content = read_header(self.jpeg_file.name, 2)
        self.assertEqual(test_content, b'\xff\xd8')

        test_content = read_header(self.png_file.name, 8)
        self.assertEqual(test_content, b'\x89PNG\r\n\x1a\n')

    def test_is_jpeg(self):
        """Test JPEG detection"""
        self.assertTrue(is_jpeg(self.jpeg_file.name))
        self.assertFalse(is_jpeg(self.gif87_file.name))
        self.assertFalse(is_jpeg(self.png_file.name))
        self.assertFalse(is_jpeg(self.invalid_file.name))

    def test_is_gif(self):
        """Test GIF detection for both GIF87a and GIF89a"""
        self.assertTrue(is_gif(self.gif87_file.name))
        self.assertTrue(is_gif(self.gif89_file.name))
        self.assertFalse(is_gif(self.jpeg_file.name))
        self.assertFalse(is_gif(self.png_file.name))
        self.assertFalse(is_gif(self.invalid_file.name))

    def test_is_png(self):
        """Test PNG detection"""
        self.assertTrue(is_png(self.png_file.name))
        self.assertFalse(is_png(self.jpeg_file.name))
        self.assertFalse(is_png(self.gif87_file.name))
        self.assertFalse(is_png(self.invalid_file.name))

    def test_nonexistent_file(self):
        """Test handling of non-existent files"""
        with self.assertRaises(Exception):
            read_header("nonexistent_file.jpg", 2)
