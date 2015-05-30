from enum import Enum

from .iri import IRI
from owlapy.vocab.namespaces import Namespaces


class DataRangeType(Enum):

    DATATYPE = 'Datatype'
    DATA_ONE_OF = 'DataOneOf'
    DATATYPE_RESTRICTION = 'DatatypeRestriction'
    DATA_COMPLEMENT_OF = 'DataComplementOf'
    DATA_UNION_OF = 'DataUnionOf'
    DATA_INTERSECTION_OF = 'DataIntersectionOf'

    def __init__(self, name):
        self.name_ = name
        self.short_form = name
        self.prefixed_name = Namespaces.OWL.prefix_name + ':' + name
        self.iri = IRI(Namespaces.OWL.prefix_iri, name)
