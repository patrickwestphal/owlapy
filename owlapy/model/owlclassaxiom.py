import owlapy.model


class OWLClassAxiom(owlapy.model.OWLLogicalAxiom):
    """TODO: implement"""

    def __init__(self, annotations):
        """
        :param annotations: set/list of OWLAnnotation objects
        """
        super().__init__(annotations)