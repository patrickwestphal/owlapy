import unittest

from owlapy.model import NodeID
from owlapy.model import IRI


class TestNodeID(unittest.TestCase):
    def test___init__01(self):
        target_id = '_:23'
        node_id = NodeID('34')
        self.assertFalse(node_id.id == target_id)

    def test___init__02(self):
        target_id = '_:23'
        node_id = NodeID('23')
        self.assertTrue(node_id.id == target_id)

    def test___init__03(self):
        target_id = '_:23'
        node_id = NodeID('_:23')
        self.assertTrue(node_id.id == target_id)

    def test___eq__01(self):
        """node ID vs. None --> False"""
        node_id = NodeID('23')
        self.assertFalse(node_id == None)

    def test___eq__02(self):
        """None vs. node ID --> False"""
        node_id = NodeID('23')
        self.assertFalse(None == node_id)

    def test___eq__03(self):
        """node ID vs. arbitrary object --> False"""
        node_id = NodeID('23')
        not_a_node_id = 23
        self.assertFalse(node_id == not_a_node_id)

    def test___eq__04(self):
        """arbitrary object vs. node ID --> False"""
        not_a_node_id = 23
        node_id = NodeID('23')
        self.assertFalse(not_a_node_id == node_id)

    def test___eq__05(self):
        """node ID vs. node ID (differing IDs) --> False"""
        node_id1 = NodeID('23')
        node_id2 = NodeID('5')
        self.assertFalse(node_id1 == node_id2)

    def test___eq__06(self):
        """node ID vs. node ID (same IDs) --> True"""
        node_id1 = NodeID('23')
        node_id2 = NodeID('23')
        self.assertTrue(node_id1 == node_id2)

    def test___eq__07(self):
        """node ID vs. node ID (same objects) --> True"""
        node_id1 = NodeID('23')
        self.assertTrue(node_id1 == node_id1)

    def test___str___(self):
        prefix = NodeID._prefix
        id_str = prefix + '23'
        node_id = NodeID(id_str)
        self.assertEqual(id_str, str(node_id))

    def test_node_string(self):
        prefix_node = NodeID._prefix_node  # _:genid
        node_id = 23
        self.assertEqual(prefix_node + str(23), NodeID.node_string(node_id))

    def test_get_iri_from_node_id(self):
        node_id_prefix = NodeID._node_id_prefix  # genid
        prefix_shared_node = NodeID._prefix_shared_node  # genid-nodeid-
        node_id = 23
        node_id_str = node_id_prefix + str(node_id)  # genid23
        node_iri = prefix_shared_node + str(node_id)  # _:genid-nodeid-23
        self.assertEqual(node_iri, NodeID.get_iri_from_node_id(node_id_str))

    def test_next_anonymous_iri(self):
        NodeID._counter = 1
        prefix_node = NodeID._prefix_node
        iri1 = NodeID.next_anonymous_iri()
        self.assertTrue(iri1.endswith(prefix_node + '1'))

        iri2 = NodeID.next_anonymous_iri()
        self.assertTrue(iri2.endswith(prefix_node + '2'))

        iri3 = NodeID.next_anonymous_iri()
        self.assertTrue(iri3.endswith(prefix_node + '3'))

    def test_is_anonymous_node_iri_01(self):
        self.assertFalse(NodeID.is_anonymous_node_iri(None))

    def test_is_anonymous_node_iri_02(self):
        self.assertFalse(NodeID.is_anonymous_node_iri('I am not an IRI!'))

    def test_is_anonymous_node_iri_03(self):
        prefix = NodeID._prefix  # _:
        not_a_node_iri = prefix + str(23)
        self.assertFalse(NodeID.is_anonymous_node_iri(not_a_node_iri))

    def test_is_anonymous_node_iri_04(self):
        prefix = NodeID._prefix  # _:
        node_id_prefix = NodeID._node_id_prefix  # genid
        not_a_node_iri = prefix + node_id_prefix + str(23)
        self.assertTrue(NodeID.is_anonymous_node_iri(not_a_node_iri))

    def test_is_anonymous_node_iri_05(self):
        prefix = NodeID._prefix  # _:
        node_id_prefix = NodeID._node_id_prefix  # genid
        not_a_node_iri = prefix + node_id_prefix + 'blablah' + str(23)
        self.assertTrue(NodeID.is_anonymous_node_iri(not_a_node_iri))

    def test_is_anonymous_node_iri_06(self):
        iri = IRI('http://ex.org/sth')
        self.assertFalse(NodeID.is_anonymous_node_iri(iri))

    def test_is_anonymous_node_iri_07(self):
        prefix = NodeID._prefix
        iri = IRI(prefix + '23')
        self.assertFalse(NodeID.is_anonymous_node_iri(iri))

    def test_is_anonymous_node_iri_08(self):
        prefix = NodeID._prefix
        node_id_prefix = NodeID._node_id_prefix
        iri = IRI(prefix + node_id_prefix + '23')
        self.assertTrue(NodeID.is_anonymous_node_iri(iri))

    def test_is_anonymous_node_id_01(self):
        self.assertFalse(NodeID.is_anonymous_node_id(None))

    def test_is_anonymous_node_id_02(self):
        prefix = NodeID._prefix
        node_id_str = prefix + '23'
        self.assertFalse(NodeID.is_anonymous_node_id(node_id_str))

    def test_is_anonymous_node_id_03(self):
        prefix_shared_node = NodeID._prefix_shared_node
        node_id_str = prefix_shared_node + 'lalala' + '23'
        self.assertTrue(NodeID.is_anonymous_node_id(node_id_str))

    def test_get_node_id_01(self):
        node_id_prefix = NodeID._node_id_prefix
        NodeID._counter = 1
        gen_node_id = NodeID.get_node_id(None)
        node_id = NodeID(node_id_prefix + '1')
        self.assertEqual(node_id, gen_node_id)

        gen_node_id = NodeID.get_node_id(None)
        node_id = NodeID(node_id_prefix + '2')
        self.assertEqual(node_id, gen_node_id)

        gen_node_id = NodeID.get_node_id(None)
        node_id = NodeID(node_id_prefix + '3')
        self.assertEqual(node_id, gen_node_id)

    def test_get_node_id_02(self):
        gen_node_id = NodeID.get_node_id('23')
        node_id = NodeID('23')
        self.assertEqual(node_id, gen_node_id)

    def test_compare_to_01(self):
        """same node ID str --> 0"""
        node_id1 = NodeID('23')
        node_id2 = NodeID('23')
        self.assertEqual(0, node_id1.compare_to(node_id2))

    def test_compare_to_02(self):
        """same generated node ID str --> 0"""
        node_id1 = NodeID('_:23')
        node_id2 = NodeID('23')
        self.assertEqual(0, node_id1.compare_to(node_id2))

    def test_compare_to_03(self):
        """same generated node ID str --> 0"""
        node_id1 = NodeID('23')
        node_id2 = NodeID('_:23')
        self.assertEqual(0, node_id1.compare_to(node_id2))

    def test_compare_to_04(self):
        """different length --> length difference"""
        id_str1 = '_:23lala'
        len_id_str1 = len(id_str1)
        node_id1 = NodeID(id_str1)
        id_str2 = '_:23'
        len_id_str2 = len(id_str2)
        node_id2 = NodeID(id_str2)
        diff = len_id_str1- len_id_str2  # 4
        self.assertEqual(diff, node_id1.compare_to(node_id2))

    def test_compare_to_05(self):
        """different length --> length difference"""
        id_str1 = '_:23'
        len_id_str1 = len(id_str1)
        node_id1 = NodeID(id_str1)
        id_str2 = '_:23lala'
        len_id_str2 = len(id_str2)
        node_id2 = NodeID(id_str2)
        diff = len_id_str1- len_id_str2  # -4
        self.assertEqual(diff, node_id1.compare_to(node_id2))

    def test_compare_to_06(self):
        """different chars --> char difference"""
        id_str1 = '_:23a'
        diff_char_int_id_str1 = ord('a')  # 97
        node_id1 = NodeID(id_str1)
        id_str2 = '_:23z'
        diff_char_int_id_str2 = ord('z')  # 122
        node_id2 = NodeID(id_str2)
        diff = diff_char_int_id_str1 - diff_char_int_id_str2 # -25
        self.assertEqual(diff, node_id1.compare_to(node_id2))

    def test_compare_to_07(self):
        """different chars --> char difference"""
        id_str1 = '_:23z'
        diff_char_int_id_str1 = ord('z')  # 122
        node_id1 = NodeID(id_str1)
        id_str2 = '_:23a'
        diff_char_int_id_str2 = ord('a')  # 97
        node_id2 = NodeID(id_str2)
        diff = diff_char_int_id_str1 - diff_char_int_id_str2 # 25
        self.assertEqual(diff, node_id1.compare_to(node_id2))

    def test___hash__(self):
        id_str1 = '_:23'
        id_str1_hash  = hash(id_str1)
        node_id1 = NodeID(id_str1)
        self.assertEqual(id_str1_hash, hash(node_id1))
