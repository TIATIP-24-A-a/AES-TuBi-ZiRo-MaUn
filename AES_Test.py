import unittest

from AES import split_blocks, sub_word, shift_rows, mix_columns


class AesTestCase(unittest.TestCase):
    def test_split_blocks_must_return_16_bytes_blocks(self):
        text = 'Hallo ich binnnnHallo ich binnnnHallo ich binnnnHallo ich binnnn'
        expected = [
            b'Hallo ich binnnn',
            b'Hallo ich binnnn',
            b'Hallo ich binnnn',
            b'Hallo ich binnnn',
        ]
        result = split_blocks(text)

        self.assertEqual(result, expected)

    def test_split_blocks_must_return_16_bytes_blocks_with_pad_bytes(self):
        text = 'Hallo ich binnnnHallo ich binnnn 123'
        expected = [
            b'Hallo ich binnnn',
            b'Hallo ich binnnn',
            b' 123            ',
        ]
        result = split_blocks(text)

        self.assertEqual(result, expected)

    def test_subword(self):
        block = b'Hallo ich binnnn'
        expected = [
            82,
            239,
            80,
            80,
            168,
            183,
            249,
            251,
            69,
            183,
            170,
            249,
            159,
            159,
            159,
            159
        ]
        result = sub_word(block)

        self.assertEqual(result, expected)

    def test_shift_rows(self):
        block = [
            'Hall',
            'o ic',
            'h bi',
            'nnnn'
        ]
        expected = [
            'Hall',
            ' ico',
            'bih ',
            'nnnn'
        ]
        result = shift_rows(block)

        self.assertEqual(result, expected)

    def test_mix_columns(self):
        block = [
            [82, 239, 80, 80],
            [168, 183, 249, 251],
            [69, 183, 170, 249],
            [159, 159, 159, 159]
        ]
        expected = [
            [478, 764, 658, 739],
            [340, 398, 318, 241],
            [142, 398, 160, 237],
            [160, 446, 340, 421]
        ]
        result = mix_columns(block)

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
