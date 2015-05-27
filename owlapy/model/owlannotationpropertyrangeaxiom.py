from .axiomtype import AxiomType
from .owlaxiom import OWLAxiom


class OWLAnnotationPropertyRangeAxiom(OWLAxiom):
    """TODO: implement"""

    def __init__(self, property, range, annotations):
        """
        :param property: an owlapy.model.OWLAnnotationProperty object
        :param range: an owlapy.model.IRI object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.property = property
        self.range = range

    @classmethod
    def get_axiom_type(cls):
        return AxiomType.ANNOTATION_PROPERTY_RANGE
