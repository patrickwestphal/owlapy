import unittest

from owlapy import model
from owlapy import OWLEntityCollectionContainerCollector
from owlapy import CollectionContainerVisitor
from owlapy.model import IRI
from owlapy.model import NodeID
from owlapy.model import OWLAnonymousIndividual
from owlapy.model import OWLClass


class DummyVisitor(CollectionContainerVisitor):
    def __init__(self, collector):
        super().__init__(collector)
        self.visited = False
        self.item_visited = False

    def visit(self, visitee):
        self.visited = True

    def visit_item(self, entity):
        self.item_visited = True


class TestOWLEntityCollectionContainerCollector(unittest.TestCase):
    def test___init__01(self):
        entities = {OWLClass(IRI('http://ex.org/SomeCls'))}
        anons = {OWLAnonymousIndividual(NodeID('_:23'))}
        eccc = OWLEntityCollectionContainerCollector(entities, anons)

        self.assertEqual(set(entities), eccc._objects)
        self.assertEqual(set(anons), eccc._anonymous_individuals)
        self.assertTrue(eccc.collect_classes)
        self.assertTrue(eccc.collect_object_properties)
        self.assertTrue(eccc.collect_data_properties)
        self.assertTrue(eccc.collect_individuals)
        self.assertTrue(eccc.collect_datatypes)

    def test___init__02(self):
        entities = {OWLClass(IRI('http://ex.org/SomeCls'))}
        eccc = OWLEntityCollectionContainerCollector(entities)

        self.assertEqual(entities, eccc._objects)
        self.assertEqual(set(), eccc._anonymous_individuals)
        self.assertTrue(eccc.collect_classes)
        self.assertTrue(eccc.collect_object_properties)
        self.assertTrue(eccc.collect_data_properties)
        self.assertTrue(eccc.collect_individuals)
        self.assertTrue(eccc.collect_datatypes)

    def test_reset(self):
        entities = {OWLClass(IRI('http://ex.org/SomeCls'))}
        anons = {OWLAnonymousIndividual(NodeID('_:23'))}
        eccc = OWLEntityCollectionContainerCollector(entities, anons)

        self.assertEqual(entities, eccc._objects)
        self.assertEqual(set(anons), eccc._anonymous_individuals)

        reset_entities = [OWLClass(IRI('http://ex.org/AnotherCls'))]
        eccc.reset(reset_entities)
        self.assertEqual(reset_entities, eccc._objects)
        self.assertEqual(set(), eccc._anonymous_individuals)

    def test__process_axiom_annotations_01(self):
        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)

        # axiom
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/property'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1_dtype = model.OWLDatatype(
            model.IRI('http://ex.org/dtype/string'))
        ann_val1 = model.OWLLiteral('annotation 1', None, ann_val1_dtype)
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLSymmetricObjectPropertyAxiom(prop, anns)

        # dummy visitor
        dummy_visitor = DummyVisitor(eccc)
        eccc._annotation_visitor = dummy_visitor

        eccc.visit(axiom)

        self.assertFalse(dummy_visitor.visited)
        self.assertTrue(dummy_visitor.item_visited)

    def test_visit_01(self):
        sub_cls = model.OWLClass(model.IRI('http;//ex.org/SomeClass'))  # e
        super_cls = model.OWLClass(model.IRI('http;//ex.org/AnotherClass'))  # e

        ann_prop1 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp'))
        ann_val1_dtype = model.OWLDatatype(  # e
            model.IRI('http://ex.org/dtype/string'))
        ann_val1 = model.OWLLiteral('annotation 1', None, ann_val1_dtype)
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp2'))
        # rdf:plainLiteral dtype is implicitly set --> e
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        visitee = model.OWLSubClassOfAxiom(sub_cls, super_cls, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)

        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(visitee)
        self.assertEqual(6, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(sub_cls, entities)
        self.assertIn(super_cls, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_02(self):
        # e
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))  # e
        # a (not counted)
        obj = model.OWLAnonymousIndividual(model.NodeID('_:23'))

        ann_prop1 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp'))
        ann_val1_dtype = model.OWLDatatype(  # e
            model.IRI('http://ex.org/dtype/string'))
        ann_val1 = model.OWLLiteral('annotation 1', None, ann_val1_dtype)
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp2'))
        # rdf:plainLiteral dtype is implicitly set --> e
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLObjectPropertyAssertionAxiom(subj, prop, obj, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)

        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(6, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(subj, entities)
        self.assertIn(prop, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_03(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/property'))  # e

        ann_prop1 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp'))
        ann_val1_dtype = model.OWLDatatype(  # e
            model.IRI('http://ex.org/dtype/string'))
        ann_val1 = model.OWLLiteral('annotation 1', None, ann_val1_dtype)
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp2'))
        # rdf:plainLiteral dtype is implicitly set --> e
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLSymmetricObjectPropertyAxiom(prop, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)

        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(5, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(prop, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_04(self):
        cls1 = model.OWLClass(model.IRI('http://ex.org/Cls1'))  # e
        cls2 = model.OWLClass(model.IRI('http://ex.org/Cls2'))  # e
        operands = {cls1, cls2}
        ce1 = model.OWLObjectIntersectionOf(operands)

        ce2 = model.OWLClass(model.IRI('http://ex.org/Cls3'))  # e

        ces = {ce1, ce2}

        ann_prop1 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp'))
        ann_val1_dtype = model.OWLDatatype(  # e
            model.IRI('http://ex.org/dtype/string'))
        ann_val1 = model.OWLLiteral('annotation 1', None, ann_val1_dtype)
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp2'))
        # rdf:plainLiteral dtype is implicitly set --> e
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLEquivalentClassesAxiom(ces, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)

        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(7, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(cls1, entities)
        self.assertIn(cls2, entities)
        self.assertIn(ce2, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_05(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))  # e
        dom = model.OWLClass(model.IRI('http://ex.org/SomeClass'))  # e

        ann_prop1 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp'))
        ann_val1_dtype = model.OWLDatatype(  # e
            model.IRI('http://ex.org/dtype/string'))
        ann_val1 = model.OWLLiteral('annotation 1', None, ann_val1_dtype)
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp2'))
        # rdf:plainLiteral dtype is implicitly set --> e
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDataPropertyDomainAxiom(prop, dom, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)

        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(6, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(prop, entities)
        self.assertIn(dom, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_06(self):
        prop1 = model.OWLDataProperty(model.IRI('http;//ex.org/prop1'))  # e
        prop2 = model.OWLDataProperty(model.IRI('http;//ex.org/prop2'))  # e
        prop3 = model.OWLDataProperty(model.IRI('http;//ex.org/prop3'))  # e
        prop4 = model.OWLDataProperty(model.IRI('http;//ex.org/prop4'))  # e
        props = {prop1, prop2, prop3, prop4}

        ann_prop1 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp'))
        ann_val1_dtype = model.OWLDatatype(  # e
            model.IRI('http://ex.org/dtype/string'))
        ann_val1 = model.OWLLiteral('annotation 1', None, ann_val1_dtype)
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp2'))
        # rdf:plainLiteral dtype is implicitly set --> e
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDisjointDataPropertiesAxiom(props, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)

        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(8, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(prop1, entities)
        self.assertIn(prop2, entities)
        self.assertIn(prop3, entities)
        self.assertIn(prop4, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_07(self):
        i1 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))  # e
        # a, but not counted
        i2 = model.OWLAnonymousIndividual(model.NodeID('_:23'))
        i3 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))  # e
        indivs = {i1, i2, i3}

        ann_prop1 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp'))
        ann_val1_dtype = model.OWLDatatype(  # e
            model.IRI('http://ex.org/dtype/string'))
        ann_val1 = model.OWLLiteral('annotation 1', None, ann_val1_dtype)
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp2'))
        # rdf:plainLiteral dtype is implicitly set --> e
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLSameIndividualAxiom(indivs, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(6, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(i1, entities)
        self.assertIn(i3, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_08(self):
        # prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        # axiom = model.OWLDataPropertyRangeAxiom(prop, rnge, anns)
        # go on here
        self.fail()

    def test_visit_09(self):
        self.fail()

    def test_visit_10(self):
        self.fail()

    def test_visit_11(self):
        self.fail()

    def test_visit_12(self):
        self.fail()

    def test_visit_13(self):
        self.fail()

    def test_visit_14(self):
        self.fail()

    def test_visit_15(self):
        self.fail()

    def test_visit_16(self):
        self.fail()

    def test_visit_17(self):
        self.fail()

    def test_visit_18(self):
        self.fail()

    def test_visit_19(self):
        self.fail()

    def test_visit_20(self):
        self.fail()

    def test_visit_21(self):
        self.fail()

    def test_visit_22(self):
        self.fail()

    def test_visit_23(self):
        self.fail()

    def test_visit_24(self):
        self.fail()

    def test_visit_25(self):
        self.fail()

    def test_visit_26(self):
        self.fail()

    def test_visit_27(self):
        self.fail()

    def test_visit_28(self):
        self.fail()

    def test_visit_29(self):
        self.fail()

    def test_visit_30(self):
        self.fail()

    def test_visit_31(self):
        self.fail()

    def test_visit_32(self):
        self.fail()

    def test_visit_33(self):
        self.fail()

    def test_visit_34(self):
        self.fail()

    def test_visit_35(self):
        self.fail()

    def test_visit_36(self):
        self.fail()

    def test_visit_37(self):
        self.fail()

    def test_visit_38(self):
        self.fail()

    def test_visit_39(self):
        self.fail()

    def test_visit_40(self):
        self.fail()

    def test_visit_41(self):
        self.fail()

    def test_visit_42(self):
        self.fail()

    def test_visit_43(self):
        self.fail()

    def test_visit_44(self):
        self.fail()

    def test_visit_45(self):
        self.fail()

    def test_visit_46(self):
        self.fail()

    def test_visit_47(self):
        self.fail()

    def test_visit_48(self):
        self.fail()

    def test_visit_49(self):
        self.fail()
