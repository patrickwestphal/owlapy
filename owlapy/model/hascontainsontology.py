class HasContainsOntology(object):
    """Marker class"""

    def contains(self, ontology_id):
        """Determines if this object contains an ontology that has the specified
        owlapy.model.OWLOntologyID

        :param ontology_id: The owlapy.model.OWLOntologyID to test for.
        :return: True if this object contains an ontology that has the specified
            ID, otherwise, False.
        """
        raise NotImplementedError()
