from owlapy import CollectionContainer
from owlapy import CollectionContainerVisitor
from owlapy.model import OWLAnonymousIndividual
from owlapy.model import OWLAnnotation
from owlapy.model import OWLAnnotationAssertionAxiom
from owlapy.model import OWLAnnotationProperty
from owlapy.model import OWLAnnotationPropertyDomainAxiom
from owlapy.model import OWLAnnotationPropertyRangeAxiom
from owlapy.model import OWLAsymmetricObjectPropertyAxiom
from owlapy.model import OWLClassAssertionAxiom
from owlapy.model import OWLClass
from owlapy.model import OWLDataAllValuesFrom
from owlapy.model import OWLDataComplementOf
from owlapy.model import OWLDataExactCardinality
from owlapy.model import OWLDataHasValue
from owlapy.model import OWLDataIntersectionOf
from owlapy.model import OWLDataMaxCardinality
from owlapy.model import OWLDataMinCardinality
from owlapy.model import OWLDataOneOf
from owlapy.model import OWLDataProperty
from owlapy.model import OWLDataPropertyAssertionAxiom
from owlapy.model import OWLDataPropertyDomainAxiom
from owlapy.model import OWLDataPropertyRangeAxiom
from owlapy.model import OWLDataSomeValuesFrom
from owlapy.model import OWLDatatype
from owlapy.model import OWLDatatypeDefinitionAxiom
from owlapy.model import OWLDatatypeRestriction
from owlapy.model import OWLDataUnionOf
from owlapy.model import OWLDeclarationAxiom
from owlapy.model import OWLDisjointClassesAxiom
from owlapy.model import OWLDisjointDataPropertiesAxiom
from owlapy.model import OWLDisjointUnionAxiom
from owlapy.model import OWLDifferentIndividualsAxiom
from owlapy.model import OWLEquivalentClassesAxiom
from owlapy.model import OWLEquivalentDataPropertiesAxiom
from owlapy.model import OWLEquivalentObjectPropertiesAxiom
from owlapy.model import OWLFacetRestriction
from owlapy.model import OWLFunctionalDataPropertyAxiom
from owlapy.model import OWLFunctionalObjectPropertyAxiom
from owlapy.model import OWLIrreflexiveObjectPropertyAxiom
from owlapy.model import OWLInverseFunctionalObjectPropertyAxiom
from owlapy.model import OWLInverseObjectPropertiesAxiom
from owlapy.model import OWLHasKeyAxiom
from owlapy.model import OWLLiteral
from owlapy.model import OWLNamedIndividual
from owlapy.model import OWLNegativeDataPropertyAssertionAxiom
from owlapy.model import OWLNegativeObjectPropertyAssertionAxiom
from owlapy.model import OWLObjectAllValuesFrom
from owlapy.model import OWLObjectComplementOf
from owlapy.model import OWLObjectExactCardinality
from owlapy.model import OWLObjectHasSelf
from owlapy.model import OWLObjectHasValue
from owlapy.model import OWLObjectIntersectionOf
from owlapy.model import OWLObjectInverseOf
from owlapy.model import OWLObjectMaxCardinality
from owlapy.model import OWLObjectMinCardinality
from owlapy.model import OWLObjectOneOf
from owlapy.model import OWLObjectProperty
from owlapy.model import OWLObjectPropertyAssertionAxiom
from owlapy.model import OWLObjectPropertyDomainAxiom
from owlapy.model import OWLObjectPropertyRangeAxiom
from owlapy.model import OWLObjectSomeValuesFrom
from owlapy.model import OWLObjectUnionOf
from owlapy.model import OWLObjectVisitor
from owlapy.model import OWLOntology
from owlapy.model import OWLReflexiveObjectPropertyAxiom
from owlapy.model import OWLSameIndividualAxiom
from owlapy.model import OWLSubAnnotationPropertyOfAxiom
from owlapy.model import OWLSubClassOfAxiom
from owlapy.model import OWLSubDataPropertyOfAxiom
from owlapy.model import OWLSubObjectPropertyOfAxiom
from owlapy.model import OWLSubPropertyChainOfAxiom
from owlapy.model import OWLSymmetricObjectPropertyAxiom
from owlapy.model import OWLTransitiveObjectPropertyAxiom
from owlapy.model import SWRLClassAtom
from owlapy.model import SWRLBuiltInAtom
from owlapy.model import SWRLDataPropertyAtom
from owlapy.model import SWRLDataRangeAtom
from owlapy.model import SWRLDifferentIndividualsAtom
from owlapy.model import SWRLIndividualArgument
from owlapy.model import SWRLLiteralArgument
from owlapy.model import SWRLObjectPropertyAtom
from owlapy.model import SWRLRule
from owlapy.model import SWRLSameIndividualAtom


