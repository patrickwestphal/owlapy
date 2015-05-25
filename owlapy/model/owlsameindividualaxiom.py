from .exceptions import OWLRuntimeException
from .axiomtype import AxiomType
from .owlnaryindividualaxiom import OWLNaryIndividualAxiom
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLSameIndividualAxiom(OWLNaryIndividualAxiom):
    """TODO: implement"""

    def __init__(self, individuals, annotations):
        """
        :param individuals: a set of owlapy.model.OWLIndividual objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(individuals, annotations)

    def accept(self, visitor):
        """
        :param visitor: an object of one of the following classes:
            - owlapy.model.OWLAxiomVisitor
            - owlapy.model.OWLObjectVisitor
            - owlapy.model.OWLAxiomVisitorEx
            - owlapy.model.OWLObjectVisitorEx
        :return:
        """
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.SAME_INDIVIDUAL