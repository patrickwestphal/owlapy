from .owldatarangevisitor import OWLDataRangeVisitor, OWLDataRangeVisitorEx
from .owldatavisitor import OWLDataVisitor, OWLDataVisitorEx
from .owlobject import OWLObject
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex


class OWLDatatypeRestriction(OWLObject):
    """TODO: implement"""

    def __init__(self, datatype, facet_restrictions):
        """
        :param datatype: an owlapy.model.OWLDatatype object
        :param facet_restrictions: facet restrictions on this data range; a set
            of owlapy.model.OWLFacetRestriction objects
        """
        super().__init__()
        self.datatype = datatype
        self.facet_restrictions = facet_restrictions

        self._accept_fn_for_visitor_cls[OWLDataRangeVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLDataRangeVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLDataVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLDataVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex
