class CollectionContainer(object):
    def accept(self, coll_container_visitor):
        """

        :param coll_container_visitor: an owlapy.CollectionContainerVisitor
            object
        """
        raise NotImplementedError()