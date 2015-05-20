from .owllogicalaxiom import OWLLogicalAxiom


class SWRLRule(OWLLogicalAxiom):
    """TODO: implement"""

    def __init__(self, body, head, annotations):
        """
        :param body: a set of owlapy.model.SWRLAtom objects
        :param head: a set of owlapy.model.SWRLAtom objects
        :param annotations: a set/list of owlapy.model.OWLAnnotation objects
        """
        super().__init__(annotations)
        self.head = head
        self.body = body
        # containsAnonymousClassExpressions = hasAnon();
