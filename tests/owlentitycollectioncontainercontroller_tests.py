import unittest

from owlapy import model
from owlapy import OWLEntityCollectionContainerCollector
from owlapy import CollectionContainerVisitor
from owlapy.model import IRI
from owlapy.model import NodeID
from owlapy.model import OWLAnonymousIndividual
from owlapy.model import OWLClass
from owlapy.vocab.owlfacet import OWLFacet


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
        # a
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
        self.assertEqual(1, len(anons))

        self.assertIn(subj, entities)
        self.assertIn(prop, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

        self.assertIn(obj, anons)

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
        i2 = model.OWLAnonymousIndividual(model.NodeID('_:23'))  # a
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
        self.assertEqual(1, len(anons))

        self.assertIn(i1, entities)
        self.assertIn(i3, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

        self.assertIn(i2, anons)

    def test_visit_08(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))  # e
        rnge = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))  # e

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

        axiom = model.OWLDataPropertyRangeAxiom(prop, rnge, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(6, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(prop, entities)
        self.assertIn(rnge, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_09(self):
        sub_prop = model.OWLDataProperty(model.IRI('http://ex.org/prop1'))  # e
        tmp_prop = model.OWLDataProperty(model.IRI('http://ex.org/prop2'))  # e
        super_prop = model.OWLDataComplementOf(tmp_prop)

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

        axiom = model.OWLSubDataPropertyOfAxiom(sub_prop, super_prop, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(6, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(sub_prop, entities)
        self.assertIn(tmp_prop, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_10(self):
        owl_cls = model.OWLClass(model.IRI('http://ex.org/SomeClass'))  # e

        ce_cls1 = model.OWLClass(model.IRI('http://ex.org/CECls1'))  # e
        ce_cls2 = model.OWLClass(model.IRI('http://ex.org/CECls2'))  # e
        ce1 = model.OWLObjectIntersectionOf({ce_cls1, ce_cls2})

        ce2 = model.OWLClass(model.IRI('http://ex.org/AnotherClass'))  # e

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

        axiom = model.OWLDisjointUnionAxiom(owl_cls, ces, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(8, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(owl_cls, entities)
        self.assertIn(ce_cls1, entities)
        self.assertIn(ce_cls2, entities)
        self.assertIn(ce2, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_11(self):
        entity = model.OWLDataProperty(model.IRI('http://ex.org/prop'))  # e

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

        axiom = model.OWLDeclarationAxiom(entity, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(5, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(entity, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_12(self):
        indiv = model.OWLAnonymousIndividual(model.NodeID('_:23'))  # a
        ce = model.OWLClass(model.IRI('http://ex.org/SomeClass'))  # e

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

        axiom = model.OWLClassAssertionAxiom(indiv, ce, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(5, len(entities))
        self.assertEqual(1, len(anons))

        self.assertIn(ce, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

        self.assertIn(indiv, anons)

    def test_visit_13(self):
        prop1 = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))  # e
        prop2 = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))  # e
        prop3 = model.OWLObjectProperty(model.IRI('http://ex.org/prop3'))  # e
        prop_chain = [prop1, prop2, prop3]

        # e
        super_prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop4'))

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

        axiom = model.OWLSubPropertyChainOfAxiom(prop_chain, super_prop, anns)

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
        self.assertIn(super_prop, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_14(self):
        first = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))  # e
        second = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))  # e

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

        axiom = model.OWLInverseObjectPropertiesAxiom(first, second, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(6, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(first, entities)
        self.assertIn(second, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_15(self):
        cls1 = model.OWLClass(model.IRI('http://ex.org/SomeClass'))  # e
        cls2 = model.OWLClass(model.IRI('http://ex.org/AnotherClass'))  # e
        ce = model.OWLObjectUnionOf({cls1, cls2})

        prop1 = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))  # e
        prop2 = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))  # e
        pes = {prop1, prop2}

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

        axiom = model.OWLHasKeyAxiom(ce, pes, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(8, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(cls1, entities)
        self.assertIn(cls2, entities)
        self.assertIn(prop1, entities)
        self.assertIn(prop2, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_16(self):
        cls = model.OWLClass(model.IRI('http://ex.org/SomeClass'))  # e

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(cls)
        self.assertEqual(1, len(entities))
        self.assertIn(cls, entities)

    def test_visit_17(self):
        cls1 = model.OWLClass(model.IRI('http://ex.org/SomeClass'))  # e
        cls2 = model.OWLClass(model.IRI('http://ex.org/AnotherClass'))  # e
        ce = model.OWLObjectUnionOf({cls1, cls2})

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(ce)
        self.assertEqual(2, len(entities))
        self.assertIn(cls1, entities)
        self.assertIn(cls2, entities)

    def test_visit_18(self):
        op = model.OWLClass(model.IRI('http://ex.org/SomeClass'))  # e
        ce = model.OWLObjectComplementOf(op)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(ce)
        self.assertEqual(1, len(entities))
        self.assertIn(op, entities)

    def test_visit_19(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))  # e
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))  # e
        ce = model.OWLDataAllValuesFrom(prop, filler)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(ce)
        self.assertEqual(2, len(entities))
        self.assertIn(prop, entities)
        self.assertIn(filler, entities)

    def test_visit_20(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))  # e
        # rdf:plainLiteral dtype is implicitly set --> e
        val = model.OWLLiteral('plain')

        ce = model.OWLDataHasValue(prop, val)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(ce)
        self.assertEqual(2, len(entities))
        self.assertIn(prop, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_21(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        re = model.OWLObjectHasSelf(prop)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(re)
        self.assertEqual(1, len(entities))
        self.assertIn(prop, entities)

    def test_visit_22(self):
        # e
        indiv1 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))
        indiv2 = model.OWLAnonymousIndividual(model.NodeID('_:23'))  # a
        # e
        indiv3 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        ce = model.OWLObjectOneOf({indiv1, indiv2, indiv3})

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(ce)
        self.assertEqual(2, len(entities))
        self.assertEqual(1, len(anons))
        self.assertIn(indiv1, entities)
        self.assertIn(indiv3, entities)

        self.assertIn(indiv2, anons)

    def test_visit_23(self):
        # e
        data_range = model.OWLDatatype(model.IRI('http://ex.org/dtype/negInt'))
        ce = model.OWLDataComplementOf(data_range)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(ce)
        self.assertEqual(1, len(entities))
        self.assertIn(data_range, entities)

    def test_visit_24(self):
        # rdf:plainLiteral dtype is implicitly set --> e
        val1 = model.OWLLiteral('one', 'en')
        # rdf:plainLiteral dtype is implicitly set --> e (not counted twice...)
        val2 = model.OWLLiteral('two')
        dtype = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))  # e
        val3 = model.OWLLiteral('three', None, dtype)

        ce = model.OWLDataOneOf({val1, val2, val3})

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(ce)
        self.assertEqual(2, len(entities))
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)
        self.assertIn(dtype, entities)

    def test_visit_25(self):
        # e
        data_range1 = model.OWLDatatype(model.IRI('http://ex.org/dtype/negInt'))
        # e
        data_range2 = model.OWLDatatype(model.IRI('http://ex.org/dtype/posInt'))
        ce = model.OWLDataUnionOf({data_range1, data_range2})

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(ce)
        self.assertEqual(2, len(entities))
        self.assertIn(data_range1, entities)
        self.assertIn(data_range2, entities)

    def test_visit_26(self):
        dtype = model.OWLDatatype(model.IRI('http://ex.org/dtype/string'))  # e

        facet1 = OWLFacet.LANG_RANGE
        # rdf:plainLiteral dtype is implicitly set --> e
        facet_val1 = model.OWLLiteral('en')
        fr1 = model.OWLFacetRestriction(facet1, facet_val1)

        facet2 = OWLFacet.LENGTH
        f_dtype = model.OWLDatatype(model.IRI('http://ex.org/dytpe/int'))  # e
        facet_val2 = model.OWLLiteral('23', None, f_dtype)
        fr2 = model.OWLFacetRestriction(facet2, facet_val2)

        re = model.OWLDatatypeRestriction(dtype, {fr1, fr2})

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(re)
        self.assertEqual(3, len(entities))
        self.assertIn(dtype, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)
        self.assertIn(f_dtype, entities)

    def test_visit_27(self):
        facet = OWLFacet.LANG_RANGE
        # rdf:plainLiteral dtype is implicitly set --> e
        facet_value = model.OWLLiteral('en')
        re = model.OWLFacetRestriction(facet, facet_value)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(re)
        self.assertEqual(1, len(entities))
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_28(self):
        dtype = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))  # e
        node = model.OWLLiteral('34', None, dtype)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(node)
        self.assertEqual(1, len(entities))
        self.assertIn(dtype, entities)

    def test_visit_29(self):
        inv_prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))  # e
        pe = model.OWLObjectInverseOf(inv_prop)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(pe)
        self.assertEqual(1, len(entities))
        self.assertIn(inv_prop, entities)

    def test_visit_30(self):
        pe = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))  # e

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(pe)
        self.assertEqual(1, len(entities))
        self.assertIn(pe, entities)

    def test_visit_31(self):
        pe = model.OWLDataProperty(model.IRI('http://ex.org/prop'))  # e

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(pe)
        self.assertEqual(1, len(entities))
        self.assertIn(pe, entities)

    def test_visit_32(self):
        # e
        indiv = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(indiv)
        self.assertEqual(1, len(entities))
        self.assertIn(indiv, entities)

    def test_visit_33(self):
        dtype = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))  # e

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(dtype)
        self.assertEqual(1, len(entities))
        self.assertIn(dtype, entities)

    def test_visit_34(self):
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop'))  # e
        # rdf:plainLiteral dtype is implicitly set --> e
        val = model.OWLLiteral('foo')

        ann_prop1 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp'))
        ann_val1_dtype = model.OWLDatatype(  # e
            model.IRI('http://ex.org/dtype/string'))
        ann_val1 = model.OWLLiteral('annotation 1', None, ann_val1_dtype)
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/anProp2'))
        # rdf:plainLiteral dtype is implicitly set --> e (not counted twice)
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        ann = model.OWLAnnotation(prop, val, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(ann)
        self.assertEqual(5, len(entities))
        self.assertIn(prop, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)

    def test_visit_35(self):
        subj = model.OWLAnonymousIndividual(model.NodeID('_:23'))  # a
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop'))  # e

        dtype = model.OWLDatatype('http://ex.org/dtype/int')  # e
        val = model.OWLLiteral('23', None, dtype)

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

        axiom = model.OWLAnnotationAssertionAxiom(subj, prop, val, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(6, len(entities))
        self.assertEqual(1, len(anons))

        self.assertIn(prop, entities)
        self.assertIn(dtype, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

        self.assertIn(subj, anons)

    def test_visit_36(self):
        indiv = model.OWLAnonymousIndividual(model.NodeID('_:23'))  # a

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(indiv)
        self.assertEqual(0, len(entities))
        self.assertEqual(1, len(anons))

        self.assertIn(indiv, anons)

    def test_visit_37(self):
        self.fail('OWLOntology need to be implemented first')

    def test_visit_38(self):
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop'))  # e

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(prop)
        self.assertEqual(1, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(prop, entities)

    def test_visit_39(self):
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop'))  # e
        # e (but not counted)
        rnge = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))

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

        axiom = model.OWLAnnotationPropertyRangeAxiom(prop, rnge, anns)

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

    def test_visit_40(self):
        # e
        sub_prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop1'))
        super_prop = model.OWLAnnotationProperty(  # e
            model.IRI('http://ex.org/prop2'))

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

        axiom = model.OWLSubAnnotationPropertyOfAxiom(
            sub_prop, super_prop, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(6, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(sub_prop, entities)
        self.assertIn(super_prop, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_41(self):
        # e
        d_type = model.OWLDatatype(model.IRI('http://ex.org/dtype/neg_int'))
        # e
        comp_dtype = model.OWLDatatype(model.IRI('http://ex.org/dtype/pos_int'))
        d_range = model.OWLDataComplementOf(comp_dtype)

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

        axiom = model.OWLDatatypeDefinitionAxiom(d_type, d_range, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(axiom)
        self.assertEqual(6, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(d_type, entities)
        self.assertIn(comp_dtype, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)

    def test_visit_42(self):
        pred_b = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))  # e
        # rdf:plainLiteral dtype is implicitly set --> e (not counted twice)
        literal = model.OWLLiteral('plain')
        arg_b = model.SWRLLiteralArgument(literal)
        body = {model.SWRLDataRangeAtom(pred_b, arg_b)}

        pred_h = model.OWLDataProperty(model.IRI('http://ex.org/prop1'))  # e
        # e
        indiv1 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))
        arg1_h = model.SWRLIndividualArgument(indiv1)
        # a
        indiv2 = model.OWLAnonymousIndividual(model.NodeID('_:23'))
        arg2_h = model.SWRLIndividualArgument(indiv2)
        head = {model.SWRLDataPropertyAtom(pred_h, arg1_h, arg2_h)}

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

        node = model.SWRLRule(body, head, anns)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(node)
        self.assertEqual(7, len(entities))
        self.assertEqual(1, len(anons))

        self.assertIn(pred_b, entities)
        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)
        self.assertIn(pred_h, entities)
        self.assertIn(indiv1, entities)
        self.assertIn(ann_prop1, entities)
        self.assertIn(ann_val1_dtype, entities)
        self.assertIn(ann_prop2, entities)

        self.assertIn(indiv2, anons)

    def test_visit_43(self):
        pred = model.OWLClass(model.IRI('http://ex.org/SomeClass'))  # e
        indiv = model.OWLAnonymousIndividual(model.NodeID('_:23'))  # a
        arg = model.SWRLIndividualArgument(indiv)
        node = model.SWRLClassAtom(pred, arg)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(node)
        self.assertEqual(1, len(entities))
        self.assertEqual(1, len(anons))

        self.assertIn(pred, entities)
        self.assertIn(indiv, anons)

    def test_visit_44(self):
        pred = model.OWLDataProperty(model.IRI('http://ex.org/prop'))  # e
        indiv1 = model.OWLAnonymousIndividual(model.NodeID('_:23'))  # a
        arg0 = model.SWRLIndividualArgument(indiv1)
        # e
        indiv2 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))
        arg1 = model.SWRLIndividualArgument(indiv2)
        node = model.SWRLDataPropertyAtom(pred, arg0, arg1)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(node)
        self.assertEqual(2, len(entities))
        self.assertEqual(1, len(anons))

        self.assertIn(pred, entities)
        self.assertIn(indiv2, entities)

        self.assertIn(indiv1, anons)

    def test_visit_45(self):
        pred = model.IRI('http://ex.org/sth')
        # rdf:plainLiteral dtype is implicitly set --> e (not counted twice)
        lit1 = model.OWLLiteral('plain1')
        arg1 = model.SWRLLiteralArgument(lit1)
        dtype = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))  # e
        lit2 = model.OWLLiteral('23', None, dtype)
        arg2 = model.SWRLLiteralArgument(lit2)
        node = model.SWRLBuiltInAtom(pred, {arg1, arg2})

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(node)
        self.assertEqual(2, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(model.OWLLiteral.RDF_PLAIN_LITERAL, entities)
        self.assertIn(dtype, entities)

    def test_visit_46(self):
        indiv = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))
        node = model.SWRLIndividualArgument(indiv)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(node)
        self.assertEqual(1, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(indiv, entities)

    def test_visit_47(self):
        dtype = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        literal = model.OWLLiteral('23', None, dtype)
        node = model.SWRLLiteralArgument(literal)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(node)
        self.assertEqual(1, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(dtype, entities)

    def test_visit_48(self):
        data_factory = model.OWLDataFactory()
        indiv1 = model.OWLAnonymousIndividual(model.NodeID('_:23'))  # a
        arg0 = model.SWRLIndividualArgument(indiv1)

        indiv2 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg1 = model.SWRLIndividualArgument(indiv2)
        node = model.SWRLDifferentIndividualsAtom(data_factory, arg0, arg1)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(node)
        self.assertEqual(0, len(entities))
        self.assertEqual(1, len(anons))

        self.assertIn(indiv1, anons)

    def test_visit_49(self):
        data_factory = model.OWLDataFactory()
        indiv1 = model.OWLAnonymousIndividual(model.NodeID('_:23'))  # a
        arg0 = model.SWRLIndividualArgument(indiv1)

        indiv2 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg1 = model.SWRLIndividualArgument(indiv2)
        node = model.SWRLSameIndividualAtom(data_factory, arg0, arg1)

        entities = set()
        anons = set()
        eccc = OWLEntityCollectionContainerCollector(entities, anons)
        self.assertEqual(0, len(entities))
        self.assertEqual(0, len(anons))

        eccc.visit(node)
        self.assertEqual(1, len(entities))
        self.assertEqual(0, len(anons))

        self.assertIn(indiv2, entities)
