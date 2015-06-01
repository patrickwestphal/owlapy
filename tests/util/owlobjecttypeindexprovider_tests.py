import unittest

from owlapy import model
import owlapy
from owlapy.util.owlobjecttypeindexprovider import OWLObjectTypeIndexProvider
from owlapy.vocab.owlfacet import OWLFacet

class TestOWLObjectTypeIndexProvider(unittest.TestCase):

    def test___init__(self):
        otip = OWLObjectTypeIndexProvider()
        self.assertIsNone(otip.type)

    def test_get_type_index_01(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.IRI('http://ex.org/sth')
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.IRI,
                         otip.get_type_index(visitee))

    def test_get_type_index_02(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLClass(model.IRI('http://ex.org/SomeCls'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.OWL_CLASS,
                         otip.get_type_index(visitee))

    def test_get_type_index_03(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLObjectProperty(model.IRI('http://ex.org/objProp'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.OBJECT_PROPERTY,
                         otip.get_type_index(visitee))

    def test_get_type_index_04(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/objProp'))
        visitee = model.OWLObjectInverseOf(prop)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.OBJECT_PROPERTY_INVERSE,
                         otip.get_type_index(visitee))

    def test_get_type_index_05(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLDataProperty(model.IRI('http://ex.org/dataProp'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_PROPERTY,
                         otip.get_type_index(visitee))

    def test_get_type_index_06(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.INDIVIDUAL,
                         otip.get_type_index(visitee))

    def test_get_type_index_07(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.ANNOTATION_PROPERTY,
                         otip.get_type_index(visitee))

    def test_get_type_index_08(self):
        otip = OWLObjectTypeIndexProvider()
        data_factory = model.OWLDataFactory()
        manager = owlapy.OWLOntologyManager(data_factory)
        ont_id = model.OWLOntologyID()
        visitee = model.OWLOntology(manager, ont_id)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.ONTOLOGY,
                         otip.get_type_index(visitee))

    def test_get_type_index_09(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLAnonymousIndividual(model.NodeID('_:23'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.ANON_INDIVIDUAL,
                         otip.get_type_index(visitee))

    def test_get_type_index_10(self):
        otip = OWLObjectTypeIndexProvider()
        sub_class = model.OWLClass(model.IRI('http://ex.org/Sub'))
        super_class = model.OWLClass(model.IRI('http://ex.org/Super'))
        annotations = []
        visitee = model.OWLSubClassOfAxiom(sub_class, super_class, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.SUBCLASS_AXIOM,
                         otip.get_type_index(visitee))

    def test_get_type_index_11(self):
        otip = OWLObjectTypeIndexProvider()
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop23'))
        obj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))
        annotations = []
        visitee = model.OWLNegativeObjectPropertyAssertionAxiom(
            subj, prop, obj, annotations)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.NEGATIVE_OBJECT_PROPERTY_ASSERTION,
            otip.get_type_index(visitee))

    def test_get_type_index_12(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLAsymmetricObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_13(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLReflexiveObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_14(self):
        otip = OWLObjectTypeIndexProvider()
        cls = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        annotations = []
        visitee = model.OWLDisjointClassesAxiom(cls, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_15(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        dom = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        annotations = []
        visitee = model.OWLDataPropertyDomainAxiom(prop, dom, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_16(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        dom = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        annotations = []
        visitee = model.OWLObjectPropertyDomainAxiom(prop, dom, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_17(self):
        otip = OWLObjectTypeIndexProvider()
        props = {model.OWLObjectProperty(model.IRI('http://ex.org/prop1')),
                 model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))}
        annotations = []
        visitee = model.OWLEquivalentObjectPropertiesAxiom(props, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_18(self):
        otip = OWLObjectTypeIndexProvider()
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        obj = model.OWLLiteral("abc", None, None)
        annotations = []
        visitee = model.OWLNegativeDataPropertyAssertionAxiom(
            subj, prop, obj, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_19(self):
        otip = OWLObjectTypeIndexProvider()
        indivs = {model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ')),
                  model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))}
        annotations = []
        visitee = model.OWLDifferentIndividualsAxiom(indivs, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_20(self):
        otip = OWLObjectTypeIndexProvider()
        props = {model.OWLObjectProperty(model.IRI('http://ex.org/prop1')),
                 model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))}
        annotations = []
        visitee = model.OWLDisjointDataPropertiesAxiom(props, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_21(self):
        otip = OWLObjectTypeIndexProvider()
        props = {model.OWLObjectProperty(model.IRI('http://ex.org/prop1')),
                 model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))}
        annotations = []
        visitee = model.OWLDisjointObjectPropertiesAxiom(props, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_22(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        rnge = model.OWLClass(model.IRI('http://ex.org/SomeCls'))
        annotations = []
        visitee = model.OWLObjectPropertyRangeAxiom(prop, rnge, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_23(self):
        otip = OWLObjectTypeIndexProvider()
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/SomeCls'))
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        obj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        anns = []
        visitee = model.OWLObjectPropertyAssertionAxiom(subj, prop, obj, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_24(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLFunctionalObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_25(self):
        otip = OWLObjectTypeIndexProvider()
        sub_prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))
        super_prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))
        anns = []
        visitee = model.OWLSubObjectPropertyOfAxiom(sub_prop, super_prop, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_26(self):
        otip = OWLObjectTypeIndexProvider()
        cls1 = model.OWLClass(model.IRI('http://ex.org/SomeCls'))
        cls2 = model.OWLClass(model.IRI('http://ex.org/AnotherCls'))
        annotations = []
        visitee = model.OWLDisjointUnionAxiom(cls1, cls2, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_27(self):
        otip = OWLObjectTypeIndexProvider()
        entity = model.OWLClass(model.IRI('http://ex.org/SomeCls'))
        annotations = []
        visitee = model.OWLDeclarationAxiom(entity, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_28(self):
        otip = OWLObjectTypeIndexProvider()
        subj = model.IRI('http://ex.org/sth')
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop'))
        val = model.IRI('http://ex.org/sthElse')
        anns = []
        visitee = model.OWLAnnotationAssertionAxiom(subj, prop, val, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_29(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop'))
        dom = model.IRI('http://ex.org/sth')
        anns = []
        visitee = model.OWLAnnotationPropertyDomainAxiom(prop, dom, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_30(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/annProp'))
        rnge = model.IRI('http://ex.org/sth')
        anns = []
        visitee = model.OWLAnnotationPropertyRangeAxiom(prop, rnge, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_31(self):
        otip = OWLObjectTypeIndexProvider()
        sub_prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop1'))
        super_prop = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/prop2'))
        annotations = []
        visitee = model.OWLSubAnnotationPropertyOfAxiom(sub_prop, super_prop,
                                                        annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_32(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLSymmetricObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_33(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        rnge = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        annotations = []
        visitee = model.OWLDataPropertyRangeAxiom(prop, rnge, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_34(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        rnge = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        annotations = []
        visitee = model.OWLFunctionalDataPropertyAxiom(prop, rnge, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_35(self):
        otip = OWLObjectTypeIndexProvider()
        props = {model.OWLDataProperty(model.IRI('http://ex.org/prop1')),
                 model.OWLDataProperty(model.IRI('http://ex.org/prop2'))}
        annotations = []
        visitee = model.OWLEquivalentDataPropertiesAxiom(props, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_36(self):
        otip = OWLObjectTypeIndexProvider()
        individual = model.OWLNamedIndividual(model.IRI('http://ex.org/indiv'))
        cls = model.OWLClass(model.IRI('http://ex.org/SomeCls'))
        annotations = []
        visitee = model.OWLClassAssertionAxiom(individual, cls, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_37(self):
        otip = OWLObjectTypeIndexProvider()
        classes = {model.OWLClass(model.IRI('http://ex.org/SomeClass')),
                   model.OWLClass(model.IRI('http://ex.org/AnotherClass'))}
        annotations = []
        visitee = model.OWLEquivalentClassesAxiom(classes, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_38(self):
        otip = OWLObjectTypeIndexProvider()
        d_type = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        d_range = model.OWLDatatype(model.IRI('http://ex.org/dtype/foo'))
        annotations = []
        visitee = model.OWLDatatypeDefinitionAxiom(d_type, d_range, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_39(self):
        otip = OWLObjectTypeIndexProvider()
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        val = model.OWLLiteral('abc')
        anns = []
        visitee = model.OWLDataPropertyAssertionAxiom(subj, prop, val, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_40(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLTransitiveObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_41(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLIrreflexiveObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_42(self):
        otip = OWLObjectTypeIndexProvider()
        sub_prop = model.OWLDataProperty(model.IRI('http://ex.org/prop1'))
        super_prop = model.OWLDataProperty(model.IRI('http://ex.org/prop2'))
        anns = []
        visitee = model.OWLSubDataPropertyOfAxiom(sub_prop, super_prop, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_43(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        anns = []
        visitee = model.OWLInverseFunctionalObjectPropertyAxiom(prop, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_44(self):
        otip = OWLObjectTypeIndexProvider()
        indivs = {model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ')),
                  model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))}
        annotations = []
        visitee = model.OWLSameIndividualAxiom(indivs, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_45(self):
        otip = OWLObjectTypeIndexProvider()
        prop_chain = [model.OWLObjectProperty(model.IRI('http://ex.org/prop1')),
                      model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))]
        super_prop = model.OWLObjectProperty(model.IRI('http://ex.org/sProp'))
        anns = []
        visitee = model.OWLSubPropertyChainOfAxiom(prop_chain, super_prop, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_46(self):
        otip = OWLObjectTypeIndexProvider()
        first = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))
        secnd = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))
        anns = []
        visitee = model.OWLInverseObjectPropertiesAxiom(first, secnd, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_47(self):
        otip = OWLObjectTypeIndexProvider()
        body = model.SWRLAtom(model.IRI('http://ex.org/sth'))
        head = model.SWRLAtom(model.IRI('http://ex.org/sthElse'))
        annotations = []
        visitee = model.SWRLRule(body, head, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_48(self):
        otip = OWLObjectTypeIndexProvider()
        cls = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLHasKeyAxiom(cls, prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index,
                         otip.get_type_index(visitee))

    def test_get_type_index_49(self):
        otip = OWLObjectTypeIndexProvider()
        operands = {model.OWLClass(model.IRI('http://ex.org/SomeClass')),
                    model.OWLClass(model.IRI('http://ex.org/AnotherClass'))}
        visitee = model.OWLObjectIntersectionOf(operands)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE +
            OWLObjectTypeIndexProvider.ONTOLOGY, otip.get_type_index(visitee))

    def test_get_type_index_50(self):
        otip = OWLObjectTypeIndexProvider()
        operands = {model.OWLClass(model.IRI('http://ex.org/SomeClass')),
                    model.OWLClass(model.IRI('http://ex.org/SomeClass'))}
        visitee = model.OWLObjectUnionOf(operands)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 2,
            otip.get_type_index(visitee))

    def test_get_type_index_51(self):
        otip = OWLObjectTypeIndexProvider()
        operand = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectComplementOf(operand)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 3,
            otip.get_type_index(visitee))

    def test_get_type_index_52(self):
        otip = OWLObjectTypeIndexProvider()
        values = {model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ')),
                  model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))}
        visitee = model.OWLObjectOneOf(values)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 5,
            otip.get_type_index(visitee))

    def test_get_type_index_53(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectSomeValuesFrom(prop, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 4,
            otip.get_type_index(visitee))

    def test_get_type_index_54(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectAllValuesFrom(prop, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 6,
            otip.get_type_index(visitee))

    def test_get_type_index_55(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        value = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        visitee = model.OWLObjectHasValue(prop, value)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 7,
            otip.get_type_index(visitee))

    def test_get_type_index_56(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectMinCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 8,
            otip.get_type_index(visitee))

    def test_get_type_index_57(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectExactCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 9,
            otip.get_type_index(visitee))

    def test_get_type_index_58(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectMaxCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 10,
            otip.get_type_index(visitee))

    def test_get_type_index_59(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        visitee = model.OWLObjectHasSelf(prop)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 11,
            otip.get_type_index(visitee))

    def test_get_type_index_60(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        visitee = model.OWLDataSomeValuesFrom(prop, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 12,
            otip.get_type_index(visitee))

    def test_get_type_index_61(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        visitee = model.OWLDataAllValuesFrom(prop, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 13,
            otip.get_type_index(visitee))

    def test_get_type_index_62(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        value = model.OWLLiteral('abc')
        visitee = model.OWLDataHasValue(prop, value)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 14,
            otip.get_type_index(visitee))

    def test_get_type_index_63(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        visitee = model.OWLDataMinCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 15,
            otip.get_type_index(visitee))

    def test_get_type_index_64(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLDatatype('http://ex.org/dtype/int')
        visitee = model.OWLDataExactCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 16,
            otip.get_type_index(visitee))

    def test_get_type_index_65(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        visitee = model.OWLDataMaxCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 17,
            otip.get_type_index(visitee))

    def test_get_type_index_66(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE +
            OWLObjectTypeIndexProvider.ONTOLOGY, otip.get_type_index(visitee))

    def test_get_type_index_67(self):
        otip = OWLObjectTypeIndexProvider()
        data_range = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        visitee = model.OWLDataComplementOf(data_range)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 2,
            otip.get_type_index(visitee))

    def test_get_type_index_68(self):
        otip = OWLObjectTypeIndexProvider()
        values = {model.OWLLiteral('one'), model.OWLLiteral('two')}
        visitee = model.OWLDataOneOf(values)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 3,
                         otip.get_type_index(visitee))

    def test_get_type_index_69(self):
        otip = OWLObjectTypeIndexProvider()
        operands = {model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))}
        visitee = model.OWLDataIntersectionOf(operands)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 4,
                         otip.get_type_index(visitee))

    def test_get_type_index_70(self):
        otip = OWLObjectTypeIndexProvider()
        operands = {model.OWLDatatype(model.IRI('http://ex.org/dtype/negint')),
                    model.OWLDatatype(model.IRI('http://ex.org/dtype/negint'))}
        visitee = model.OWLDataUnionOf(operands)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE + 5,
                         otip.get_type_index(visitee))

    def test_get_type_index_71(self):
        otip = OWLObjectTypeIndexProvider()
        dtype = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))

        facet1 = OWLFacet.LENGTH
        facet_value1 = model.OWLLiteral('23')
        facet_restriction1 = model.OWLFacetRestriction(facet1, facet_value1)

        facet2 = OWLFacet.MAX_EXCLUSIVE
        facet_value2 = model.OWLLiteral('5')
        facet_restriction2 = model.OWLFacetRestriction(facet2, facet_value2)

        facet_restrictions = {facet_restriction1, facet_restriction2}
        visitee = model.OWLDatatypeRestriction(dtype, facet_restrictions)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 6,
                         otip.get_type_index(visitee))

    def test_get_type_index_72(self):
        otip = OWLObjectTypeIndexProvider()
        facet = OWLFacet.LENGTH
        facet_value = model.OWLLiteral('23')
        visitee = model.OWLFacetRestriction(facet, facet_value)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 7,
                         otip.get_type_index(visitee))

    def test_get_type_index_73(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLLiteral('23')
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 8,
                         otip.get_type_index(visitee))

    def test_get_type_index_74(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.og/prop'))
        value = model.OWLLiteral('abc')
        annotations = []
        visitee = model.OWLAnnotation(prop, value, annotations)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.ANNOTATION_TYPE_INDEX_BASE + 1,
            otip.get_type_index(visitee))

    def test_get_type_index_75(self):
        otip = OWLObjectTypeIndexProvider()
        predicate = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        indiv = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg = model.SWRLIndividualArgument(indiv)
        visitee = model.SWRLClassAtom(predicate, arg)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE +
            OWLObjectTypeIndexProvider.ONTOLOGY, otip.get_type_index(visitee))

    def test_get_type_index_76(self):
        otip = OWLObjectTypeIndexProvider()
        predicate = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        arg = model.SWRLLiteralArgument(model.OWLLiteral('foo'))
        visitee = model.SWRLDataRangeAtom(predicate, arg)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 2,
            otip.get_type_index(visitee))

    def test_get_type_index_77(self):
        otip = OWLObjectTypeIndexProvider()
        predicate = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        arg0 = model.SWRLIndividualArgument(
            model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ')))
        arg1 = model.SWRLIndividualArgument(
            model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC')))
        visitee = model.SWRLObjectPropertyAtom(predicate, arg0, arg1)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 3,
            otip.get_type_index(visitee))

    def test_get_type_index_78(self):
        otip = OWLObjectTypeIndexProvider()
        predicate = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        arg0 = model.SWRLIndividualArgument(
            model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ')))
        arg1 = model.SWRLIndividualArgument(
            model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC')))
        visitee = model.SWRLDataPropertyAtom(predicate, arg0, arg1)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 4,
            otip.get_type_index(visitee))

    def test_get_type_index_79(self):
        otip = OWLObjectTypeIndexProvider()
        predicate = model.IRI('http://ex.og/sth')
        args = [model.SWRLLiteralArgument(model.OWLLiteral('foo')),
                model.SWRLLiteralArgument(model.OWLLiteral('bar'))]
        visitee = model.SWRLBuiltInAtom(predicate, args)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 5,
            otip.get_type_index(visitee))

    def test_get_type_index_80(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.SWRLVariable(model.IRI('http://ex.org/foo'))
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 6,
            otip.get_type_index(visitee))

    def test_get_type_index_81(self):
        otip = OWLObjectTypeIndexProvider()
        indiv = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        visitee = model.SWRLIndividualArgument(indiv)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 7,
            otip.get_type_index(visitee))

    def test_get_type_index_82(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.SWRLLiteralArgument(model.OWLLiteral('23'))
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 8,
            otip.get_type_index(visitee))

    def test_get_type_index_83(self):
        otip = OWLObjectTypeIndexProvider()
        data_factory = owlapy.model.OWLDataFactory()

        indiv0 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg0 = model.SWRLIndividualArgument(indiv0)

        indiv1 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg1 = model.SWRLIndividualArgument(indiv1)

        visitee = model.SWRLSameIndividualAtom(data_factory, arg0, arg1)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 9,
            otip.get_type_index(visitee))

    def test_get_type_index_84(self):
        otip = OWLObjectTypeIndexProvider()
        data_factory = owlapy.model.OWLDataFactory()

        indiv0 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg0 = model.SWRLIndividualArgument(indiv0)

        indiv1 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg1 = model.SWRLIndividualArgument(indiv1)

        visitee = model.SWRLDifferentIndividualsAtom(data_factory, arg0, arg1)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 10,
            otip.get_type_index(visitee))

    # -------------------------------------------------------------------------
    def test_visit_01(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.IRI('http://ex.org/sth')
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.IRI, otip.type)

    def test_visit_02(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLClass(model.IRI('http://ex.org/SomeCls'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.OWL_CLASS, otip.type)

    def test_visit_03(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLObjectProperty(model.IRI('http://ex.org/objProp'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.OBJECT_PROPERTY, otip.type)

    def test_visit_04(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/objProp'))
        visitee = model.OWLObjectInverseOf(prop)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.OBJECT_PROPERTY_INVERSE,
                         otip.type)

    def test_visit_05(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLDataProperty(model.IRI('http://ex.org/dataProp'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_PROPERTY, otip.type)

    def test_visit_06(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.INDIVIDUAL, otip.type)

    def test_visit_07(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.ANNOTATION_PROPERTY,
                         otip.type)

    def test_visit_08(self):
        otip = OWLObjectTypeIndexProvider()
        data_factory = model.OWLDataFactory()
        manager = owlapy.OWLOntologyManager(data_factory)
        ont_id = model.OWLOntologyID()
        visitee = model.OWLOntology(manager, ont_id)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.ONTOLOGY, otip.type)

    def test_visit_09(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLAnonymousIndividual(model.NodeID('_:23'))
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.ANON_INDIVIDUAL, otip.type)

    def test_visit_10(self):
        otip = OWLObjectTypeIndexProvider()
        sub_class = model.OWLClass(model.IRI('http://ex.org/Sub'))
        super_class = model.OWLClass(model.IRI('http://ex.org/Super'))
        annotations = []
        visitee = model.OWLSubClassOfAxiom(sub_class, super_class, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.SUBCLASS_AXIOM, otip.type)

    def test_visit_11(self):
        otip = OWLObjectTypeIndexProvider()
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop23'))
        obj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))
        annotations = []
        visitee = model.OWLNegativeObjectPropertyAssertionAxiom(
            subj, prop, obj, annotations)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.NEGATIVE_OBJECT_PROPERTY_ASSERTION,
            otip.type)

    def test_visit_12(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLAsymmetricObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_13(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLReflexiveObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_14(self):
        otip = OWLObjectTypeIndexProvider()
        cls = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        annotations = []
        visitee = model.OWLDisjointClassesAxiom(cls, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_15(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        dom = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        annotations = []
        visitee = model.OWLDataPropertyDomainAxiom(prop, dom, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_16(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        dom = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        annotations = []
        visitee = model.OWLObjectPropertyDomainAxiom(prop, dom, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_17(self):
        otip = OWLObjectTypeIndexProvider()
        props = [model.OWLObjectProperty(model.IRI('http://ex.org/prop1')),
                 model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))]
        annotations = []
        visitee = model.OWLEquivalentObjectPropertiesAxiom(props, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_18(self):
        otip = OWLObjectTypeIndexProvider()
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        obj = model.OWLLiteral("abc", None, None)
        annotations = []
        visitee = model.OWLNegativeDataPropertyAssertionAxiom(
            subj, prop, obj, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_19(self):
        otip = OWLObjectTypeIndexProvider()
        indivs = {model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ')),
                  model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))}
        annotations = []
        visitee = model.OWLDifferentIndividualsAxiom(indivs, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_20(self):
        otip = OWLObjectTypeIndexProvider()
        props = {model.OWLObjectProperty(model.IRI('http://ex.org/prop1')),
                 model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))}
        annotations = []
        visitee = model.OWLDisjointDataPropertiesAxiom(props, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_21(self):
        otip = OWLObjectTypeIndexProvider()
        props = {model.OWLObjectProperty(model.IRI('http://ex.org/prop1')),
                 model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))}
        annotations = []
        visitee = model.OWLDisjointObjectPropertiesAxiom(props, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_22(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        rnge = model.OWLClass(model.IRI('http://ex.org/SomeCls'))
        annotations = []
        visitee = model.OWLObjectPropertyRangeAxiom(prop, rnge, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_23(self):
        otip = OWLObjectTypeIndexProvider()
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/SomeCls'))
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        obj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        anns = []
        visitee = model.OWLObjectPropertyAssertionAxiom(subj, prop, obj, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_24(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLFunctionalObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_25(self):
        otip = OWLObjectTypeIndexProvider()
        sub_prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))
        super_prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))
        anns = []
        visitee = model.OWLSubObjectPropertyOfAxiom(sub_prop, super_prop, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_26(self):
        otip = OWLObjectTypeIndexProvider()
        cls1 = model.OWLClass(model.IRI('http://ex.org/SomeCls'))
        cls2 = model.OWLClass(model.IRI('http://ex.org/AnotherCls'))
        annotations = []
        visitee = model.OWLDisjointUnionAxiom(cls1, cls2, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_27(self):
        otip = OWLObjectTypeIndexProvider()
        entity = model.OWLClass(model.IRI('http://ex.org/SomeCls'))
        annotations = []
        visitee = model.OWLDeclarationAxiom(entity, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_28(self):
        otip = OWLObjectTypeIndexProvider()
        subj = model.IRI('http://ex.org/sth')
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop'))
        val = model.IRI('http://ex.org/sthElse')
        anns = []
        visitee = model.OWLAnnotationAssertionAxiom(subj, prop, val, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_29(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop'))
        dom = model.IRI('http://ex.org/sth')
        anns = []
        visitee = model.OWLAnnotationPropertyDomainAxiom(prop, dom, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_30(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/annProp'))
        rnge = model.IRI('http://ex.org/sth')
        anns = []
        visitee = model.OWLAnnotationPropertyRangeAxiom(prop, rnge, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_31(self):
        otip = OWLObjectTypeIndexProvider()
        sub_prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop1'))
        super_prop = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/prop2'))
        annotations = []
        visitee = model.OWLSubAnnotationPropertyOfAxiom(sub_prop, super_prop,
                                                        annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_32(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLSymmetricObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_33(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        rnge = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        annotations = []
        visitee = model.OWLDataPropertyRangeAxiom(prop, rnge, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_34(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        rnge = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        annotations = []
        visitee = model.OWLFunctionalDataPropertyAxiom(prop, rnge, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_35(self):
        otip = OWLObjectTypeIndexProvider()
        props = {model.OWLDataProperty(model.IRI('http://ex.org/prop1')),
                 model.OWLDataProperty(model.IRI('http://ex.org/prop2'))}
        annotations = []
        visitee = model.OWLEquivalentDataPropertiesAxiom(props, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_36(self):
        otip = OWLObjectTypeIndexProvider()
        individual = model.OWLNamedIndividual(model.IRI('http://ex.org/indiv'))
        cls = model.OWLClass(model.IRI('http://ex.org/SomeCls'))
        annotations = []
        visitee = model.OWLClassAssertionAxiom(individual, cls, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_37(self):
        otip = OWLObjectTypeIndexProvider()
        classes = {model.OWLClass(model.IRI('http://ex.org/SomeClass')),
                   model.OWLClass(model.IRI('http://ex.org/AnotherClass'))}
        annotations = []
        visitee = model.OWLEquivalentClassesAxiom(classes, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_38(self):
        otip = OWLObjectTypeIndexProvider()
        d_type = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        d_range = model.OWLDatatype(model.IRI('http://ex.org/dtype/foo'))
        annotations = []
        visitee = model.OWLDatatypeDefinitionAxiom(d_type, d_range, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_39(self):
        otip = OWLObjectTypeIndexProvider()
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        val = model.OWLLiteral('abc')
        anns = []
        visitee = model.OWLDataPropertyAssertionAxiom(subj, prop, val, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_40(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLTransitiveObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_41(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLIrreflexiveObjectPropertyAxiom(prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_42(self):
        otip = OWLObjectTypeIndexProvider()
        sub_prop = model.OWLDataProperty(model.IRI('http://ex.org/prop1'))
        super_prop = model.OWLDataProperty(model.IRI('http://ex.org/prop2'))
        anns = []
        visitee = model.OWLSubDataPropertyOfAxiom(sub_prop, super_prop, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_43(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        anns = []
        visitee = model.OWLInverseFunctionalObjectPropertyAxiom(prop, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_44(self):
        otip = OWLObjectTypeIndexProvider()
        indivs = {model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ')),
                  model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))}
        annotations = []
        visitee = model.OWLSameIndividualAxiom(indivs, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_45(self):
        otip = OWLObjectTypeIndexProvider()
        prop_chain = [model.OWLObjectProperty(model.IRI('http://ex.org/prop1')),
                      model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))]
        super_prop = model.OWLObjectProperty(model.IRI('http://ex.org/sProp'))
        anns = []
        visitee = model.OWLSubPropertyChainOfAxiom(prop_chain, super_prop, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_46(self):
        otip = OWLObjectTypeIndexProvider()
        first = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))
        secnd = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))
        anns = []
        visitee = model.OWLInverseObjectPropertiesAxiom(first, secnd, anns)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_47(self):
        otip = OWLObjectTypeIndexProvider()
        body = model.SWRLAtom(model.IRI('http://ex.org/sth'))
        head = model.SWRLAtom(model.IRI('http://ex.org/sthElse'))
        annotations = []
        visitee = model.SWRLRule(body, head, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_48(self):
        otip = OWLObjectTypeIndexProvider()
        cls = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        annotations = []
        visitee = model.OWLHasKeyAxiom(cls, prop, annotations)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.AXIOM_TYPE_INDEX_BASE +
                         visitee.get_axiom_type().index, otip.type)

    def test_visit_49(self):
        otip = OWLObjectTypeIndexProvider()
        operands = {model.OWLClass(model.IRI('http://ex.org/SomeClass')),
                    model.OWLClass(model.IRI('http://ex.org/AnotherClass'))}
        visitee = model.OWLObjectIntersectionOf(operands)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE +
            OWLObjectTypeIndexProvider.ONTOLOGY, otip.type)

    def test_visit_50(self):
        otip = OWLObjectTypeIndexProvider()
        operands = {model.OWLClass(model.IRI('http://ex.org/SomeClass')),
                    model.OWLClass(model.IRI('http://ex.org/SomeClass'))}
        visitee = model.OWLObjectUnionOf(operands)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 2,
            otip.type)

    def test_visit_51(self):
        otip = OWLObjectTypeIndexProvider()
        operand = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectComplementOf(operand)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 3,
            otip.type)

    def test_visit_52(self):
        otip = OWLObjectTypeIndexProvider()
        values = {model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ')),
                  model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))}
        visitee = model.OWLObjectOneOf(values)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 4,
            otip.type)

    def test_visit_53(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectSomeValuesFrom(prop, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 5,
            otip.type)

    def test_visit_54(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectAllValuesFrom(prop, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 6,
            otip.type)

    def test_visit_55(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        value = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        visitee = model.OWLObjectHasValue(prop, value)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 7,
            otip.type)

    def test_visit_56(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectMinCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 8,
            otip.type)

    def test_visit_57(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectExactCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 9,
            otip.type)

    def test_visit_58(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        visitee = model.OWLObjectMaxCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 10,
            otip.type)

    def test_visit_59(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        visitee = model.OWLObjectHasSelf(prop)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 11,
            otip.type)

    def test_visit_60(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        visitee = model.OWLDataSomeValuesFrom(prop, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 12,
            otip.type)

    def test_visit_61(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        visitee = model.OWLDataAllValuesFrom(prop, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 13,
            otip.type)

    def test_visit_62(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        value = model.OWLLiteral('abc')
        visitee = model.OWLDataHasValue(prop, value)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 14,
            otip.type)

    def test_visit_63(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        visitee = model.OWLDataMinCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 15,
            otip.type)

    def test_visit_64(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLDatatype('http://ex.org/dtype/int')
        visitee = model.OWLDataExactCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 16,
            otip.type)

    def test_visit_65(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        cardinality = 5
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        visitee = model.OWLDataMaxCardinality(prop, cardinality, filler)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.CLASS_EXPRESSION_TYPE_INDEX_BASE + 17,
            otip.type)

    def test_visit_66(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE +
            OWLObjectTypeIndexProvider.ONTOLOGY, otip.type)

    def test_visit_67(self):
        otip = OWLObjectTypeIndexProvider()
        data_range = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        visitee = model.OWLDataComplementOf(data_range)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 2, otip.type)

    def test_visit_68(self):
        otip = OWLObjectTypeIndexProvider()
        values = {model.OWLLiteral('one'), model.OWLLiteral('two')}
        visitee = model.OWLDataOneOf(values)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 3,
                         otip.type)

    def test_visit_69(self):
        otip = OWLObjectTypeIndexProvider()
        operands = {model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))}
        visitee = model.OWLDataIntersectionOf(operands)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 4,
                         otip.type)

    def test_visit_70(self):
        otip = OWLObjectTypeIndexProvider()
        operands = {model.OWLDatatype(model.IRI('http://ex.org/dtype/negint')),
                    model.OWLDatatype(model.IRI('http://ex.org/dtype/negint'))}
        visitee = model.OWLDataUnionOf(operands)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 5,
                         otip.type)

    def test_visit_71(self):
        otip = OWLObjectTypeIndexProvider()
        dtype = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))

        facet1 = OWLFacet.LENGTH
        facet_value1 = model.OWLLiteral('23')
        facet_restriction1 = model.OWLFacetRestriction(facet1, facet_value1)

        facet2 = OWLFacet.MAX_EXCLUSIVE
        facet_value2 = model.OWLLiteral('5')
        facet_restriction2 = model.OWLFacetRestriction(facet2, facet_value2)

        facet_restrictions = {facet_restriction1, facet_restriction2}
        visitee = model.OWLDatatypeRestriction(dtype, facet_restrictions)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 6,
                         otip.type)

    def test_visit_72(self):
        otip = OWLObjectTypeIndexProvider()
        facet = OWLFacet.LENGTH
        facet_value = model.OWLLiteral('23')
        visitee = model.OWLFacetRestriction(facet, facet_value)
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 7,
                         otip.type)

    def test_visit_73(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.OWLLiteral('23')
        otip.visit(visitee)
        self.assertEqual(OWLObjectTypeIndexProvider.DATA_TYPE_INDEX_BASE + 8,
                         otip.type)

    def test_visit_74(self):
        otip = OWLObjectTypeIndexProvider()
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.og/prop'))
        value = model.OWLLiteral('abc')
        annotations = []
        visitee = model.OWLAnnotation(prop, value, annotations)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.ANNOTATION_TYPE_INDEX_BASE + 1,
            otip.type)

    def test_visit_75(self):
        otip = OWLObjectTypeIndexProvider()
        predicate = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        indiv = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg = model.SWRLIndividualArgument(indiv)
        visitee = model.SWRLClassAtom(predicate, arg)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE +
            OWLObjectTypeIndexProvider.ONTOLOGY, otip.type)

    def test_visit_76(self):
        otip = OWLObjectTypeIndexProvider()
        predicate = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        arg = model.SWRLLiteralArgument(model.OWLLiteral('foo'))
        visitee = model.SWRLDataRangeAtom(predicate, arg)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 2,
            otip.type)

    def test_visit_77(self):
        otip = OWLObjectTypeIndexProvider()
        predicate = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        arg0 = model.SWRLIndividualArgument(
            model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ')))
        arg1 = model.SWRLIndividualArgument(
            model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC')))
        visitee = model.SWRLObjectPropertyAtom(predicate, arg0, arg1)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 3,
            otip.type)

    def test_visit_78(self):
        otip = OWLObjectTypeIndexProvider()
        predicate = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        arg0 = model.SWRLIndividualArgument(
            model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ')))
        arg1 = model.SWRLIndividualArgument(
            model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC')))
        visitee = model.SWRLDataPropertyAtom(predicate, arg0, arg1)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 4,
            otip.type)

    def test_visit_79(self):
        otip = OWLObjectTypeIndexProvider()
        predicate = model.IRI('http://ex.og/sth')
        args = [model.SWRLLiteralArgument(model.OWLLiteral('foo')),
                model.SWRLLiteralArgument(model.OWLLiteral('bar'))]
        visitee = model.SWRLBuiltInAtom(predicate, args)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 5,
            otip.type)

    def test_visit_80(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.SWRLVariable(model.IRI('http://ex.org/foo'))
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 6,
            otip.type)

    def test_visit_81(self):
        otip = OWLObjectTypeIndexProvider()
        indiv = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        visitee = model.SWRLIndividualArgument(indiv)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 7,
            otip.type)

    def test_visit_82(self):
        otip = OWLObjectTypeIndexProvider()
        visitee = model.SWRLLiteralArgument(model.OWLLiteral('23'))
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 8,
            otip.type)

    def test_visit_83(self):
        otip = OWLObjectTypeIndexProvider()
        data_factory = owlapy.model.OWLDataFactory()

        indiv0 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg0 = model.SWRLIndividualArgument(indiv0)

        indiv1 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg1 = model.SWRLIndividualArgument(indiv1)

        visitee = model.SWRLSameIndividualAtom(data_factory, arg0, arg1)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 9,
            otip.type)

    def test_visit_84(self):
        otip = OWLObjectTypeIndexProvider()
        data_factory = owlapy.model.OWLDataFactory()

        indiv0 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg0 = model.SWRLIndividualArgument(indiv0)

        indiv1 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg1 = model.SWRLIndividualArgument(indiv1)

        visitee = model.SWRLDifferentIndividualsAtom(data_factory, arg0, arg1)
        otip.visit(visitee)
        self.assertEqual(
            OWLObjectTypeIndexProvider.RULE_OBJECT_TYPE_INDEX_BASE + 10,
            otip.type)
