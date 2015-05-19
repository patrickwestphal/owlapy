from .unimplementedclasses import OWLObjectPropertyExpression


class OWLObjectProperty(OWLObjectPropertyExpression):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri