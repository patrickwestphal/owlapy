from .owlclassaxiom import OWLClassAxiom


class OWLDisjointUnionAxiom(OWLClassAxiom):
    """TODO: implement"""

    def __init__(self, owl_class, class_expressions, annotations):
        """
        :param owl_class: an owlapy.model.OWLClass object
        :param class_expressions: a set of OWLClassExpression objects
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(annotations)
        self.owl_class = owl_class
        self.class_expressions = class_expressions