from .owlclassaxiom import OWLClassAxiom


class OWLSubClassOfAxiom(OWLClassAxiom):
    """TODO: implement"""

    def __init__(self, sub_class, super_class, annotations):
        """
        :param sub_class: an owlapy.model.OWLClassExpression object
        :param super_class: an owlapy.model.OWLClassExpression object
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(annotations)
        self.sub_class = sub_class
        self.super_class = super_class
