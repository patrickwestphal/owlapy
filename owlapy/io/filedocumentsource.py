from .owlontologydocumentsource import OWLOntologyDocumentSource


class FileDocumentSource(OWLOntologyDocumentSource):

    def __init__(self, file):
        self.file = file

    def get_document_iri(self):
        from owlapy.model import IRI
        return IRI.create(self.file)

    def is_input_stream_available(self):
        return True

    def get_input_stream(self):
        return self.file

    def is_reader_available(self):
        return True

    def get_reader(self):
        return self.file
