from .owlontologychangebroadcaststrategy import \
    OWLOntologyChangeBroadcastStrategy


class DefaultChangeBroadcastStrategy(OWLOntologyChangeBroadcastStrategy):

    def broadcast_changes(self, listener, changes):
        listener.ontologies_changed(changes)
