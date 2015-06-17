import unittest

from owlapy.model import IRI
from owlapy.util.nonmappingontologyirimapper import NonMappingOntologyIRIMapper


class TestNonMappingOntologyIRIMapper(unittest.TestCase):

    def test_get_document_iri(self):
        ont_iri = IRI('http://ex.org/ont23')
        mapper = NonMappingOntologyIRIMapper()
        self.assertEqual(ont_iri, mapper.get_document_iri(ont_iri))
