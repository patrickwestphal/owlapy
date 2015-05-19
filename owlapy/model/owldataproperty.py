from .owldatapropertyexpression import OWLDataPropertyExpression


class OWLDataProperty(OWLDataPropertyExpression):
    """TODO: implement"""

    def __init__(self, iri):
        """
        :param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri