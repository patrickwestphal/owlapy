import unittest

from owlapy.model import DataRangeType
from owlapy.model import EntityType
from owlapy.model import IRI
from owlapy.model import OWL2Datatype
from owlapy.model import OWLDatatype
from owlapy.model import OWLObjectProperty
from owlapy.model import OWLObjectVisitor
from owlapy.model import OWLObjectVisitorEx
from owlapy.model import OWLRuntimeException
from owlapy.vocab.owl2datatype import OWL2Datatype as OWL2DtypeVoc


class OWL2DatatypeTest(unittest.TestCase):

    def test___init__(self):
        dtype = OWL2DtypeVoc.XSD_BASE_64_BINARY
        owl2datatype = OWL2Datatype(dtype)

        self.assertEqual(dtype, owl2datatype.owl2_datatype)

    def test___str__(self):
        iri_str = str(OWL2DtypeVoc.OWL_RATIONAL.iri)
        self.assertEqual(iri_str, str(OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL)))

    def test___eq__01(self):
        """same object"""
        self.assertEqual(
            OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER),
            OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER))

    def test___eq__02(self):
        """same IRI string, model.OWLDatatype class"""
        dtype = OWLDatatype(IRI('http://www.w3.org/2001/XMLSchema#integer'))
        self.assertEqual(dtype, OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER))

    def test___eq__03(self):
        """same class, differing IRI"""
        self.assertNotEqual(
            OWL2Datatype(OWL2DtypeVoc.XSD_INT),
            OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER))

    def test___eq__06(self):
        """completely different"""
        self.assertNotEqual(23, OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER))

    def test_accept_01(self):
        class DummyVisitor(OWLObjectVisitor):
            def __init__(self):
                self.visited = False

            def visit(self, axiom):
                self.visited = True

        visitor = DummyVisitor()
        owl2datatype = OWL2Datatype(OWL2DtypeVoc.XSD_BASE_64_BINARY)
        res = owl2datatype.accept(visitor)

        self.assertIsNone(res)
        self.assertTrue(visitor.visited)

    def test_accept_02(self):
        class DummyVisitor(OWLObjectVisitorEx):
            def __init__(self):
                self.return_value = 23
                self.visited = False

            def visit(self, axiom):
                self.visited = True
                return self.return_value

        visitor = DummyVisitor()
        owl2datatype = OWL2Datatype(OWL2DtypeVoc.XSD_BASE_64_BINARY)
        res = owl2datatype.accept(visitor)

        self.assertEqual(visitor.return_value, res)
        self.assertTrue(visitor.visited)

    def test_accept_03(self):
        class DummyVisitor(object):
            def __init__(self):
                self.return_value = 23
                self.visited = False

            def visit(self, axiom):
                self.visited = True
                return self.return_value

        visitor = DummyVisitor()
        owl2datatype = OWL2Datatype(OWL2DtypeVoc.XSD_BASE_64_BINARY)

        self.assertRaises(OWLRuntimeException, owl2datatype.accept, visitor)

    def test_instance_map(self):
        self.assertEqual(len(OWL2DtypeVoc), len(OWL2Datatype.instance_map))

        for (vocab_dtype, owl2_dtype) in OWL2Datatype.instance_map.items():
            self.assertEqual(vocab_dtype, owl2_dtype.owl2_datatype)

    def test_get_datatype(self):
        owl2_datatype = OWL2Datatype(OWL2DtypeVoc.XSD_DOUBLE)
        self.assertEqual(owl2_datatype,
                         OWL2Datatype.get_datatype(OWL2DtypeVoc.XSD_DOUBLE))

    def test_get_built_in_type(self):
        owl2_datatype = OWL2Datatype(OWL2DtypeVoc.XSD_DOUBLE)
        self.assertEqual(OWL2DtypeVoc.XSD_DOUBLE,
                         owl2_datatype.get_built_in_type())

    def test_is_string(self):
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.OWL_REAL).is_string())
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).is_string())
        self.assertTrue(OWL2Datatype(OWL2DtypeVoc.XSD_STRING).is_string())

    def test_is_integer(self):
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).is_integer())
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.XSD_DOUBLE).is_integer())
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.XSD_INT).is_integer())
        self.assertTrue(OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).is_integer())

    def test_is_float(self):
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).is_float())
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.XSD_DOUBLE).is_float())
        self.assertTrue(OWL2Datatype(OWL2DtypeVoc.XSD_FLOAT).is_float())

    def test_is_double(self):
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).is_double())
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.XSD_FLOAT).is_double())
        self.assertTrue(OWL2Datatype(OWL2DtypeVoc.XSD_DOUBLE).is_double())

    def test_is_boolean(self):
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).is_boolean())
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).is_boolean())
        self.assertTrue(OWL2Datatype(OWL2DtypeVoc.XSD_BOOLEAN).is_boolean())

    def test_is_rdf_plain_literal(self):
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).is_rdf_plain_literal())
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.RDFS_LITERAL).is_rdf_plain_literal())
        self.assertTrue(
            OWL2Datatype(OWL2DtypeVoc.RDF_PLAIN_LITERAL).is_rdf_plain_literal())

    def test_is_datatype(self):
        self.assertTrue(OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).is_datatype())
        self.assertTrue(OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).is_datatype())
        self.assertTrue(OWL2Datatype(OWL2DtypeVoc.XSD_STRING).is_datatype())

    def test_is_top_datatype(self):
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).is_top_datatype())
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.RDF_PLAIN_LITERAL).is_top_datatype())
        self.assertTrue(
            OWL2Datatype(OWL2DtypeVoc.RDFS_LITERAL).is_top_datatype())

    def test_as_owl_datatype(self):
        dtype = OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL)
        self.assertEqual(dtype, dtype.as_owl_datatype())

    def test_get_data_range_type(self):
        self.assertEqual(
            DataRangeType.DATATYPE,
            OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).get_data_range_type())
        self.assertEqual(
            DataRangeType.DATATYPE,
            OWL2Datatype(
                OWL2DtypeVoc.XSD_NEGATIVE_INTEGER).get_data_range_type())
        self.assertEqual(
            DataRangeType.DATATYPE,
            OWL2Datatype(OWL2DtypeVoc.XSD_STRING).get_data_range_type())

    def test_get_entity_type(self):
        self.assertEqual(
            EntityType.DATATYPE,
            OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).get_entity_type())

    def test_get_owl_entity(self):
        entity = OWLDatatype(OWL2DtypeVoc.RDF_PLAIN_LITERAL.iri)
        owl2_datatype = OWL2Datatype(OWL2DtypeVoc.XSD_INT)

        self.assertEqual(
            entity, owl2_datatype.get_owl_entity(EntityType.DATATYPE))

    def test_is_type(self):
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.XSD_INT).is_type(
                EntityType.ANNOTATION_PROPERTY))
        self.assertTrue(
            OWL2Datatype(OWL2DtypeVoc.XSD_INT).is_type(EntityType.DATATYPE))

    def test_get_annotations(self):
        self.fail('OWLOntology needs to be implemented first')

    def test_get_annotation_assertion_axioms(self):
        self.fail('OWLOntology needs to be implemented first')

    def test_is_built_in(self):
        self.assertTrue(OWL2Datatype(OWL2DtypeVoc.XSD_INT).is_built_in())
        self.assertTrue(OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).is_built_in())
        self.assertTrue(OWL2Datatype(OWL2DtypeVoc.RDFS_LITERAL).is_built_in())

    def test_is_owl_class(self):
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.XSD_INT).is_owl_class())
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.XSD_DOUBLE).is_owl_class())

    def test_as_owl_class(self):
        self.assertRaises(OWLRuntimeException,
                          OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).as_owl_class)

    def test_is_owl_object_property(self):
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).is_owl_object_property())
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.XSD_STRING).is_owl_object_property())

    def test_as_owl_object_property(self):
        self.assertRaises(
            OWLRuntimeException,
            OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).as_owl_object_property)

    def test_is_owl_data_property(self):
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).is_owl_data_property())
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).is_owl_data_property())

    def test_as_owl_data_property(self):
        self.assertRaises(
            OWLRuntimeException,
            OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).as_owl_data_property)

    def test_is_owl_named_individual(self):
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.XSD_INT).is_owl_named_individual())
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).is_owl_named_individual())

    def test_as_owl_named_individual(self):
        self.assertRaises(
            OWLRuntimeException,
            OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).as_owl_named_individual)

    def test_is_owl_datatype(self):
        self.assertTrue(
            OWL2Datatype(OWL2DtypeVoc.XSD_STRING).is_owl_datatype())
        self.assertTrue(
            OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).is_owl_datatype())

    def test_is_owl_annotation_property(self):
        self.assertFalse(OWL2Datatype(
            OWL2DtypeVoc.XSD_STRING).is_owl_annotation_property())
        self.assertFalse(OWL2Datatype(
            OWL2DtypeVoc.OWL_RATIONAL).is_owl_annotation_property())

    def test_as_owl_annotation_property(self):
        self.assertRaises(
            OWLRuntimeException,
            OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER).as_owl_annotation_property)

    def test_to_string_id(self):
        iri_str = str(OWL2DtypeVoc.OWL_RATIONAL.iri)
        self.assertEqual(
            iri_str, OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).to_string_id())

    def test_get_referencing_axioms(self):
        self.fail('OWLOntology needs to be implemented first')

    def test_get_signature(self):
        self.assertEqual({OWL2Datatype(OWL2DtypeVoc.XSD_BOOLEAN)},
                         OWL2Datatype(OWL2DtypeVoc.XSD_BOOLEAN).get_signature())

    def test_contains_entity_in_signature(self):
        self.assertTrue(
            OWL2Datatype(OWL2DtypeVoc.XSD_BOOLEAN).contains_entity_in_signature(
                OWL2Datatype(OWL2DtypeVoc.XSD_BOOLEAN)))
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.XSD_BOOLEAN).contains_entity_in_signature(
                OWL2Datatype(OWL2DtypeVoc.XSD_INT)))

    def test_get_anonymous_individuals(self):
        self.assertEqual(
            set(),
            OWL2Datatype(OWL2DtypeVoc.XSD_NEGATIVE_INTEGER).
            get_anonymous_individuals())

    def test_get_classes_in_signature(self):
        self.assertEqual(
            set(),
            OWL2Datatype(OWL2DtypeVoc.OWL_RATIONAL).get_classes_in_signature())

    def test_get_data_properties_in_signature(self):
        self.assertEqual(
            set(),
            OWL2Datatype(OWL2DtypeVoc.RDF_PLAIN_LITERAL).
            get_data_properties_in_signature())

    def test_get_object_properties_in_signature(self):
        self.assertEqual(
            set(),
            OWL2Datatype(OWL2DtypeVoc.RDFS_LITERAL).
            get_object_properties_in_signature())

    def test_get_individuals_in_signature(self):
        self.assertEqual(
            set(),
            OWL2Datatype(OWL2DtypeVoc.XSD_ANY_URI).
            get_individuals_in_signature())

    def test_get_datatypes_in_signature(self):
        self.assertEqual(
            {OWL2Datatype(OWL2DtypeVoc.OWL_REAL)},
            OWL2Datatype(OWL2DtypeVoc.OWL_REAL).get_datatypes_in_signature())

    def test_get_nested_class_expressions(self):
        self.assertEqual(
            set(),
            OWL2Datatype(OWL2DtypeVoc.XSD_DOUBLE).
            get_nested_class_expressions())

    def test_is_top_entity(self):
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.XSD_STRING).is_top_entity())
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.XSD_FLOAT).is_top_entity())
        self.assertTrue(
            OWL2Datatype(OWL2DtypeVoc.RDF_PLAIN_LITERAL).is_top_entity())

    def test_is_bottom_entity(self):
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.XSD_STRING).is_bottom_entity())
        self.assertFalse(OWL2Datatype(OWL2DtypeVoc.OWL_REAL).is_bottom_entity())
        self.assertFalse(
            OWL2Datatype(OWL2DtypeVoc.RDF_XML_LITERAL).is_bottom_entity())

    def test_compare_to_01(self):
        """same object"""
        dtype = OWL2Datatype(OWL2DtypeVoc.XSD_STRING)
        self.assertEqual(0, dtype.compare_to(dtype))

    def test_compare_to_02(self):
        """differing class"""
        dtype = OWL2Datatype(OWL2DtypeVoc.XSD_STRING)  # OWL2Datatype
        # ObjectProperty --> index = 1002
        other = OWLObjectProperty(IRI('http://ex.org/prop'))

        self.assertEqual(1002, dtype.compare_to(other))

    def test_compare_to_03(self):
        """same class, differing IRI"""
        iri_diff = OWL2DtypeVoc.RDF_PLAIN_LITERAL.iri.compare_to(
            OWL2DtypeVoc.XSD_INTEGER.iri)
        dtype1 = OWL2Datatype(OWL2DtypeVoc.RDF_PLAIN_LITERAL)
        dtype2 = OWL2Datatype(OWL2DtypeVoc.XSD_INTEGER)
        self.assertEqual(iri_diff, dtype1.compare_to(dtype2))
