class OWLOntologyFactory(object):
    """Marker class"""

    def set_owl_ontology_manager(self, owl_ontology_manager):
        """
        :param owl_ontology_manager: the owlapy.model.OWLOntology manager object
            to set. Cannot be None
        """
        raise NotImplementedError()

    def get_owl_ontology_manager(self):
        """
        :return: the ontology manager
        """
        raise NotImplementedError()

    def create_owl_ontology(self, ontology_id, document_iri, handler):
        """Creates an (empty) ontology.

        :param ontology_id: The owlapy.model.OWLOntologyID object of the
            ontology to create. This MUST NOT BE None
        :param document_iri: The document IRI of the ontology
        :param handler: The ontology creation handler
            (OWLOntologyCreationHandler) that will be notified when the ontology
            has been created. @return The newly created ontology
        :return: The created ontology
        """
        raise NotImplementedError()

    def load_owl_ontology(self, document_source, handler, configuration=None):
        """Creates and loads an owlapy.model.OWLOntology.

        :param document_source: The document source
            (owlapy.model.OWLOntologySource) that provides the means of getting
            a representation of a document.
        :param handler: A pointer to an OWLOntologyCreationHandler which will be
            notified immediately after an empty ontology has been created, but
            before the source data is read and the ontology is loaded with
            axioms.
        :param configuration: An owlapy.model.OWLOntologyLoaderConfiguration
            object which can be used to pass various options to the loader.
        :return: The newly created and loaded owlapy.model.OWLOntology object
        """
        raise NotImplementedError()

    def can_create_from_document_iri(self, document_iri):
        """Determines if the factory can create an ontology for the specified
        ontology document IRI.

        :param document_iri: The document IRI
        :return: True if the factory can create an ontology given the specified
            document IRI, or False if the factory cannot create an ontology
            given the specified document IRI.
        """
        raise NotImplementedError()

    def can_load(self, document_source):
        """Determines if the factory can load an ontology for the specified
        input souce.

        :param document_source: The input source
            (owlapy.model.OWLOntologyDocumentSource) from which to load the
            ontology
        :return: True if the factory can load from the specified input source.
        """
        raise NotImplementedError()

    class OWLOntologyCreationHandler(object):
        """Marker class"""

        def ontology_created(self, ontology):
            """The factory calls this method as soon as it has created an
            ontology. If the factory is loading an ontology then the ontology
            will not have been populated with axioms at this stage.

            :param ontology: The newly created owlapy.model.OWLOntology object
            """
            raise NotImplementedError()

        def set_ontology_format(self, ontology, format):
            """
            :param ontology: the owlapy.model.OWLOntology object
            :param format: the owlapy.model.OWLOntologyFormat object
                representing the format
            """
            raise NotImplementedError()
