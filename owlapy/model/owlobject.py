from owlapy.vocab.owlrdfvocabulary import OWLRDFVocabulary
import owlapy.model


class OWLObject(object):
    NO_ANNOTATIONS = set()

    def __init__(self):
        self.OWL_THING = owlapy.model.OWLClass(OWLRDFVocabulary.OWL_THING.iri)
        self._hash_code = 0
        self._signature = None  # set<OWLEntity>
        self._anons = None

    @classmethod
    def get_owl_entity(cls, entity_type, iri):
        """
        :param entity_type: an owlapy.model.EntityType object
        :param iri: an owlapy.model.IRI object
        :return: a new object based on the IRI and a class determined by the
            entity type
        """
        if entity_type == owlapy.model.EntityType.CLASS:
            return owlapy.model.OWLClass(iri)

        elif entity_type == owlapy.model.EntityType.OBJECT_PROPERTY:
            return owlapy.model.OWLObjectProperty(iri)

        elif entity_type == owlapy.model.EntityType.DATA_PROPERTY:
            return owlapy.model.OWLDataProperty(iri)

        elif entity_type == owlapy.model.EntityType.ANNOTATION_PROPERTY:
            return owlapy.model.OWLAnnotationProperty(iri)

        elif entity_type == owlapy.model.EntityType.NAMED_INDIVIDUAL:
            return owlapy.model.OWLNamedIndividual(iri)

        elif entity_type == owlapy.model.EntityType.DATATYPE:
            return owlapy.model.OWLDatatype(iri)

        else:
            return None

    def get_signature(self):
        """Gets the signature of this object

        :return: A set of owlapy.model.OWLEntity objects that correspond to the
            signature of this object. The set is a copy,
            changes are not reflected back.
        """
        entity_set = None

        if self._signature is not None:
            entity_set = self._signature.copy()

        if entity_set is None:
            entity_set = set()  # set<OWLEntity>
            anon = set()  # set<OWLAnonymousIndividual>
            # XXX stopped here
 
        # TODO: return copy!!!
        raise NotImplementedError()

    def get_anonymous_individuals(self):
        """Gets the anonymous individuals occurring in this object. The set is
        a copy, changes are not reflected back.

        :return: A set of anonymous individuals (i.e.
            owlapy.model.OWLAnonymousIndividual objects)
        """
        # TODO: return copy!
        raise NotImplementedError()
        # Set<OWLAnonymousIndividual> getAnonymousIndividuals();

    def get_classes_in_signature(self):
        raise NotImplementedError()
        # Set<OWLClass> getClassesInSignature();

    def get_data_properties_in_signature(self):
        raise NotImplementedError
        # Set<OWLDataProperty> getDataPropertiesInSignature();

    def get_object_properties_in_signature(self):
        raise NotImplementedError()
        # Set<OWLObjectProperty> getObjectPropertiesInSignature();

    def get_individuals_in_signature(self):
        raise NotImplementedError()
        # Set<OWLNamedIndividual> getIndividualsInSignature();

    def get_datatypes_in_signature(self):
        raise NotImplementedError()
        # Set<OWLDatatype> getDatatypesInSignature();

    def get_nested_class_expression(self):
        raise NotImplementedError()
        # Set<OWLClassExpression> getNestedClassExpressions();

    def accept(self, visitor):
        raise NotImplementedError()
        # void accept(OWLObjectVisitor visitor);
        # <O> O accept(OWLObjectVisitorEx<O> visitor);

    def is_top_entity(self):
        raise NotImplementedError()
        # boolean isTopEntity();

    def is_bottom_entity(self):
        raise NotImplementedError()
        # boolean isBottomEntity();

        # TODO: add additional methods from Comparable<OWLObject>, Serializable,
        #   HasSignature, HasContainsEntityInSignature, HasAnonymousIndividuals,
        #   HasClassesInSignature, HasObjectPropertiesInSignature,
        #   HasDataPropertiesInSignature, HasIndividualsInSignature,
        #   HasDatatypesInSignature