class OWLEntityCollectionContainerCollector(OWLObjectVisitor):
    # TODO: maybe implement List<OWLAnonymousIndividual> fake

    def __init__(self, to_return, anons_to_return=None):
        """
        :param to_return: the set of owlapy.model.OWLEntity objects that will
            contain the results
        :param anons_to_return: the set that will contain the
            owlapy.model.OWLAnonymousIndividual objects
        """
        self._objects = to_return
        self._anonymous_individuals = anons_to_return \
            if anons_to_return is not None else set()

        self.collect_classes = True
        self.collect_object_properties = True
        self.collect_data_properties = True
        self.collect_individuals = True
        self.collect_datatypes = True
        self._annotation_visitor = CollectionContainerVisitor(self)

    def reset(self, to_return):
        """Clears all objects that have accumulated during the course of
        visiting axioms, class expressions etc.

        :param to_return: the OWLEntity set that will contain the results
        """
        self._objects = to_return
        self._anonymous_individuals.clear()

    def _process_axiom_annotations(self, axiom):
        """
        :param axiom: an owlapy.model.OWLAxiom object
        """
        if isinstance(axiom, CollectionContainer):
            # in the OWLAPI all OWLAxioms implement the CollectionContainer
            # interface, so the else branch would never be taken:
            #
            # public abstract class OWLAxiomImpl extends OWLObjectImpl
            #                    implements OWLAxiom,
            #                               CollectionContainer<OWLAnnotation> {
            # ...
            axiom.accept(self._annotation_visitor)
        else:
            # default behavior: iterate over the annotations outside the axiom
            # as far as I understand, this branch will never be taken...
            for annotation in axiom.annotations:
                annotation.accept(self)

    def visit(self, visitee):
        # TODO: check the elif order and type hierarchy!!!
        # ---------------- axiom visits ----------------
        # 01
        if isinstance(visitee, OWLSubClassOfAxiom):
            visitee.sub_class.accept(self)
            visitee.super_class.accept(self)
            self._process_axiom_annotations(visitee)

        # TODO: common superclass OWLIndividualRelationshipAxiom sufficient???
        # 02
        elif isinstance(visitee, OWLNegativeObjectPropertyAssertionAxiom) or \
                isinstance(visitee, OWLNegativeDataPropertyAssertionAxiom) or \
                isinstance(visitee, OWLObjectPropertyAssertionAxiom) or \
                isinstance(visitee, OWLDataPropertyAssertionAxiom):
            visitee.subject.accept(self)
            visitee.property.accept(self)
            visitee.object.accept(self)
            self._process_axiom_annotations(visitee)

        # TODO: common supercls OWLObjectPropertyCharacteristicAxiom sufficient?
        #                   &   OWLPropertyRangeAxiom
        # 03
        elif isinstance(visitee, OWLAsymmetricObjectPropertyAxiom) or \
                isinstance(visitee, OWLReflexiveObjectPropertyAxiom) or \
                isinstance(visitee, OWLFunctionalObjectPropertyAxiom) or \
                isinstance(visitee, OWLSymmetricObjectPropertyAxiom) or \
                isinstance(visitee, OWLFunctionalDataPropertyAxiom) or \
                isinstance(visitee, OWLTransitiveObjectPropertyAxiom) or \
                isinstance(visitee, OWLIrreflexiveObjectPropertyAxiom) or \
                isinstance(visitee, OWLInverseFunctionalObjectPropertyAxiom):
            visitee.property.accept(self)
            self._process_axiom_annotations(visitee)

        # 04
        elif isinstance(visitee, OWLDisjointClassesAxiom) or \
                isinstance(visitee, OWLEquivalentClassesAxiom):
            for desc in visitee.class_expressions:
                desc.accept(self)
            self._process_axiom_annotations(visitee)

        # TODO: common superclass OWLPropertyDomainaxiom sufficient???
        # 05
        elif isinstance(visitee, OWLDataPropertyDomainAxiom) or \
                isinstance(visitee, OWLObjectPropertyDomainAxiom):
            visitee.domain.accept(self)
            visitee.property.accept(self)
            self._process_axiom_annotations(visitee)

        # TODO: common superclass OWLNaryPropertyAxiom sufficient???
        # 06
        elif isinstance(visitee, OWLEquivalentObjectPropertiesAxiom) or \
                isinstance(visitee, OWLDisjointDataPropertiesAxiom) or \
                isinstance(visitee, OWLEquivalentDataPropertiesAxiom):
            for prop in visitee.properties:
                prop.accept(self)
            self._process_axiom_annotations(visitee)

        # 07
        elif isinstance(visitee, OWLDifferentIndividualsAxiom) or \
                isinstance(visitee, OWLSameIndividualAxiom):
            for ind in visitee.individuals:
                ind.accept(self)
            self._process_axiom_annotations(visitee)

        # TODO: common superclass OWLPropertyRangeAxiom sufficient???
        # 08
        elif isinstance(visitee, OWLObjectPropertyRangeAxiom) or \
                isinstance(visitee, OWLDataPropertyRangeAxiom):
            visitee.range.accept(self)
            visitee.property.accept(self)
            self._process_axiom_annotations(visitee)

        # 09
        elif isinstance(visitee, OWLSubObjectPropertyOfAxiom) or \
                isinstance(visitee, OWLSubDataPropertyOfAxiom):
            visitee.sub_property.accept(self)
            visitee.super_property.accept(self)
            self._process_axiom_annotations(visitee)

        # 10
        elif isinstance(visitee, OWLDisjointUnionAxiom):
            visitee.owl_class.accept(self)
            for desc in visitee.class_expressions:
                desc.accept(self)
            self._process_axiom_annotations(visitee)

        # 11
        elif isinstance(visitee, OWLDeclarationAxiom):
            visitee.entity.accept(self)
            self._process_axiom_annotations(visitee)

        # 12
        elif isinstance(visitee, OWLClassAssertionAxiom):
            visitee.class_expression.accept(self)
            visitee.individual.accept(self)
            self._process_axiom_annotations(visitee)

        # 13
        elif isinstance(visitee, OWLSubPropertyChainOfAxiom):
            for prop in visitee.property_chain:
                prop.accept(self)
            visitee.super_property.accept(self)
            self._process_axiom_annotations(visitee)

        # 14
        elif isinstance(visitee, OWLInverseObjectPropertiesAxiom):
            visitee.first_property.accept(self)
            visitee.second_property.accept(self)
            self._process_axiom_annotations(visitee)

        # 15
        elif isinstance(visitee, OWLHasKeyAxiom):
            visitee.class_expression.accept(self)
            for prop in visitee.property_expressions:
                prop.accept(self)
            self._process_axiom_annotations(visitee)

        # ---------------- class expression visits ----------------
        # 16
        elif isinstance(visitee, OWLClass):
            if self.collect_classes:
                self._objects.add(visitee)

        # TODO: common superclass OWLNaryBooleanClassExpressionImpl sufficient??
        # 17
        elif isinstance(visitee, OWLObjectIntersectionOf) or \
                isinstance(visitee, OWLObjectUnionOf):
            for operand in visitee.operands:
                operand.accept(self)

        # 18
        elif isinstance(visitee, OWLObjectComplementOf):
            visitee.operand.accept(self)

        # 19
        elif isinstance(visitee, OWLObjectSomeValuesFrom) or \
                isinstance(visitee, OWLObjectAllValuesFrom) or \
                isinstance(visitee, OWLObjectMinCardinality) or \
                isinstance(visitee, OWLObjectExactCardinality) or \
                isinstance(visitee, OWLObjectMaxCardinality) or \
                isinstance(visitee, OWLDataSomeValuesFrom) or \
                isinstance(visitee, OWLDataAllValuesFrom) or \
                isinstance(visitee, OWLDataMinCardinality) or \
                isinstance(visitee, OWLDataExactCardinality) or \
                isinstance(visitee, OWLDataMaxCardinality):
            visitee.property.accept(self)
            visitee.filler.accept(self)

        # 20
        elif isinstance(visitee, OWLObjectHasValue) or \
                isinstance(visitee, OWLDataHasValue):
            visitee.property.accept(self)
            visitee.value.accept(self)

        # 21
        elif isinstance(visitee, OWLObjectHasSelf):
            visitee.property.accept(self)

        # 22
        elif isinstance(visitee, OWLObjectOneOf):
            for ind in visitee.individuals:
                ind.accept(self)

        # ---------------- data visits ----------------
        # 23
        elif isinstance(visitee, OWLDataComplementOf):
            visitee.data_range.accept(self)

        # 24
        elif isinstance(visitee, OWLDataOneOf):
            for val in visitee.values:
                val.accept(self)

        # 25
        elif isinstance(visitee, OWLDataIntersectionOf) or \
                isinstance(visitee, OWLDataUnionOf):
            for data_range in visitee.operands:
                data_range.accept(self)

        # 26
        elif isinstance(visitee, OWLDatatypeRestriction):
            visitee.datatype.accept(self)
            for facet_restriction in visitee.facet_restrictions:
                facet_restriction.accept(self)

        # 27
        elif isinstance(visitee, OWLFacetRestriction):
            visitee.facet_value.accept(self)

        # 28
        elif isinstance(visitee, OWLLiteral):
            visitee.datatype.accept(self)

        # ---------------- property expression visits ----------------
        # 29
        elif isinstance(visitee, OWLObjectInverseOf):
            visitee.inverse.accept(self)

        # ---------------- entity visits ----------------
        # 30
        elif isinstance(visitee, OWLObjectProperty):
            if self.collect_object_properties:
                self._objects.add(visitee)

        # 31
        elif isinstance(visitee, OWLDataProperty):
            if self.collect_data_properties:
                self._objects.add(visitee)

        # 32
        elif isinstance(visitee, OWLNamedIndividual):
            if self.collect_individuals:
                self._objects.add(visitee)

        # 33
        elif isinstance(visitee, OWLDatatype):
            if self.collect_datatypes:
                self._objects.add(visitee)

        # 34
        elif isinstance(visitee, OWLAnnotation):
            visitee.property.accept(self)
            visitee.value.accept(self)
            for anno in visitee.annotations:
                anno.accept(self)

        # 35
        elif isinstance(visitee, OWLAnnotationAssertionAxiom):
            visitee.subject.accept(self)
            visitee.property.accept(self)
            visitee.value.accept(self)
            self._process_axiom_annotations(visitee)

        # 36
        elif isinstance(visitee, OWLAnonymousIndividual):
            # Anon individuals aren't entities
            # But store them in a set anyway for utility
            self._anonymous_individuals.add(visitee)

        # 37
        elif isinstance(visitee, OWLOntology):
            self._objects = self._objects.union(visitee.get_signature())

        # 38
        elif isinstance(visitee, OWLAnnotationProperty):
            self._objects.add(visitee)

        # 39
        elif isinstance(visitee, OWLAnnotationPropertyDomainAxiom) or \
                isinstance(visitee, OWLAnnotationPropertyRangeAxiom):
            visitee.property.accept(self)
            self._process_axiom_annotations(visitee)

        # 40
        elif isinstance(visitee, OWLSubAnnotationPropertyOfAxiom):
            visitee.sub_property.accept(self)
            visitee.super_property.accept(self)
            self._process_axiom_annotations(visitee)

        # 41
        elif isinstance(visitee, OWLDatatypeDefinitionAxiom):
            visitee.datatype.accept(self)
            visitee.data_range.accept(self)
            self._process_axiom_annotations(visitee)

        # ---------------- SWRL object visits ----------------
        # 42
        elif isinstance(visitee, SWRLRule):
            for atom in visitee.body:
                atom.accept(self)
            for atom in visitee.head:
                atom.accept(self)
            self._process_axiom_annotations(visitee)

        # 43
        elif isinstance(visitee, SWRLClassAtom) or \
                isinstance(visitee, SWRLDataRangeAtom):
            visitee.argument.accept(self)
            visitee.predicate.accept(self)

        # 44
        elif isinstance(visitee, SWRLObjectPropertyAtom) or \
                isinstance(visitee, SWRLDataPropertyAtom):
            visitee.predicate.accept(self)
            visitee.first_argument.accept(self)
            visitee.second_argument.accept(self)

        # 45
        elif isinstance(visitee, SWRLBuiltInAtom):
            for obj in visitee.arguments:
                obj.accept(self)

        # 46
        elif isinstance(visitee, SWRLIndividualArgument):
            visitee.individual.accept(self)

        # 47
        elif isinstance(visitee, SWRLLiteralArgument):
            visitee.literal.accept(self)

        # 48
        elif isinstance(visitee, SWRLDifferentIndividualsAtom):
            visitee.first_argument.accept(self)

        # 49
        elif isinstance(visitee, SWRLSameIndividualAtom):
            visitee.second_argument.accept(self)
