import unittest

from owlapy import CollectionContainer
from owlapy import CollectionContainerVisitor

class TestCollectionContainer(unittest.TestCase):
    def test_accept(self):
        coll_container = CollectionContainer()
        visitor = CollectionContainerVisitor()
        self.assertRaises(NotImplementedError, CollectionContainer.accept,
                          coll_container, visitor)