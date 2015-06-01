from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlclassaxiom import OWLClassAxiom
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


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

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
