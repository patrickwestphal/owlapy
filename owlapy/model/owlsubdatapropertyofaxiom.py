from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlsubpropertyaxiom import OWLSubPropertyAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLSubDataPropertyOfAxiom(OWLSubPropertyAxiom):
    """TODO: implement"""

    def __init__(self, sub_property, super_property, annotations):
        """
        :param sub_property: an owlapy.model.OWLDataPropertyExpression object
        :param super_property: an owlapy.model.OWLDataPropertyExpression object
        :param annotations:a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(sub_property, super_property, annotations)

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.SUB_DATA_PROPERTY

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
