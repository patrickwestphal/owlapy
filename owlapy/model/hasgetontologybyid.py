class HasGetOntologyById(object):
    """Marker class"""

    def get_ontology(self, ontology_id):
        """
        :param ontology_id: an owlapy.model.OntologyID object
        :return: The owlapy.model.OWLOntology object with the specified ID, or
            None if there is no ontology with the specified ID
        """
        raise NotImplementedError()
