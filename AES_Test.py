import unittest
from os import urandom

from AES import split_blocks, sub_word, shift_rows, mix_columns, add_round_key, key_expansion, rot_word, bytes_to_matrix


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

    def test_rotate_word_with_chars(self):
        input = ['a', 'b', 'c', 'd']
        expected = ['b', 'c', 'd', 'a']

        result = rot_word(input)

        self.assertEqual(expected, result)

    def test_rotate_word_with_words(self):
        input = ['Hallo', 'ich', 'bin', 'ein', 'Test']
        expected = ['ich', 'bin', 'ein', 'Test', 'Hallo']

        result = rot_word(input)

        self.assertEqual(expected, result)

    def test_key_expansion_return_11_keys(self):
        key = 'Hallo ich bin ein Mensch'
        expected = 11

        result = key_expansion(key)

        self.assertEqual(expected, len(result))

    def test_key_expansion_expect_16bytes_key(self):
        key = 'Hallo ich binnnn'

        result = key_expansion(key)
        for i in result:
            self.assertEqual(len(i), 16)

    def test_key_expansion_input_must_occur_first(self):
        key = 'Hallo ich binnnn'
        expected = key.encode()

        result = key_expansion(key)

        self.assertEqual(expected, result[0])

    def test_key_expansion_result_must_be_unique_for_all_elements(self):
        key = 'Hallo ich binnnn'
        expected = 11

        result = key_expansion(key)
        unique_result_len = len(set(result))

        self.assertEqual(expected, unique_result_len)

    def test_sub_word(self):
        word = [65, 66, 67, 68]
        expected = [131, 44, 26, 27]

        result = sub_word(word)

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

    def test_add_round_key(self):
        state = [
            [b'Hall'],
            [b'o ic'],
            [b'h in'],
            [b'1234'],
        ]
        key = [
            [b'aaaa'],
            [b'aaaa'],
            [b'aaaa'],
            [b'aaaa'],
        ]
        expected = [
            [b')\x00\r\r'],
            [b'\x0eA\x08\x02'],
            [b'\tA\x08\x0f'],
            [b'PSRU']
        ]

        result = add_round_key(state, key)

        self.assertEqual(expected, result)

    def test_bytes_to_matrix_should_raise_error_when_not_16_bytes(self):
        value = urandom(15)
        self.assertRaises(ValueError, bytes_to_matrix, value)

    def test_bytes_to_matrx_should_return_matrix(self):
        value = b'ABCDEFGHIJKLMNOP'
        expected = [
            [65, 69, 73, 77],
            [66, 70, 74, 78],
            [67, 71, 75, 79],
            [68, 72, 76, 80]
        ]

        result = bytes_to_matrix(value)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
