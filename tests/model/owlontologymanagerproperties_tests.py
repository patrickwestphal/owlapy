import unittest

from owlapy.model import OWLOntologyManagerProperties


class TestOWLOntologyManagerProperties(unittest.TestCase):

    def test___init___(self):
        man_props = OWLOntologyManagerProperties()

        self.assertTrue(man_props.load_annotation_axioms)
        self.assertTrue(
            man_props.treat_dublin_core_vocabulary_as_built_in_vocabulary)

    def test_restore_defaults(self):
        man_props = OWLOntologyManagerProperties()
        man_props.restore_defaults()

        self.assertTrue(man_props.load_annotation_axioms)
        self.assertTrue(
            man_props.treat_dublin_core_vocabulary_as_built_in_vocabulary)
