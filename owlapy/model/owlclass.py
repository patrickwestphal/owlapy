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