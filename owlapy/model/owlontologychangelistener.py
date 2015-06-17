class OWLOntologyChangeListener(object):

    def ontologies_changed(self, changes):
        """Called when some changes have been applied to various ontologies.
        These may be an axiom added or an axiom removed changes.

        :param changes: A list of changes, i.e. owlapy.model.OWLOntologyChange
            objects that have occurred. Each change may be examined to
            determine which ontology it was applied to.
        """
        raise NotImplementedError()
