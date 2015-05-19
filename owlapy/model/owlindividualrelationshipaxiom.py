from .owllogicalaxiom import OWLLogicalAxiom


class OWLIndividualRelationshipAxiom(OWLLogicalAxiom):
    """TODO: implement"""
    # ABSTRACT!

    def __init__(self, subject, property, object, annotations):
        """
        :param subject: an owlapy.model.OWLIndividual object
        :param property: an owlapy.model.OWLPropertyExpression object
        :param object: an owlapy.model.OWLPropertyAssertionObject object
        :param annotations: a list/set of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.subject = subject
        self.property = property
        self.object = object
