from .exceptions import OWLOntologyInputSourceException
from .owlontologydocumentsource import OWLOntologyDocumentSource


class IRIDocumentSource(OWLOntologyDocumentSource):

    def __init__(self, ducument_iri):
        """
        :param ducument_iri: an owlapy.model.IRI object
        """
        self.document_iri = ducument_iri

    def __str__(self):
        return str(self.document_iri)

    def __repr__(self):
        return str(self.document_iri)

    def get_document_iri(self):
        return self.document_iri

    def is_input_stream_available(self):
        return False

    def get_input_stream(self):
        raise OWLOntologyInputSourceException(
            'InputStream not available. Check with '
            'IRIDocumentSource.is_input_stream_available() first!')

    def is_reader_available(self):
        return False

    def get_reader(self):
        raise OWLOntologyInputSourceException(
            'Reader not available. Check with'
            'IRIDocumentSource.is_reader_available() first!')
