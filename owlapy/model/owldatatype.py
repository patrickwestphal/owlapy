from .owldatarange import OWLDataRange
from .owllogicalentity import OWLLogicalEntity
from .owlnamedobject import OWLNamedObject


class OWLDatatype(OWLDataRange, OWLLogicalEntity, OWLNamedObject):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri