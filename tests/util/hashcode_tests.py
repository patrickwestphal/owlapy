import unittest

from rdflib import URIRef

from owlapy import model
from owlapy.util.hashcode import HashCode
from owlapy.vocab.owlfacet import OWLFacet


class TestHashCode(unittest.TestCase):

    def test_hash_ontology(self):
        ont_id = model.OWLOntologyID()
        data_factory = model.OWLDataFactory()
        man = model.OWLOntologyManager(data_factory)
        ont = model.OWLOntology(man, ont_id)
        ont_id_hash = hash(ont_id)
        self.assertEqual(ont_id_hash, HashCode.hash_code(ont))

    def test_asym_obj_prop_axiom(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        asym_obj_prop = model.OWLAsymmetricObjectPropertyAxiom(prop, anns)
        asym_obj_prop_hash = (((3 * HashCode.MULT) + hash(prop)) *
                              HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(asym_obj_prop_hash, HashCode.hash_code(asym_obj_prop))

    def test_cls_assertion_axiom(self):
        indiv = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        ce = model.OWLClass(model.IRI('http://ex.org/SomeCls'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        cls_ass_ax = model.OWLClassAssertionAxiom(indiv, ce, anns)
        cls_ass_ax_hash = (((((7 * HashCode.MULT) + hash(indiv)) *
                             HashCode.MULT) + hash(ce)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(cls_ass_ax_hash, HashCode.hash_code(cls_ass_ax))

    def test_data_prop_assertion_axiom(self):
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        val = model.OWLLiteral('abcd')

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDataPropertyAssertionAxiom(subj, prop, val, anns)
        axiom_hash = (((((((11 * HashCode.MULT) + hash(subj)) *
                          HashCode.MULT) + hash(prop)) * HashCode.MULT) +
                       hash(val)) * HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_data_prop_dom_axiom(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        dom = model.OWLClass(model.IRI('http://ex.org/SomeClass'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDataPropertyDomainAxiom(prop, dom, anns)
        axiom_hash = (((((13 * HashCode.MULT) + hash(prop)) *
                        HashCode.MULT) + hash(dom)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_data_prop_range_axiom(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        rnge = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDataPropertyRangeAxiom(prop, rnge, anns)
        axiom_hash = (((((17 * HashCode.MULT) + hash(prop)) *
                        HashCode.MULT) + hash(rnge)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_sub_data_prop_of_axiom(self):
        sub_prop = model.OWLDataProperty('http://ex.org/subProp')
        super_prop = model.OWLDataProperty('http://ex.org/superProp')

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLSubDataPropertyOfAxiom(sub_prop, super_prop, anns)
        axiom_hash = (((((19 * HashCode.MULT) + hash(sub_prop)) *
                        HashCode.MULT) + hash(super_prop)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_declaration_axiom(self):
        entity = model.OWLClass(model.IRI('http://ex.org/SomeClass'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDeclarationAxiom(entity, anns)
        axiom_hash = (((23 * HashCode.MULT) + hash(entity)) *
                      HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_diff_indivs_axiom(self):
        indiv1 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))
        indiv2 = model.OWLAnonymousIndividual(model.NodeID('_:23'))
        indivs = {indiv1, indiv2}

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDifferentIndividualsAxiom(indivs, anns)
        axiom_hash = (((29 * HashCode.MULT) + HashCode._hash_list(indivs)) *
                      HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_disjoint_classes_axiom(self):
        ce1 = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLClass(model.IRI('http://ex.org/AnotherClass'))
        ce2 = model.OWLObjectSomeValuesFrom(prop, filler)
        ces = {ce1, ce2}

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDisjointClassesAxiom(ces, anns)
        axiom_hash = (((31 * HashCode.MULT) + HashCode._hash_list(ces)) *
                      HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_disjoint_data_props_axiom(self):
        prop1 = model.OWLDataProperty(model.IRI('http://ex.org/prop1'))
        prop2 = model.OWLDataProperty(model.IRI('http://ex.org/prop2'))
        properties = {prop1, prop2}

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDisjointDataPropertiesAxiom(properties, anns)
        axiom_hash = (((37 * HashCode.MULT) +
                       HashCode._hash_list(properties)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_disjoint_obj_props_axiom(self):
        prop1 = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))
        prop2 = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))
        prop3 = model.OWLObjectInverseOf(model.IRI('http://ex.org/prop3'))
        properties = {prop1, prop2, prop3}

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDisjointObjectPropertiesAxiom(properties, anns)
        axiom_hash = (((41 * HashCode.MULT) +
                       HashCode._hash_list(properties)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_disjoint_union_axiom(self):
        cls = model.OWLClass(model.IRI('http://ex.org/SomeClass'))

        ce1 = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLClass(model.IRI('http://ex.org/AnotherClass'))
        ce2 = model.OWLObjectAllValuesFrom(prop, filler)
        ces = {ce1, ce2}

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDisjointUnionAxiom(cls, ces, anns)
        axiom_hash = (((((43 * HashCode.MULT) + hash(axiom.owl_class)) *
                        HashCode.MULT) + HashCode._hash_list(ces)) *
                      HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_annotation_assertion_axiom(self):
        subj = model.IRI('http://ex.org/sth')
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop'))
        val = model.OWLLiteral('abcabc')

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLAnnotationAssertionAxiom(subj, prop, val, anns)
        axiom_hash = (((((((47 * HashCode.MULT) + hash(subj)) *
                          HashCode.MULT) + hash(prop)) * HashCode.MULT) +
                       hash(val)) * HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_equiv_classes_axiom(self):
        ce1 = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        prop1 = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))
        filler1 = model.OWLClass(model.IRI('http://ex.org/AnotherClass'))
        ce2 = model.OWLObjectSomeValuesFrom(prop1, filler1)
        prop2 = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))
        filler2 = model.OWLClass(model.IRI('http://ex.org/YetAnotherClass'))
        ce3 = model.OWLObjectAllValuesFrom(prop2, filler2)
        classes = {ce1, ce2, ce3}

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLEquivalentClassesAxiom(classes, anns)
        axiom_hash = (((53 * HashCode.MULT) + HashCode._hash_list(classes)) *
                      HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_equiv_data_prop_axiom(self):
        prop1 = model.OWLDataProperty(model.IRI('http://ex.org/prop1'))
        prop2 = model.OWLDataProperty(model.IRI('http://ex.org/prop2'))
        properties = {prop1, prop2}

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLEquivalentDataPropertiesAxiom(properties, anns)
        axiom_hash = (((59 * HashCode.MULT) +
                       HashCode._hash_list(properties)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_equiv_obj_prop_axiom(self):
        prop1 = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))
        prop2 = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))
        properties = {prop1, prop2}

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLEquivalentObjectPropertiesAxiom(properties, anns)
        axiom_hash = (((61 * HashCode.MULT) +
                       HashCode._hash_list(properties)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_functional_data_prop_axiom(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        rnge = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLFunctionalDataPropertyAxiom(prop, rnge, anns)
        axiom_hash = (((67 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_functional_obj_prop_axiom(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLFunctionalObjectPropertyAxiom(prop, anns)
        axiom_hash = (((71 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_inv_functional_obj_prop_axiom(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLInverseFunctionalObjectPropertyAxiom(prop, anns)
        axiom_hash = (((79 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_inv_obj_props_axiom(self):
        prop1 = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))
        prop2 = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLInverseObjectPropertiesAxiom(prop1, prop2, anns)
        axiom_hash = (((83 * HashCode.MULT) + hash(prop1) + hash(prop2)) *
                      HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_irrefl_obj_prop_axiom(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLIrreflexiveObjectPropertyAxiom(prop, anns)
        axiom_hash = (((89 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_negative_data_prop_assertion_axiom(self):
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        obj = model.OWLLiteral('acab')

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLNegativeDataPropertyAssertionAxiom(
            subj, prop, obj, anns)
        axiom_hash = (((((((97 * HashCode.MULT) + hash(subj)) *
                          HashCode.MULT) + hash(prop)) * HashCode.MULT) +
                       hash(obj)) * HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_negative_obj_prop_assertion_axiom(self):
        subj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        obj = model.OWLAnonymousIndividual(model.NodeID('_:23'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLNegativeObjectPropertyAssertionAxiom(
            subj, prop, obj, anns)
        axiom_hash = (((((((101 * HashCode.MULT) + hash(subj)) *
                          HashCode.MULT) + hash(prop)) * HashCode.MULT) +
                       hash(obj)) * HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_obj_prop_assertion_axiom(self):
        subj = model.OWLAnonymousIndividual(model.NodeID('_:23'))
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        obj = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLObjectPropertyAssertionAxiom(subj, prop, obj, anns)
        axiom_hash = (((((((103 * HashCode.MULT) + hash(subj)) *
                          HashCode.MULT) + hash(prop)) * HashCode.MULT) +
                       hash(obj)) * HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_sub_prop_chain_of_axiom(self):
        prop1 = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))
        prop2 = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))
        prop3 = model.OWLObjectProperty(model.IRI('http://ex.org/prop3'))
        prop_chain = [prop1, prop2, prop3]

        super_prop = model.OWLObjectProperty(model.IRI('http://ex.org/sProp'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLSubPropertyChainOfAxiom(prop_chain, super_prop, anns)
        axiom_hash = (((((107 * HashCode.MULT) +
                         HashCode._hash_list(prop_chain)) * HashCode.MULT) +
                       hash(super_prop)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_obj_prop_dom_axiom(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))

        cls1 = model.OWLClass(model.IRI('http://ex.org/SomeCls'))
        cls2 = model.OWLClass(model.IRI('http://ex.org/AnotherCls'))
        operands = {cls1, cls2}
        dom = model.OWLObjectUnionOf(operands)

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLObjectPropertyDomainAxiom(prop, dom, anns)
        axiom_hash = (((((109 * HashCode.MULT) + hash(prop)) *
                        HashCode.MULT) + hash(dom)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_obj_prop_range_axiom(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        rnge = model.OWLClass(model.IRI('http://ex.org/SomeClass'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLObjectPropertyRangeAxiom(prop, rnge, anns)
        axiom_hash = (((((113 * HashCode.MULT) + hash(prop)) *
                        HashCode.MULT) + hash(rnge)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_sub_obj_prop_of_axiom(self):
        sub_prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))
        super_prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop2'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLSubObjectPropertyOfAxiom(sub_prop, super_prop, anns)
        axiom_hash = (((((127 * HashCode.MULT) + hash(sub_prop)) *
                        HashCode.MULT) + hash(super_prop)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_refl_obj_prop_axiom(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLReflexiveObjectPropertyAxiom(prop, anns)
        axiom_hash = (((131 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_same_indiv_axiom(self):
        indiv1 = model.OWLAnonymousIndividual(model.NodeID('_:23'))
        indiv2 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))
        indivs = {indiv1, indiv2}

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLSameIndividualAxiom(indivs, anns)
        axiom_hash = (((137 * HashCode.MULT) + HashCode._hash_list(indivs)) *
                      HashCode.MULT) + HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_sub_cls_of_axiom(self):
        sub_cls = model.OWLClass(model.IRI('http://ex.org/SomeClass'))

        cls1 = model.OWLClass(model.IRI('http://ex.org/AnotherClass'))
        cls2 = model.OWLClass(model.IRI('http://ex.org/YetAnotherClass'))
        operands = {cls1, cls2}
        super_cls = model.OWLObjectIntersectionOf(operands)

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLSubClassOfAxiom(sub_cls, super_cls, anns)
        axiom_hash = (((((139 * HashCode.MULT) + hash(sub_cls)) *
                        HashCode.MULT) + hash(super_cls)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_symm_obj_prop_axiom(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/property'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLSymmetricObjectPropertyAxiom(prop, anns)
        axiom_hash = (((149 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_trans_obj_prop_axiom(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLTransitiveObjectPropertyAxiom(prop, anns)
        axiom_hash = (((151 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            HashCode._hash_list(anns)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_cls(self):
        iri = model.IRI('http://ex.org/SomeCls')
        cls = model.OWLClass(iri)
        cls_hash = (157 * HashCode.MULT) + hash(iri)

        self.assertEqual(cls_hash, HashCode.hash_code(cls))

    def test_data_all_vals_from(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))

        ce = model.OWLDataAllValuesFrom(prop, filler)
        ce_hash = (((163 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            hash(filler)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_data_exact_cardinality(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        card = 5
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))

        ce = model.OWLDataExactCardinality(prop, card, filler)
        ce_hash = (((((167 * HashCode.MULT) + hash(prop)) * HashCode.MULT) +
                    card) * HashCode.MULT) + hash(filler)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_data_max_cardinality(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        card = 23
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/str'))

        ce = model.OWLDataMaxCardinality(prop, card, filler)
        ce_hash = (((((173 * HashCode.MULT) + hash(prop)) * HashCode.MULT) +
                    card) * HashCode.MULT) + hash(filler)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_data_min_cardinality(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        card = 5
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))

        ce = model.OWLDataMinCardinality(prop, card, filler)
        ce_hash = (((((179 * HashCode.MULT) + hash(prop)) * HashCode.MULT) +
                    card) * HashCode.MULT) + hash(filler)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_data_some_vals_from(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))

        ce = model.OWLDataSomeValuesFrom(prop, filler)
        ce_hash = (((181 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            hash(filler)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_data_has_val(self):
        prop = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        val = model.OWLLiteral('abc')

        ce = model.OWLDataHasValue(prop, val)
        ce_hash = (((191 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            hash(val)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_obj_all_vals_from(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/property'))

        ce1 = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        ce2 = model.OWLClass(model.IRI('http://ex.org/AnotherClass'))
        operands = {ce1, ce2}
        filler = model.OWLObjectUnionOf(operands)

        ce = model.OWLObjectAllValuesFrom(prop, filler)
        ce_hash = (((193 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            hash(filler)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_obj_complement_of(self):
        operand = model.OWLClass(model.IRI('http://ex.org/SomeClass'))

        ce = model.OWLObjectComplementOf(operand)
        ce_hash = (197 * HashCode.MULT) + hash(operand)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_obj_exact_cardinality(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        card = 5

        cls1 = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        cls2 = model.OWLClass(model.IRI('http://ex.org/AnotherClass'))
        operands = {cls1, cls2}
        filler = model.OWLObjectUnionOf(operands)

        ce = model.OWLObjectExactCardinality(prop, card, filler)
        ce_hash = (((((199 * HashCode.MULT) + hash(prop)) * HashCode.MULT) +
                    card) * HashCode.MULT) + hash(filler)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_obj_intersect_of(self):
        ce1 = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        ce2 = model.OWLClass(model.IRI('http://ex.org/AnotherClass'))
        ce3 = model.OWLClass(model.IRI('http://ex.org/YetAnotherClass'))
        operands = {ce1, ce2, ce3}

        ce = model.OWLObjectIntersectionOf(operands)
        ce_hash = (211 * HashCode.MULT) + HashCode._hash_list(operands)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_obj_max_cardinality(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        card = 5
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))

        ce = model.OWLObjectMaxCardinality(prop, card, filler)
        ce_hash = (((((223 * HashCode.MULT) + hash(prop)) * HashCode.MULT) +
                    card) * HashCode.MULT) + hash(filler)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_obj_min_cardinality(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        card = 25
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))

        ce = model.OWLObjectMinCardinality(prop, card, filler)
        ce_hash = (((((227 * HashCode.MULT) + hash(prop)) * HashCode.MULT) +
                    card) * HashCode.MULT) + hash(filler)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_obj_one_of(self):
        indiv1 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        indiv2 = model.OWLAnonymousIndividual(model.NodeID('_:23'))
        values = {indiv1, indiv2}

        ce = model.OWLObjectOneOf(values)
        ce_hash = (229 * HashCode.MULT) + HashCode._hash_list(values)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_obj_has_self(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))

        ce = model.OWLObjectHasSelf(prop)
        ce_hash = (233 * HashCode.MULT) + hash(prop)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_obj_some_val_from(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        filler = model.OWLClass(model.IRI('http://ex.org/SomeClass'))

        ce = model.OWLObjectSomeValuesFrom(prop, filler)
        ce_hash = (((239 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            hash(filler)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_obj_union_of(self):
        ce1 = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        ce2 = model.OWLClass(model.IRI('http://ex.org/AnotherClass'))
        ce3 = model.OWLClass(model.IRI('http://ex.org/YetAnotherClass'))
        operands = {ce1, ce2, ce3}

        ce = model.OWLObjectUnionOf(operands)
        ce_hash = (241 * HashCode.MULT) + HashCode._hash_list(operands)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_obj_has_val(self):
        prop = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        val = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))

        ce = model.OWLObjectHasValue(prop, val)
        ce_hash = (((251 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            hash(val)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_data_complement_of(self):
        rnge = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))

        ce = model.OWLDataComplementOf(rnge)
        ce_hash = (257 * HashCode.MULT) + hash(rnge)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_data_one_of(self):
        val1 = model.OWLLiteral('abc')
        val2 = model.OWLLiteral('def')
        val3 = model.OWLLiteral('ghi')
        values = {val1, val2, val3}

        ce = model.OWLDataOneOf(values)
        ce_hash = (263 * HashCode.MULT) + HashCode._hash_list(values)

        self.assertEqual(ce_hash, HashCode.hash_code(ce))

    def test_datatype(self):
        iri = model.IRI('http://ex.org/dtype/int')
        dtype = model.OWLDatatype(iri)
        dtype_hash = (269 * HashCode.MULT) + hash(iri)

        self.assertEqual(dtype_hash, HashCode.hash_code(dtype))

    def test_datatype_restr(self):
        dtype = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))

        facet1 = OWLFacet.LENGTH
        facet_val1 = model.OWLLiteral('23')
        fr1 = model.OWLFacetRestriction(facet1, facet_val1)
        facet2 = OWLFacet.MAX_EXCLUSIVE
        facet_value2 = model.OWLLiteral('5')
        fr2 = model.OWLFacetRestriction(facet2, facet_value2)
        facet_restrictions = {fr1, fr2}

        node = model.OWLDatatypeRestriction(dtype, facet_restrictions)
        node_hash = (((271 * HashCode.MULT) + hash(dtype)) * HashCode.MULT) + \
            HashCode._hash_list(facet_restrictions)

        self.assertEqual(node_hash, HashCode.hash_code(node))

    def test_facet_restr(self):
        facet = OWLFacet.LENGTH
        facet_val = model.OWLLiteral('23')

        node = model.OWLFacetRestriction(facet, facet_val)
        node_hash = (((563 * HashCode.MULT) + hash(facet)) * HashCode.MULT) + \
            hash(facet_val)

        self.assertEqual(node_hash, HashCode.hash_code(node))

    def test_literal(self):
        literal = model.OWLLiteral('abc')
        self.assertEqual(hash(literal), HashCode.hash_code(literal))

    def test_data_prop(self):
        iri = model.IRI('http://ex.org/dprop')
        prop = model.OWLDataProperty(iri)
        prop_hash = (283 * HashCode.MULT) + hash(iri)

        self.assertEqual(prop_hash, HashCode.hash_code(prop))

    def test_object_prop(self):
        iri = model.IRI('http://ex.org/prop')
        prop = model.OWLObjectProperty(iri)
        prop_hash = (293 * HashCode.MULT) + hash(iri)

        self.assertEqual(prop_hash, HashCode.hash_code(prop))

    def test_obj_inv_of(self):
        inv_prop = model.OWLObjectProperty(model.IRI('http://ex.org/iProp'))

        prop = model.OWLObjectInverseOf(inv_prop)
        prop_hash = (307 * HashCode.MULT) + hash(inv_prop)

        self.assertEqual(prop_hash, HashCode.hash_code(prop))

    def test_named_indiv(self):
        iri = model.IRI('http://ex.org/indivABC')
        indiv = model.OWLNamedIndividual(iri)
        indiv_hash = (311 * HashCode.MULT) + hash(iri)

        self.assertEqual(indiv_hash, HashCode.hash_code(indiv))

    def test_swrl_rule(self):
        pred1 = model.OWLDataProperty(model.IRI('http://ex.org/prop1'))
        b_arg0 = model.SWRLLiteralArgument(model.OWLLiteral('abc'))
        b_arg1 = model.SWRLLiteralArgument(model.OWLLiteral('def'))
        body = model.SWRLDataPropertyAtom(pred1, b_arg0, b_arg1)

        pred2 = model.OWLDataProperty(model.IRI('http://ex.org/prop2'))
        h_arg0 = model.SWRLLiteralArgument(model.OWLLiteral('23'))
        h_arg1 = model.SWRLLiteralArgument(model.OWLLiteral('42'))
        head = model.SWRLDataPropertyAtom(pred2, h_arg0, h_arg1)

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        rule = model.SWRLRule(body, head, anns)
        rule_hash = (((631 * HashCode.MULT) + hash(body)) * HashCode.MULT) +\
            hash(head)

        self.assertEqual(rule_hash, HashCode.hash_code(rule))

    def test_swrl_cls_atom(self):
        pred = model.OWLClass(model.IRI('http://ex.org/SomeClass'))
        indiv = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg = model.SWRLIndividualArgument(indiv)

        atom = model.SWRLClassAtom(pred, arg)
        atom_hash = (((641 * HashCode.MULT) + hash(arg)) * HashCode.MULT) + \
            hash(pred)

        self.assertEqual(atom_hash, HashCode.hash_code(atom))

    def test_srwl_data_range_atom(self):
        pred = model.OWLDatatype(model.IRI('http://ex.org/SomeClass'))
        literal = model.OWLLiteral('foo')
        arg = model.SWRLLiteralArgument(literal)

        atom = model.SWRLDataRangeAtom(pred, arg)
        atom_hash = (((643 * HashCode.MULT) + hash(arg)) * HashCode.MULT) + \
            hash(pred)

        self.assertEqual(atom_hash, HashCode.hash_code(atom))

    def test_swrl_obj_prop_atom(self):
        pred = model.OWLObjectProperty(model.IRI('http://ex.org/prop'))
        indiv0 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivABC'))
        arg0 = model.SWRLIndividualArgument(indiv0)
        indiv1 = model.OWLAnonymousIndividual(model.NodeID('_:23'))
        arg1 = model.SWRLIndividualArgument(indiv1)

        atom = model.SWRLObjectPropertyAtom(pred, arg0, arg1)
        atom_hash = (((((647 * HashCode.MULT) + hash(arg0)) * HashCode.MULT) +
                      hash(arg1)) * HashCode.MULT) + hash(pred)

        self.assertEqual(atom_hash, HashCode.hash_code(atom))

    def test_swrl_data_prop_atom(self):
        pred = model.OWLDataProperty(model.IRI('http://ex.org/prop'))
        arg0 = model.SWRLLiteralArgument(model.OWLLiteral('abc'))
        arg1 = model.SWRLLiteralArgument(model.OWLLiteral('def'))

        atom = model.SWRLDataPropertyAtom(pred, arg0, arg1)
        atom_hash = (((((653 * HashCode.MULT) + hash(arg0)) * HashCode.MULT) +
                      hash(arg1)) * HashCode.MULT) + hash(pred)

        self.assertEqual(atom_hash, HashCode.hash_code(atom))

    def test_swrl_built_in_atom(self):
        pred = model.IRI('http://ex.org/sth')
        arg1 = model.SWRLLiteralArgument(model.OWLLiteral('abc'))
        arg2 = model.SWRLLiteralArgument(model.OWLLiteral('def'))
        arg3 = model.SWRLLiteralArgument(model.OWLLiteral('ghi'))
        args = [arg1, arg2, arg3]

        atom = model.SWRLBuiltInAtom(pred, args)
        atom_hash = (((659 * HashCode.MULT) + HashCode._hash_list(args)) *
                     HashCode.MULT) + hash(pred)

        self.assertEqual(atom_hash, HashCode.hash_code(atom))

    def test_swrl_variable(self):
        iri = model.IRI('http://ex.org/sth')
        var = model.SWRLVariable(iri)
        var_hash = (661 * HashCode.MULT) + hash(iri)

        self.assertEqual(var_hash, HashCode.hash_code(var))

    def test_swrl_indiv_arg(self):
        indiv = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))

        arg = model.SWRLIndividualArgument(indiv)
        arg_hash = (677 * HashCode.MULT) + hash(indiv)

        self.assertEqual(arg_hash, HashCode.hash_code(arg))

    def test_swrl_literal_arg(self):
        literal = model.OWLLiteral('abc')
        arg = model.SWRLLiteralArgument(literal)
        arg_hash = (683 * HashCode.MULT) + hash(literal)

        self.assertEqual(arg_hash, HashCode.hash_code(arg))

    def test_swrl_diff_indivs_atom(self):
        data_factory = model.OWLDataFactory()
        indiv0 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg0 = model.SWRLIndividualArgument(indiv0)
        indiv1 = model.OWLAnonymousIndividual(model.NodeID('_:23'))
        arg1 = model.SWRLIndividualArgument(indiv1)

        atom = model.SWRLDifferentIndividualsAtom(data_factory, arg0, arg1)
        atom_hash = (((797 * HashCode.MULT) + hash(arg0)) * HashCode.MULT) + \
            hash(arg1)

        self.assertEqual(atom_hash, HashCode.hash_code(atom))

    def test_swrl_same_indivs_atom(self):
        data_factory = model.OWLDataFactory()
        indiv0 = model.OWLNamedIndividual(model.IRI('http://ex.org/indivXYZ'))
        arg0 = model.SWRLIndividualArgument(indiv0)
        indiv1 = model.OWLAnonymousIndividual(model.NodeID('_:23'))
        arg1 = model.SWRLIndividualArgument(indiv1)

        atom = model.SWRLSameIndividualAtom(data_factory, arg0, arg1)
        atom_hash = (((811 * HashCode.MULT) + hash(arg0)) * HashCode.MULT) + \
            hash(arg1)

        self.assertEqual(atom_hash, HashCode.hash_code(atom))

    def test_has_key_axiom(self):
        ce = model.OWLClass(model.IRI('http://ex.org/SomeClass'))

        pe1 = model.OWLObjectProperty(model.IRI('http://ex.org/prop1'))
        pe2 = model.OWLObjectInverseOf(
            model.OWLObjectProperty(model.IRI('http://ex.org/prop2')))
        pe3 = model.OWLObjectProperty(model.IRI('http://ex.org/prop3'))
        pes = {pe1, pe2, pe3}

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLHasKeyAxiom(ce, pes, anns)
        axiom_hash = (((821 * HashCode.MULT) + hash(ce)) * HashCode.MULT) + \
            HashCode._hash_list(pes)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_ann_prop_dom_axiom(self):
        prop = model.OWLAnnotationProperty('http://ex.org/prop')
        dom = model.IRI('http://ex.org/sth')

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLAnnotationPropertyDomainAxiom(prop, dom, anns)
        axiom_hash = (((823 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            hash(dom)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test__owl_ann_prop_range_axiom(self):
        prop = model.OWLAnnotationProperty('http://ex.org/prop')
        rnge = model.IRI('http://ex.org/sth')

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLAnnotationPropertyRangeAxiom(prop, rnge, anns)
        axiom_hash = (((827 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            hash(rnge)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_sub_ann_prop_of_axiom(self):
        sub_prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/prop1'))
        super_prop = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/prop2'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLSubAnnotationPropertyOfAxiom(
            sub_prop, super_prop, anns)
        axiom_hash = (((829 * HashCode.MULT) + hash(sub_prop)) *
                      HashCode.MULT) + hash(super_prop)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))

    def test_data_intersect_of(self):
        dtype1 = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        dtype2 = model.OWLDatatype(model.IRI('http://ex.org/dtype/float'))
        operands = {dtype1, dtype2}

        node = model.OWLDataIntersectionOf(operands)
        node_hash = (839 * HashCode.MULT) + HashCode._hash_list(operands)

        self.assertEqual(node_hash, HashCode.hash_code(node))

    def test_data_union_of(self):
        dtype1 = model.OWLDatatype(model.IRI('http://ex.org/dtype/int'))
        dtype2 = model.OWLDatatype(model.IRI('http://ex.org/dtype/float'))
        operands = {dtype1, dtype2}

        node = model.OWLDataUnionOf(operands)
        node_hash = (853 * HashCode.MULT) + HashCode._hash_list(operands)

        self.assertEqual(node_hash, HashCode.hash_code(node))

    def test_annotation_prop(self):
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/anProp'))
        prop_hash = (857 * HashCode.MULT) + hash(prop.iri)

        self.assertEqual(prop_hash, HashCode.hash_code(prop))

    def test_anon_indiv(self):
        node_id = model.NodeID('_:23')
        indiv = model.OWLAnonymousIndividual(node_id)
        indiv_hash = (859 * HashCode.MULT) + hash(node_id)

        self.assertEqual(indiv_hash, HashCode.hash_code(indiv))

    def test_iri(self):
        uri = URIRef('http//ex.org/some/uri')
        iri = model.IRI(uri)
        iri_hash = (863 * HashCode.MULT) + hash(uri)

        self.assertEqual(iri_hash, HashCode.hash_code(iri))
        # TOOD: the test below fails... think about this!
        # self.assertEqual(iri_hash, hash(iri))

    def test_annotation(self):
        prop = model.OWLAnnotationProperty(model.IRI('http://ex.org/anProp'))
        val = model.OWLLiteral('annotation')
        ann = model.OWLAnnotation(prop, val, [])
        ann_hash = (((877 * HashCode.MULT) + hash(prop)) * HashCode.MULT) + \
            hash(val)

        self.assertEqual(ann_hash, HashCode.hash_code(ann))

    def test_datatype_definition_axiom(self):
        dtype = model.OWLDatatype(model.IRI('http://ex.org/dtype/posInt'))
        drange = model.OWLDataComplementOf(
            model.IRI('http://ex.org/dtype/negInt'))

        ann_prop1 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp'))
        ann_val1 = model.OWLLiteral('annotation 1')
        ann1 = model.OWLAnnotation(ann_prop1, ann_val1, [])
        ann_prop2 = model.OWLAnnotationProperty(
            model.IRI('http://ex.org/anProp2'))
        ann_val2 = model.OWLLiteral('annotation 2')
        ann2 = model.OWLAnnotation(ann_prop2, ann_val2, [])
        anns = {ann1, ann2}

        axiom = model.OWLDatatypeDefinitionAxiom(dtype, drange, anns)
        axiom_hash = (((897 * HashCode.MULT) + hash(dtype)) * HashCode.MULT) + \
            hash(drange)

        self.assertEqual(axiom_hash, HashCode.hash_code(axiom))
