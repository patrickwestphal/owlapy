from .owlnarypropertyaxiom import OWLNaryPropertyAxiom


class OWLEquivalentDataPropertiesAxiom(OWLNaryPropertyAxiom):
    """TODO: implement"""

    def __init__(self, properties, annotations):
        """
        :param properties: a set of owlapy,model.OWLDataPropertyExpression
            objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        :return:
        """
        super().__init__(properties, annotations)