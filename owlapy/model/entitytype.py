from enum import Enum
from owlapy.util.decorators import ClassProperty

from owlapy.vocab.owlrdfvocabulary import OWLRDFVocabulary


class EntityType(Enum):
    """Represents the different types of OWL 2 Entities."""

    CLASS = ('Class', 'Class', 'Classes', OWLRDFVocabulary.OWL_CLASS)
    OBJECT_PROPERTY = ('ObjectProperty', 'Object property', 'Object properties',
                       OWLRDFVocabulary.OWL_OBJECT_PROPERTY)
    DATA_PROPERTY = ('DataProperty', 'Data property', 'Data properties',
                     OWLRDFVocabulary.OWL_DATA_PROPERTY)
    ANNOTATION_PROPERTY = ('AnnotationProperty', 'Annotation property',
                           'Annotation properties',
                           OWLRDFVocabulary.OWL_ANNOTATION_PROPERTY)
    NAMED_INDIVIDUAL = ('NamedIndividual', 'Named individual',
                        'Named individuals',
                        OWLRDFVocabulary.OWL_NAMED_INDIVIDUAL)
    DATATYPE = ('Datatype', 'Datatype', 'Datatypes',
                OWLRDFVocabulary.RDFS_DATATYPE)

    def __init__(self, name, print_name, plural_print_name, vocabulary):
        """
        :param name: a string containing the type name
        :param print_name: a string containing the type's print name
        :param plural_print_name: a string containing the type's plural print
            name
        :param vocabulary: a owlapy.vocab vocabulary
        """
        # FIXME: should be name but doesn't work with Enum
        self.name_ = name
        self.short_form = name
        self.print_name = print_name
        self.plural_print_name = plural_print_name
        self.vocabulary = vocabulary

    def __str__(self):
        return self.name_

    def __repr__(self):
        return self.name_

    @ClassProperty
    @classmethod
    def values(cls):
        return [cls.CLASS, cls.OBJECT_PROPERTY, cls.DATA_PROPERTY,
                cls.ANNOTATION_PROPERTY, cls.NAMED_INDIVIDUAL, cls.DATATYPE]

    @property
    def prefixed_name(self):
        """
        :return: a string containing the prefixed name,
            i.e. <prefix>:<short_name>
        """
        return self.vocabulary.prefixed_name

    @property
    def iri(self):
        return self.vocabulary.iri
