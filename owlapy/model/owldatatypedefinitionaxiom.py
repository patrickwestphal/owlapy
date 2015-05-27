from .axiomtype import AxiomType
from .owlaxiom import OWLAxiom


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

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.DATATYPE_DEFINITION
