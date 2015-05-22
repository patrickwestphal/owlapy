from .owlentity import OWLEntity


class OWLAnnotationProperty(OWLEntity):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        self.iri = iri
