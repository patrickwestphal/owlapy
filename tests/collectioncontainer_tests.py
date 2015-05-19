import unittest

from owlapy import CollectionContainer
from owlapy import CollectionContainerVisitor
from owlapy import OWLEntityCollectionContainerCollector
from owlapy.model import IRI
from owlapy.model import NodeID
from owlapy.model import OWLClass
from owlapy.model import OWLAnonymousIndividual


class TestCollectionContainer(unittest.TestCase):
    def test_accept(self):
        entities = [OWLClass(IRI('http://ex.org/SomeCls'))]
        anons = [OWLAnonymousIndividual(NodeID('_:23'))]
        collector = OWLEntityCollectionContainerCollector(entities, anons)
        coll_container = CollectionContainer()
        visitor = CollectionContainerVisitor(collector)
        self.assertRaises(NotImplementedError, CollectionContainer.accept,
                          coll_container, visitor)