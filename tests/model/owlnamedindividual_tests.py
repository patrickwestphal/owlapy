import unittest

from owlapy.model import IRI
from owlapy.model import OWLAnnotationProperty
from owlapy.model import OWLClass
from owlapy.model import OWLDataProperty
from owlapy.model import OWLDatatype
from owlapy.model import OWLNamedIndividual
from owlapy.model import OWLObject
from owlapy.model import OWLObjectProperty
from owlapy.model import OWLRuntimeException
from owlapy.model import OWLVisitorEx, OWLVisitor
from owlapy.model import EntityType


class TestOWLNamedIndividual(unittest.TestCase):

    def test___init___(self):
        iri = IRI('http://ex.org/sth')
        named_indiv = OWLNamedIndividual(iri)
        self.assertEqual(iri, named_indiv.iri)

    def test___str__(self):
        iri = IRI('http://ex.org/sth')
        named_indiv = OWLNamedIndividual(iri)
        self.assertEqual(str(iri), str(named_indiv))

    def test___repr__(self):
        iri = IRI('http://ex.org/sth')
        named_indiv = OWLNamedIndividual(iri)
        self.assertEqual(str(iri), named_indiv.__repr__())

    def test___eq__01(self):
        """named indiv vs. None --> False"""
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertNotEqual(named_indiv, None)

    def test___eq__02(self):
        """None vs. named indiv --> False"""
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertNotEqual(None, named_indiv)

    def test___eq__03(self):
        """named indiv vs. arbitrary object --> False"""
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertFalse(named_indiv == 23)

    def test___eq__04(self):
        """arbitrary object vs. named indiv--> False"""
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertFalse(23 == named_indiv)

    def test___eq__05(self):
        """named indiv vs. superclass object (differing IRI)--> False"""
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        obj = OWLObject()
        self.assertFalse(named_indiv == obj)

    def test___eq__06(self):
        """named indiv vs. named indiv (differing IRI) --> False"""
        named_indiv1 = OWLNamedIndividual(IRI('http://ex.org/sth'))
        named_indiv2 = OWLNamedIndividual(IRI('http://ex.org/sthElse'))
        self.assertFalse(named_indiv1 == named_indiv2)

    def test___eq__07(self):
        """named indiv vs. named indiv (same IRI) --> True"""
        named_indiv1 = OWLNamedIndividual(IRI('http://ex.org/sth'))
        named_indiv2 = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertTrue(named_indiv1 == named_indiv2)

    def test___eq__08(self):
        """named indiv vs. named indiv (same IRI) --> True"""
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertTrue(named_indiv == named_indiv)

    def test_is_named(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertTrue(named_indiv.is_named())

    def test_get_entity_type(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertEqual(EntityType.NAMED_INDIVIDUAL,
                         named_indiv.get_entity_type())

    def test_get_owl_entity_01(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))

        # named individual
        owl_entity = named_indiv.get_owl_entity(EntityType.NAMED_INDIVIDUAL)
        self.assertTrue(isinstance(owl_entity, OWLNamedIndividual))
        self.assertEqual(named_indiv.iri, owl_entity.iri)

    def test_get_owl_entity_02(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))

        # annotation property
        owl_entity = named_indiv.get_owl_entity(EntityType.ANNOTATION_PROPERTY)
        self.assertTrue(isinstance(owl_entity, OWLAnnotationProperty))
        self.assertEqual(named_indiv.iri, owl_entity.iri)

    def test_get_owl_entity_03(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))

        # class
        owl_entity = named_indiv.get_owl_entity(EntityType.CLASS)
        self.assertTrue(isinstance(owl_entity, OWLClass))
        self.assertEqual(named_indiv.iri, owl_entity.iri)

    def test_get_owl_entity_04(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))

        # data property
        owl_entity = named_indiv.get_owl_entity(EntityType.DATA_PROPERTY)
        self.assertTrue(isinstance(owl_entity, OWLDataProperty))
        self.assertEqual(named_indiv.iri, owl_entity.iri)

    def test_get_owl_entity_05(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))

        # datatype
        owl_entity = named_indiv.get_owl_entity(EntityType.DATATYPE)
        self.assertTrue(isinstance(owl_entity, OWLDatatype))
        self.assertEqual(named_indiv.iri, owl_entity.iri)

    def test_get_owl_entity_06(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))

        # object property
        owl_entity = named_indiv.get_owl_entity(EntityType.OBJECT_PROPERTY)
        self.assertTrue(isinstance(owl_entity, OWLObjectProperty))
        self.assertEqual(named_indiv.iri, owl_entity.iri)

    def test_is_type_01(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertFalse(named_indiv.is_type(None))

    def test_is_type_02(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertFalse(named_indiv.is_type(EntityType.CLASS))

    def test_is_type_03(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertTrue(named_indiv.is_type(EntityType.NAMED_INDIVIDUAL))

    def test_is_owl_named_individual(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertTrue(named_indiv.is_owl_named_individual())

    def test_is_anonymous(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertFalse(named_indiv.is_anonymous())

    def test_as_owl_named_individual(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertEqual(named_indiv, named_indiv.as_owl_named_individual())

    def test_as_owl_anonymous_individual(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertRaises(OWLRuntimeException,
                          OWLNamedIndividual.as_owl_anonymous_individual,
                          named_indiv)

    def test_as_owl_annotation_property(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertRaises(OWLRuntimeException,
                          OWLNamedIndividual.as_owl_annotation_property,
                          named_indiv)

    def test_is_owl_annotation_property(self):
        named_indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertFalse(named_indiv.is_owl_annotation_property())

    def test_get_annotations(self):
        self.fail()

    def test_get_annotation_assertion_axioms(self):
        self.fail()

    def test_get_referencing_axioms(self):
        self.fail()

    def test__compare_object_of_same_type_01(self):
        """same named individual --> 0"""
        indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertEqual(0, indiv._compare_object_of_same_type(indiv))

    def test__compare_object_of_same_type_02(self):
        """same IRI --> 0"""
        iri = IRI('http://ex.org/sth')
        indiv1 = OWLNamedIndividual(iri)
        indiv2 = OWLNamedIndividual(iri)
        self.assertEqual(0, indiv1._compare_object_of_same_type(indiv2))

    def test__compare_object_of_same_type_03(self):
        """same IRI string --> 0"""
        indiv1 = OWLNamedIndividual(IRI('http://ex.org/sth'))
        indiv2 = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertEqual(0, indiv1._compare_object_of_same_type(indiv2))

    def test__compare_object_of_same_type_04(self):
        """differing IRI string --> -4"""
        indiv1 = OWLNamedIndividual(IRI('http://ex.org/sth'))
        indiv2 = OWLNamedIndividual(IRI('http://ex.org/sthElse'))
        self.assertEqual(-4, indiv1._compare_object_of_same_type(indiv2))

    def test_accept_01(self):
        class DummyVisitor(OWLVisitorEx):
            def __init__(self):
                self.visited = False

            def visit(self, visitee):
                self.visited = True
                return 23

        visitor = DummyVisitor()
        indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        result = indiv.accept(visitor)
        self.assertEqual(23, result)
        self.assertTrue(visitor.visited)

    def test_accept_02(self):
        class DummyVisitor(OWLVisitor):
            def __init__(self):
                self.visited = False

            def visit(self, visitee):
                self.visited = True

        visitor = DummyVisitor()
        indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        result = indiv.accept(visitor)
        self.assertIsNone(result)
        self.assertTrue(visitor.visited)

    def test_accept_03(self):
        not_a_visitor = 'this is not a visitor'
        indiv = OWLNamedIndividual(IRI('http://ex.org/sth'))
        self.assertRaises(OWLRuntimeException, OWLNamedIndividual.accept,
                          indiv, not_a_visitor)