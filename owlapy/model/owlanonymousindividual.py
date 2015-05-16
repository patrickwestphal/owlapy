from owlapy.model import OWLRuntimeException
from .owlindividual import OWLIndividual
from .owlvisitor import OWLVisitor, OWLVisitorEx


class OWLAnonymousIndividual(OWLIndividual):
    """Represents Anonymous Individuals as defined in the OWL 2
    Specification [0]

    [0] http://www.w3.org/TR/owl2-syntax/#Anonymous_Individuals
    """

    def __init__(self, node_id):
        """:param node_id: a owlapy.model.NodeID object"""
        self.id = node_id

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if id(self) == id(other):
            return True

        if not isinstance(other, OWLAnonymousIndividual):
            return False

        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def is_named(self):
        """Determines if this individual is an instance of
        owlapy.model.OWLNamedIndividual. Note that this method is the dual of
        is_anonymous()
        .
        :return: True if this individual is an instance of
            owlapy.model.OWLNamedIndividual because it is a named individual,
            otherwise False
        """
        return False

    def is_anomymous(self):
        """Determines if this object is an instance of
        owlapy.model.OWLAnonymousIndividual. Note that

        :return: True if this object represents an anonymous individual
            (owlapy.model.OWLAnomymouseIndividual) or False if this object
            represents a named individual (owlapy.model.OWLNamedIndividual)
        """
        return True

    def as_owl_named_individual(self):
        """Obtains this individual as a named individual if it is indeed named.

        :return: The individual as a named individual
        """
        raise OWLRuntimeException('Not a named individual! This method should '
                                  'only be called on named individuals')

    def as_owl_anonymous_individual(self):
        """Obtains this individual an anonymous individual if it is indeed
        anonymous

        :return: The individual as an anonymous individual
        """
        return self

    def _compare_object_of_same_type(self, other):
        """
        :param other: an owlapy.model.OWLAnonymousIndividual object
        :return:
        """
        return self.id.compare_to(other.id)

    def accept(self, visitor):
        """TODO: update the visitor class list (i.e. remove those that are not
        going to be implemented)

        :param visitor: object of one of the following classes:
            - OWLObjectVisitor
            - OWLObjectVisitorEx
            - OWLIndividualVisitor
            - OWLIndividualVisitorEx
            - OWLAnnotationValueVisitor
            - OWLAnnotationValueVisitorEx
            - OWLAnnotationSubjectVisitor
            - OWLAnnotationSubjectVisitorEx
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