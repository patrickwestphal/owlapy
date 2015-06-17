class ImpendingOWLOntologyChangeBroadcastStrategy(object):
    """Marker class"""

    def broadcast_changes(self, listener, changes):
        """Broadcasts the list of changes to the specified listeners.

        :param listener: the listener, i.e. the
            owlapy.model.ImpendingOWLOntologyChangeListener object the changes
            should be broadcasted to
        :param changes: The changes, i.e. list of owlapy.model.OWLOntologyChange
            objects to be broadcast.
        """
        raise NotImplementedError()
