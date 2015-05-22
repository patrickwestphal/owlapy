from owlapy import model
from owlapy.model import AxiomType
from owlapy.model import OWLObjectVisitor


class OWLObjectTypeIndexProvider(OWLObjectVisitor):
    ENTITY_TYPE_INDEX_BASE = 1000
    IRI = 0
    ONTOLOGY = 1
    OWL_CLASS = ENTITY_TYPE_INDEX_BASE + ONTOLOGY
    OBJECT_PROPERTY = ENTITY_TYPE_INDEX_BASE + 2
    OBJECT_PROPERTY_INVERSE = ENTITY_TYPE_INDEX_BASE + 3
    DATA_PROPERTY = ENTITY_TYPE_INDEX_BASE + 4
    INDIVIDUAL = ENTITY_TYPE_INDEX_BASE + 5
    ANNOTATION_PROPERTY = ENTITY_TYPE_INDEX_BASE + 6
    ANON_INDIVIDUAL = ENTITY_TYPE_INDEX_BASE + 7
    AXIOM_TYPE_INDEX_BASE = 2000
    SUBCLASS_AXIOM = AXIOM_TYPE_INDEX_BASE + AxiomType.SUBCLASS_OF.index
    NEGATIVE_OBJECT_PROPERTY_ASSERTION =\
        AXIOM_TYPE_INDEX_BASE +\
        AxiomType.NEGATIVE_OBJECT_PROPERTY_ASSERTION.index
    CLASS_EXPRESSION_TYPE_INDEX_BASE = 3000
    DATA_TYPE_INDEX_BASE = 4000
    ANNOTATION_TYPE_INDEX_BASE = 5000
    RULE_OBJECT_TYPE_INDEX_BASE = 6000

    _visit_dict = {
        # class of visitee
        #     0: fixed val/1: val + value of axiom.get_axiom_type() call
        model.IRI: (0, IRI),
        model.OWLClass: (0, OWL_CLASS),
        model.OWLObjectProperty: (0, OBJECT_PROPERTY),
        model.OWLObjectInverseOf: (0, OBJECT_PROPERTY_INVERSE),
        model.OWLDataProperty: (0, DATA_PROPERTY),
        model.OWLNamedIndividual: (0, INDIVIDUAL),
        model.OWLAnnotationProperty: (0, ANNOTATION_PROPERTY),
        model.OWLOntology: (0, ONTOLOGY),
        model.OWLAnonymousIndividual: (0, ANON_INDIVIDUAL),
        model.OWLSubClassOfAxiom: (0, SUBCLASS_AXIOM),
        model.OWLNegativeObjectPropertyAssertionAxiom:
            (0, NEGATIVE_OBJECT_PROPERTY_ASSERTION),
        model.OWLAsymmetricObjectPropertyAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLReflexiveObjectPropertyAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLDisjointClassesAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLDataPropertyDomainAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLObjectPropertyDomainAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLEquivalentObjectPropertiesAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLNegativeDataPropertyAssertionAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLDifferentIndividualsAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLDisjointDataPropertiesAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLDisjointObjectPropertiesAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLObjectPropertyRangeAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLObjectPropertyAssertionAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLFunctionalObjectPropertyAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLSubObjectPropertyOfAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLDisjointUnionAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLDeclarationAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLAnnotationAssertionAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLAnnotationPropertyDomainAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLAnnotationPropertyRangeAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLSubAnnotationPropertyOfAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLSymmetricObjectPropertyAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLDataPropertyRangeAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLFunctionalDataPropertyAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLEquivalentDataPropertiesAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLClassAssertionAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLEquivalentClassesAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLDatatypeDefinitionAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLDataPropertyAssertionAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLTransitiveObjectPropertyAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLIrreflexiveObjectPropertyAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLSubDataPropertyOfAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLInverseFunctionalObjectPropertyAxiom:
            (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLSameIndividualAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLSubPropertyChainOfAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLInverseObjectPropertiesAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.SWRLRule: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLHasKeyAxiom: (1, AXIOM_TYPE_INDEX_BASE),
        model.OWLObjectIntersectionOf:
            (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + ONTOLOGY),
        model.OWLObjectUnionOf: (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 2),
        model.OWLObjectComplementOf: (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 3),
        model.OWLObjectOneOf: (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 4),
        model.OWLObjectSomeValuesFrom:
            (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 5),
        model.OWLObjectAllValuesFrom: (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 6),
        model.OWLObjectHasValue: (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 7),
        model.OWLObjectMinCardinality:
            (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 8),
        model.OWLObjectExactCardinality:
            (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 9),
        model.OWLObjectMaxCardinality:
            (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 10),
        model.OWLObjectHasSelf: (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 11),
        model.OWLDataSomeValuesFrom: (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 12),
        model.OWLDataAllValuesFrom: (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 13),
        model.OWLDataHasValue: (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 14),
        model.OWLDataMinCardinality: (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 15),
        model.OWLDataExactCardinality:
            (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 16),
        model.OWLDataMaxCardinality: (0, CLASS_EXPRESSION_TYPE_INDEX_BASE + 17),
        model.OWLDatatype: (0, DATA_TYPE_INDEX_BASE + ONTOLOGY),
        model.OWLDataComplementOf: (0, DATA_TYPE_INDEX_BASE + 2),
        model.OWLDataOneOf: (0, DATA_TYPE_INDEX_BASE + 3),
        model.OWLDataIntersectionOf: (0, DATA_TYPE_INDEX_BASE + 4),
        model.OWLDataUnionOf: (0, DATA_TYPE_INDEX_BASE + 5),
        model.OWLDatatypeRestriction: (0, DATA_TYPE_INDEX_BASE + 6),
        model.OWLFacetRestriction: (0, DATA_TYPE_INDEX_BASE + 7),
        model.OWLLiteral: (0, DATA_TYPE_INDEX_BASE + 8),
        model.OWLAnnotation: (0, ANNOTATION_TYPE_INDEX_BASE + 1),
        model.SWRLClassAtom: (0, RULE_OBJECT_TYPE_INDEX_BASE + ONTOLOGY),
        model.SWRLDataRangeAtom: (0, RULE_OBJECT_TYPE_INDEX_BASE + 2),
        model.SWRLObjectPropertyAtom: (0, RULE_OBJECT_TYPE_INDEX_BASE + 3),
        model.SWRLDataPropertyAtom: (0, RULE_OBJECT_TYPE_INDEX_BASE + 4),
        model.SWRLBuiltInAtom: (0, RULE_OBJECT_TYPE_INDEX_BASE + 5),
        model.SWRLVariable: (0, RULE_OBJECT_TYPE_INDEX_BASE + 6),
        model.SWRLIndividualArgument: (0, RULE_OBJECT_TYPE_INDEX_BASE + 7),
        model.SWRLLiteralArgument: (0, RULE_OBJECT_TYPE_INDEX_BASE + 8),
        model.SWRLSameIndividualAtom: (0, RULE_OBJECT_TYPE_INDEX_BASE + 9),
        model.SWRLDifferentIndividualsAtom:
            (0, RULE_OBJECT_TYPE_INDEX_BASE + 10)
    }

    def __init__(self):
        super().__init__()
        self.type = None

    def get_type_index(self, owl_object):
        """
        :param owl_object: the owlapy.model.OWLObject objects to compute the
            type index of
        :return: integer indicating the type index
        """
        owl_object.accept(self)
        return self.type

    def visit(self, visitee):
        val_entry = self._visit_dict[type(visitee)]

        if val_entry[0]:
            self.type = val_entry[1] + visitee.get_axiom_type().index
        else:
            self.type = val_entry[1]