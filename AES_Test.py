import unittest

from AES import split_blocks


class AesTestCase(unittest.TestCase):
    def test_split_blocks_must_return_16_bytes_blocks(self):
        text = 'Hallo ich binnnnHallo ich binnnnHallo ich binnnnHallo ich binnnn'
        expected = [
            'Hallo ich binnnn',
            'Hallo ich binnnn',
            'Hallo ich binnnn',
            'Hallo ich binnnn',
        ]
        result = split_blocks(text)

        self.assertEqual(result, expected)

    def test_split_blocks_must_return_16_bytes_blocks_with_pad_bytes(self):
        text = 'Hallo ich binnnnHallo ich binnnn 123'
        expected = [
            'Hallo ich binnnn',
            'Hallo ich binnnn',
            ' 123            ',
        ]
        result = split_blocks(text)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
