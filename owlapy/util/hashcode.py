from owlapy.model import OWLObjectVisitor
from owlapy.model import SWRLObjectVisitor
from owlapy import model


class HashCode(OWLObjectVisitor, SWRLObjectVisitor):
    MULT = 37

    def __init__(self):
        self._hash_code = None

    @classmethod
    def hash_code(cls, obj):
        """
        :param obj: an owlapy.model.OWLObject object
        :return: an integer representing the hash code of the input object
        """
        hash_code_obj = HashCode()
        obj.accept(hash_code_obj)

        return hash_code_obj._hash_code

    @classmethod
    def _hash_list(cls, iterable):
        """Since sets and lists are not hashable in Python this workaround is
        made based on the getHash implementation of the java.util.AbstractList
        class (http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/6-b14/java/util/AbstractList.java#AbstractList)

        :param iterable: sth that is iterable
        :return: an integer indicating the set's/list's hash
        """
        hash_code = 1
        entries = list(iterable)
        entries.sort()
        for entry in entries:
            if entry is None:
                entry_hash = 0
            elif isinstance(entry, list) or isinstance(entry, set):
                entry_hash = cls._hash_list(entry)
            else:
                entry_hash = hash(entry)

            hash_code = 31 * hash_code + entry_hash

        return hash_code

    def visit(self, visitee):
        fn = self._visitee_type_dict[type(visitee)]
        return fn(self, visitee)

    def _visit_ontology(self, ontology):
        self._hash_code = hash(ontology.ontology_id)

    def _visit_asym_obj_prop_ax(self, axiom):
        self._hash_code = 3
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_cls_assertion_ax(self, axiom):
        self._hash_code = 7
        self._hash_code = self._hash_code * self.MULT + hash(axiom.individual)
        self._hash_code = self._hash_code * self.MULT + \
            hash(axiom.class_expression)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_data_prop_assertion_ax(self, axiom):
        self._hash_code = 11
        self._hash_code = self._hash_code * self.MULT + hash(axiom.subject)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.object)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_data_prop_dom_ax(self, axiom):
        self._hash_code = 13
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.domain)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_data_prop_range_ax(self, axiom):
        self._hash_code = 17
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.range)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_sub_data_prop_of_ax(self, axiom):
        self._hash_code = 19
        self._hash_code = self._hash_code * self.MULT + hash(axiom.sub_property)
        self._hash_code = self._hash_code * self.MULT + \
            hash(axiom.super_property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_declaration_ax(self, axiom):
        self._hash_code = 23
        self._hash_code = self._hash_code * self.MULT + hash(axiom.entity)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_diff_indivs_ax(self, axiom):
        self._hash_code = 29
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.individuals)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_disjoint_classes_ax(self, axiom):
        self._hash_code = 31
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.class_expressions)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_disjoint_data_props_ax(self, axiom):
        self._hash_code = 37
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.properties)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_disjoint_obj_props_ax(self, axiom):
        self._hash_code = 41
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.properties)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_disjoint_union_ax(self, axiom):
        self._hash_code = 43
        self._hash_code = self._hash_code * self.MULT + hash(axiom.owl_class)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.class_expressions)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_annotation_assertion_ax(self, axiom):
        self._hash_code = 47
        self._hash_code = self._hash_code * self.MULT + hash(axiom.subject)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.value)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_equiv_classes_ax(self, axiom):
        self._hash_code = 53
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.class_expressions)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_equiv_data_prop_ax(self, axiom):
        self._hash_code = 59
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.properties)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_equiv_obj_prop_ax(self, axiom):
        self._hash_code = 61
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.properties)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_functional_data_prop_ax(self, axiom):
        self._hash_code = 67
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_functional_obj_prop_ax(self, axiom):
        self._hash_code = 71
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_inv_functional_obj_prop_ax(self, axiom):
        self._hash_code = 79
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_inv_obj_props_ax(self, axiom):
        self._hash_code = 83
        self._hash_code = self._hash_code * self.MULT + \
            hash(axiom.first_property) + hash(axiom.second_property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_irrefl_obj_prop_ax(self, axiom):
        self._hash_code = 89
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_negative_data_prop_assertion_ax(self, axiom):
        self._hash_code = 97
        self._hash_code = self._hash_code * self.MULT + hash(axiom.subject)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.object)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_negative_obj_prop_assertion_ax(self, axiom):
        self._hash_code = 101
        self._hash_code = self._hash_code * self.MULT + hash(axiom.subject)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.object)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_obj_prop_assertion_ax(self, axiom):
        self._hash_code = 103
        self._hash_code = self._hash_code * self.MULT + hash(axiom.subject)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.object)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_sub_prop_chain_of_ax(self, axiom):
        self._hash_code = 107
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.property_chain)
        self._hash_code = self._hash_code * self.MULT + \
            hash(axiom.super_property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_obj_prop_dom_ax(self, axiom):
        self._hash_code = 109
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.domain)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_obj_prop_range_ax(self, axiom):
        self._hash_code = 113
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.range)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_sub_obj_prop_of_ax(self, axiom):
        self._hash_code = 127
        self._hash_code = self._hash_code * self.MULT + hash(axiom.sub_property)
        self._hash_code = self._hash_code * self.MULT + \
            hash(axiom.super_property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_refl_obj_prop_ax(self, axiom):
        self._hash_code = 131
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_same_indiv_ax(self, axiom):
        self._hash_code = 137
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.individuals)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_sub_cls_of_ax(self, axiom):
        self._hash_code = 139
        self._hash_code = self._hash_code * self.MULT + hash(axiom.sub_class)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.super_class)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_symm_obj_prop_ax(self, axiom):
        self._hash_code = 149
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_trans_obj_prop_ax(self, axiom):
        self._hash_code = 151
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.annotations)

    def _visit_cls(self, cls):
        self._hash_code = 157
        self._hash_code = self._hash_code * self.MULT + hash(cls.iri)

    def _visit_data_all_vals_from(self, ce):
        self._hash_code = 163
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + hash(ce.filler)

    def _visit_data_exact_cardinality(self, ce):
        self._hash_code = 167
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + ce.cardinality
        self._hash_code = self._hash_code * self.MULT + hash(ce.filler)

    def _visit_data_max_cardinality(self, ce):
        self._hash_code = 173
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + ce.cardinality
        self._hash_code = self._hash_code * self.MULT + hash(ce.filler)

    def _visit_data_min_cardinality(self, ce):
        self._hash_code = 179
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + ce.cardinality
        self._hash_code = self._hash_code * self.MULT + hash(ce.filler)

    def _visit_data_some_vals_from(self, ce):
        self._hash_code = 181
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + hash(ce.filler)

    def _visit_data_has_val(self, ce):
        self._hash_code = 191
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + hash(ce.value)

    def _visit_obj_all_vals_from(self, ce):
        self._hash_code = 193
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + hash(ce.filler)

    def _visit_obj_complement_of(self, ce):
        self._hash_code = 197
        self._hash_code = self._hash_code * self.MULT + hash(ce.operand)

    def _visit_obj_exact_cardinality(self, ce):
        self._hash_code = 199
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + ce.cardinality
        self._hash_code = self._hash_code * self.MULT + hash(ce.filler)

    def _visit_obj_intersect_of(self, ce):
        self._hash_code = 211
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(ce.operands)

    def _visit_obj_max_cardinality(self, ce):
        self._hash_code = 223
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + ce.cardinality
        self._hash_code = self._hash_code * self.MULT + hash(ce.filler)

    def _visit_obj_min_cardinality(self, ce):
        self._hash_code = 227
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + ce.cardinality
        self._hash_code = self._hash_code * self.MULT + hash(ce.filler)

    def _visit_obj_one_of(self, ce):
        self._hash_code = 229
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(ce.individuals)

    def _visit_obj_has_self(self, ce):
        self._hash_code = 233
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)

    def _visit_obj_some_val_from(self, ce):
        self._hash_code = 239
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + hash(ce.filler)

    def _visit_obj_union_of(self, ce):
        self._hash_code = 241
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(ce.operands)

    def _visit_obj_has_val(self, ce):
        self._hash_code = 251
        self._hash_code = self._hash_code * self.MULT + hash(ce.property)
        self._hash_code = self._hash_code * self.MULT + hash(ce.value)

    def _visit_data_complement_of(self, ce):
        self._hash_code = 257
        self._hash_code = self._hash_code * self.MULT + hash(ce.data_range)

    def _visit_data_one_of(self, ce):
        self._hash_code = 263
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(ce.values)

    def _visit_datatype(self, dtype):
        self._hash_code = 269
        self._hash_code = self._hash_code * self.MULT + hash(dtype.iri)

    def _visit_datatype_restr(self, node):
        self._hash_code = 271
        self._hash_code = self._hash_code * self.MULT + hash(node.datatype)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(node.facet_restrictions)

    def _visit_facet_restr(self, node):
        self._hash_code = 563
        self._hash_code = self._hash_code * self.MULT + hash(node.facet)
        self._hash_code = self._hash_code * self.MULT + hash(node.facet_value)

    def _visit_literal(self, literal):
        self._hash_code = hash(literal)

    def _visit_data_prop(self, prop):
        self._hash_code = 283
        self._hash_code = self._hash_code * self.MULT + hash(prop.iri)

    def _visit_object_prop(self, prop):
        self._hash_code = 293
        self._hash_code = self._hash_code * self.MULT + hash(prop.iri)

    def _visit_obj_inv_of(self, prop):
        self._hash_code = 307
        self._hash_code = self._hash_code * self.MULT + hash(prop.inverse)

    def _visit_named_indiv(self, indiv):
        self._hash_code = 311
        self._hash_code = self._hash_code * self.MULT + hash(indiv.iri)

    def _visit_swrl_rule(self, rule):
        self._hash_code = 631
        self._hash_code = self._hash_code * self.MULT + hash(rule.body)
        self._hash_code = self._hash_code * self.MULT + hash(rule.head)

    def _visit_swrl_cls_atom(self, node):
        self._hash_code = 641
        self._hash_code = self._hash_code * self.MULT + hash(node.argument)
        self._hash_code = self._hash_code * self.MULT + hash(node.predicate)

    def _visit_swrl_data_range_atom(self, node):
        self._hash_code = 643
        self._hash_code = self._hash_code * self.MULT + hash(node.argument)
        self._hash_code = self._hash_code * self.MULT + hash(node.predicate)

    def _visit_swrl_obj_prop_atom(self, node):
        self._hash_code = 647
        self._hash_code = self._hash_code * self.MULT + \
            hash(node.first_argument)
        self._hash_code = self._hash_code * self.MULT + \
            hash(node.second_argument)
        self._hash_code = self._hash_code * self.MULT + hash(node.predicate)

    def _visit_swrl_data_prop_atom(self, node):
        self._hash_code = 653
        self._hash_code = self._hash_code * self.MULT + \
            hash(node.first_argument)
        self._hash_code = self._hash_code * self.MULT + \
            hash(node.second_argument)
        self._hash_code = self._hash_code * self.MULT + hash(node.predicate)

    def _visit_swrl_built_in_atom(self, node):
        self._hash_code = 659
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(node.arguments)
        self._hash_code = self._hash_code * self.MULT + hash(node.predicate)

    def _visit_swrl_variable(self, node):
        self._hash_code = 661
        self._hash_code = self._hash_code * self.MULT + hash(node.iri)

    def _visit_swrl_indiv_arg(self, node):
        self._hash_code = 677
        self._hash_code = self._hash_code * self.MULT + hash(node.individual)

    def _visit_swrl_literal_arg(self, arg):
        self._hash_code = 683
        self._hash_code = self._hash_code * self.MULT + hash(arg.literal)

    def _visit_swrl_diff_indivs_atom(self, node):
        self._hash_code = 797
        self._hash_code = self._hash_code * self.MULT + \
            hash(node.first_argument)
        self._hash_code = self._hash_code * self.MULT + \
            hash(node.second_argument)

    def _visit_swrl_same_indivs_atom(self, node):
        self._hash_code = 811
        self._hash_code = self._hash_code * self.MULT + \
            hash(node.first_argument)
        self._hash_code = self._hash_code * self.MULT + \
            hash(node.second_argument)

    def _visit_has_key_ax(self, axiom):
        self._hash_code = 821
        self._hash_code = self._hash_code * self.MULT + \
            hash(axiom.class_expression)
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(axiom.property_expressions)

    def _visit_ann_prop_dom_ax(self, axiom):
        self._hash_code = 823
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.domain)

    def _visit_owl_ann_prop_range_ax(self, axiom):
        self._hash_code = 827
        self._hash_code = self._hash_code * self.MULT + hash(axiom.property)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.range)

    def _visit_sub_ann_prop_of_ax(self, axiom):
        self._hash_code = 829
        self._hash_code = self._hash_code * self.MULT + hash(axiom.sub_property)
        self._hash_code = self._hash_code * self.MULT + \
            hash(axiom.super_property)

    def _visit_data_intersect_of(self, node):
        self._hash_code = 839
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(node.operands)

    def _visit_data_union_of(self, node):
        self._hash_code = 853
        self._hash_code = self._hash_code * self.MULT + \
            self._hash_list(node.operands)

    def _visit_annotation_prop(self, prop):
        self._hash_code = 857
        self._hash_code = self._hash_code * self.MULT + hash(prop.iri)

    def _visit_anon_indiv(self, indiv):
        self._hash_code = 859
        self._hash_code = self._hash_code * self.MULT + hash(indiv.id)

    def _visit_iri(self, iri):
        self._hash_code = 863
        self._hash_code = self._hash_code * self.MULT + hash(iri.to_uri())

    def _visit_annotation(self, ann):
        self._hash_code = 877
        self._hash_code = self._hash_code * self.MULT + hash(ann.property)
        self._hash_code = self._hash_code * self.MULT + hash(ann.value)

    def _visit_datatype_definition_ax(self, axiom):
        self._hash_code = 897
        self._hash_code = self._hash_code * self.MULT + hash(axiom.datatype)
        self._hash_code = self._hash_code * self.MULT + hash(axiom.data_range)

    # maps the types of visitees to methods to call
    _visitee_type_dict = {
        model.OWLOntology: _visit_ontology,
        model.OWLAsymmetricObjectPropertyAxiom: _visit_asym_obj_prop_ax,
        model.OWLClassAssertionAxiom: _visit_cls_assertion_ax,
        model.OWLDataPropertyAssertionAxiom: _visit_data_prop_assertion_ax,
        model.OWLDataPropertyDomainAxiom: _visit_data_prop_dom_ax,
        model.OWLDataPropertyRangeAxiom: _visit_data_prop_range_ax,
        model.OWLSubDataPropertyOfAxiom: _visit_sub_data_prop_of_ax,
        model.OWLDeclarationAxiom: _visit_declaration_ax,
        model.OWLDifferentIndividualsAxiom: _visit_diff_indivs_ax,
        model.OWLDisjointClassesAxiom: _visit_disjoint_classes_ax,
        model.OWLDisjointDataPropertiesAxiom: _visit_disjoint_data_props_ax,
        model.OWLDisjointObjectPropertiesAxiom: _visit_disjoint_obj_props_ax,
        model.OWLDisjointUnionAxiom: _visit_disjoint_union_ax,
        model.OWLAnnotationAssertionAxiom: _visit_annotation_assertion_ax,
        model.OWLEquivalentClassesAxiom: _visit_equiv_classes_ax,
        model.OWLEquivalentDataPropertiesAxiom: _visit_equiv_data_prop_ax,
        model.OWLEquivalentObjectPropertiesAxiom: _visit_equiv_obj_prop_ax,
        model.OWLFunctionalDataPropertyAxiom: _visit_functional_data_prop_ax,
        model.OWLFunctionalObjectPropertyAxiom: _visit_functional_obj_prop_ax,
        model.OWLInverseFunctionalObjectPropertyAxiom:
            _visit_inv_functional_obj_prop_ax,
        model.OWLInverseObjectPropertiesAxiom: _visit_inv_obj_props_ax,
        model.OWLIrreflexiveObjectPropertyAxiom: _visit_irrefl_obj_prop_ax,
        model.OWLNegativeDataPropertyAssertionAxiom:
            _visit_negative_data_prop_assertion_ax,
        model.OWLNegativeObjectPropertyAssertionAxiom:
            _visit_negative_obj_prop_assertion_ax,
        model.OWLObjectPropertyAssertionAxiom: _visit_obj_prop_assertion_ax,
        model.OWLSubPropertyChainOfAxiom: _visit_sub_prop_chain_of_ax,
        model.OWLObjectPropertyDomainAxiom: _visit_obj_prop_dom_ax,
        model.OWLObjectPropertyRangeAxiom: _visit_obj_prop_range_ax,
        model.OWLSubObjectPropertyOfAxiom: _visit_sub_obj_prop_of_ax,
        model.OWLReflexiveObjectPropertyAxiom: _visit_refl_obj_prop_ax,
        model.OWLSameIndividualAxiom: _visit_same_indiv_ax,
        model.OWLSubClassOfAxiom: _visit_sub_cls_of_ax,
        model.OWLSymmetricObjectPropertyAxiom: _visit_symm_obj_prop_ax,
        model.OWLTransitiveObjectPropertyAxiom: _visit_trans_obj_prop_ax,
        model.OWLClass: _visit_cls,
        model.OWLDataAllValuesFrom: _visit_data_all_vals_from,
        model.OWLDataExactCardinality: _visit_data_exact_cardinality,
        model.OWLDataMaxCardinality: _visit_data_max_cardinality,
        model.OWLDataMinCardinality: _visit_data_min_cardinality,
        model.OWLDataSomeValuesFrom: _visit_data_some_vals_from,
        model.OWLDataHasValue: _visit_data_has_val,
        model.OWLObjectAllValuesFrom: _visit_obj_all_vals_from,
        model.OWLObjectComplementOf: _visit_obj_complement_of,
        model.OWLObjectExactCardinality: _visit_obj_exact_cardinality,
        model.OWLObjectIntersectionOf: _visit_obj_intersect_of,
        model.OWLObjectMaxCardinality: _visit_obj_max_cardinality,
        model.OWLObjectMinCardinality: _visit_obj_min_cardinality,
        model.OWLObjectOneOf: _visit_obj_one_of,
        model.OWLObjectHasSelf: _visit_obj_has_self,
        model.OWLObjectSomeValuesFrom: _visit_obj_some_val_from,
        model.OWLObjectUnionOf: _visit_obj_union_of,
        model.OWLObjectHasValue: _visit_obj_has_val,
        model.OWLDataComplementOf: _visit_data_complement_of,
        model.OWLDataOneOf: _visit_data_one_of,
        model.OWLDatatype: _visit_datatype,
        model.OWLDatatypeRestriction: _visit_datatype_restr,
        model.OWLFacetRestriction: _visit_facet_restr,
        model.OWLLiteral: _visit_literal,
        model.OWLDataProperty: _visit_data_prop,
        model.OWLObjectProperty: _visit_object_prop,
        model.OWLObjectInverseOf: _visit_obj_inv_of,
        model.OWLNamedIndividual: _visit_named_indiv,
        model.SWRLRule: _visit_swrl_rule,
        model.SWRLClassAtom: _visit_swrl_cls_atom,
        model.SWRLDataRangeAtom: _visit_swrl_data_range_atom,
        model.SWRLObjectPropertyAtom: _visit_swrl_obj_prop_atom,
        model.SWRLDataPropertyAtom: _visit_swrl_data_prop_atom,
        model.SWRLBuiltInAtom: _visit_swrl_built_in_atom,
        model.SWRLVariable: _visit_swrl_variable,
        model.SWRLIndividualArgument: _visit_swrl_indiv_arg,
        model.SWRLLiteralArgument: _visit_swrl_literal_arg,
        model.SWRLDifferentIndividualsAtom: _visit_swrl_diff_indivs_atom,
        model.SWRLSameIndividualAtom: _visit_swrl_same_indivs_atom,
        model.OWLHasKeyAxiom: _visit_has_key_ax,
        model.OWLAnnotationPropertyDomainAxiom: _visit_ann_prop_dom_ax,
        model.OWLAnnotationPropertyRangeAxiom: _visit_owl_ann_prop_range_ax,
        model.OWLSubAnnotationPropertyOfAxiom: _visit_sub_ann_prop_of_ax,
        model.OWLDataIntersectionOf: _visit_data_intersect_of,
        model.OWLDataUnionOf: _visit_data_union_of,
        model.OWLAnnotationProperty: _visit_annotation_prop,
        model.OWLAnonymousIndividual: _visit_anon_indiv,
        model.IRI: _visit_iri,
        model.OWLAnnotation: _visit_annotation,
        model.OWLDatatypeDefinitionAxiom: _visit_datatype_definition_ax
    }