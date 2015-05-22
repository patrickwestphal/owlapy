import unittest

from owlapy.model import IRI
from owlapy.vocab.namespaces import Namespaces
from owlapy.vocab.owlfacet import OWLFacet


class TestOWLFacet(unittest.TestCase):
    num_facets = 11

    def test___init__(self):
        iri = IRI(str(Namespaces.XSD), 'maxExclusive')
        self.assertEqual(iri, OWLFacet.MAX_EXCLUSIVE.iri, )
        short_form = 'maxExclusive'
        self.assertEqual(short_form, OWLFacet.MAX_EXCLUSIVE.short_form)
        symbolic_form = '<'
        self.assertEqual(symbolic_form, OWLFacet.MAX_EXCLUSIVE.symbolic_form)
        prefixed_name = 'xsd:maxExclusive'
        self.assertEqual(prefixed_name, OWLFacet.MAX_EXCLUSIVE.prefixed_name)

    def test_facet_set(self):
        self.assertEqual(self.num_facets, len(OWLFacet))

        self.assertIsNotNone(OWLFacet.LENGTH)  # 1
        self.assertIsNotNone(OWLFacet.MIN_LENGTH)  # 2
        self.assertIsNotNone(OWLFacet.MAX_LENGTH)  # 3
        self.assertIsNotNone(OWLFacet.PATTERN)  # 4
        self.assertIsNotNone(OWLFacet.MIN_INCLUSIVE)  # 5
        self.assertIsNotNone(OWLFacet.MIN_EXCLUSIVE)  # 6
        self.assertIsNotNone(OWLFacet.MAX_INCLUSIVE)  # 7
        self.assertIsNotNone(OWLFacet.MAX_EXCLUSIVE)  # 8
        self.assertIsNotNone(OWLFacet.TOTAL_DIGITS)  # 9
        self.assertIsNotNone(OWLFacet.FRACTION_DIGITS)  # 10
        self.assertIsNotNone(OWLFacet.LANG_RANGE)  # 11

    def test_facet_iris_set(self):
        self.assertEqual(self.num_facets, len(OWLFacet.FACET_IRIS))

        self.assertIn(OWLFacet.LENGTH.iri, OWLFacet.FACET_IRIS)  # 1
        self.assertIn(OWLFacet.MIN_LENGTH.iri, OWLFacet.FACET_IRIS)  # 2
        self.assertIn(OWLFacet.MAX_LENGTH.iri, OWLFacet.FACET_IRIS)  # 3
        self.assertIn(OWLFacet.PATTERN.iri, OWLFacet.FACET_IRIS)  # 4
        self.assertIn(OWLFacet.MIN_INCLUSIVE.iri, OWLFacet.FACET_IRIS)  # 5
        self.assertIn(OWLFacet.MIN_EXCLUSIVE.iri, OWLFacet.FACET_IRIS)  # 6
        self.assertIn(OWLFacet.MAX_INCLUSIVE.iri, OWLFacet.FACET_IRIS)  # 7
        self.assertIn(OWLFacet.MAX_EXCLUSIVE.iri, OWLFacet.FACET_IRIS)  # 8
        self.assertIn(OWLFacet.TOTAL_DIGITS.iri, OWLFacet.FACET_IRIS)  # 9
        self.assertIn(OWLFacet.FRACTION_DIGITS.iri, OWLFacet.FACET_IRIS)  # 10
        self.assertIn(OWLFacet.LANG_RANGE.iri, OWLFacet.FACET_IRIS)  # 11

    def test_get_facet(self):
        length_iri = IRI('http://www.w3.org/2001/XMLSchema#length')
        self.assertEqual(OWLFacet.LENGTH, OWLFacet.get_facet(length_iri))

        min_length_iri = IRI('http://www.w3.org/2001/XMLSchema#minLength')
        self.assertEqual(OWLFacet.MIN_LENGTH,
                         OWLFacet.get_facet(min_length_iri))

        max_length_iri = IRI('http://www.w3.org/2001/XMLSchema#maxLength')
        self.assertEqual(OWLFacet.MAX_LENGTH,
                         OWLFacet.get_facet(max_length_iri))

        pattern_iri = IRI('http://www.w3.org/2001/XMLSchema#pattern')
        self.assertEqual(OWLFacet.PATTERN, OWLFacet.get_facet(pattern_iri))

        min_incl_iri = IRI('http://www.w3.org/2001/XMLSchema#minInclusive')
        self.assertEqual(OWLFacet.MIN_INCLUSIVE,
                         OWLFacet.get_facet(min_incl_iri))

        min_excl_iri = IRI('http://www.w3.org/2001/XMLSchema#minExclusive')
        self.assertEqual(OWLFacet.MIN_EXCLUSIVE,
                         OWLFacet.get_facet(min_excl_iri))

        max_incl_iri = IRI('http://www.w3.org/2001/XMLSchema#maxInclusive')
        self.assertEqual(OWLFacet.MAX_INCLUSIVE,
                         OWLFacet.get_facet(max_incl_iri))

        max_excl_iri = IRI('http://www.w3.org/2001/XMLSchema#maxExclusive')
        self.assertEqual(OWLFacet.MAX_EXCLUSIVE,
                         OWLFacet.get_facet(max_excl_iri))

        total_digits_iri = IRI('http://www.w3.org/2001/XMLSchema#totalDigits')
        self.assertEqual(OWLFacet.TOTAL_DIGITS,
                         OWLFacet.get_facet(total_digits_iri))

        frac_digits_iri = IRI('http://www.w3.org/2001/XMLSchema#fractionDigits')
        self.assertEqual(OWLFacet.FRACTION_DIGITS,
                         OWLFacet.get_facet(frac_digits_iri))

        lang_range_iri = IRI(
            'http://www.w3.org/1999/02/22-rdf-syntax-ns#langRange')
        self.assertEqual(OWLFacet.LANG_RANGE,
                         OWLFacet.get_facet(lang_range_iri))

    def test_get_facet_by_short_name(self):
        self.assertEqual(OWLFacet.LENGTH,
                         OWLFacet.get_facet_by_short_name('length'))
        self.assertEqual(OWLFacet.MIN_LENGTH,
                         OWLFacet.get_facet_by_short_name('minLength'))
        self.assertEqual(OWLFacet.MAX_LENGTH,
                         OWLFacet.get_facet_by_short_name('maxLength'))
        self.assertEqual(OWLFacet.PATTERN,
                         OWLFacet.get_facet_by_short_name('pattern'))
        self.assertEqual(OWLFacet.MIN_INCLUSIVE,
                         OWLFacet.get_facet_by_short_name('minInclusive'))
        self.assertEqual(OWLFacet.MIN_EXCLUSIVE,
                         OWLFacet.get_facet_by_short_name('minExclusive'))
        self.assertEqual(OWLFacet.MAX_INCLUSIVE,
                         OWLFacet.get_facet_by_short_name('maxInclusive'))
        self.assertEqual(OWLFacet.MAX_EXCLUSIVE,
                         OWLFacet.get_facet_by_short_name('maxExclusive'))
        self.assertEqual(OWLFacet.TOTAL_DIGITS,
                         OWLFacet.get_facet_by_short_name('totalDigits'))
        self.assertEqual(OWLFacet.FRACTION_DIGITS,
                         OWLFacet.get_facet_by_short_name('fractionDigits'))
        self.assertEqual(OWLFacet.LANG_RANGE,
                         OWLFacet.get_facet_by_short_name('langRange'))

    def test_get_facet_by_symbolic_name(self):
        self.assertEqual(OWLFacet.LENGTH,
                         OWLFacet.get_facet_by_symbolic_name('length'))
        self.assertEqual(OWLFacet.MIN_LENGTH,
                         OWLFacet.get_facet_by_symbolic_name('minLength'))
        self.assertEqual(OWLFacet.MAX_LENGTH,
                         OWLFacet.get_facet_by_symbolic_name('maxLength'))
        self.assertEqual(OWLFacet.PATTERN,
                         OWLFacet.get_facet_by_symbolic_name('pattern'))
        self.assertEqual(OWLFacet.MIN_INCLUSIVE,
                         OWLFacet.get_facet_by_symbolic_name('>='))
        self.assertEqual(OWLFacet.MIN_EXCLUSIVE,
                         OWLFacet.get_facet_by_symbolic_name('>'))
        self.assertEqual(OWLFacet.MAX_INCLUSIVE,
                         OWLFacet.get_facet_by_symbolic_name('<='))
        self.assertEqual(OWLFacet.MAX_EXCLUSIVE,
                         OWLFacet.get_facet_by_symbolic_name('<'))
        self.assertEqual(OWLFacet.TOTAL_DIGITS,
                         OWLFacet.get_facet_by_symbolic_name('totalDigits'))
        self.assertEqual(OWLFacet.FRACTION_DIGITS,
                         OWLFacet.get_facet_by_symbolic_name('fractionDigits'))
        self.assertEqual(OWLFacet.LANG_RANGE,
                         OWLFacet.get_facet_by_symbolic_name('langRange'))

    def test_get_facets(self):
        self.assertIn('length', OWLFacet.get_facets())
        self.assertIn('minLength', OWLFacet.get_facets())
        self.assertIn('maxLength', OWLFacet.get_facets())
        self.assertIn('pattern', OWLFacet.get_facets())
        self.assertIn('>=', OWLFacet.get_facets())
        self.assertIn('>', OWLFacet.get_facets())
        self.assertIn('<=', OWLFacet.get_facets())
        self.assertIn('<', OWLFacet.get_facets())
        self.assertIn('totalDigits', OWLFacet.get_facets())
        self.assertIn('fractionDigits', OWLFacet.get_facets())
        self.assertIn('langRange', OWLFacet.get_facets())