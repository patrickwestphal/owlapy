import unittest

from owlapy import CollectionContainer
from owlapy import CollectionContainerVisitor
from owlapy import OWLEntityCollectionContainerCollector
from owlapy.model import IRI
from owlapy.model import NodeID
from owlapy.model import OWLAnonymousIndividual
from owlapy.model import OWLClass


class TestCollectionContainerVisitor(unittest.TestCase):
    def test___init__(self):
        entities = {OWLClass(IRI('http://ex.org/SomeCls'))}
        anons = {OWLAnonymousIndividual(NodeID('_:23'))}
        collector = OWLEntityCollectionContainerCollector(entities, anons)
        coll_container_visitor = CollectionContainerVisitor(collector)
        self.assertEqual(collector, coll_container_visitor._collector)

    def test_visit(self):
        entities = {OWLClass(IRI('http://ex.org/SomeCls'))}
        anons = {OWLAnonymousIndividual(NodeID('_:23'))}
        collector = OWLEntityCollectionContainerCollector(entities, anons)
        coll_container_visitor = CollectionContainerVisitor(collector)
        coll_container = CollectionContainer()
        self.assertIsNone(coll_container_visitor.visit(coll_container))

    def test_visit_item(self):
        self.fail()  # owlapy.model.OWLAnnotation needs to be implemented first