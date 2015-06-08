class HasApplyChanges(object):
    """Marker class"""

    def apply_changes(self, changes):
        """Applies a list ontology changes to some ontologies.

        :param changes: a list of owlapy.model,OWLOntologyChange objects
        :return: The changes that were actually applied.
        """
        raise NotImplementedError()
