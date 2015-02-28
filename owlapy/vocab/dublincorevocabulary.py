from enum import Enum

from owlapy.vocab.namespaces import Namespaces
from owlapy.model import IRI


class ClassProperty(property):
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()


class DublinCoreVocabulary(Enum):
    CONTRIBUTOR = 'contributor'  # http://purl.org/dc/elements/1.1/contributor
    COVERAGE = 'coverage'  # http://purl.org/dc/elements/1.1/coverage
    CREATOR = 'creator'  # http://purl.org/dc/elements/1.1/creator
    DATE = 'date'  # http://purl.org/dc/elements/1.1/date
    DESCRIPTION = 'description'  # http://purl.org/dc/elements/1.1/description
    FORMAT = 'format'  # http://purl.org/dc/elements/1.1/format
    IDENTIFIER = 'identifier'  # http://purl.org/dc/elements/1.1/identifier
    LANGUAGE = 'language'  # http://purl.org/dc/elements/1.1/language
    PUBLISHER = 'publisher'  # http://purl.org/dc/elements/1.1/publisher
    RELATION = 'relation'  # http://purl.org/dc/elements/1.1/relation
    RIGHTS = 'rights'  # http://purl.org/dc/elements/1.1/rights
    SOURCE = 'source'  # http://purl.org/dc/elements/1.1/source
    SUBJECT = 'subject'  # http://purl.org/dc/elements/1.1/subject
    TITLE = 'title'  # http://purl.org/dc/elements/1.1/title
    TYPE = 'type'  # http://purl.org/dc/elements/1.1/type

    def __init__(self, name):
        self.short_form = name
        self.qname = Namespaces.DC.prefix_name + ':' + name
        self.prefixed_name = self.qname
        self.iri = IRI.create(Namespaces.DC.ns, name)

    def __str__(self):
        return str(self.iri)

    def __repr__(self):
        return str(self.iri)

    @ClassProperty
    @classmethod
    def ALL_URIS(cls):
        return [entry.iri for entry in cls]
