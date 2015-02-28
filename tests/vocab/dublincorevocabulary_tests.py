import unittest
from owlapy.model.iri import IRI

from owlapy.vocab.dublincorevocabulary import DublinCoreVocabulary


class TestDublinCoreVocabulary(unittest.TestCase):
    def test___init__(self):
        # dc:contributor
        self.assertEqual('contributor',
                         DublinCoreVocabulary.CONTRIBUTOR.short_form)
        self.assertEqual('dc:contributor',
                         DublinCoreVocabulary.CONTRIBUTOR.qname)
        self.assertEqual('dc:contributor',
                         DublinCoreVocabulary.CONTRIBUTOR.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/contributor'),
                         DublinCoreVocabulary.CONTRIBUTOR.iri)
        # dc:coverage
        self.assertEqual('coverage',
                         DublinCoreVocabulary.COVERAGE.short_form)
        self.assertEqual('dc:coverage',
                         DublinCoreVocabulary.COVERAGE.qname)
        self.assertEqual('dc:coverage',
                         DublinCoreVocabulary.COVERAGE.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/coverage'),
                         DublinCoreVocabulary.COVERAGE.iri)
        # dc:creator
        self.assertEqual('creator',
                         DublinCoreVocabulary.CREATOR.short_form)
        self.assertEqual('dc:creator',
                         DublinCoreVocabulary.CREATOR.qname)
        self.assertEqual('dc:creator',
                         DublinCoreVocabulary.CREATOR.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/creator'),
                         DublinCoreVocabulary.CREATOR.iri)
        # dc:date
        self.assertEqual('date',
                         DublinCoreVocabulary.DATE.short_form)
        self.assertEqual('dc:date',
                         DublinCoreVocabulary.DATE.qname)
        self.assertEqual('dc:date',
                         DublinCoreVocabulary.DATE.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/date'),
                         DublinCoreVocabulary.DATE.iri)
        # dc:description
        self.assertEqual('description',
                         DublinCoreVocabulary.DESCRIPTION.short_form)
        self.assertEqual('dc:description',
                         DublinCoreVocabulary.DESCRIPTION.qname)
        self.assertEqual('dc:description',
                         DublinCoreVocabulary.DESCRIPTION.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/description'),
                         DublinCoreVocabulary.DESCRIPTION.iri)
        # dc:format
        self.assertEqual('format',
                         DublinCoreVocabulary.FORMAT.short_form)
        self.assertEqual('dc:format',
                         DublinCoreVocabulary.FORMAT.qname)
        self.assertEqual('dc:format',
                         DublinCoreVocabulary.FORMAT.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/format'),
                         DublinCoreVocabulary.FORMAT.iri)
        # dc:identifier
        self.assertEqual('identifier',
                         DublinCoreVocabulary.IDENTIFIER.short_form)
        self.assertEqual('dc:identifier',
                         DublinCoreVocabulary.IDENTIFIER.qname)
        self.assertEqual('dc:identifier',
                         DublinCoreVocabulary.IDENTIFIER.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/identifier'),
                         DublinCoreVocabulary.IDENTIFIER.iri)
        # dc:language
        self.assertEqual('language',
                         DublinCoreVocabulary.LANGUAGE.short_form)
        self.assertEqual('dc:language',
                         DublinCoreVocabulary.LANGUAGE.qname)
        self.assertEqual('dc:language',
                         DublinCoreVocabulary.LANGUAGE.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/language'),
                         DublinCoreVocabulary.LANGUAGE.iri)
        # dc:publisher
        self.assertEqual('publisher',
                         DublinCoreVocabulary.PUBLISHER.short_form)
        self.assertEqual('dc:publisher',
                         DublinCoreVocabulary.PUBLISHER.qname)
        self.assertEqual('dc:publisher',
                         DublinCoreVocabulary.PUBLISHER.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/publisher'),
                         DublinCoreVocabulary.PUBLISHER.iri)
        # dc:relation
        self.assertEqual('relation',
                         DublinCoreVocabulary.RELATION.short_form)
        self.assertEqual('dc:relation',
                         DublinCoreVocabulary.RELATION.qname)
        self.assertEqual('dc:relation',
                         DublinCoreVocabulary.RELATION.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/relation'),
                         DublinCoreVocabulary.RELATION.iri)
        # dc:rights
        self.assertEqual('rights',
                         DublinCoreVocabulary.RIGHTS.short_form)
        self.assertEqual('dc:rights',
                         DublinCoreVocabulary.RIGHTS.qname)
        self.assertEqual('dc:rights',
                         DublinCoreVocabulary.RIGHTS.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/rights'),
                         DublinCoreVocabulary.RIGHTS.iri)
        # dc:source
        self.assertEqual('source',
                         DublinCoreVocabulary.SOURCE.short_form)
        self.assertEqual('dc:source',
                         DublinCoreVocabulary.SOURCE.qname)
        self.assertEqual('dc:source',
                         DublinCoreVocabulary.SOURCE.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/source'),
                         DublinCoreVocabulary.SOURCE.iri)
        # dc:subject
        self.assertEqual('subject',
                         DublinCoreVocabulary.SUBJECT.short_form)
        self.assertEqual('dc:subject',
                         DublinCoreVocabulary.SUBJECT.qname)
        self.assertEqual('dc:subject',
                         DublinCoreVocabulary.SUBJECT.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/subject'),
                         DublinCoreVocabulary.SUBJECT.iri)
        # dc:title
        self.assertEqual('title',
                         DublinCoreVocabulary.TITLE.short_form)
        self.assertEqual('dc:title',
                         DublinCoreVocabulary.TITLE.qname)
        self.assertEqual('dc:title',
                         DublinCoreVocabulary.TITLE.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/title'),
                         DublinCoreVocabulary.TITLE.iri)
        # dc:type
        self.assertEqual('type',
                         DublinCoreVocabulary.TYPE.short_form)
        self.assertEqual('dc:type',
                         DublinCoreVocabulary.TYPE.qname)
        self.assertEqual('dc:type',
                         DublinCoreVocabulary.TYPE.prefixed_name)
        self.assertEqual(IRI('http://purl.org/dc/elements/1.1/type'),
                         DublinCoreVocabulary.TYPE.iri)

    def test___str__(self):
        self.assertEqual('http://purl.org/dc/elements/1.1/subject',
                         str(DublinCoreVocabulary.SUBJECT))

    def test_ALL_URIS(self):
        dc = 'http://purl.org/dc/elements/1.1/'
        dc_iris = [
            IRI(dc, 'contributor'), IRI(dc, 'coverage'), IRI(dc, 'creator'),
            IRI(dc, 'date'), IRI(dc, 'description'), IRI(dc, 'format'),
            IRI(dc, 'identifier'), IRI(dc, 'language'), IRI(dc, 'publisher'),
            IRI(dc, 'relation'), IRI(dc, 'rights'), IRI(dc, 'source'),
            IRI(dc, 'subject'), IRI(dc, 'title'), IRI(dc, 'type')
        ]
        all_entries = DublinCoreVocabulary.ALL_URIS
        self.assertEqual(len(dc_iris), len(all_entries))
        self.assertListEqual(dc_iris, DublinCoreVocabulary.ALL_URIS)