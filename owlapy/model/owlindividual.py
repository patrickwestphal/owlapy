from .owlobject import OWLObject


class OWLIndividual(OWLObject):
    """Represents a named or anonymous individual."""

    def __cmp__(self, other):
        return isinstance(other, OWLIndividual)
        # TODO: go on here <3>
    
    def is_named(self):
        """Determines if this individual is an instance of
        owlapy.model.OWLNamedIndividual. Note that this method is the dual of
        is_anonymous()
        .
        :return: True if this individual is an instance of
            owlapy.model.OWLNamedIndividual because it is a named individual,
            otherwise False
        """
        raise NotImplementedError()
        # boolean isNamed();

    def is_anomymous(self):
        """Determines if this object is an instance of
        owlapy.model.OWLAnonymousIndividual. Note that

        :return: True if this object represents an anonymous individual
            (owlapy.model.OWLAnomymouseIndividual) or False if this object
            represents a named individual (owlapy.model.OWLNamedIndividual)
        """
        raise  NotImplementedError()
        # boolean isAnonymous();

    def as_owl_named_individual(self):
        """Obtains this individual as a named individual if it is indeed named.

        :return: The individual as a named individual
        """
        raise NotImplementedError()
        # OWLNamedIndividual asOWLNamedIndividual();

    def as_owl_anonymous_individual(self):
        """Obtains this individual an anonymous individual if it is indeed
        anonymous

        :return: The individual as an anonymous individual
        """
        raise NotImplementedError()
        # OWLAnonymousIndividual asOWLAnonymousIndividual();

    def get_types(self, ontologies):
        """A convenience method, which gets the types of this individual, that
        correspond to the types asserted with axioms in the specified ontology.

        :param ontologis: The owlapy.model.OWLOntology object or a set/list of
            owlapy.model.OWLOntology objects that should be examined for class
            assertion axioms in order to get the types for this individual.
        :return: A set of class expressions that correspond the asserted types
            of this individual in the specified ontology.
        """
        raise NotImplementedError()
        # Set<OWLClassExpression> getTypes(OWLOntology ontology);
        # Set<OWLClassExpression> getTypes(Set<OWLOntology> ontologies);

    def get_object_property_values(self, ontology, property=None):
        """Gets the object property values for this individual, or the asserted
        object property values for this individual and the specified property.

        :param ontology: The ontology to search for the property values
        :param property: The property for which values will be returned.
        :return: A map, which maps object properties to sets of individuals in
            case no property was provided, and the set of individuals that are
            the values of the provided property, otherwise. (More precisely,
            the set of individuals such that for each individual i in the set,
            is in a property assertion axiom property(this, i) is in the
            specified ontology.)
        """
        raise NotImplementedError()
        # Map<OWLObjectPropertyExpression, Set<OWLIndividual>> getObjectPropertyValues(OWLOntology ontology);
        # Set<OWLIndividual>                                   getObjectPropertyValues(OWLObjectPropertyExpression property, OWLOntology ontology);

    def has_object_property_value(self, property, individual, ontology):
        """Tests whether a specific value for a specific object property on this
        individual has been asserted.

        :param property: An owlapy.model.OWLObjectPropertyExpression whose
            values will be examined
        :param individual: The individual value (an owlapy.model.OWLIndividual
            object) of the property that will be tested for
        :param ontology: The owlapy.model.OWLOntology object to search for the
            property value
        :return: True if the individual has the specified property value, that
            is, True if the specified ontology contains an object property
            assertion ObjectPropertyAssertion(property, this, individual),
            otherwise False
        """
        raise NotImplementedError()
        # boolean hasObjectPropertyValue(OWLObjectPropertyExpression property,OWLIndividual individual, OWLOntology ontology);

    def has_data_property_value(self, property, value, ontology):
        """Test whether a specific value for a specific data property on this
        individual has been asserted.

        :param property: The owlapy.model.OWLDataPropertyExpression object
            whose values will be examined
        :param value: The owlapy.model.OWLLiteral object representing the value
            of the property that will be tested for
        :param ontology: The owlapy.model.OWLOntology object to search for the
            property value
        :return: True if the individual has the specified property value, that
            is, True if the specified ontology contains a data property
            assertion DataPropertyAssertion(property, this, value), otherwise
            False
        """
        raise NotImplementedError()
        # boolean hasDataPropertyValue(OWLDataPropertyExpression property, OWLLiteral value, OWLOntology ontology);

    def has_negative_object_property_value(self, property, individual, ontology):
        """Test whether a specific value for a specific object property has been
        asserted not to hold for this individual.

        :param property: The owlapy.model.OWLObjectPropertyExpression object to
            test for
        :param individual: The the owlapy.model.OWLIndividual object
            representing the value to test for
        :param ontology: The owlapy.model.OWLOntology to search for the
            assertion
        :return: True if the specified property value has explicitly been
            asserted not to hold, that is, True if the specified ontology
            contains a negative object property assertion
            NegativeObjectPropertyAssertion(property, this, individual),
            otherwise False
        """
        raise NotImplementedError()
        # boolean hasNegativeObjectPropertyValue(OWLObjectPropertyExpression property, OWLIndividual individual,OWLOntology ontology);

    def get_negative_object_property_values(self, ontology):
        """Gets the object property values that are explicitly asserted NOT to
        hold for this individual

        :param ontology: The owlapy.model.OWLOntology that should be examined
            for axioms
        :return: A dictionary containing the negative object property values
        """
        raise NotImplementedError()
        # Map<OWLObjectPropertyExpression, Set<OWLIndividual>> getNegativeObjectPropertyValues(OWLOntology ontology);

    def get_data_property_values(self, ontology, property=None):
        """Gets the values that this individual has for a specific data
        property, and all the data property values for this individual in case
        no property was provided.

        :param ontology: the owlapy.mode.OWLOntology to examine for property
            assertions
        :param property: an owlapy.model.OWLDataPropertyExpression object
        :return: The owlapy.model.OWLLiteral objects representing the values
            that this individual has for the specified property in the specified
            ontology. This is the set of values such that each value LV in the
            set is in an axiom of the form
            DataPropertyAssertion(property, thisIndividual, LV) in the ontology
            specified by the ontology parameter. In case no property is given
            a dictionary of properties and their sets of values is returned.
        """
        raise NotImplementedError()
        # Map<OWLDataPropertyExpression, Set<OWLLiteral>> getDataPropertyValues(OWLOntology ontology);
        # Set<OWLLiteral> getDataPropertyValues(OWLDataPropertyExpression property, OWLOntology ontology);

    def get_negative_data_property_values(self, ontology):
        """Gets the data property values that are explicitly asserted NOT to
        hold for this individual

        :param ontology: The owlapy.model.OWLOntology object that should be
            examined for axioms
        :return: A dictionary containing the negative data property values
        """
        raise NotImplementedError()
        # Map<OWLDataPropertyExpression, Set<OWLLiteral>> getNegativeDataPropertyValues(OWLOntology ontology);

    def has_negative_data_property_value(self, property, literal, ontology):
        """Test whether a specific value for a specific data property has been
        asserted not to hold for this individual.

        :param property: The owlapy.model.OWLDataPropertyExpression object to
            test for
        :param literal: The owlapy.model.OWLLiteral object representing the
            value to test for
        :param ontology: The owlapy.model.OWLOntology to search for the
            assertion
        :return: True if the specified property value has explicitly been
            asserted not to hold, that is, True if the specified ontology
            contains a negative data property assertion
            NegativeDataPropertyAssertion(property, this, literal), otherwise
            False
        """
        raise NotImplementedError()
        # boolean hasNegativeDataPropertyValue(OWLDataPropertyExpression property, OWLLiteral literal, OWLOntology ontology);

    def get_same_individuals(self, ontology):
        """A convenience method that examines axioms in an ontology to determine
            the individuals that are asserted to be the same as this individual.

        :param ontology: the ontology to use
        :return: Individuals (i.e. owlapy.model.OWLIndividual objects) that have
            been asserted to be the same as this individual.
        """
        raise NotImplementedError()
        # Set<OWLIndividual> getSameIndividuals(OWLOntology ontology);

    def get_different_individuals(self, ontology):
        """A convenience method that examines axioms in the specified ontology
        to determine the individuals that are asserted to be different to this
        individual.

        :param ontology: the owlapy.model.OWLOntology to examine
        :return: the set of different individuals (i.e.
            owlapy.model.OWLIndividual)
        """
        raise NotImplementedError()
        # Set<OWLIndividual> getDifferentIndividuals(OWLOntology ontology);


    def accept(self, visitor):
        """
        :param visitor: an owlapy.model.OWLIndividualVisitor object to accept
        :return:
        """
        raise NotImplementedError()
        # void accept(OWLIndividualVisitor visitor);
        # <O> O accept(OWLIndividualVisitorEx<O> visitor);