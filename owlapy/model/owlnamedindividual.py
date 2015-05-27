from .entitytype import EntityType
from .owlindividual import OWLIndividual
from .exceptions import OWLRuntimeException
from .owllogicalentity import OWLLogicalEntity
import owlapy.util


class OWLNamedIndividual(OWLIndividual, OWLLogicalEntity):
    """Represents a Named Individual [0] as defined in the the OWL 2
    Specification.

    [0] href="http://www.w3.org/TR/owl2-syntax/#Named_Individuals
    """

    def __init__(self, iri):
        """:param iri: an owlapy.model.IRI object
        """
        super().__init__()
        self.iri = iri

    def __str__(self):
        return str(self.iri)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if super().__eq__(other):
            if not isinstance(other, OWLNamedIndividual):
                return False

            other_iri = other.iri

            return self.iri == other_iri

        return False

    def __hash__(self):
        return super().__hash__()

    def is_named(self):
        """Determines if this individual is an instance of
        owlapy.model.OWLNamedIndividual. Note that this method is the dual of
        is_anonymous()
        .
        :return: True if this individual is an instance of
            owlapy.model.OWLNamedIndividual because it is a named individual,
            otherwise False
        """
        return True

    def get_entity_type(self):
        return EntityType.NAMED_INDIVIDUAL

    def get_owl_entity(self, entity_type):
        """
        :param entity_type: an owlapy.model.EntityType object
        :return: an instance of OWLEntity or one of its subclasses
        """
        return super().get_owl_entity(entity_type, self.iri)

    def is_type(self, other_entity_type):
        return self.get_entity_type() == other_entity_type

    def is_owl_named_individual(self):
        return True

    def is_anonymous(self):
        return False

    def as_owl_named_individual(self):
        return self

    def as_owl_anonymous_individual(self):
        raise OWLRuntimeException('Not an anonymous individual')

    def as_owl_annotation_property(self):
        raise OWLRuntimeException('Not an annotation property')

    def is_owl_annotation_property(self):
        return False

    def get_annotations(self, ontology, annotation_property=None):
        """
        :param ontology: an owlapy.model.OWLOntology object
        :param annotation_property: an owlapy.model.OWLAnnotationProperty object
        :return: a set of owlapy.model.OWLAnnotation objects
        """
        return owlapy.util.get_annotations(self, [ontology],
                                           annotation_property)

    def get_annotation_assertion_axioms(self, ontology):
        """
        :param ontology: an owlapy.model.OWLOntology object
        :return: a set of owlapy.model.OWLAxiom objects
        """
        return owlapy.util.get_annotation_axioms(self, [ontology])

    def get_referencing_axioms(self, ontology, include_imports):
        """Gets the axioms in the specified ontology and possibly its imports
        closure that contain this entity in their signature.

        :param ontology: The owlapy.model.OWLOntology object that will be
            searched for axioms
        :param include_imports: If True then axioms in the imports closure will
            also be returned, if False then only the axioms in the specified
            ontology will be returned.
        :return: The axioms (list of owlapy.model.OWLAxiom objects) in the
            specified ontology whose signature contains this entity.
        """
        return ontology.get_referencing_axioms(self, include_imports)

    def _compare_object_of_same_type(self, obj):
        """
        :param obj: an owlapy.model.OWLObject object
        :return: an integer indicating the difference between self and obj
        """
        return self.iri.compare_to(obj.iri)
