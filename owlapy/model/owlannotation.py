from .owlobject import OWLObject


class OWLAnnotation(OWLObject):
    """TODO: implement"""

    def __init__(self, property, value, annotations):
        """
        :param property: an owlapy.model.OWLAnnotationProperty object
        :param value: an owlapy.model.OWLAnnotationValue object
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__()
        self.property = property
        self.value = value
        self.annotations = annotations