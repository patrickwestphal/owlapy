class OWLOntologyDocumentSource(object):
    """Marker class"""

    def is_reader_available(self):
        """Determines if a reader is available which an ontology document can be
        parsed from.

        :return: True if a reader can be obtained from this document source, or
            False if a reader cannot be obtained from this document source.
        """
        raise NotImplementedError()

    def get_reader(self):
        """Gets a file-like object which an ontology document can be read from.
        This method may be called multiple times. Each invocation will return a
        new file-like object. This method should not be called if the
        is_reader_available method returns False. An exception will be thrown
        if this happens.

        :return: A new file-like object which the ontology can be read from.
        """
        raise NotImplementedError()

    def is_input_stream_available(self):
        """Determines if a file-like object is available which an ontology
        document can be parsed from.

        :return: True if a file-like object can be obtained, False if a
            file-like object cannot be obtained from this document source.
        """
        raise NotImplementedError()

    def get_input_stream(self):
        """If file-like object can be obtained from this document source then
        this method creates it. This method may be called multiple times. Each
        invocation will return a new file-like object. This method should not be
        called if the is_input_stream_available method returns False.

        :return: A new file-like object which the ontology can be read from.
        """
        raise NotImplementedError()

    def get_document_iri(self):
        """Gets the IRI of the ontology document.

        :return: An owlapy.model.IRI object which represents the ontology
            document IRI - this will never be None.
        """
        raise NotImplementedError()
