import unittest
from KeyExpansion import rot_word

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

        self.assertEqual(expected, result.len())

if __name__ == '__main__':
    unittest.main()
