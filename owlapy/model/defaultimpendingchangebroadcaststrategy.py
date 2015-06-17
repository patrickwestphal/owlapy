from .impendingowlontologychangebroadcaststrategy import \
    ImpendingOWLOntologyChangeBroadcastStrategy


class DefaultImpendingChangeBroadcastStrategy(
        ImpendingOWLOntologyChangeBroadcastStrategy):

    def broadcast_changes(self, listener, changes):
        listener.handle_impending_ontology_changes(changes)
