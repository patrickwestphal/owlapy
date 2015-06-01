from .owlclassexpressionvisitor import OWLClassExpressionVisitor, \
    OWLClassExpressionVisitorEx
from .owldatamincardinality import OWLDataCardinalityRestriction
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLDataExactCardinality(OWLDataCardinalityRestriction):
    """TODO: implement"""

    def __init__(self, property, cardinality, filler):
        """
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :param cardinality: an integer
        :param filler: an owlapy.model.OWLDataRange object (i.e. an
            owlapy.model.OWLDataComplementOf object, an
            owlapy,model.OWLDataOneOf object, an owlapy.model.OWLDatatype
            object, an owlapy.model.OWLDatatypeRestriction, or an
            owlapy.model.OWLNaryDataRange object)
        """
        super().__init__(property, cardinality, filler)

        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitor] = \
            accept_default
        self._accept_fn_for_visitor_cls[OWLClassExpressionVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
