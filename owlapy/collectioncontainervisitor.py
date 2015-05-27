from owlapy.model import OWLVisitor


class CollectionContainerVisitor(OWLVisitor):

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
