import owlapy.model


class OWLLogicalAxiom(owlapy.model.OWLAxiom):
    """TODO: implement"""

    def __init__(self, annotations):
        """
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(annotations)