from .owlannotationaxiomvisitor import OWLAnnotationAxiomVisitor


class OWLAxiomVisitor(OWLAnnotationAxiomVisitor):
    """Marker class"""

    def visit(self, axiom):
        """
        :param axiom: an object of one of the following classes:
            - owlapy.model.OWLDeclarationAxiom
            - owlapy.model.OWLSubClassOfAxiom
            - owlapy.model.OWLNegativeObjectPropertyAssertionAxiom
            - owlapy.model.OWLAsymmetricObjectPropertyAxiom
            - owlapy.model.OWLReflexiveObjectPropertyAxiom
            - owlapy.model.OWLDisjointClassesAxiom
            - owlapy.model.OWLDataPropertyDomainAxiom
            - owlapy.model.OWLObjectPropertyDomainAxiom
            - owlapy.model.OWLEquivalentObjectPropertiesAxiom
            - owlapy.model.OWLNegativeDataPropertyAssertionAxiom
            - owlapy.model.OWLDifferentIndividualsAxiom
            - owlapy.model.OWLDisjointDataPropertiesAxiom
            - owlapy.model.OWLDisjointObjectPropertiesAxiom
            - owlapy.model.OWLObjectPropertyRangeAxiom
            - owlapy,model.OWLObjectPropertyAssertionAxiom
            - owlapy.model.OWLFunctionalObjectPropertyAxiom
            - owlapy.model.OWLSubObjectPropertyOfAxiom
            - owlapy.model.OWLDisjointUnionAxiom
            - owlapy.model.OWLSymmetricObjectPropertyAxiom
            - owlapy.model.OWLDataPropertyRangeAxiom
            - owlapy.model.OWLFunctionalDataPropertyAxiom
            - owlapy.model.OWLEquivalentDataPropertiesAxiom
            - owlapy.model.OWLClassAssertionAxiom
            - owlapy.model.OWLEquivalentClassesAxiom
            - owlapy.model.OWLDataPropertyAssertionAxiom
            - owlapy.model.OWLTransitiveObjectPropertyAxiom
            - owlapy.model.OWLIrreflexiveObjectPropertyAxiom
            - owlapy.model.OWLSubDataPropertyOfAxiom
            - owlapy.model.OWLInverseFunctionalObjectPropertyAxiom
            - owlapy.model.OWLSameIndividualAxiom
            - owlapy.model.OWLSubPropertyChainOfAxiom
            - owlapy.model.OWLInverseObjectPropertiesAxiom
            - owlapy.model.OWLHasKeyAxiom
            - owlapy.model.OWLDatatypeDefinitionAxiom
            - owlapy.model.SWRLRule
        :return:
        """
        raise NotImplementedError()
