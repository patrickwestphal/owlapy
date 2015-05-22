from .exceptions import OWLRuntimeException
from .owlclassaxiom import OWLClassAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLSubClassOfAxiom(OWLClassAxiom):
    """TODO: implement"""

    def __init__(self, sub_class, super_class, annotations):
        """
        :param sub_class: an owlapy.model.OWLClassExpression object
        :param super_class: an owlapy.model.OWLClassExpression object
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(annotations)
        self.sub_class = sub_class
        self.super_class = super_class

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
