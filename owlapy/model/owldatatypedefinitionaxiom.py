from .axiomtype import AxiomType
from .owlaxiomvisitor import OWLAxiomVisitor, OWLAxiomVisitorEx
from .owlaxiom import OWLAxiom
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLDatatypeDefinitionAxiom(OWLAxiom):
    """TODO: implement"""

    def __init__(self, datatype, data_range, annotations):
        """
        :param datatype: an owlapy.model.OWLDatatype object
        :param data_range: an owlapy.model.OWLDataRange object
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(annotations)
        self.datatype = datatype
        self.data_range = data_range

        self._accept_fn_for_visitor_cls[OWLAxiomVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLAxiomVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DATATYPE_DEFINITION
