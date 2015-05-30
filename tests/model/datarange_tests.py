import unittest

from owlapy.model import DataRangeType
from owlapy.model import IRI


class TestDataRangeType(unittest.TestCase):

    def test___init__(self):
        # test all attributes on one item
        self.assertEqual('DataOneOf', DataRangeType.DATA_ONE_OF.name_)
        self.assertEqual('DataOneOf', DataRangeType.DATA_ONE_OF.short_form)
        self.assertEqual('owl:DataOneOf',
                         DataRangeType.DATA_ONE_OF.prefixed_name)
        self.assertEqual(IRI('http://www.w3.org/2002/07/owl#DataOneOf'),
                         DataRangeType.DATA_ONE_OF.iri)

        # test all items on one attribute
        self.assertEqual('Datatype', DataRangeType.DATATYPE.name_)
        self.assertEqual('DatatypeRestriction',
                         DataRangeType.DATATYPE_RESTRICTION.name_)
        self.assertEqual('DataComplementOf',
                         DataRangeType.DATA_COMPLEMENT_OF.name_)
        self.assertEqual('DataUnionOf', DataRangeType.DATA_UNION_OF.name_)
        self.assertEqual('DataIntersectionOf',
                         DataRangeType.DATA_INTERSECTION_OF.name_)
