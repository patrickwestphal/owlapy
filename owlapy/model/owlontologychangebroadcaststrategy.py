class OWLOntologyChangeBroadcastStrategy(object):
    """Marker class"""

    def broadcast_changes(self, listener, changes):
        """Broadcasts the list of changes to the specified listeners.

        :param listener: The listeners that the changes should be broadcast to
        :param changes: The changes, i.e. owlapy.model.OWLOntologyChange
            objects, to be broadcast.
        """
        raise NotImplementedError()
