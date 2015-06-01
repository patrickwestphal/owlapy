from owlapy.model import OWLAnnotation


class CollectionContainerVisitor(object):

    def __init__(self, collector):
        self._collector = collector

    def visit(self, collection_container):
        """
        :param collection_container: an owlapy.CollectionContainer object
        :return:
        """
        pass

    def visit_item(self, entity):
        """
        :param entity: an owlapy.model.OWLAnnotation object
        """
        if isinstance(entity, OWLAnnotation):
            # defined in OWLEntityCollectionContainerCollector class in OWLAPI
            entity.accept(self._collector)
