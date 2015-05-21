from enum import Enum
from owlapy.util.decorators import ClassProperty


class AxiomType(Enum):
    """Represents the type of axioms which can belong to ontologies. Axioms can
    be retrieved from ontologies by their AxiomType.
    """

    def __init__(self, ind, name, owl2_axiom, non_syntactic_owl2_axiom,
                 is_logical):
        """
        :param ind: an integer indicating the index in the axiom type list
        :param name: a string containing the name of the axiom type
        :param owl2_axiom: boolean indicating whether this is an OWL2 axiom;
            Some OWL 2 axioms, for example,
            owlapy.model.OWLNegativeDataPropertyAssertionAxiom axioms are
            structurally OWL 2 axioms, but can be represented using OWL 1
            syntax. This boolean determines if this axiom type is a pure OWL 2
            axiom and cannot be represented using OWL 1 syntax.
        :param non_syntactic_owl2_axiom: boolean indicating whether this is a
            syntactical OWL2 axiom
        :param is_logical: boolean indicating whether this axiom type is a
            logical axiom type
        """
        self.name_ = name
        self.owl2_axiom = owl2_axiom
        self.non_syntactic_owl2_axiom = non_syntactic_owl2_axiom
        self.is_logical = is_logical
        self.index = ind

    def __str__(self):
        return self.name_

    def __repr__(self):
        return self.__str__()

    @classmethod
    def get_instance(cls, idx, name, owl2_axiom, non_syntactic_owl2_axiom,
                     is_logical):
        return AxiomType(idx, name, owl2_axiom, non_syntactic_owl2_axiom,
                         is_logical)

    @classmethod
    def get_axioms_without_types(cls, source_axioms, *axiom_types):
        """Gets the set of axioms from a source set of axioms that are not of
        the specified type

        :param source_axioms: The source set of owlapy.modelOWLAxiom objects
        :param axiom_types: The owlapy.model.AxiomType objects that will be
            filtered out of the source set
        :return: A set of owlapy.model.OWLAxiom objects that represents the
            source_axioms without the specified types. Note that source_axioms
            will not be modified. The returned set is a copy.
        """
        result = set()
        disallowed = set()
        for axiom_type in axiom_types:
            disallowed.add(axiom_type)

        for axiom in source_axioms:
            if axiom.axiom_type not in disallowed:
                result.add(axiom)

        return result

    @classmethod
    def get_axioms_of_types(cls, source_axions, *axiom_types):
        """Gets the set of axioms from a source set of axioms that have a
        specified type

        :param source_axions: The source set of owlapy.model.OWLAxiom objects
        :param axiom_types: The owlapy.model.AxiomType objects of axioms that
            will be returned
        :return: A set of OWLAxiom objects that represents the source_axioms
            that have the specified types. Note that source_axioms will not be
            modified. The returned set is a copy.
        """
        results = set()
        allowed = set()

        for axiom_type in axiom_types:
            allowed.add(axiom_type)

        for axiom in source_axions:
            if axiom.axiom_type in allowed:
                results.add(axiom)

        return results

    @classmethod
    def get_axiom_type(cls, name):
        """Gets an axiom type by its name

        :param name: a string
        :return: an owlapy.model.AxiomType object
        """
        return cls.NAME_TYPE_MAP[name]

    @classmethod
    def is_axiom_type(cls, name):
        """Determines if there is an axiom type with the specified name

        :param name: a string containing he name to test for
        :return: True if there is an axiom type with the specified name,
            or False if there is no axiom type with the specified name.
        """
        return name in cls.NAME_TYPE_MAP

    DECLARATION = (0, 'Declaration', True, True, False)
    # class axioms
    EQUIVALENT_CLASSES = (1, 'EquivalentClasses', False, False, True)
    SUBCLASS_OF = (2, 'SubClassOf', False, False, True)
    DISJOINT_CLASSES = (3, 'DisjointClasses', False, False, True)
    DISJOINT_UNION = (4, 'DisjointUnion', True, False, True)
    # individual axioms
    CLASS_ASSERTION = (5, 'ClassAssertion', False, False, True)
    SAME_INDIVIDUAL = (6, 'SameIndividual', False, False, True)
    DIFFERENT_INDIVIDUALS = (7, 'DifferentIndividuals', False, False, True)
    OBJECT_PROPERTY_ASSERTION = (
        8, 'ObjectPropertyAssertion', False, False, True)
    NEGATIVE_OBJECT_PROPERTY_ASSERTION = (
        9, 'NegativeObjectPropertyAssertion', True, False, True)
    DATA_PROPERTY_ASSERTION = (10, 'DataPropertyAssertion', False, False, True)
    NEGATIVE_DATA_PROPERTY_ASSERTION = (
        11, 'NegativeDataPropertyAssertion', True, False, True)
    # object property axioms
    EQUIVALENT_OBJECT_PROPERTIES = (
        12, 'EquivalentObjectProperties', False, False, True)
    SUB_OBJECT_PROPERTY = (13, 'SubObjectPropertyOf', False, False, True)
    INVERSE_OBJECT_PROPERTIES = (
        14, 'InverseObjectProperties', False, False, True)
    FUNCTIONAL_OBJECT_PROPERTY = (
        15, 'FunctionalObjectProperty', False, False, True)
    INVERSE_FUNCTIONAL_OBJECT_PROPERTY = (
        16, 'InverseFunctionalObjectProperty', False, False, True)
    SYMMETRIC_OBJECT_PROPERTY = (
        17, 'SymmetricObjectProperty', False, False, True)
    ASYMMETRIC_OBJECT_PROPERTY = (
        18, 'AsymmetricObjectProperty', True, True, True)
    TRANSITIVE_OBJECT_PROPERTY = (
        19, 'TransitiveObjectProperty', False, False, True)
    REFLEXIVE_OBJECT_PROPERTY = (
        20, 'ReflexiveObjectProperty', True, True, True)
    IRREFLEXIVE_OBJECT_PROPERTY = (
        21, 'IrrefexiveObjectProperty', True, True, True)
    OBJECT_PROPERTY_DOMAIN = (22, 'ObjectPropertyDomain', False, False, True)
    OBJECT_PROPERTY_RANGE = (23, 'ObjectPropertyRange', False, False, True)
    DISJOINT_OBJECT_PROPERTIES = (
        24, 'DisjointObjectProperties', True, True, True)
    SUB_PROPERTY_CHAIN_OF = (25, 'SubPropertyChainOf', True, True, True)
    EQUIVALENT_DATA_PROPERTIES = (
        26, 'EquivalentDataProperties', False, False, True)
    SUB_DATA_PROPERTY = (27, 'SubDataPropertyOf', False, False, True)
    FUNCTIONAL_DATA_PROPERTY = (
        28, 'FunctionalDataProperty', False, False, True)
    DATA_PROPERTY_DOMAIN = (29, 'DataPropertyDomain', False, False, True)
    DATA_PROPERTY_RANGE = (30, 'DataPropertyRange', False, False, True)
    DISJOINT_DATA_PROPERTIES = (31, 'DisjointDataProperties', True, True, True)
    HAS_KEY = (32, 'HasKey', True, True, True)
    SWRL_RULE = (33, 'Rule', False, False, True)
    ANNOTATION_ASSERTION = (34, 'AnnotationAssertion', False, False, False)
    SUB_ANNOTATION_PROPERTY_OF = (
        35, 'SubAnnotationPropertyOf', True, True, False)
    ANNOTATION_PROPERTY_RANGE = (
        36, 'AnnotationPropertyRangeOf', True, True, False)
    ANNOTATION_PROPERTY_DOMAIN = (
        37, 'AnnotationPropertyDomain', True, True, False)
    DATATYPE_DEFINITION = (
        38, 'DatatypeDefinition', True, True, True)

    @ClassProperty
    @classmethod
    def AXIOM_TYPES(cls):
        if not hasattr(cls, '_AXIOM_TYPES'):
            cls._AXIOM_TYPES = {
                cls.SUBCLASS_OF, cls.EQUIVALENT_CLASSES, cls.DISJOINT_CLASSES,
                cls.CLASS_ASSERTION, cls.SAME_INDIVIDUAL,
                cls.DIFFERENT_INDIVIDUALS, cls.OBJECT_PROPERTY_ASSERTION,
                cls.NEGATIVE_OBJECT_PROPERTY_ASSERTION,
                cls.DATA_PROPERTY_ASSERTION,
                cls.NEGATIVE_DATA_PROPERTY_ASSERTION,
                cls.OBJECT_PROPERTY_DOMAIN, cls.OBJECT_PROPERTY_RANGE,
                cls.DISJOINT_OBJECT_PROPERTIES, cls.SUB_OBJECT_PROPERTY,
                cls.EQUIVALENT_OBJECT_PROPERTIES, cls.INVERSE_OBJECT_PROPERTIES,
                cls.SUB_PROPERTY_CHAIN_OF, cls.FUNCTIONAL_OBJECT_PROPERTY,
                cls.INVERSE_FUNCTIONAL_OBJECT_PROPERTY,
                cls.SYMMETRIC_OBJECT_PROPERTY, cls.ASYMMETRIC_OBJECT_PROPERTY,
                cls.TRANSITIVE_OBJECT_PROPERTY, cls.REFLEXIVE_OBJECT_PROPERTY,
                cls.IRREFLEXIVE_OBJECT_PROPERTY, cls.DATA_PROPERTY_DOMAIN,
                cls.DATA_PROPERTY_RANGE, cls.DISJOINT_DATA_PROPERTIES,
                cls.SUB_DATA_PROPERTY, cls.EQUIVALENT_DATA_PROPERTIES,
                cls.FUNCTIONAL_DATA_PROPERTY, cls.DATATYPE_DEFINITION,
                cls.DISJOINT_UNION, cls.DECLARATION, cls.SWRL_RULE,
                cls.ANNOTATION_ASSERTION, cls.SUB_ANNOTATION_PROPERTY_OF,
                cls.ANNOTATION_PROPERTY_DOMAIN, cls.ANNOTATION_PROPERTY_RANGE,
                cls.HAS_KEY}

        return cls._AXIOM_TYPES

    @ClassProperty
    @classmethod
    def NAME_TYPE_MAP(cls):
        if not hasattr(cls, '_NAME_TYPE_MAP'):
            cls._NAME_TYPE_MAP = {}

            for axiom_type in cls.AXIOM_TYPES:
                cls._NAME_TYPE_MAP[axiom_type.name_] = axiom_type

        return cls._NAME_TYPE_MAP

    @ClassProperty
    @classmethod
    def TBOX_AXIOM_TYPES(cls):
        if not hasattr(cls, '_TBOX_AXIOM_TYPES'):
            cls._TBOX_AXIOM_TYPES = {
                cls.SUBCLASS_OF, cls.EQUIVALENT_CLASSES, cls.DISJOINT_CLASSES,
                cls.OBJECT_PROPERTY_DOMAIN, cls.OBJECT_PROPERTY_RANGE,
                cls.INVERSE_OBJECT_PROPERTIES, cls.FUNCTIONAL_OBJECT_PROPERTY,
                cls.INVERSE_FUNCTIONAL_OBJECT_PROPERTY,
                cls.SYMMETRIC_OBJECT_PROPERTY, cls.ASYMMETRIC_OBJECT_PROPERTY,
                cls.TRANSITIVE_OBJECT_PROPERTY, cls.REFLEXIVE_OBJECT_PROPERTY,
                cls.IRREFLEXIVE_OBJECT_PROPERTY, cls.DATA_PROPERTY_DOMAIN,
                cls.DATA_PROPERTY_RANGE, cls.FUNCTIONAL_DATA_PROPERTY,
                cls.DATATYPE_DEFINITION, cls.DISJOINT_UNION, cls.HAS_KEY
            }
        return cls._TBOX_AXIOM_TYPES

    @ClassProperty
    @classmethod
    def ABOX_AXIOM_TYPES(cls):
        if not hasattr(cls, '_ABOX_AXIOM_TYPES'):
            cls._ABOX_AXIOM_TYPES = {
                cls.CLASS_ASSERTION, cls.SAME_INDIVIDUAL,
                cls.DIFFERENT_INDIVIDUALS, cls.OBJECT_PROPERTY_ASSERTION,
                cls.NEGATIVE_OBJECT_PROPERTY_ASSERTION,
                cls.DATA_PROPERTY_ASSERTION,
                cls.NEGATIVE_DATA_PROPERTY_ASSERTION
            }

        return cls._ABOX_AXIOM_TYPES

    @ClassProperty
    @classmethod
    def RBOX_AXIOM_TYPES(cls):
        if not hasattr(cls, '_RBOX_AXIOM_TYPES'):
            cls._RBOX_AXIOM_TYPES = {
                cls.TRANSITIVE_OBJECT_PROPERTY, cls.DISJOINT_DATA_PROPERTIES,
                cls.SUB_DATA_PROPERTY, cls.EQUIVALENT_DATA_PROPERTIES,
                cls.DISJOINT_OBJECT_PROPERTIES, cls.SUB_OBJECT_PROPERTY,
                cls.EQUIVALENT_OBJECT_PROPERTIES, cls.SUB_PROPERTY_CHAIN_OF
            }

        return cls._RBOX_AXIOM_TYPES

    @ClassProperty
    @classmethod
    def TBOX_AND_RBOX_AXIOM_TYPES(cls):
        return cls.TBOX_AXIOM_TYPES.union(cls.RBOX_AXIOM_TYPES)
