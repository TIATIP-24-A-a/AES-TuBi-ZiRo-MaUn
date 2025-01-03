import unittest

from AES import split_blocks


class AesTestCase(unittest.TestCase):
    def test_to_blocks_must_return_blocks(self):
        text = 'Hallo ich binnnnHallo ich binnnnHallo ich binnnnHallo ich binnnn'
        expected = [
            'Hallo ich binnnn',
            'Hallo ich binnnn',
            'Hallo ich binnnn',
            'Hallo ich binnnn',
        ]

        result = split_blocks(text)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
