from enum import Enum

from owlapy.model.iri import IRI
from owlapy.util.decorators import ClassProperty
from owlapy.vocab.namespaces import Namespaces


class OWLRDFVocabulary(Enum):
    """http://www.w3.org/2002/07/owl#"""

    OWL_THING = (Namespaces.OWL, 'Thing')
    OWL_NOTHING = (Namespaces.OWL, 'Nothing')
    OWL_CLASS = (Namespaces.OWL, 'Class')
    OWL_ONTOLOGY = (Namespaces.OWL, 'Ontology')
    OWL_ONTOLOGY_PROPERTY = (Namespaces.OWL, 'OntologyProperty')  # deprecated
    OWL_IMPORTS = (Namespaces.OWL, 'imports')
    OWL_VERSION_IRI = (Namespaces.OWL, 'versionIRI')
    OWL_VERSION_INFO = (Namespaces.OWL, 'versionInfo')
    OWL_EQUIVALENT_CLASS = (Namespaces.OWL, 'equivalentClass')
    OWL_OBJECT_PROPERTY = (Namespaces.OWL, 'ObjectProperty')
    OWL_DATA_PROPERTY = (Namespaces.OWL, 'DatatypeProperty')
    OWL_FUNCTIONAL_PROPERTY = (Namespaces.OWL, 'FunctionalProperty')
    OWL_INVERSE_FUNCTIONAL_PROPERTY = (Namespaces.OWL,
                                       'InverseFunctionalProperty')
    # deprecated
    OWL_ANTI_SYMMETRIC_PROPERTY = (Namespaces.OWL, 'AntisymmetricProperty')
    OWL_ASYMMETRIC_PROPERTY = (Namespaces.OWL, 'AsymmetricProperty')
    OWL_SYMMETRIC_PROPERTY = (Namespaces.OWL, 'SymmetricProperty')
    OWL_RESTRICTION = (Namespaces.OWL, 'Restriction')
    OWL_DATA_RESTRICTION = (Namespaces.OWL, 'DataRestriction')  # deprecated
    OWL_OBJECT_RESTRICTION = (Namespaces.OWL, 'ObjectRestriction')  # deprecated
    OWL_ON_PROPERTY = (Namespaces.OWL, 'onProperty')
    OWL_INTERSECTION_OF = (Namespaces.OWL, 'intersectionOf')
    OWL_UNION_OF = (Namespaces.OWL, 'unionOf')
    OWL_ALL_VALUES_FROM = (Namespaces.OWL, 'allValuesFrom')
    OWL_SOME_VALUES_FROM = (Namespaces.OWL, 'someValuesFrom')
    OWL_HAS_VALUE = (Namespaces.OWL, 'hasValue')
    OWL_DISJOINT_WITH = (Namespaces.OWL, 'disjointWith')
    OWL_ONE_OF = (Namespaces.OWL, 'oneOf')
    OWL_SELF_RESTRICTION = (Namespaces.OWL, 'SelfRestriction')  # deprecated
    OWL_HAS_SELF = (Namespaces.OWL, 'hasSelf')
    OWL_DISJOINT_UNION_OF = (Namespaces.OWL, 'disjointUnionOf')
    OWL_MIN_CARDINALITY = (Namespaces.OWL, 'minCardinality')
    OWL_MIN_QUALIFIED_CARDINALITY = (Namespaces.OWL, 'minQualifiedCardinality')
    OWL_CARDINALITY = (Namespaces.OWL, 'cardinality')
    OWL_QUALIFIED_CARDINALITY = (Namespaces.OWL, 'qualifiedCardinality')
    OWL_ANNOTATION_PROPERTY = (Namespaces.OWL, 'AnnotationProperty')
    OWL_ANNOTATION = (Namespaces.OWL, 'Annotation')
    OWL_DECLARED_AS = (Namespaces.OWL, 'declaredAs')  # deprecated
    OWL_INDIVIDUAL = (Namespaces.OWL, 'Individual')
    OWL_NAMED_INDIVIDUAL = (Namespaces.OWL, 'NamedIndividual')
    OWL_DATATYPE = (Namespaces.OWL, 'Datatype')
    RDFS_SUBCLASS_OF = (Namespaces.RDFS, 'subClassOf')
    RDFS_SUB_PROPERTY_OF = (Namespaces.RDFS, 'subPropertyOf')
    RDF_TYPE = (Namespaces.RDF, 'type')
    RDF_NIL = (Namespaces.RDF, 'nil')
    RDF_REST = (Namespaces.RDF, 'rest')
    RDF_FIRST = (Namespaces.RDF, 'first')
    RDF_LIST = (Namespaces.RDF, 'List')
    OWL_MAX_CARDINALITY = (Namespaces.OWL, 'maxCardinality')
    OWL_MAX_QUALIFIED_CARDINALITY = (Namespaces.OWL, 'maxQualifiedCardinality')
    # deprecated
    OWL_NEGATIVE_OBJECT_PROPERTY_ASSERTION = (Namespaces.OWL,
                                              'NegativeObjectPropertyAssertion')
    # deprecated
    OWL_NEGATIVE_DATA_PROPERTY_ASSERTION = (Namespaces.OWL,
                                            'NegativeDataPropertyAssertion')
    OWL_NEGATIVE_PROPERTY_ASSERTION = (Namespaces.OWL,
                                       'NegativePropertyAssertion')
    RDFS_LABEL = (Namespaces.RDFS, 'label')
    RDFS_COMMENT = (Namespaces.RDFS, 'comment')
    RDFS_SEE_ALSO = (Namespaces.RDFS, 'seeAlso')
    RDFS_IS_DEFINED_BY = (Namespaces.RDFS, 'isDefinedBy')
    RDFS_RESOURCE = (Namespaces.RDFS, 'Resource')
    RDFS_LITERAL = (Namespaces.RDFS, 'Literal')
    RDF_PLAIN_LITERAL = (Namespaces.RDF, 'PlainLiteral')
    RDFS_DATATYPE = (Namespaces.RDFS, 'Datatype')
    OWL_TRANSITIVE_PROPERTY = (Namespaces.OWL, 'TransitiveProperty')
    OWL_REFLEXIVE_PROPERTY = (Namespaces.OWL, 'ReflexiveProperty')
    OWL_IRREFLEXIVE_PROPERTY = (Namespaces.OWL, 'IrreflexiveProperty')
    OWL_INVERSE_OF = (Namespaces.OWL, 'inverseOf')
    OWL_COMPLEMENT_OF = (Namespaces.OWL, 'complementOf')
    OWL_DATATYPE_COMPLEMENT_OF = (Namespaces.OWL, 'datatypeComplementOf')
    OWL_ALL_DIFFERENT = (Namespaces.OWL, 'AllDifferent')
    OWL_DISTINCT_MEMBERS = (Namespaces.OWL, 'distinctMembers')
    OWL_SAME_AS = (Namespaces.OWL, 'sameAs')
    OWL_DIFFERENT_FROM = (Namespaces.OWL, 'differentFrom')
    OWL_DEPRECATED_PROPERTY = (Namespaces.OWL, 'DeprecatedProperty')
    OWL_EQUIVALENT_PROPERTY = (Namespaces.OWL, 'equivalentProperty')
    OWL_DEPRECATED_CLASS = (Namespaces.OWL, 'DeprecatedClass')
    OWL_DATA_RANGE = (Namespaces.OWL, 'DataRange')
    RDFS_DOMAIN = (Namespaces.RDFS, 'domain')
    RDFS_RANGE = (Namespaces.RDFS, 'range')
    RDFS_CLASS = (Namespaces.RDFS, 'Class')
    RDF_PROPERTY = (Namespaces.RDF, 'Property')
    RDF_SUBJECT = (Namespaces.RDF, 'subject')  # deprecated
    RDF_PREDICATE = (Namespaces.RDF, 'predicate')  # deprecated
    RDF_OBJECT = (Namespaces.RDF, 'object')  # deprecated
    OWL_SUBJECT = (Namespaces.OWL, 'subject')  # deprecated
    OWL_PREDICATE = (Namespaces.OWL, 'predicate')  # deprecated
    OWL_OBJECT = (Namespaces.OWL, 'object')  # deprecated
    RDF_DESCRIPTION = (Namespaces.RDF, 'Description')
    RDF_XML_LITERAL = (Namespaces.RDF, 'XMLLiteral')
    OWL_PRIOR_VERSION = (Namespaces.OWL, 'priorVersion')
    OWL_DEPRECATED = (Namespaces.OWL, 'deprecated')
    OWL_BACKWARD_COMPATIBLE_WITH = (Namespaces.OWL, 'backwardCompatibleWith')
    OWL_INCOMPATIBLE_WITH = (Namespaces.OWL, 'incompatibleWith')
    # deprecated
    OWL_OBJECT_PROPERTY_DOMAIN = (Namespaces.OWL, 'objectPropertyDomain')
    # deprecated
    OWL_DATA_PROPERTY_DOMAIN = (Namespaces.OWL, 'dataPropertyDomain')
    # deprecated
    OWL_DATA_PROPERTY_RANGE = (Namespaces.OWL, 'dataPropertyRange')
    # deprecated
    OWL_OBJECT_PROPERTY_RANGE = (Namespaces.OWL, 'objectPropertyRange')
    # deprecated
    OWL_SUB_OBJECT_PROPERTY_OF = (Namespaces.OWL, 'subObjectPropertyOf')
    # deprecated
    OWL_SUB_DATA_PROPERTY_OF = (Namespaces.OWL, 'subDataPropertyOf')
    # deprecated
    OWL_DISJOINT_DATA_PROPERTIES = (Namespaces.OWL, 'disjointDataProperties')
    # deprecated
    OWL_DISJOINT_OBJECT_PROPERTIES = (Namespaces.OWL,
                                      'disjointObjectProperties')
    OWL_PROPERTY_DISJOINT_WITH = (Namespaces.OWL, 'propertyDisjointWith')
    # deprecated
    OWL_EQUIVALENT_DATA_PROPERTIES = (Namespaces.OWL, 'equivalentDataProperty')
    # deprecated
    OWL_EQUIVALENT_OBJECT_PROPERTIES = (Namespaces.OWL,
                                        'equivalentObjectProperty')
    # deprecated
    OWL_FUNCTIONAL_DATA_PROPERTY = (Namespaces.OWL, 'FunctionalDataProperty')
    # deprecated
    OWL_FUNCTIONAL_OBJECT_PROPERTY = (Namespaces.OWL,
                                      'FunctionalObjectProperty')
    OWL_ON_CLASS = (Namespaces.OWL, 'onClass')
    OWL_ON_DATA_RANGE = (Namespaces.OWL, 'onDataRange')
    OWL_ON_DATA_TYPE = (Namespaces.OWL, 'onDatatype')
    OWL_WITH_RESTRICTIONS = (Namespaces.OWL, 'withRestrictions')
    OWL_INVERSE_OBJECT_PROPERTY_EXPRESSION = (Namespaces.OWL,
                                              'inverseObjectPropertyExpression')
    OWL_AXIOM = (Namespaces.OWL, 'Axiom')
    OWL_PROPERTY_CHAIN = (Namespaces.OWL, 'propertyChain')  # deprecated
    OWL_PROPERTY_CHAIN_AXIOM = (Namespaces.OWL, 'propertyChainAxiom')
    OWL_ALL_DISJOINT_CLASSES = (Namespaces.OWL, 'AllDisjointClasses')
    OWL_MEMBERS = (Namespaces.OWL, 'members')
    OWL_ALL_DISJOINT_PROPERTIES = (Namespaces.OWL, 'AllDisjointProperties')
    OWL_TOP_OBJECT_PROPERTY = (Namespaces.OWL, 'topObjectProperty')
    OWL_BOTTOM_OBJECT_PROPERTY = (Namespaces.OWL, 'bottomObjectProperty')
    OWL_TOP_DATA_PROPERTY = (Namespaces.OWL, 'topDataProperty')
    OWL_BOTTOM_DATA_PROPERTY = (Namespaces.OWL, 'bottomDataProperty')
    OWL_HAS_KEY = (Namespaces.OWL, 'hasKey')
    OWL_ANNOTATED_SOURCE = (Namespaces.OWL, 'annotatedSource')
    OWL_ANNOTATED_PROPERTY = (Namespaces.OWL, 'annotatedProperty')
    OWL_ANNOTATED_TARGET = (Namespaces.OWL, 'annotatedTarget')
    OWL_SOURCE_INDIVIDUAL = (Namespaces.OWL, 'sourceIndividual')
    OWL_ASSERTION_PROPERTY = (Namespaces.OWL, 'assertionProperty')
    OWL_TARGET_INDIVIDUAL = (Namespaces.OWL, 'targetIndividual')
    OWL_TARGET_VALUE = (Namespaces.OWL, 'targetValue')

    def __init__(self, namespace, short_name):
        """
        :param namespace: one of owlapy.vocab.namespaces.Namespaces
        :param short_name: a string containing the IRI suffix
        """
        self.namespace = namespace
        self.short_name = short_name
        self.short_form = short_name
        self.prefixed_name = namespace.prefix_name + ':' + short_name
        self.iri = IRI.create(str(namespace), short_name)

    def __str__(self):
        return str(self.iri)

    def __repr__(self):
        return str(self.iri)

    @ClassProperty
    @classmethod
    def BUILT_IN_VOCABULARY_IRIS(cls):
        return [entry.iri for entry in cls]

    @ClassProperty
    @classmethod
    def BUILT_IN_ANNOTATION_PROPERTY_IRIS(cls):
        ann_props = [
            cls.RDFS_LABEL.iri, cls.RDFS_COMMENT.iri, cls.OWL_VERSION_INFO.iri,
            cls.OWL_BACKWARD_COMPATIBLE_WITH.iri, cls.OWL_PRIOR_VERSION.iri,
            cls.RDFS_SEE_ALSO.iri, cls.RDFS_IS_DEFINED_BY.iri,
            cls.OWL_INCOMPATIBLE_WITH.iri, cls.OWL_DEPRECATED.iri
        ]

        return ann_props