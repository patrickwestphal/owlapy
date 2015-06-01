from .datarangetype import DataRangeType
from .entitytype import EntityType
from .exceptions import NoneValueException, OWLRuntimeException
from .owldatarangevisitor import OWLDataRangeVisitor, OWLDataRangeVisitorEx
from .owldatatype import OWLDatatype
from .owldatavisitor import OWLDataVisitor, OWLDataVisitorEx
from .owlentityvisitor import OWLEntityVisitor, OWLEntityVisitorEx
from .owlnamedobjectvisitor import OWLNamedObjectVisitor
from .owlobjectvisitor import OWLObjectVisitor, OWLObjectVisitorEx
from owlapy.util import accept_default, accept_default_ex
from owlapy.util.decorators import ClassProperty
import owlapy.vocab.owl2datatype as vocab_owl2datatype
import owlapy.util


class OWL2Datatype(OWLDatatype):

    def __init__(self, owl2_datatype):
        if owl2_datatype is None:
            raise NoneValueException('owl2_datatype must not be null')

        self.owl2_datatype = owl2_datatype
        super().__init__(owl2_datatype.iri)

        self._accept_fn_for_visitor_cls[OWLDataRangeVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLDataRangeVisitorEx] = \
            accept_default_ex
        self._accept_fn_for_visitor_cls[OWLDataVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLDataVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLEntityVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLEntityVisitorEx] = accept_default_ex
        self._accept_fn_for_visitor_cls[OWLNamedObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitor] = accept_default
        self._accept_fn_for_visitor_cls[OWLObjectVisitorEx] = accept_default_ex

    def __str__(self):
        return self.to_string_id()

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if id(self) == id(other):
            return True

        if not isinstance(other, OWLDatatype):
            return False

        return self.owl2_datatype.iri == other.iri

    def __hash__(self):
        return super().__hash__()

    @ClassProperty
    @classmethod
    def instance_map(cls):
        if not hasattr(cls, '_instance_map'):
            cls._instance_map = {}
            for dtype in vocab_owl2datatype.OWL2Datatype:
                cls._instance_map[dtype] = OWL2Datatype(dtype)

        return cls._instance_map

    @classmethod
    def get_datatype(cls, datatype):
        """
        :param datatype: an owlapy.vocab.OWL2Datatype object
        :return: an owlapy.model.OWLDatatype object
        """
        return cls.instance_map[datatype]

    def get_built_in_type(self):
        return self.owl2_datatype

    def is_string(self):
        return self.owl2_datatype == vocab_owl2datatype.OWL2Datatype.XSD_STRING

    def is_integer(self):
        return self.owl2_datatype == vocab_owl2datatype.OWL2Datatype.XSD_INTEGER

    def is_float(self):
        return self.owl2_datatype == vocab_owl2datatype.OWL2Datatype.XSD_FLOAT

    def is_double(self):
        return self.owl2_datatype == vocab_owl2datatype.OWL2Datatype.XSD_DOUBLE

    def is_boolean(self):
        return self.owl2_datatype == vocab_owl2datatype.OWL2Datatype.XSD_BOOLEAN

    def is_rdf_plain_literal(self):
        return self.owl2_datatype == \
            vocab_owl2datatype.OWL2Datatype.RDF_PLAIN_LITERAL

    def is_datatype(self):
        return True

    def is_top_datatype(self):
        return self.owl2_datatype == \
            vocab_owl2datatype.OWL2Datatype.RDFS_LITERAL

    def as_owl_datatype(self):
        return self

    def get_data_range_type(self):
        return DataRangeType.DATATYPE

    def get_entity_type(self):
        return EntityType.DATATYPE

    def get_owl_entity(self, entity_type):
        from owlapy.model import OWLObject
        return OWLObject.get_owl_entity(
            entity_type, vocab_owl2datatype.OWL2Datatype.RDF_PLAIN_LITERAL.iri)

    def is_type(self, other_entity_type):
        return other_entity_type == EntityType.DATATYPE

    def get_annotations(self, ontology, annotation_property=None):
        """
        :param ontology: an owlapy.model.OWLOntology object
        :param annotation_property: an owlapy.model.OWLAnnotationProperty object
        :return: a set of owlapy.model.OWLAnnotation objects
        """
        return owlapy.util.get_annotations(
            self, {ontology}, annotation_property)

    def get_annotation_assertion_axioms(self, ontology):
        """
        :param ontology: an owlapy.model.OWLOntology object
        :return: a set of owlapy.model.OWLAnnotationAssertionAxiom objects
        """
        return owlapy.util.get_annotation_axioms(self, {ontology})

    def is_built_in(self):
        return True

    def is_owl_class(self):
        return False

    def as_owl_class(self):
        raise OWLRuntimeException('Not an OWLClass')

    def is_owl_object_property(self):
        return False

    def as_owl_object_property(self):
        raise OWLRuntimeException('Not an OWLObjectProperty')

    def is_owl_data_property(self):
        return False

    def as_owl_data_property(self):
        raise OWLRuntimeException('Not an OWLDataProperty')

    def is_owl_named_individual(self):
        return False

    def as_owl_named_individual(self):
        raise OWLRuntimeException('Not an OWLNamedIndividual')

    def is_owl_datatype(self):
        return True

    def is_owl_annotation_property(self):
        return False

    def as_owl_annotation_property(self):
        raise OWLRuntimeException('Not an OWLAnnotationProperty')

    def to_string_id(self):
        return str(self.owl2_datatype.iri)

    def get_referencing_axioms(self, ontology, include_imports=False):
        """
        :param ontology: an owlapy.model.OWLOntology object
        :return: a set of owlapy.model.OWLAxiom objects
        """
        return ontology.get_referencing_axioms(self, include_imports)

    def get_signature(self):
        return {self}

    def contains_entity_in_signature(self, entity):
        """
        :param entity: an owlapy.model.OWLEntity object
        """
        return self == entity

    def get_anonymous_individuals(self):
        return set()

    def get_classes_in_signature(self):
        return set()

    def get_data_properties_in_signature(self):
        return set()

    def get_object_properties_in_signature(self):
        return set()

    def get_individuals_in_signature(self):
        return set()

    def get_datatypes_in_signature(self):
        # note: in the original OWLAPI code, self is casted to model.OWLDatatype
        # hence, the type will be different here (i.e. OWL2Datatype instead of
        # OWLDatatype)
        return {self}

    def get_nested_class_expressions(self):
        return set()

    def is_top_entity(self):
        return self.owl2_datatype == \
            vocab_owl2datatype.OWL2Datatype.RDF_PLAIN_LITERAL

    def is_bottom_entity(self):
        return False

    def compare_to(self, other):
        if not isinstance(other, OWLDatatype):
            from owlapy.util.owlobjecttypeindexprovider import \
                OWLObjectTypeIndexProvider
            provider = OWLObjectTypeIndexProvider()
            return provider.get_type_index(other)

        return self.iri.compare_to(other.iri)
