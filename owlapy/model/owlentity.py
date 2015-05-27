"""TODO: remove! This is just an 'empty' interface in OWLAPI"""

from .owlobject import OWLObject

class OWLEntity(OWLObject):
    """Represents Entities in the OWL 2 Specification."""

    def __str__(self):
        """Returns a string representation that can be used as the ID of this
        entity.
        """
        raise NotImplementedError()
        # String toStringID();

    def get_entity_type(self):
        """Gets the entity type for this entity
        :return: The entity type (an owlapy.model.EntityType object)
        """
        raise NotImplementedError()
        # EntityType<?> getEntityType();

    def is_type(self, other_entity_type):
        """Tests to see if this entity is of the specified type
        :param other_entity_type: The entity type to check
        :return: True if this entity is of the specified type; False otherwise
        """
        raise NotImplementedError()
        # boolean isType(EntityType<?> entityType);

    def get_annotations(self, ontology, annotation_property=None):
        """Obtains the annotations on this entity where the annotation has the
        specified annotation property.
        If no annotation property is provided, this gets the annotations for
        this entity. These are deemed to be annotations in annotation assertion
        axioms that have a subject that is an owlapy.model.IRI that is equal to
        the IRI of this entity.

        :param ontology: The owlapy.model.Ontology objects to be examined for
            annotation assertion axioms
        :param annotation_property: The annotation property (an
            owlapy.model.OWLAnnotationProperty object)
        :return: The annotations that participate directly in an annotation
            assertion whose subject is an owlapy.model.IRI object corresponding
            to the IRI of this entity.
        """
        raise NotImplementedError()
        # Set<OWLAnnotation> getAnnotations(OWLOntology ontology);
        # Set<OWLAnnotation> getAnnotations(OWLOntology ontology, OWLAnnotationProperty annotationProperty);

    def get_annotation_assertion_axioms(self, ontology):
        """Obtains all annotation assertions on this entity specified in an
        input ontology

        :param ontology: The input owlapy.model.OWLOntology object to examine
        for annotation axioms
        :return: The annotation assertion axioms about this entity in the
        provided ontology
        """
        raise NotImplementedError()
        # Set<OWLAnnotationAssertionAxiom> getAnnotationAssertionAxioms(OWLOntology ontology);

    def is_built_in(self):
        """Determines if this entity is a built in entity. The entity is a
        built in entity if it is
        - a class and the URI corresponds to owl:Thing or owl:Nothing
        - an object property and the URI corresponds to owl:topObjectProperty
          or owl:bottomObjectProperty
        - a data property and the URI corresponds to owl:topDataProperty or
          owl:bottomDataProperty
        - datatype and the IRI is rdfs:Literal or is in the OWL 2 datatype map
          or is rdf:PlainLiteral
        - an annotation property and the URI is in the set of built in
          annotation property URIs, i.e. one of:
          - rdfs:label
          - rdfs:comment
          - rdfs:seeAlso
          - rdfs:isDefinedBy
          - owl:deprecated
          - owl:priorVersion
          - owl:backwardCompatibleWith
          - owl:incompatibleWith

        :return: True if this entity is a built in entity, and false if this
            entity is not a builtin entity.
        """
        raise NotImplementedError()
        # boolean isBuiltIn();

    def is_owl_class(self):
        """A convenience method that determines if this entity is an OWLClass

        :return: True if this entity is an OWLClass, otherwise False
        """
        raise NotImplementedError()
        # boolean isOWLClass();

    def as_owl_class(self):
        """A convenience method that obtains this entity as an OWLClass

        :return: The entity as an OWLClass.
        """
        raise NotImplementedError()
        # OWLClass asOWLClass();

    def is_owl_object_property(self):
        """A convenience method that determines if this entity is an
        OWLObjectProperty

        :return: True if this entity is an OWLObjectProperty, otherwise False
        """
        raise NotImplementedError()
        # boolean isOWLObjectProperty();

    def as_owl_object_property(self):
        """A convenience method that obtains this entity as an
        OWLObjectProperty

        :return: The entity as an OWLObjectProperty.
        """
        raise NotImplementedError()
        # OWLObjectProperty asOWLObjectProperty();

    def is_owl_data_property(self):
        """A convenience method that determines if this entity is an
        OWLDataProperty

        :return: True if this entity is an OWLDataProperty, otherwise False
        """
        raise NotImplementedError()
        # boolean isOWLDataProperty();

    def as_owl_data_property(self):
        """A convenience method that obtains this entity as an OWLDataProperty

        :return: The entity as an OWLDataProperty.
        """
        raise NotImplementedError()
        # OWLDataProperty asOWLDataProperty();

    def is_owl_named_individual(self):
        """A convenience method that determines if this entity is an
        OWLNamedIndividual

        :return: True if this entity is an OWLNamedIndividual, otherwise False
        """
        raise NotImplementedError()
        # boolean isOWLNamedIndividual();

    def as_owl_named_individual(self):
        """A convenience method that obtains this entity as an
        OWLNamedIndividual

        :return: The entity as an OWLNamedIndividual.
        """
        raise NotImplementedError()
        # OWLNamedIndividual asOWLNamedIndividual();

    def is_owl_datatype(self):
        """A convenience method that determines if this entity is an OWLDatatype

        :return: True if this entity is an OWLDatatype, otherwise False
        """
        raise NotImplementedError()
        # boolean isOWLDatatype();

    def as_owl_datatype(self):
        """A convenience method that obtains this entity as an OWLDatatype

        :return: The entity as an OWLDatatype.
        """
        raise NotImplementedError()
        # OWLDatatype asOWLDatatype();

    def is_owl_annotation_property(self):
        """A convenience method that determines if this entity is an
        OWLAnnotationProperty

        :return: True if this entity is an OWLAnnotationProperty, otherwise
            False
        """
        raise NotImplementedError()
        # boolean isOWLAnnotationProperty();

    def as_owl_annotation_property(self):
        """A convenience method that obtains this entity as an
        OWLAnnotationProperty

        :return: The entity as an OWLAnnotationProperty.
        """
        raise NotImplementedError()
        # OWLAnnotationProperty asOWLAnnotationProperty();

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
        raise NotImplementedError()
        # Set<OWLAxiom> getReferencingAxioms(OWLOntology ontology);
        # Set<OWLAxiom> getReferencingAxioms(OWLOntology ontology, boolean includeImports);
