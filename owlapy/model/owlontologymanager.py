from .hasaddaxioms import HasAddAxioms
from .hasapplychanges import HasApplyChanges
from .hascontainsontology import HasContainsOntology
from .hasdatafactory import HasDataFactory
from .hasgetontologybyid import HasGetOntologyById
from .owlontologyfactory import OWLOntologyFactory
from .owlontologysetprovider import OWLOntologySetProvider


class OWLOntologyManager(OWLOntologySetProvider, HasDataFactory,
                         HasGetOntologyById, HasApplyChanges, HasAddAxioms,
                         HasContainsOntology,
                         OWLOntologyFactory.OWLOntologyCreationHandler):
    """TODO: implement"""

    def __init__(self, data_factory):
        """
        :param data_factory: an owlapy.model.OWLDataFactory object
        """
        self.owl_data_factory = data_factory

    def get_owl_data_factory(self):
        """Gets a data factory which can be used to create owlapy objects such
        as classes, properties, individuals, axioms etc.

        :return: A reference to an owlapy.model.OWLDataFactory object for
            creating owlapy objects.
        """
        raise NotImplementedError()

    def get_ontologies(self, axiom):
        """Gets the ontologies that are managed by this manager that contain the
        specified axiom.

        :param axiom: An owlapy.model.OWLAxiom object
        :return: The set of owlapy.model.OWLOntology objects such that for each
            ontology, O the specified axiom is contained in O.
        """
        raise NotImplementedError()

    def get_versions(self, ontology):
        """Gets the versions (if any) of the ontology that have the specified
        IRI

        :param ontology: an owlapy.model.IRI object
        :return: The set of owlapy.model.OWLOntology objects that have the
            specified ontology IRI.
        """
        raise NotImplementedError()

    def contains(self, ontology_iri_or_id):
        """Determines if there is an ontology with the specified IRI (and no
        version IRI), or with the specified ID that is managed by this manager

        :param ontology_iri_or_id: The IRI of the ontology to test for (in this
            case the version IRI is assumed to be None) or the ontology's ID
        :return: True if there is an owlapy.model.OWLOntology objcet with the
            specified IRI (and no version IRI) or ontology ID, respectively,
            that is managed by this manager, otherwise False
        """
        # ...rock rock rockaway beach...
        raise NotImplementedError()

    def contains_version(self, ontology_version_iri):
        """Determines if there is an ontology with the specified version IRI,
        that is managed by this manager.

        :param ontology_version_iri: The version IRI of the ontology to test for
            (the ontology IRI may be anything)
        :return: Tue if there is an ontology with the specified version IRI,
            that is managed by this manager, otherwise False
        """
        raise NotImplementedError()

    def get_ontology_ids_by_version(self, ontology_version_iri):
        """Gets a set of owlapy.model.OWLOntologyID objects representing
        ontologies that are managed by this manager.

        :param ontology_version_iri: The owlapy.model.OWLOntologyID object to
            match against all of the known ontologies.
        :return: A set of owlapy.model.OWLOntologyID objects where the version
            matches the given version or the empty set if none match.
        """
        raise NotImplementedError()
