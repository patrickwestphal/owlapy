from .exceptions import OWLRuntimeException
from .owlobject import OWLObject
from .owlvisitor import OWLVisitorEx, OWLVisitor


class OWLOntology(OWLObject):
    """Represents an OWL 2 Ontology in the OWL 2 specification.
    An OWLOntology consists of a possibly empty set of OWLAxioms and a possibly
    empty set of OWLAnnotations. An ontology can have an ontology IRI which can
    be used to identify the ontology. If it has an ontology IRI then it may also
    have an ontology version IRI. Since OWL 2, an ontology need not have an
    ontology IRI. An ontology cannot be modified directly. Changes must be
    applied via its OWLOntologyManager.
    """

    def __init__(self, manager, ontology_id):
        """
        :param manager: an owlapy.model.OWLOntologyManager object
        :param ontology_id: an owlapy.model.OWLOntologyID object
        :return:
        """
        super().__init__()
        self.owl_ontology_manager = manager
        self.ontology_id = ontology_id

    def contains_annotation_property_in_signaturee(
            self, annotation_property, include_imports_closure=False):
        """Determines if the signature of this ontology contains an
        OWLAnnotationProperty with the specified IRI

        TODO: check if default for include_imports_closure is OK

        :param annotation_property: an owlapy.model.IRI object indicating the
            OWLAnnotationProperty to check for.
        :param include_imports_closure: boolean indicating whether the
            signature of the ontologies in the imports closure of this
            ontology, or only the signature of this ontology should be checked
        :return: bool indicating whether the signature of this ontology contains
            an OWLAnnotationProperty that has annotation_property as its IRI
        """
        raise NotImplementedError()

    def contains_axiom(self, axiom, include_imports_closure=False):
        """Determines if this ontology, and possibly the imports closure,
        contains the specified axiom.

        TODO: check if default for include_imports_closure is correct

        :param axiom: an owlapy.model.Axiom object to test for.
        :param include_imports_closure: bool indicating whether the imports
            closure of this ontology will be searched for the specific axiom,
            or just this ontology
        :return: boolean indicating whether the ontology contains the specified
            axiom
        """
        raise NotImplementedError()

    def accept(self, visitor):
        if isinstance(visitor, OWLVisitorEx):
            return visitor.visit(self)
        elif isinstance(visitor, OWLVisitor):
            visitor.visit(self)
        else:
            raise OWLRuntimeException('Can only accept instances of'
                                      'owlapy.model.OWLVisitor or '
                                      'owlapy.model.OWLVisitorEx')
