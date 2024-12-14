import unittest

class KeyExpansionTestCase(unittest.TestCase):
    def test_rotate_word_with_chars(self):
        input = ['a', 'b', 'c', 'd']
        expected = ['b', 'c', 'd', 'a']

        result = rot_word(input)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
