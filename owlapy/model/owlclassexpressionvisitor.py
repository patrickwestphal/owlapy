class OWLClassExpressionVisitor(object):
    """Marker class"""

    def visit(self, ce):
        """
        :param ce: an object of one of the following classes:
            - owlapy.model.OWLClass
            - owlapy.model.OWLObjectIntersectionOf
            - owlapy.model.OWLObjectUnionOf
            - owlapy.model.OWLObjectComplementOf
            - owlapy.model.OWLObjectSomeValuesFrom
            - owlapy.model.OWLObjectAllValuesFrom
            - owlapy.model.OWLObjectHasValue
            - owlapy.model.OWLObjectMinCardinality
            - owlapy.model.OWLObjectExactCardinality
            - owlapy.model.OWLObjectMaxCardinality
            - owlapy.model.OWLObjectHasSelf
            - owlapy.model.OWLObjectOneOf
            - owlapy.model.OWLDataSomeValuesFrom
            - owlapy.model.OWLDataAllValuesFrom
            - owlapy.model.OWLDataHasValue
            - owlapy.model.OWLDataMinCardinality
            - owlapy.model.OWLDataExactCardinality
            - owlapy.model.OWLDataMaxCardinality
        :return: None
        """
        raise NotImplementedError()