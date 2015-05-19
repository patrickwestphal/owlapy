from owlapy.model import OWLClassAxiom


class OWLNaryClassAxiom(OWLClassAxiom):
    """TODO: implement"""

    def __init__(self, class_expressions, annotations):
        """
        :param class_expressions: a set of owlapy.model.OWLClassExpression
            objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.class_expressions = class_expressions