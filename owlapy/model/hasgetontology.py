class HasGetOntologies(object):
    """Marker class"""

    def get_ontologies(self):
        """Gets the (possibly empty) set of owlapy.model.OWLOntology objects
        contained within this object.

        :return: The set of owlapy.model.OWLOntology objects. Possibly empty.
        """
        raise NotImplementedError()
