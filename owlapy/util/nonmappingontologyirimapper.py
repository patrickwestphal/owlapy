from owlapy.model import OWLOntologyIRIMapper


class NonMappingOntologyIRIMapper(OWLOntologyIRIMapper):
    """TODO: implement"""

    def get_document_iri(self, ontology_iri):
        return ontology_iri
