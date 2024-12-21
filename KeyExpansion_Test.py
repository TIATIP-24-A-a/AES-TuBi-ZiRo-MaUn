import unittest
from KeyExpansion import rot_word, key_expansion
import numpy as np


class KeyExpansionTestCase(unittest.TestCase):
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
        input = 'Hallo ich bin ein Mensch'
        expected = 11

        result = key_expansion(input)

        self.assertEqual(expected, len(result))

    def test_key_expansion_expect_16bytes_key(self):
        input = 'Hallo ich binnnn'

        result = key_expansion(input)
        for i in result:
            self.assertEqual(len(i), 16)

    def test_key_expansion_input_must_occur_first(self):
        input = 'Hallo ich binnnn'

        result = key_expansion(input)
        self.assertEqual(result [0], input)

    def test_key_expansion_result_must_be_unique_for_all_elements(self):
        input = 'Hallo ich binnnn'

        result = key_expansion(input)
        uniqueResult = set(result)

        self.assertEqual(len(uniqueResult), 11)

if __name__ == '__main__':
    unittest.main()
