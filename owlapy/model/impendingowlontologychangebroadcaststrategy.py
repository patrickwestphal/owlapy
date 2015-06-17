class ImpendingOWLOntologyChangeBroadcastStrategy(object):
    """Marker class"""

    def broadcast_changes(self, changes):
        """Broadcasts the list of changes to the specified listeners.

        :param changes: The changes, i.e. list of owlapy.model.OWLOntologyChange
            objects to be broadcast.
        """
        raise NotImplementedError()
