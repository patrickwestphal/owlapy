import owlapy.model


class OWLSubClassOfAxiom(owlapy.model.OWLClassAxiom):
    """TODO: implement"""

    def __init__(self, sub_class, super_class, annotations):
        """
        :param sub_class: an owlapy.model.OWLClassExpression object
        :param super_class: an owlapy.model.OWLClassExpression object
        :param annotations: a set/list of OWLAnnotation objects
        """
        super().__init__(annotations)
