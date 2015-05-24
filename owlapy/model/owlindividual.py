from .owlpropertyassertionobject import OWLPropertyAssertionObject


class OWLIndividual(OWLPropertyAssertionObject):
    """Represents a named or anonymous individual."""

    def __eq__(self, other):
        return isinstance(other, OWLIndividual)

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
        raise NotImplementedError()

    def is_anonymous(self):
        """Determines if this object is an instance of
        owlapy.model.OWLAnonymousIndividual. Note that

        :return: True if this object represents an anonymous individual
            (owlapy.model.OWLAnomymouseIndividual) or False if this object
            represents a named individual (owlapy.model.OWLNamedIndividual)
        """
        raise NotImplementedError()

    def as_owl_named_individual(self):
        """Obtains this individual as a named individual if it is indeed named.

        :return: The individual as a named individual
        """
        raise NotImplementedError()

    def as_owl_anonymous_individual(self):
        """Obtains this individual an anonymous individual if it is indeed
        anonymous

        :return: The individual as an anonymous individual
        """
        raise NotImplementedError()

    def get_types(self, ontologies):
        """A convenience method, which gets the types of this individual, that
        correspond to the types asserted with axioms in the specified ontology.

        :param ontologies: The owlapy.model.OWLOntology object or a set/list of
            owlapy.model.OWLOntology objects that should be examined for class
            assertion axioms in order to get the types for this individual.
        :return: A set of class expressions that correspond the asserted types
            of this individual in the specified ontology.
        """
        result = set()

        # in case a single ontology is given, it will be wrapped in a list
        if not hasattr(ontologies, '__iter__'):
            ontologies = [ontologies]

        for ontology in ontologies:
            for axiom in ontology.get_class_assertion_axioms(self):
                result.add(axiom.get_class_expression())

        return result

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
        if property:
            result = {}  # OWLObjectPropertyExpression: set<OWLIndividual>>

            for axiom in ontology.get_object_property_assertion_axioms(self):
                inds = result.get(axiom.property)

                if inds is None:
                    inds = set()
                    result[axiom.property] = inds

                inds.add(axiom.object)

        else:  # no property given
            # OWLObjectPropertyExpression: set<OWLIndividual>
            map = self.get_object_property_values(ontology)
            vals = map.get(property)  # set<OWLIndividual>
            result = set() if vals is None else vals

        return result

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
        for axiom in ontology.get_object_property_assertion_axioms(self):
            if axiom.property == property and axiom.object == individual:
                return True

        return False

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
        for axiom in ontology.get_data_property_assertion_axioms(self):
            if axiom.property == property and axiom.object == value:
                return True

        return False

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
        for ax in ontology.get_negative_object_property_assertion_axioms(self):
            if ax.property == property and ax.object == individual:
                return True

        return False

    def get_negative_object_property_values(self, ontology):
        """Gets the object property values that are explicitly asserted NOT to
        hold for this individual

        :param ontology: The owlapy.model.OWLOntology that should be examined
            for axioms
        :return: A dictionary containing the negative object property values
        """
        result = {}  # OWLObjectPropertyExpression: set<OWLIndividual>

        for ax in ontology.get_negative_object_property_assertion_axioms(self):
            inds = result.get(ax.property)

            if inds is None:
                inds = set()
                result[ax.property] = inds
            inds.add(ax.object)

        return result

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
        if property:
            result = set()  # set<OWLLiteral>

            for axiom in ontology.get_data_property_assertion_axioms(self):
                if axiom.property == property:
                    result.add(axiom.object)

        else:
            result = {}  # OWLDataPropertyExpression: set<OWLLiteral>

            for axiom in ontology.get_data_property_assertion_axioms(self):
                vals = result.get(axiom.property)  # set<OWLLiteral>

                if vals is None:
                    vals = set()
                    result[axiom.property] = vals
                vals.add(axiom.object)

        return result

    def get_negative_data_property_values(self, ontology):
        """Gets the data property values that are explicitly asserted NOT to
        hold for this individual

        :param ontology: The owlapy.model.OWLOntology object that should be
            examined for axioms
        :return: A dictionary containing the negative data property values
        """
        result = {}  # OWLDataPropertyExpression: set<OWLLiteral>

        for axiom in ontology.get_negative_data_property_assertion_axioms(self):
            inds = result.get(axiom.property)

            if inds is None:
                inds = set()
                result[axiom.property] = inds

            inds.add(axiom.object)

        return result

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
        for axiom in ontology.get_negative_data_property_assertion_axioms(self):
            if axiom.property == property and axiom.object == literal:
                return True

        return False

    def get_same_individuals(self, ontology):
        """A convenience method that examines axioms in an ontology to determine
            the individuals that are asserted to be the same as this individual.

        :param ontology: the ontology to use
        :return: Individuals (i.e. owlapy.model.OWLIndividual objects) that have
            been asserted to be the same as this individual.
        """
        result = set()  # set<OWLIndividual>

        for axiom in ontology.get_same_individual_axioms(self):
            result = result.union(axiom.get_individuals())

        result.remove(self)
        return result

    def get_different_individuals(self, ontology):
        """A convenience method that examines axioms in the specified ontology
        to determine the individuals that are asserted to be different to this
        individual.

        :param ontology: the owlapy.model.OWLOntology to examine
        :return: the set of different individuals (i.e.
            owlapy.model.OWLIndividual)
        """
        result = set()  # set<OWLIndividual>
        for axiom in ontology.get_different_individual_axioms(self):
            result = result.union(axiom.get_individuals())

        result.remove(self)
        return result

    def accept(self, visitor):
        """
        :param visitor: an owlapy.model.OWLIndividualVisitor object to accept
        """
        raise NotImplementedError()