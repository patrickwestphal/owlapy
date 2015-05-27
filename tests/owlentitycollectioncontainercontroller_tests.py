import unittest

from owlapy import OWLEntityCollectionContainerCollector
from owlapy.model import IRI
from owlapy.model import NodeID
from owlapy.model import OWLAnonymousIndividual
from owlapy.model import OWLClass


class TestOWLEntityCollectionContainerCollector(unittest.TestCase):
    def test___init__01(self):
        entities = {OWLClass(IRI('http://ex.org/SomeCls'))}
        anons = {OWLAnonymousIndividual(NodeID('_:23'))}
        eccc = OWLEntityCollectionContainerCollector(entities, anons)

        self.assertEqual(set(entities), eccc._objects)
        self.assertEqual(set(anons), eccc._anonymous_individuals)
        self.assertTrue(eccc.collect_classes)
        self.assertTrue(eccc.collect_object_properties)
        self.assertTrue(eccc.collect_data_properties)
        self.assertTrue(eccc.collect_individuals)
        self.assertTrue(eccc.collect_datatypes)

    def test___init__02(self):
        entities = {OWLClass(IRI('http://ex.org/SomeCls'))}
        eccc = OWLEntityCollectionContainerCollector(entities)

        self.assertEqual(entities, eccc._objects)
        self.assertEqual(set(), eccc._anonymous_individuals)
        self.assertTrue(eccc.collect_classes)
        self.assertTrue(eccc.collect_object_properties)
        self.assertTrue(eccc.collect_data_properties)
        self.assertTrue(eccc.collect_individuals)
        self.assertTrue(eccc.collect_datatypes)

    def test_reset(self):
        entities = {OWLClass(IRI('http://ex.org/SomeCls'))}
        anons = {OWLAnonymousIndividual(NodeID('_:23'))}
        eccc = OWLEntityCollectionContainerCollector(entities, anons)

        self.assertEqual(entities, eccc._objects)
        self.assertEqual(set(anons), eccc._anonymous_individuals)

        reset_entities = [OWLClass(IRI('http://ex.org/AnotherCls'))]
        eccc.reset(reset_entities)
        self.assertEqual(reset_entities, eccc._objects)
        self.assertEqual(set(), eccc._anonymous_individuals)

    def test__process_axiom_annotations(self):
        self.fail()  # OWLAxiom needs to be implemented first

    def test_visit(self):
        # all the visited objects' classes need to be implemented first
        self.fail()