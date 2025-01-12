from os import urandom
import pytest

from AES import matrix_to_bytes, split_blocks, sub_word, shift_rows, mix_columns, add_round_key, key_expansion, rot_word, \
    bytes_to_matrix, sub_bytes


class TestAes:
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

        assert expected_block_len == result_block_len
        assert expected_first_block == result[0]
        assert expected_second_block == result[1]


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

        assert expected_last_block == result_last_block


    rot_word_testdata = [
        (['a', 'b', 'c', 'd'], ['b', 'c', 'd', 'a']),
        (['Hallo', 'ich', 'bin', 'ein', 'Test'], ['ich', 'bin', 'ein', 'Test', 'Hallo'])
    ]
    @pytest.mark.parametrize('input, expected', rot_word_testdata)
    def test_rot_word(self, input, expected):
        result = rot_word(input)
        assert expected == result

    sub_word_testdata = [
        ([65, 66, 67, 68], [131, 44, 26, 27]),
        ([0x25, 0xfe, 0x51, 0x32], [0x3f, 0xbb, 0xd1, 0x23])
    ]
    @pytest.mark.parametrize('input, expected', sub_word_testdata)
    def test_sub_word(self, input, expected):
        result = sub_word(input)
        assert expected == result

    def test_sub_bytes(self):
        block = [
            [0x52, 0xef, 0x50, 0x50],
            [0xa8, 0xb7, 0xf9, 0xfb],
            [0x45, 0xb7, 0xaa, 0xf9],
            [0x9f, 0x9f, 0x9f, 0x9f]
        ]
        expected = [
            [0x00, 0xdf, 0x53, 0x53],
            [0xc2, 0xa9, 0x99, 0x0f],
            [0x6e, 0xa9, 0xac, 0x99],
            [0xdb, 0xdb, 0xdb, 0xdb]
        ]

        result = sub_bytes(block)

        assert expected == result

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

        assert expected == result

    def test_mix_columns(self):
        block = [
            [0x52, 0xef, 0x50, 0x50],
            [0xa8, 0xb7, 0xf9, 0xfb],
            [0x45, 0xb7, 0xaa, 0xf9],
            [0x9f, 0x9f, 0x9f, 0x9f]
        ]
        expected = [
            [0x1de, 0x2fc, 0x292, 0x2e3],
            [0x154, 0x18e, 0x13e, 0xf1],
            [0x8e, 0x18e, 0xa0, 0xed],
            [0xa0, 0x1be, 0x154, 0x1a5]
        ]

        result = mix_columns(block)

        assert expected == result

    def test_add_round_key(self):
        state = [
            [ord('H'), ord('o'), ord('h'), ord('1')],
            [ord('a'), ord(' '), ord(' '), ord('2')],
            [ord('l'), ord('i'), ord('i'), ord('3')],
            [ord('l'), ord('c'), ord('n'), ord('4')]
        ]
        key = [
            [ord('m'), ord('u'), ord(' '), ord('r')],
            [ord('y'), ord('p'), ord('s'), ord('e')],
            [ord(' '), ord('e'), ord('e'), ord('t')],
            [ord('s'), ord('r'), ord('c'), ord(' ')]
        ]
        expected = [
            [ord('%'), ord('\x1a'), ord('H'), ord('C')],
            [ord('\x18'), ord('P'), ord('S'), ord('W')],
            [ord('L'), ord('\x0c'), ord('\x0c'), ord('G')],
            [ord('\x1f'), ord('\x11'), ord('\x0d'), ord('\x14')]
        ]

        result = add_round_key(state, key)

        assert expected == result

    def test_bytes_to_matrix_should_raise_error_when_not_16_bytes(self):
        with pytest.raises(ValueError):
            value = urandom(15)
            bytes_to_matrix(value)

    def test_bytes_to_matrx_should_return_matrix(self):
        value = b'ABCDEFGHIJKLMNOP'
        expected = [
            [65, 69, 73, 77],
            [66, 70, 74, 78],
            [67, 71, 75, 79],
            [68, 72, 76, 80]
        ]

        result = bytes_to_matrix(value)

        assert expected == result

    def test_matrix_to_bytes(self):
        matrix = [
            [ord('A'), ord('E'), ord('I'), ord('M')],
            [ord('B'), ord('F'), ord('J'), ord('N')],
            [ord('C'), ord('G'), ord('K'), ord('O')],
            [ord('D'), ord('H'), ord('L'), ord('P')]
        ]
        expected = b'ABCDEFGHIJKLMNOP'

        result = matrix_to_bytes(matrix)

        assert expected == result


class TestKeyExpansion:
    def test_key_expansion_return_11_keys(self):
        key = urandom(16)
        expected = 11

        result = key_expansion(key)

        assert expected == len(result)

    def test_key_expansion_expect_44_words_total(self):
        key = b'Hallo ich binnnn'
        expected = 44

        round_keys = key_expansion(key)
        total_words_len = 0

        for words in round_keys:
            total_words_len += len(words)

        assert expected == total_words_len

    def test_key_expansion_has_correct_first_and_last_key(self):
        key = b'This is a key123'
        expected_first_key = [
            [ord('T'), ord(' '), ord('a'), ord('y')],
            [ord('h'), ord('i'), ord(' '), ord('1')],
            [ord('i'), ord('s'), ord('k'), ord('2')],
            [ord('s'), ord(' '), ord('e'), ord('3')]
        ]
        expected_last_key = [
            [ord('\xe2'), ord('F'), ord('!'), ord('\x02')],
            [ord('H'), ord('\xc0'), ord('P'), ord('\xc3')],
            [ord('\xac'), ord('\x8e'), ord('E'), ord('~')],
            [ord('\x92'), ord('g'), ord('\xd8'), ord('f')]
        ]

        result = key_expansion(key)
        first_key = result[0]
        last_key = result[-1]

        assert expected_first_key == first_key
        assert expected_last_key == last_key
