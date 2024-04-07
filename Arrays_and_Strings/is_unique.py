# Implement an Algorithm to determine if a string has all unique characters.

import unittest


def is_unique(string):
    dict_ = {}
    for i in string:
        count = dict_.get(i, 0)
        count += 1
        dict_[i] = count
        if count > 1:
            print(dict_)
            return False
    print(dict_)
    return True


class UniteTest(unittest.TestCase):
    def test_unique_string(self):
        self.assertTrue(is_unique("abcdefg"))

    def test_non_unique_string(self):
        self.assertFalse(is_unique("hello"))

    def test_empty_string(self):
        self.assertTrue(is_unique(""))

    def test_string_with_spaces(self):
        self.assertFalse(is_unique("the quick brown fox"))

    def test_string_with_special_characters(self):
        self.assertTrue(is_unique("!@#$%^&*()"))


if __name__ == "__main__":
    unittest.main()
