import unittest

from owlapy.model import NodeID
from owlapy.model import OWLAnonymousIndividual
from owlapy.model import OWLObjectVisitor
from owlapy.model import OWLObjectVisitorEx
from owlapy.model import OWLRuntimeException


class TestOWLAnonymousIndividual(unittest.TestCase):
    def test___init__(self):
        node_id = NodeID('23')
        anon_indiv = OWLAnonymousIndividual(node_id)

        self.assertEqual(node_id, anon_indiv.id)

    def test___str__(self):
        node_id = NodeID('23')
        anon_indiv = OWLAnonymousIndividual(node_id)

        self.assertEqual(str(node_id), str(anon_indiv))

    def test___repr__(self):
        node_id = NodeID('23')
        anon_indiv = OWLAnonymousIndividual(node_id)

        self.assertEqual(node_id.__repr__(), anon_indiv.__repr__())

    def test___eq__01(self):
        """anon indiv. vs. None --> False"""
        node_id = NodeID('23')
        anon_indiv = OWLAnonymousIndividual(node_id)
        self.assertFalse(anon_indiv is None)

    def test___eq__02(self):
        """None vs. anon indiv. --> False"""
        node_id = NodeID('23')
        anon_indiv = OWLAnonymousIndividual(node_id)
        self.assertFalse(None == anon_indiv)

    def test___eq__03(self):
        """anon indiv. vs.  arbitrary object --> False"""
        node_id = NodeID('23')
        anon_indiv = OWLAnonymousIndividual(node_id)
        not_an_anon_indiv = 23
        self.assertFalse(anon_indiv == not_an_anon_indiv)

    def test___eq__04(self):
        """arbitrary object vs. anon indiv --> False"""
        not_an_anon_indiv = 23
        node_id = NodeID('23')
        anon_indiv = OWLAnonymousIndividual(node_id)
        self.assertFalse(not_an_anon_indiv == anon_indiv)

    def test___eq__05(self):
        """anon indiv vs. anon indiv (differing node IDs) --> False"""
        node_id1 = NodeID('23')
        anon_indiv1 = OWLAnonymousIndividual(node_id1)
        node_id2 = NodeID('42')
        anon_indiv2 = OWLAnonymousIndividual(node_id2)

        self.assertFalse(anon_indiv1 == anon_indiv2)

    def test___eq__06(self):
        """anon indiv vs. anon indiv (same node ID strs) --> True"""
        node_id1 = NodeID('23')
        anon_indiv1 = OWLAnonymousIndividual(node_id1)
        node_id2 = NodeID('23')
        anon_indiv2 = OWLAnonymousIndividual(node_id2)

        self.assertTrue(anon_indiv1 == anon_indiv2)

    def test___eq__07(self):
        """anon indiv vs. anon indiv (same node IDs) --> True"""
        node_id = NodeID('23')
        anon_indiv1 = OWLAnonymousIndividual(node_id)
        anon_indiv2 = OWLAnonymousIndividual(node_id)

        self.assertTrue(anon_indiv1 == anon_indiv2)

    def test___eq__08(self):
        """anon indiv vs. same anon indiv --> True"""
        node_id = NodeID('23')
        anon_indiv = OWLAnonymousIndividual(node_id)

        self.assertTrue(anon_indiv == anon_indiv)

    def test___hash__(self):
        node_id = NodeID('23')
        node_id_hash = hash(node_id)
        anon_indiv = OWLAnonymousIndividual(node_id)

        self.assertTrue(node_id_hash == hash(anon_indiv))

    def test_is_named(self):
        anon_indiv = OWLAnonymousIndividual(NodeID('23'))
        self.assertFalse(anon_indiv.is_named())

    def test_is_anonymous(self):
        anon_indiv = OWLAnonymousIndividual(NodeID('23'))
        self.assertTrue(anon_indiv.is_anonymous())

    def test_as_owl_named_individual(self):
        anon_indiv = OWLAnonymousIndividual(NodeID('23'))
        self.assertRaises(OWLRuntimeException,
                          OWLAnonymousIndividual.as_owl_named_individual,
                          anon_indiv)

    def test_as_owl_anonymous_individual(self):
        anon_indiv = OWLAnonymousIndividual(NodeID('23'))
        self.assertEqual(anon_indiv, anon_indiv.as_owl_anonymous_individual())

    def test__compare_object_of_same_type_01(self):
        """same node ID --> 0"""
        anon_indiv1 = OWLAnonymousIndividual(NodeID('23'))
        anon_indiv2 = OWLAnonymousIndividual(NodeID('23'))

        self.assertEqual(0,
                         anon_indiv1._compare_object_of_same_type(anon_indiv2))

    def test__compare_object_of_same_type_02(self):
        """2nd node ID str 4 chars longer --> -4"""
        anon_indiv1 = OWLAnonymousIndividual(NodeID('23'))
        anon_indiv2 = OWLAnonymousIndividual(NodeID('23lala'))

        self.assertEqual(-4,
                         anon_indiv1._compare_object_of_same_type(anon_indiv2))

    def test__compare_object_of_same_type_03(self):
        """1st node ID str 4 chars longer --> 4"""
        anon_indiv1 = OWLAnonymousIndividual(NodeID('23lala'))
        anon_indiv2 = OWLAnonymousIndividual(NodeID('23'))

        self.assertEqual(4,
                         anon_indiv1._compare_object_of_same_type(anon_indiv2))

    def test__compare_object_of_same_type_04(self):
        """differing char (a (97) vs. z (122) --> -25"""
        anon_indiv1 = OWLAnonymousIndividual(NodeID('23a'))
        anon_indiv2 = OWLAnonymousIndividual(NodeID('23z'))

        self.assertEqual(-25,
                         anon_indiv1._compare_object_of_same_type(anon_indiv2))

    def test_accept_01(self):
        """visitor without return value for visit method"""
        class DummyVisitor(OWLObjectVisitor):
            def __init__(self):
                self.called = False

            def visit(self, visitee):
                self.called = True

        visitor = DummyVisitor()
        self.assertFalse(visitor.called)

        anon_indiv = OWLAnonymousIndividual(NodeID('23'))
        res = anon_indiv.accept(visitor)

        self.assertTrue(visitor.called)
        self.assertTrue(res is None)
    
    def test_accept_02(self):
        """visitor without return value for visit method"""
        class DummyVisitor(OWLObjectVisitorEx):
            def __init__(self):
                self.called = False

            def visit(self, visitee):
                self.called = True
                return 23

        visitor = DummyVisitor()
        self.assertFalse(visitor.called)

        anon_indiv = OWLAnonymousIndividual(NodeID('23'))
        res = anon_indiv.accept(visitor)

        self.assertTrue(visitor.called)
        self.assertEqual(23, res)

    def test_accept_03(self):
        anon_indiv = OWLAnonymousIndividual(NodeID('23'))
        self.assertRaises(OWLRuntimeException, OWLAnonymousIndividual.accept,
                          anon_indiv, 23)
