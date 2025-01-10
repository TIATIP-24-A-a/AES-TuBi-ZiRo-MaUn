import unittest
from os import urandom

from AES import split_blocks, sub_word, shift_rows, mix_columns, add_round_key, key_expansion, rot_word, bytes_to_matrix


class AesTestCase(unittest.TestCase):
    def test_split_blocks_must_return_correct_blocks(self):
        text = b"Hallo ich binnnnI'm a 4x4 Matrix"
        expected_block_len = 2
        expected_first_block = [
            [ord('H'), ord('o'), ord('h'), ord('n')],
            [ord('a'), ord(' '), ord(' '), ord('n')],
            [ord('l'), ord('i'), ord('b'), ord('n')],
            [ord('l'), ord('c'), ord('i'), ord('n')]
        ]
        expected_second_block = [
            [ord('I'), ord('a'), ord('4'), ord('t')],
            [ord("'"), ord(' '), ord(' '), ord('r')],
            [ord('m'), ord('4'), ord('M'), ord('i')],
            [ord(' '), ord('x'), ord('a'), ord('x')]
        ]


        result = split_blocks(text)
        result_block_len = len(result)

        self.assertEqual(expected_block_len, result_block_len)
        self.assertEqual(expected_first_block, result[0])
        self.assertEqual(expected_second_block, result[1])


    def test_split_blocks_must_return_last_block_with_padding(self):
        text = b'Hallo ich binnnn 123'
        expected_last_block = [
            [ord(' '), ord(' '), ord(' '), ord(' ')],
            [ord('1'), ord(' '), ord(' '), ord(' ')],
            [ord('2'), ord(' '), ord(' '), ord(' ')],
            [ord('3'), ord(' '), ord(' '), ord(' ')]
        ]

        result = split_blocks(text)
        result_last_block = result[-1]

        self.assertEqual(expected_last_block, result_last_block)

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

    def test_sub_word(self):
        word = [65, 66, 67, 68]
        expected = [131, 44, 26, 27]

        result = sub_word(word)

        self.assertEqual(expected, result)

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


class KeyExpansionTestCase(unittest.TestCase):
    def test_key_expansion_return_11_keys(self):
        key = urandom(16)
        expected = 11

        result = key_expansion(key)

        self.assertEqual(expected, len(result))

    def test_key_expansion_expect_44_words_total(self):
        key = b'Hallo ich binnnn'
        expected = 44

        round_keys = key_expansion(key)
        total_words_len = 0

        for words in round_keys:
            total_words_len += len(words)

        self.assertEqual(expected, total_words_len)

    def test_key_expansion_input_must_occur_first(self):
        key = b'Hallo ich binnnn'
        expected = [
            [72, 111, 104, 110],
            [97, 32, 32, 110],
            [108, 105, 98, 110],
            [108, 99, 105, 110]
        ]

        result = key_expansion(key)
        first_key = result[0]

        self.assertEqual(expected, first_key)

if __name__ == '__main__':
    unittest.main()
