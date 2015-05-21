import unittest

from owlapy.model import AxiomType


class TestAxiomType(unittest.TestCase):

    def test___init__(self):
        self.assertEqual('Declaration', AxiomType.DECLARATION.name_)
        self.assertEqual(0, AxiomType.DECLARATION.index)
        self.assertTrue(AxiomType.DECLARATION.owl2_axiom)
        self.assertTrue(AxiomType.DECLARATION.non_syntactic_owl2_axiom)
        self.assertFalse(AxiomType.DECLARATION.is_logical)

        self.assertEqual('EquivalentClasses',
                         AxiomType.EQUIVALENT_CLASSES.name_)
        self.assertEqual('SubClassOf', AxiomType.SUBCLASS_OF.name_)
        self.assertEqual('DisjointClasses', AxiomType.DISJOINT_CLASSES.name_)
        self.assertEqual('DisjointUnion', AxiomType.DISJOINT_UNION.name_)
        self.assertEqual('ClassAssertion', AxiomType.CLASS_ASSERTION.name_)
        self.assertEqual('SameIndividual', AxiomType.SAME_INDIVIDUAL.name_)
        self.assertEqual('DifferentIndividuals',
                         AxiomType.DIFFERENT_INDIVIDUALS.name_)
        self.assertEqual('ObjectPropertyAssertion',
                         AxiomType.OBJECT_PROPERTY_ASSERTION.name_)
        self.assertEqual('NegativeObjectPropertyAssertion',
                         AxiomType.NEGATIVE_OBJECT_PROPERTY_ASSERTION.name_)
        self.assertEqual('DataPropertyAssertion',
                         AxiomType.DATA_PROPERTY_ASSERTION.name_)
        self.assertEqual('NegativeDataPropertyAssertion',
                         AxiomType.NEGATIVE_DATA_PROPERTY_ASSERTION.name_)
        self.assertEqual('EquivalentObjectProperties',
                         AxiomType.EQUIVALENT_OBJECT_PROPERTIES.name_)
        self.assertEqual('SubObjectPropertyOf',
                         AxiomType.SUB_OBJECT_PROPERTY.name_)
        self.assertEqual('InverseObjectProperties',
                         AxiomType.INVERSE_OBJECT_PROPERTIES.name_)
        self.assertEqual('FunctionalObjectProperty',
                         AxiomType.FUNCTIONAL_OBJECT_PROPERTY.name_)
        self.assertEqual('InverseFunctionalObjectProperty',
                         AxiomType.INVERSE_FUNCTIONAL_OBJECT_PROPERTY.name_)
        self.assertEqual('SymmetricObjectProperty',
                         AxiomType.SYMMETRIC_OBJECT_PROPERTY.name_)
        self.assertEqual('AsymmetricObjectProperty',
                         AxiomType.ASYMMETRIC_OBJECT_PROPERTY.name_)
        self.assertEqual('TransitiveObjectProperty',
                         AxiomType.TRANSITIVE_OBJECT_PROPERTY.name_)
        self.assertEqual('ReflexiveObjectProperty',
                         AxiomType.REFLEXIVE_OBJECT_PROPERTY.name_)
        self.assertEqual('IrrefexiveObjectProperty',
                         AxiomType.IRREFLEXIVE_OBJECT_PROPERTY.name_)
        self.assertEqual('ObjectPropertyDomain',
                         AxiomType.OBJECT_PROPERTY_DOMAIN.name_)
        self.assertEqual('ObjectPropertyRange',
                         AxiomType.OBJECT_PROPERTY_RANGE.name_)
        self.assertEqual('DisjointObjectProperties',
                         AxiomType.DISJOINT_OBJECT_PROPERTIES.name_)
        self.assertEqual('SubPropertyChainOf',
                         AxiomType.SUB_PROPERTY_CHAIN_OF.name_)
        self.assertEqual('EquivalentDataProperties',
                         AxiomType.EQUIVALENT_DATA_PROPERTIES.name_)
        self.assertEqual('SubDataPropertyOf', AxiomType.SUB_DATA_PROPERTY.name_)
        self.assertEqual('FunctionalDataProperty',
                         AxiomType.FUNCTIONAL_DATA_PROPERTY.name_)
        self.assertEqual('DataPropertyDomain',
                         AxiomType.DATA_PROPERTY_DOMAIN.name_)
        self.assertEqual('DataPropertyRange',
                         AxiomType.DATA_PROPERTY_RANGE.name_)
        self.assertEqual('DisjointDataProperties',
                         AxiomType.DISJOINT_DATA_PROPERTIES.name_)
        self.assertEqual('HasKey', AxiomType.HAS_KEY.name_)
        self.assertEqual('Rule', AxiomType.SWRL_RULE.name_)
        self.assertEqual('AnnotationAssertion',
                         AxiomType.ANNOTATION_ASSERTION.name_)
        self.assertEqual('SubAnnotationPropertyOf',
                         AxiomType.SUB_ANNOTATION_PROPERTY_OF.name_)
        self.assertEqual('AnnotationPropertyRangeOf',
                         AxiomType.ANNOTATION_PROPERTY_RANGE.name_)
        self.assertEqual('AnnotationPropertyDomain',
                         AxiomType.ANNOTATION_PROPERTY_DOMAIN.name_)
        self.assertEqual('DatatypeDefinition',
                         AxiomType.DATATYPE_DEFINITION.name_)

    def test___str__(self):
        self.assertEqual(AxiomType.DECLARATION.name_,
                         str(AxiomType.DECLARATION))

    def test___repr__(self):
        self.assertEqual(AxiomType.DECLARATION.name_,
                         AxiomType.DECLARATION.__repr__())

    def test_get_axioms_without_types(self):
        self.fail()  # axiom classes need to be implemented first

    def test_get_axioms_of_types(self):
        self.fail()  # axiom classes need to be implemented first

    def test_get_axiom_type(self):
        ax_type_01 = AxiomType.ANNOTATION_ASSERTION
        name_01 = ax_type_01.name_
        self.assertEqual(ax_type_01, AxiomType.get_axiom_type(name_01))

        ax_type_02 = AxiomType.DATA_PROPERTY_ASSERTION
        name_02 = ax_type_02.name_
        self.assertEqual(ax_type_02, AxiomType.get_axiom_type(name_02))

        ax_type_03 = AxiomType.FUNCTIONAL_DATA_PROPERTY
        name_03 = ax_type_03.name_
        self.assertEqual(ax_type_03, AxiomType.get_axiom_type(name_03))

    def test_is_axiom_type(self):
        ax_type_name_01 = 'SameIndividual'
        self.assertTrue(AxiomType.is_axiom_type(ax_type_name_01))

        ax_type_name_02 = 'ReflexiveObjectProperty'
        self.assertTrue(AxiomType.is_axiom_type(ax_type_name_02))

        ax_type_name_03 = 'SubAnnotationPropertyOf'
        self.assertTrue(AxiomType.is_axiom_type(ax_type_name_03))

        not_ax_type_name_01 = 'SameIndividua'
        self.assertFalse(AxiomType.is_axiom_type(not_ax_type_name_01))

        not_ax_type_name_02 = 23
        self.assertFalse(AxiomType.is_axiom_type(not_ax_type_name_02))

        not_ax_type_name_03 = 'NOT A TYPE NAME'
        self.assertFalse(AxiomType.is_axiom_type(not_ax_type_name_03))

    def test_axiom_types_set(self):
        self.assertTrue(AxiomType.DECLARATION in AxiomType.AXIOM_TYPES)  # 0
        self.assertTrue(AxiomType.EQUIVALENT_CLASSES in AxiomType.AXIOM_TYPES)
        self.assertTrue(AxiomType.SUBCLASS_OF in AxiomType.AXIOM_TYPES)  # 2
        self.assertTrue(AxiomType.DISJOINT_CLASSES in AxiomType.AXIOM_TYPES)
        self.assertTrue(AxiomType.DISJOINT_UNION in AxiomType.AXIOM_TYPES)  # 4
        self.assertTrue(AxiomType.CLASS_ASSERTION in AxiomType.AXIOM_TYPES)  # 5
        self.assertTrue(AxiomType.SAME_INDIVIDUAL in AxiomType.AXIOM_TYPES)  # 6
        self.assertTrue(
            AxiomType.DIFFERENT_INDIVIDUALS in AxiomType.AXIOM_TYPES)  # 7
        self.assertTrue(
            AxiomType.OBJECT_PROPERTY_ASSERTION in AxiomType.AXIOM_TYPES)  # 8
        self.assertTrue(AxiomType.NEGATIVE_OBJECT_PROPERTY_ASSERTION in
                        AxiomType.AXIOM_TYPES)  # 9
        self.assertTrue(
            AxiomType.DATA_PROPERTY_ASSERTION in AxiomType.AXIOM_TYPES)  # 10
        self.assertTrue(
            AxiomType.NEGATIVE_DATA_PROPERTY_ASSERTION in AxiomType.AXIOM_TYPES)
        self.assertTrue(
            AxiomType.EQUIVALENT_OBJECT_PROPERTIES in AxiomType.AXIOM_TYPES)
        self.assertTrue(AxiomType.SUB_OBJECT_PROPERTY in AxiomType.AXIOM_TYPES)
        self.assertTrue(
            AxiomType.INVERSE_OBJECT_PROPERTIES in AxiomType.AXIOM_TYPES)  # 14
        self.assertTrue(
            AxiomType.FUNCTIONAL_OBJECT_PROPERTY in AxiomType.AXIOM_TYPES)  # 15
        self.assertTrue(AxiomType.INVERSE_FUNCTIONAL_OBJECT_PROPERTY in
                        AxiomType.AXIOM_TYPES)  # 16
        self.assertTrue(
            AxiomType.SYMMETRIC_OBJECT_PROPERTY in AxiomType.AXIOM_TYPES)  # 17
        self.assertTrue(
            AxiomType.ASYMMETRIC_OBJECT_PROPERTY in AxiomType.AXIOM_TYPES)  # 18
        self.assertTrue(
            AxiomType.TRANSITIVE_OBJECT_PROPERTY in AxiomType.AXIOM_TYPES)  # 19
        self.assertTrue(
            AxiomType.REFLEXIVE_OBJECT_PROPERTY in AxiomType.AXIOM_TYPES)  # 20
        self.assertTrue(
            AxiomType.IRREFLEXIVE_OBJECT_PROPERTY in AxiomType.AXIOM_TYPES)
        self.assertTrue(
            AxiomType.OBJECT_PROPERTY_DOMAIN in AxiomType.AXIOM_TYPES)  # 22
        self.assertTrue(
            AxiomType.OBJECT_PROPERTY_RANGE in AxiomType.AXIOM_TYPES)  # 23
        self.assertTrue(
            AxiomType.DISJOINT_OBJECT_PROPERTIES in AxiomType.AXIOM_TYPES)  # 24
        self.assertTrue(
            AxiomType.SUB_PROPERTY_CHAIN_OF in AxiomType.AXIOM_TYPES)  # 25
        self.assertTrue(
            AxiomType.EQUIVALENT_DATA_PROPERTIES in AxiomType.AXIOM_TYPES)  # 26
        self.assertTrue(AxiomType.SUB_DATA_PROPERTY in AxiomType.AXIOM_TYPES)
        self.assertTrue(
            AxiomType.FUNCTIONAL_DATA_PROPERTY in AxiomType.AXIOM_TYPES)  # 28
        self.assertTrue(AxiomType.DATA_PROPERTY_DOMAIN in AxiomType.AXIOM_TYPES)
        self.assertTrue(AxiomType.DATA_PROPERTY_RANGE in AxiomType.AXIOM_TYPES)
        self.assertTrue(
            AxiomType.DISJOINT_DATA_PROPERTIES in AxiomType.AXIOM_TYPES)  # 31
        self.assertTrue(AxiomType.HAS_KEY in AxiomType.AXIOM_TYPES)  # 32
        self.assertTrue(AxiomType.SWRL_RULE in AxiomType.AXIOM_TYPES)  # 33
        self.assertTrue(AxiomType.ANNOTATION_ASSERTION in AxiomType.AXIOM_TYPES)
        self.assertTrue(
            AxiomType.SUB_ANNOTATION_PROPERTY_OF in AxiomType.AXIOM_TYPES)  # 35
        self.assertTrue(
            AxiomType.ANNOTATION_PROPERTY_RANGE in AxiomType.AXIOM_TYPES)  # 36
        self.assertTrue(
            AxiomType.ANNOTATION_PROPERTY_DOMAIN in AxiomType.AXIOM_TYPES)  # 37
        self.assertTrue(AxiomType.DATATYPE_DEFINITION in AxiomType.AXIOM_TYPES)

    def test_tbox_axiom_types_set(self):
        self.assertEqual(19, len(AxiomType.TBOX_AXIOM_TYPES))

        self.assertTrue(AxiomType.SUBCLASS_OF in AxiomType.TBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.EQUIVALENT_CLASSES in AxiomType.TBOX_AXIOM_TYPES)  # 2
        self.assertTrue(
            AxiomType.DISJOINT_CLASSES in AxiomType.TBOX_AXIOM_TYPES)  # 3
        self.assertTrue(
            AxiomType.OBJECT_PROPERTY_DOMAIN in AxiomType.TBOX_AXIOM_TYPES)  # 4
        self.assertTrue(
            AxiomType.OBJECT_PROPERTY_RANGE in AxiomType.TBOX_AXIOM_TYPES)  # 5
        self.assertTrue(
            AxiomType.INVERSE_OBJECT_PROPERTIES in AxiomType.TBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.FUNCTIONAL_OBJECT_PROPERTY in AxiomType.TBOX_AXIOM_TYPES)
        self.assertTrue(AxiomType.INVERSE_FUNCTIONAL_OBJECT_PROPERTY in
                        AxiomType.TBOX_AXIOM_TYPES)  # 8
        self.assertTrue(
            AxiomType.SYMMETRIC_OBJECT_PROPERTY in AxiomType.TBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.ASYMMETRIC_OBJECT_PROPERTY in AxiomType.TBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.TRANSITIVE_OBJECT_PROPERTY in AxiomType.TBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.REFLEXIVE_OBJECT_PROPERTY in AxiomType.TBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.IRREFLEXIVE_OBJECT_PROPERTY in AxiomType.TBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.DATA_PROPERTY_DOMAIN in AxiomType.TBOX_AXIOM_TYPES)  # 14
        self.assertTrue(
            AxiomType.DATA_PROPERTY_RANGE in AxiomType.TBOX_AXIOM_TYPES)  # 15
        self.assertTrue(
            AxiomType.FUNCTIONAL_DATA_PROPERTY in AxiomType.TBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.DATATYPE_DEFINITION in AxiomType.TBOX_AXIOM_TYPES)  # 17
        self.assertTrue(AxiomType.DISJOINT_UNION in AxiomType.TBOX_AXIOM_TYPES)
        self.assertTrue(AxiomType.HAS_KEY in AxiomType.TBOX_AXIOM_TYPES)  # 19

    def test_abox_axiom_types_set(self):
        self.assertEqual(7, len(AxiomType.ABOX_AXIOM_TYPES))

        self.assertTrue(AxiomType.CLASS_ASSERTION in AxiomType.ABOX_AXIOM_TYPES)
        self.assertTrue(AxiomType.SAME_INDIVIDUAL in AxiomType.ABOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.DIFFERENT_INDIVIDUALS in AxiomType.ABOX_AXIOM_TYPES)  # 3
        self.assertTrue(
            AxiomType.OBJECT_PROPERTY_ASSERTION in AxiomType.ABOX_AXIOM_TYPES)
        self.assertTrue(AxiomType.NEGATIVE_OBJECT_PROPERTY_ASSERTION in
                        AxiomType.ABOX_AXIOM_TYPES)  # 5
        self.assertTrue(
            AxiomType.DATA_PROPERTY_ASSERTION in AxiomType.ABOX_AXIOM_TYPES)
        self.assertTrue(AxiomType.NEGATIVE_DATA_PROPERTY_ASSERTION in
                        AxiomType.ABOX_AXIOM_TYPES)  # 7

    def test_rbox_axiom_types_set(self):
        self.assertEqual(8, len(AxiomType.RBOX_AXIOM_TYPES))

        self.assertTrue(
            AxiomType.TRANSITIVE_OBJECT_PROPERTY in AxiomType.RBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.DISJOINT_DATA_PROPERTIES in AxiomType.RBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.SUB_DATA_PROPERTY in AxiomType.RBOX_AXIOM_TYPES)  # 3
        self.assertTrue(
            AxiomType.EQUIVALENT_DATA_PROPERTIES in AxiomType.RBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.DISJOINT_OBJECT_PROPERTIES in AxiomType.RBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.SUB_OBJECT_PROPERTY in AxiomType.RBOX_AXIOM_TYPES)  # 6
        self.assertTrue(AxiomType.EQUIVALENT_OBJECT_PROPERTIES in
                        AxiomType.RBOX_AXIOM_TYPES)  # 7
        self.assertTrue(
            AxiomType.SUB_PROPERTY_CHAIN_OF in AxiomType.RBOX_AXIOM_TYPES)  # 8

    def test_tbox_and_rbox_axiom_types_set(self):
        self.assertEqual(26, len(AxiomType.TBOX_AND_RBOX_AXIOM_TYPES))

        self.assertTrue(
            AxiomType.SUBCLASS_OF in AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  #1
        self.assertTrue(
            AxiomType.EQUIVALENT_CLASSES in AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.DISJOINT_CLASSES in AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)
        self.assertTrue(AxiomType.OBJECT_PROPERTY_DOMAIN in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 4
        self.assertTrue(AxiomType.OBJECT_PROPERTY_RANGE in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 5
        self.assertTrue(AxiomType.INVERSE_OBJECT_PROPERTIES in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 6
        self.assertTrue(AxiomType.FUNCTIONAL_OBJECT_PROPERTY in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 7
        self.assertTrue(AxiomType.INVERSE_FUNCTIONAL_OBJECT_PROPERTY in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 8
        self.assertTrue(AxiomType.SYMMETRIC_OBJECT_PROPERTY in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 9
        self.assertTrue(AxiomType.ASYMMETRIC_OBJECT_PROPERTY in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 10
        self.assertTrue(AxiomType.TRANSITIVE_OBJECT_PROPERTY in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 11
        self.assertTrue(AxiomType.REFLEXIVE_OBJECT_PROPERTY in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 12
        self.assertTrue(AxiomType.IRREFLEXIVE_OBJECT_PROPERTY in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 13
        self.assertTrue(AxiomType.DATA_PROPERTY_DOMAIN in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 14
        self.assertTrue(AxiomType.DATA_PROPERTY_RANGE in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 15
        self.assertTrue(AxiomType.FUNCTIONAL_DATA_PROPERTY in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 16
        self.assertTrue(AxiomType.DATATYPE_DEFINITION in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 17
        self.assertTrue(
            AxiomType.DISJOINT_UNION in AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)
        self.assertTrue(
            AxiomType.HAS_KEY in AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 19
        self.assertTrue(AxiomType.DISJOINT_DATA_PROPERTIES in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 20
        self.assertTrue(
            AxiomType.SUB_DATA_PROPERTY in AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)
        self.assertTrue(AxiomType.EQUIVALENT_DATA_PROPERTIES in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 22
        self.assertTrue(AxiomType.DISJOINT_OBJECT_PROPERTIES in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 23
        self.assertTrue(AxiomType.SUB_OBJECT_PROPERTY in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 24
        self.assertTrue(AxiomType.EQUIVALENT_OBJECT_PROPERTIES in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 25
        self.assertTrue(AxiomType.SUB_PROPERTY_CHAIN_OF in
                        AxiomType.TBOX_AND_RBOX_AXIOM_TYPES)  # 26