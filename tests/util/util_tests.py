import unittest

from owlapy.util import str_compare_to


class TestUtil(unittest.TestCase):

    def test_get_annotation_axioms(self):
        self.fail()  # OWLOntology needs to be implemented first

    def test_get_annotations(self):
        self.fail()  # OWLOntology needs to be implemented first

    def test_str_compare_to_01(self):
        """same str"""
        str1 = 'abcdefghij'
        self.assertEqual(0, str_compare_to(str1, str1))

    def test_str_compare_to_02(self):
        """same substring, differing length"""
        str1 = 'abcdef'
        str2 = 'abcdefghij'
        self.assertEqual(-4, str_compare_to(str1, str2))

    def test_str_compare_to_03(self):
        """same substring, differing length"""
        str1 = 'abcdefghij'
        str2 = 'abcdef'
        self.assertEqual(4, str_compare_to(str1, str2))

    def test_str_compare_to_04(self):
        """different str, same prefix, different length"""
        str1 = 'abchij'  # ord('h') = 104
        str2 = 'abcdefg'  # ord('d') = 100

        self.assertEqual(4, str_compare_to(str1, str2))

    def test_str_compare_to_05(self):
        """completely different str"""
        str1 = 'hjkluiop'  # ord('h') = 104
        str2 = 'rtuipo'  # ord('r') = 114

        self.assertEqual(-10, str_compare_to(str1, str2))
