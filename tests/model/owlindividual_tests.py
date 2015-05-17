import unittest

from owlapy.model import OWLIndividual


class TestOWLIndividual(unittest.TestCase):

    def test___eq__(self):
        """OWL individual vs. OWL individual --> equal
        in all other cases, e.g. OWL individual vs. OWL named individual the
        __eq__ method of the more special classes is called
        """
        indiv1 = OWLIndividual()
        indiv2 = OWLIndividual()
        self.assertTrue(indiv1 == indiv2)

    def test_get_types(self):
        self.fail()  # OWLOntology has to be implemented first

    def test_get_object_property_values(self):
        self.fail()  # OWLOntology has to be implemented first

    def test_has_object_property_value(self):
        self.fail()  # OWLOntology has to be implemented first

    def test_has_data_property_value(self):
        self.fail()  # OWLOntology has to be implemented first

    def test_has_negative_object_property_value(self):
        self.fail()  # OWLOntology has to be implemented first

    def test_get_negative_object_property_values(self):
        self.fail()  # OWLOntology has to be implemented first

    def test_get_data_property_values(self):
        self.fail()  # OWLOntology has to be implemented first

    def test_get_negative_data_property_values(self):
        self.fail()  # OWLOntology has to be implemented first

    def test_has_negative_data_property_value(self):
        self.fail()  # OWLOntology has to be implemented first

    def test_get_same_individuals(self):
        self.fail()  # OWLOntology has to be implemented first

    def test_get_different_individuals(self):
        self.fail()  # OWLOntology has to be implemented first
