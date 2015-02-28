import unittest

from owlapy.model import IRI
from owlapy.vocab.owlrdfvocabulary import OWLRDFVocabulary


class TestOWLRDFVocabulary(unittest.TestCase):
    def test___init__(self):
        self.assertEqual('http://www.w3.org/2002/07/owl#',
                         str(OWLRDFVocabulary.OWL_ALL_DIFFERENT.namespace))
        self.assertEqual('AllDifferent',
                         OWLRDFVocabulary.OWL_ALL_DIFFERENT.short_name)
        self.assertEqual('AllDifferent',
                         OWLRDFVocabulary.OWL_ALL_DIFFERENT.short_form)
        self.assertEqual('owl:AllDifferent',
                         OWLRDFVocabulary.OWL_ALL_DIFFERENT.prefixed_name)
        iri = IRI('http://www.w3.org/2002/07/owl#', 'AllDifferent')
        self.assertEqual(iri, OWLRDFVocabulary.OWL_ALL_DIFFERENT.iri)

    def test___str__(self):
        iri_str = 'http://www.w3.org/2002/07/owl#onDatatype'
        self.assertEqual(iri_str, str(OWLRDFVocabulary.OWL_ON_DATA_TYPE))

    def test_BUILT_IN_VOCABULARY_IRIS(self):
        owl = 'http://www.w3.org/2002/07/owl#'
        rdfs = 'http://www.w3.org/2000/01/rdf-schema#'
        rdf = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
        iris = [
            IRI(owl, 'Thing'), IRI(owl, 'Nothing'), IRI(owl, 'Class'),
            IRI(owl, 'Ontology'), IRI(owl, 'OntologyProperty'),
            IRI(owl, 'imports'), IRI(owl, 'versionIRI'),
            IRI(owl, 'versionInfo'), IRI(owl, 'equivalentClass'),
            IRI(owl, 'ObjectProperty'), IRI(owl, 'DatatypeProperty'),
            IRI(owl, 'FunctionalProperty'),
            IRI(owl, 'InverseFunctionalProperty'),
            IRI(owl, 'AntisymmetricProperty'),
            IRI(owl, 'AsymmetricProperty'), IRI(owl, 'SymmetricProperty'),
            IRI(owl, 'Restriction'), IRI(owl, 'DataRestriction'),
            IRI(owl, 'ObjectRestriction'), IRI(owl, 'onProperty'),
            IRI(owl, 'intersectionOf'), IRI(owl, 'unionOf'),
            IRI(owl, 'allValuesFrom'), IRI(owl, 'someValuesFrom'),
            IRI(owl, 'hasValue'), IRI(owl, 'disjointWith'),
            IRI(owl, 'oneOf'), IRI(owl, 'SelfRestriction'),
            IRI(owl, 'hasSelf'), IRI(owl, 'disjointUnionOf'),
            IRI(owl, 'minCardinality'), IRI(owl, 'minQualifiedCardinality'),
            IRI(owl, 'cardinality'), IRI(owl, 'qualifiedCardinality'),
            IRI(owl, 'AnnotationProperty'), IRI(owl, 'Annotation'),
            IRI(owl, 'declaredAs'), IRI(owl, 'Individual'),
            IRI(owl, 'NamedIndividual'), IRI(owl, 'Datatype'),
            IRI(rdfs, 'subClassOf'), IRI(rdfs, 'subPropertyOf'),
            IRI(rdf, 'type'), IRI(rdf, 'nil'), IRI(rdf, 'rest'),
            IRI(rdf, 'first'), IRI(rdf, 'List'), IRI(owl, 'maxCardinality'),
            IRI(owl, 'maxQualifiedCardinality'),
            IRI(owl, 'NegativeObjectPropertyAssertion'),
            IRI(owl, 'NegativeDataPropertyAssertion'),
            IRI(owl, 'NegativePropertyAssertion'), IRI(rdfs, 'label'),
            IRI(rdfs, 'comment'), IRI(rdfs, 'seeAlso'),
            IRI(rdfs, 'isDefinedBy'), IRI(rdfs, 'Resource'),
            IRI(rdfs, 'Literal'), IRI(rdf, 'PlainLiteral'),
            IRI(rdfs, 'Datatype'), IRI(owl, 'TransitiveProperty'),
            IRI(owl, 'ReflexiveProperty'), IRI(owl, 'IrreflexiveProperty'),
            IRI(owl, 'inverseOf'), IRI(owl, 'complementOf'),
            IRI(owl, 'datatypeComplementOf'), IRI(owl, 'AllDifferent'),
            IRI(owl, 'distinctMembers'), IRI(owl, 'sameAs'),
            IRI(owl, 'differentFrom'), IRI(owl, 'DeprecatedProperty'),
            IRI(owl, 'equivalentProperty'), IRI(owl, 'DeprecatedClass'),
            IRI(owl, 'DataRange'), IRI(rdfs, 'domain'), IRI(rdfs, 'range'),
            IRI(rdfs, 'Class'), IRI(rdf, 'Property'), IRI(rdf, 'subject'),
            IRI(rdf, 'predicate'), IRI(rdf, 'object'), IRI(owl, 'subject'),
            IRI(owl, 'predicate'), IRI(owl, 'object'), IRI(rdf, 'Description'),
            IRI(rdf, 'XMLLiteral'), IRI(owl, 'priorVersion'),
            IRI(owl, 'deprecated'), IRI(owl, 'backwardCompatibleWith'),
            IRI(owl, 'incompatibleWith'), IRI(owl, 'objectPropertyDomain'),
            IRI(owl, 'dataPropertyDomain'), IRI(owl, 'dataPropertyRange'),
            IRI(owl, 'objectPropertyRange'), IRI(owl, 'subObjectPropertyOf'),
            IRI(owl, 'subDataPropertyOf'), IRI(owl, 'disjointDataProperties'),
            IRI(owl, 'disjointObjectProperties'),
            IRI(owl, 'propertyDisjointWith'),
            IRI(owl, 'equivalentDataProperty'),
            IRI(owl, 'equivalentObjectProperty'),
            IRI(owl, 'FunctionalDataProperty'),
            IRI(owl, 'FunctionalObjectProperty'), IRI(owl, 'onClass'),
            IRI(owl, 'onDataRange'), IRI(owl, 'onDatatype'),
            IRI(owl, 'withRestrictions'),
            IRI(owl, 'inverseObjectPropertyExpression'), IRI(owl, 'Axiom'),
            IRI(owl, 'propertyChain'), IRI(owl, 'propertyChainAxiom'),
            IRI(owl, 'AllDisjointClasses'), IRI(owl, 'members'),
            IRI(owl, 'AllDisjointProperties'), IRI(owl, 'topObjectProperty'),
            IRI(owl, 'bottomObjectProperty'), IRI(owl, 'topDataProperty'),
            IRI(owl, 'bottomDataProperty'), IRI(owl, 'hasKey'),
            IRI(owl, 'annotatedSource'), IRI(owl, 'annotatedProperty'),
            IRI(owl, 'annotatedTarget'), IRI(owl, 'sourceIndividual'),
            IRI(owl, 'assertionProperty'), IRI(owl, 'targetIndividual'),
            IRI(owl, 'targetValue')
        ]
        self.assertListEqual(iris, OWLRDFVocabulary.BUILT_IN_VOCABULARY_IRIS)

    def test_BUILT_IN_ANNOTATION_PROPERTY_IRIS(self):
        owl = 'http://www.w3.org/2002/07/owl#'
        rdfs = 'http://www.w3.org/2000/01/rdf-schema#'
        iris = [
            IRI(rdfs, 'label'), IRI(rdfs, 'comment'), IRI(owl, 'versionInfo'),
            IRI(owl, 'backwardCompatibleWith'), IRI(owl, 'priorVersion'),
            IRI(rdfs, 'seeAlso'), IRI(rdfs, 'isDefinedBy'),
            IRI(owl, 'incompatibleWith'), IRI(owl, 'deprecated')
        ]
        self.assertListEqual(iris,
                             OWLRDFVocabulary.BUILT_IN_ANNOTATION_PROPERTY_IRIS)