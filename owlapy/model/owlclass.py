from .owlclassexpression import OWLClassExpression
from .owllogicalentity import OWLLogicalEntity
from .owlnamedobject import OWLNamedObject


class OWLClass(OWLClassExpression, OWLLogicalEntity, OWLNamedObject):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri

    def compare_object_of_same_type(self, other):
        """
        :param other: an owlapy.model.OWLObject object
        :return: an integer indicating the difference  between self and other
        """
        return self.iri.compare_to(other.iri)
