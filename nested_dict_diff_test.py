import unittest
from nested_dict_diff import nested_dict_diff

__author__ = 'yury_gnutov'



class NestedDictDiffTest(unittest.TestCase):

    # @unittest.skip("")
    def test_flat_dict_equal(self):
        first = {'a': 1, 'b': 2}
        second = {'a': 1, 'b': 2}
        self.assertEqual(nested_dict_diff(first, second), {})

    # @unittest.skip("")
    def test_flat_dict_equal_with_ignored_list(self):
        first = {'a': 1, 'b': 2}
        second = {'a': 1, 'b': 2, 'c': 3}
        ignored = ['c', ]
        self.assertEqual(nested_dict_diff(first, second, ignored), {})

    # @unittest.skip("")
    def test_flat_dict_key_missing_in_first(self):
        first = {'a': 1, 'b': 2}
        second = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(nested_dict_diff(first, second), {'c': 'key not found in first dict'})

    # @unittest.skip("")
    def test_flat_dict_key_missing_in_second(self):
        first = {'a': 1, 'b': 2, 'c': 3}
        second = {'a': 1, 'b': 2}
        self.assertEqual(nested_dict_diff(first, second), {'c': 'key not found in second dict'})

    # @unittest.skip("")
    def test_flat_dict_key_missing_first_with_ignored_list(self):
        first = {'a': 1, 'b': 2}
        second = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        ignored = ['c', ]
        self.assertEqual(nested_dict_diff(first, second, ignored), {'d': 'key not found in first dict'})

    # @unittest.skip("")
    def test_flat_dict_key_missing_second_with_ignored_list(self):
        first = {'a': 1, 'b': 2, 'd': 4}
        second = {'a': 1, 'b': 2, 'c': 3}
        ignored = ['c', ]
        self.assertEqual(nested_dict_diff(first, second, ignored), {'d': 'key not found in second dict'})

    # @unittest.skip("")
    def test_flat_dict_not_equal(self):
        first = {'a': 1, 'b': 3}
        second = {'a': 1, 'b': 2}
        self.assertEqual(nested_dict_diff(first, second), {'b': (3, 2)})

    # @unittest.skip("")
    def test_flat_dict_not_equal_with_ignore(self):
        first = {'a': 1, 'b': 3, 'c': 2}
        second = {'a': 1, 'b': 2, 'c': 3}
        ignored = ['c', ]
        self.assertEqual(nested_dict_diff(first, second, ignored), {'b': (3, 2)})

    # @unittest.skip("")
    def test_flat_dict_equal_float_string_list_turple_unicode_data(self):
        first = {'a': 1, 'b': 2.2, 'd': 'test', 'e': (1, 2), 'g': [1, "a"], 'h': u'_'}
        second = {'a': 1, 'b': 2.2, 'd': 'test', 'e': (1, 2), 'g': [1, "a"], 'h': u'_'}
        self.assertEqual(nested_dict_diff(first, second), {})

    # @unittest.skip("")
    def test_nested_equal(self):
        first = {'a': {'b': 1}}
        second = {'a': {'b': 1}}
        self.assertEqual(nested_dict_diff(first, second), {})

    # @unittest.skip("")
    def test_nested_equal_with_ignored(self):
        first = {'a': {'b': 1, 'ignored': 2}}
        second = {'a': {'b': 1}, 'ignored': 2}
        ignored = ['ignored', ]
        self.assertEqual(nested_dict_diff(first, second, ignored), {})

    # @unittest.skip("")
    def test_nested_not_equal(self):
        first = {'a': {'b': 1}}
        second = {'a': {'b': 2}}
        self.assertEqual(nested_dict_diff(first, second), {'b': (1, 2)})

    # @unittest.skip("")
    def test_nested_not_equal_with_ignored(self):
        first = {'a': {'b': 1, 'ignored': 2}}
        second = {'a': {'b': 2}, 'ignored': 3}
        ignored = ['ignored', ]
        self.assertEqual(nested_dict_diff(first, second, ignored), {'b': (1, 2)})

    # @unittest.skip("")
    def test_deep_nested_equal(self):
        first = {'a': {'b': [{'c': [{'d': [{'e': 1, 'f': 2}]}]}]}, 'b': 1}
        second = {'a': {'b': [{'c': [{'d': [{'e': 1, 'f': 2}]}]}]}, 'b': 1}
        self.assertEqual(nested_dict_diff(first, second), {})

    # @unittest.skip("")
    def test_deep_nested_not_equal(self):
        first = {'a': {'b': [{'c': [{'d': [{'e': 1, 'f': 3}]}]}]}, 'b': 1}
        second = {'a': {'b': [{'c': [{'d': [{'e': 1, 'f': 2}]}]}]}, 'b': 1}
        self.assertEqual(nested_dict_diff(first, second), {'f': (3, 2)})

    # @unittest.skip("")
    def test_deep_nested_equal_with_ignored(self):
        first = {'a': {'b': [{'c': [{'d': [{'e': 1, 'f': 2}]}]}]}}
        second = {'a': {'b': [{'c': [{'d': [{'e': 1}]}]}]}}
        ignored = ['f', ]
        self.assertEqual(nested_dict_diff(first, second, ignored), {})