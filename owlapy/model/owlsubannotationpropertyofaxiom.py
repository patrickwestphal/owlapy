from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlaxiom import OWLAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLSubAnnotationPropertyOfAxiom(OWLAxiom):
    """TODO: implement"""

    def __init__(self, sub_property, super_property, annotations):
        """
        :param sub_property: an owlapy.model.OWLAnnotationProperty object
        :param super_property: an owlapy.model.OWLAnnotationProperty object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        :return:
        """
        super().__init__(annotations)
        self.sub_property = sub_property
        self.super_property = super_property

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.SUB_ANNOTATION_PROPERTY_OF

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
