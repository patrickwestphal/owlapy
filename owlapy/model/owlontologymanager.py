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

    def get_ontology(self, ontology_id_or_iri):
        """Gets a previously loaded/created ontology that has the specified
        ontology IRI and no version IRI, or the specified ontology ID

        :param ontology_id_or_iri: The owlapy.model.OWLontologyID or
            owlapy.model.IRI of the ontology to be retrieved.
        :return: The ontology that has the specified ontology ID, or IRI and no
            version IRI, or None if this manager does not manage an ontology
            with the specified IRI and no version IRI.
        """
        raise NotImplementedError()

    def get_imported_ontology(self, declaration):
        """Given an imports declaration, obtains the ontology that this import
        has been resolved to.

        :param declaration: The owlapy.model.OWLImportsDeclaration object that
            points to the imported ontology.
        :return: The ontology that the imports declaration resolves to, or None
            if the imports declaration could not be resolved to an ontology,
            because the ontology was not loaded or has been removed from this
            manager
        """
        raise NotImplementedError()

    def get_direct_imports(self, ontology):
        """Gets the set of *loaded* ontologies that the specified ontology is
        related to via the directlyImports relation as defined in Section 3.4 of
        the OWL 2 Structural specification

        :param ontology: The owlapy.model.OWLOntology object whose direct
            imports are to be retrieved.
        :return: The set of *loaded* ontologies that the specified ontology is
            related to via the directlyImports relation. If the ontology is not
            managed by this manager then the empty set will be returned.
        """
        raise NotImplementedError()

    def get_imports(self, ontology):
        """Gets the set of ontologies that are in the transitive closure of the
        directly imports relation.

        :param ontology: The owlapy.model.OWLOntology object whose imports are
            to be retrieved.
        :return: A set of owlapy.model.OWLOntology objects that are in the
            transitive closure of the directly imports relation of this
            ontology. If, for what ever reason, an imported ontology could not
            be loaded, then it will not be contained in the returned set of
            ontologies. If the ontology is not managed by this manager then the
            empty set will be returned.
        """
        raise NotImplementedError()

    def get_imports_closure(self, ontology):
        """Gets the imports closure for the specified ontology.

        :param ontology: The owlapy.model.OWLOntology object whose imports
            closure is to be retrieved.
        :return: A set of owlapy.model.OWLOntology objects that contains the
            imports closure for the specified ontology. This set will also
            include the specified ontology. Example: if A imports B and B
            imports C, then calling this method with A will return the set
            consisting of A, B and C. If, for what ever reason, an imported
            ontology could not be loaded, then it will not be contained in the
            returned set of ontologies. If the ontology is not managed by this
            manager then the empty set will be returned.
        """
        raise NotImplementedError()

    def get_sorted_imports_closure(self, ontology):
        """Gets the topologically ordered imports closure.

        :param ontology: The owlapy.model.OWLOntology object whose imports
            closure is to be determined.
        :return: A list that represents a topological ordering of the imports
            closure. The first element in the list will be the specified
            ontology. If the ontology is not managed by this manager then an
            empty list will be returned.
        """
        raise NotImplementedError()

    def apply_changes(self, changes):
        """Applies a list of changes to some or all of the ontologies that are
        managed by this manager. The changes will be applied to the appropriate
        ontologies.

        :param changes: The changes, i.e. owlapy.model.OWLOntologyChange objects
            to be applied.
        :return: The changes that were actually applied.
        """
        raise NotImplementedError()

    def add_axioms(self, ont, axioms):
        """A convenience method that adds a set of axioms to an ontology. The
        appropriate AddAxiom change objects are automatically generated.

        :param ont: The owlapy.model.OWLOntology object to which the axioms
            should be added.
        :param axioms: The set of owlapy.model.OWLAxiom objects to be added.
        :return: A list of ontology changes that represent the changes which
            took place in order to add the axioms.
        """
        raise NotImplementedError()

    def add_axiom(self, ont, axiom):
        """A convenience method that adds a single axiom to an ontology. The
        appropriate AddAxiom change object is automatically generated.

        :param ont: The owlapy.model.OWLOntology object to add the axiom to.
        :param axiom: The owlapy.model.OWLAxiom object to be added
        :return: A list of ontology changes that represent the changes that
            actually took place.
        """
        raise NotImplementedError()

    def remove_axiom(self, ont, axiom):
        """A convenience method that removes a single axiom from an ontology.
        The appropriate RemoveAxiom change object is automatically generated.

        :param ont: The owlapy.model.OWLOntology object to remove the axiom from
        :param axiom: The owlapy.model.OWLAxiom object to be removed
        :return: A list of ontology changes that represent the changes that
            actually took place.
        """
        raise NotImplementedError()

    def remove_axioms(self, ont, axioms):
        """A convenience method that removes a set of axioms from an ontology.
        The appropriate RemoveAxiom change objects are automatically generated.

        :param ont: The owlapy.model.OWLOntology object from which the axioms
            should be removed.
        :param axioms: A set of owlapy.model.OWLAxiom objects to be removed.
        :return: A list of ontology changes that represent the changes which
            took place in order to remove the axioms.
        """
        raise NotImplementedError()

    def apply_change(self, change):
        """A convenience method that applies just one change to an ontology that
        is managed by this manager.

        :param change: an owlapy.model.OWLOntologyChange object to be applied
        :return: The changes that resulted of the applied ontology change.
        """
        raise NotImplementedError()

    def create_ontology(self, axioms=None, ontology_iri=None):
        """Creates a new ontology that has the specified ontology IRI and is
        initialised to contain specific axioms.

        :param axioms: The set of owlapy.model.OWLAxiom objects that should be
            copied into the new ontology
        :param ontology_iri: The IRI of the new ontology
        :return: An ontology that has the specified IRI and contains all of the
            specified axioms
        """
        # TODO: implement further create_ontology methods
        raise NotImplementedError()

    def load_ontology(self, ontology_iri):
        """Loads an ontology that is assumed to have the specified ontology_iri
        as its IRI or version IRI.
        The ontology IRI will be mapped to an ontology document IRI. The mapping
        will be determined using one of the loaded OWLOntologyIRIMapper objects.
        By default, if no custom owlapy.model.OWLOntologyIRIMapper objects have
        been registered using the add_iri_mapper(OWLOntologyIRIMapper) method,
        or no mapping can be found, the ontology document IRI is taken to be the
        specified ontology IRI.

        :param ontology_iri: an owlapy.model.IRI that identifies the ontology.
            It is expected that the ontology will also have this IRI
        :return: The owlapy.model.OWLOntology object representation of the
            ontology that was loaded.
        """
        raise NotImplementedError()

    def load_ontology_from_ontology_document(
            self, document_iri_or_file_or_document_source, config):
        """Loads an ontology from an ontology document specified by an IRI. In
        contrast the the load_ontology(IRI) method, *no mapping* is performed on
        the specified IRI.

        :param document_iri_or_file_or_document_source: The ontology document
            IRI, or the file, or the owlapy.model.OWLDocumentSource where the
            ontology will be loaded from.
        :param config: an owlapy.model.OWLOntologyLoaderConfiguration object
            to use
        :return: The ontology that was loaded.
        """
        raise NotImplementedError()

    def remove_ontology(self, ontology_or_ontology_id):
        """Attempts to remove an ontology. The ontology which is identified by
        the specified IRI, or the ontology ID is removed regardless of whether
        it is referenced by other ontologies via imports statements.

        :param ontology_or_ontology_id: The ontology to be removed. If this
            manager does not manage the ontology then nothing happens.
        """
        raise NotImplementedError()

    def get_ontology_document_iri(self, ontology):
        """Gets the document IRI for a given ontology. This will either be the
        document IRI from where the ontology was obtained from during loading,
        or the document IRI which was specified (via a mapper) when the (empty)
        ontology was created. Note that this may not correspond to the first
        document IRI found in the list of mappings from ontology IRI to document
        IRI. The reason for this is that it might not have been possible to load
        the ontology from the first document IRI found in the mapping table.

        :param ontology: The owlapy.model.OWLOntology object whose document IRI
            is to be obtained.
        :return: The document IRI of the ontology or None.
        """
        raise NotImplementedError()

    def set_ontology_document_iri(self, ontology, document_iri):
        """Overrides the current document IRI for a given ontology. This method
        does not alter the IRI mappers which are installed, but alters the
        actual document IRI of an ontology that has already been loaded.

        :param ontology: The owlapy.model.OWLOntology object that has already
            been loaded.
        :param document_iri: The owlapy.model.IRI object representing the new
            ontology document IRI
        """
        raise NotImplementedError()

    def get_ontology_format(self, ontology):
        """Gets the ontology format for the specified ontology.

        :param ontology: The owlapy.model.OWLOntology object whose format it to
            be obtained.
        :return: The owlapy.model.OWLOntologyFormat object representing the
            format of the ontology.
        """
        raise NotImplementedError()

    def set_ontology_format(self, ontology, format):
        """Sets the format for the specified ontology.

        :param ontology: The owlapy.model.OWLOntology object whose format is to
            be set.
        :param format: The owlapy.model.OWLOntologyFormat object representing
            the format for the specified ontology.
        """
        raise NotImplementedError()

    def save_ontology(self, ontology, format=None,
                      document_iri_or_file_or_document_target=None):
        """Saves the specified ontology to the specified IRI/file/document
        target in the specified ontology format.

        :param ontology:The owlapy.model.OWLOntology object to be saved
        :param format: The owlapy.model.OWLOntologyFormat object representing
            the format in which to save the ontology
        :param document_iri_or_file_or_document_target: The target where the
            ontology will be saved to. Can be an owlapy.model.IRI, a file, or an
            owlapy.model.OWLOntologyDocumentTarget object
        """
        raise NotImplementedError()

    def add_iri_mapper(self, mapper):
        """Adds a mapper to this manager. The mapper is used to obtain ontology
        document IRIs for ontology IRIs. The mapper will be added so that it is
        given the highest priority (i.e. it will be tried first).

        :param mapper: an owlapy.model.OWLOntologyIRIMapper object
        """
        raise NotImplementedError()

    def remove_iri_mapper(self, mapper):
        """Removes a mapper from this manager.

        :param mapper: an owlapy.model.OWLOntologyIRIMapper object
        """
        raise NotImplementedError()

    def clear_iri_mappers(self):
        """Clears any installed IRI mappers"""
        raise NotImplementedError()

    def add_ontology_factory(self, factory):
        """Adds an ontology factory that is capable of creating an ontology
        given a particular document IRI.

        :param factory: The owlapy.model.OWLOntologyFactory object to be added.
        """
        raise NotImplementedError()

    def remove_ontology_factory(self, factory):
        """Removes a previously added factory.

        :param factory: The owlapy.model.OWLOntologyFactory object to be
            removed.
        """
        raise NotImplementedError()

    def get_ontology_factories(self):
        """Gets the ontology factories that are registered with this manager.

        :return: a set of owlapy.model.OWLOntologyFactory objects
        """
        raise NotImplementedError()

    def add_ontology_storer(self, storer):
        """Add an ontology storer.

        :param storer: The owlapy.model.OWLOntologyStorer object to be added
        """
        raise NotImplementedError()

    def remove_ontology_storer(self, storer):
        """Removes a previously added storer

        :param storer: The owlapy.model.OWLOntologyStorer object to be removed
        :return:
        """
        raise NotImplementedError()

    def add_ontology_change_listener(self, listener, strategy=None):
        """Adds an ontology change listener, which listens to ontology changes.
        An ontology change broadcast strategy can be specified, which
        determines the changes that are broadcast to the listener.

        :param listener: The owlapy.model.OWLOntologyChangeListener object to
            be added.
        :param strategy: The owlapy.model.OWLOntologyChangeBroadcastStrategy
            object that should be used for broadcasting changes to the listener.
        """
        raise NotImplementedError()

    def add_implementing_ontology_change_listener(self, listener):
        """
        :param listener: The owlapy.model.ImpendingOWLOntologyChangeListener
            object to add
        """
        raise NotImplementedError()

    def remove_implementing_ontology_change_listener(self, listener):
        """
        :param listener: The owlapy.model.ImpendingOWLOntologyChangeListener
            object to remove
        """
        raise NotImplementedError()

    def add_ontology_changes_vetoed_listener(self, listener):
        """
        :param listener: The owlapy.model.OWLOntologyChangesVetoedListener
            object to be added
        """
        raise NotImplementedError()

    def remove_ontology_changes_vetoed_listener(self, listener):
        """
        :param listener: The owlapy.model.OWLOntologyChangesVetoedListener
            object to remove
        """
        raise NotImplementedError()

    def set_default_change_broadcast_strategy(self, strategy):
        """Sets the default strategy that is used to broadcast ontology changes.

        :param strategy: The owlapy.model.OWLOntologyChangeBroadcastStrategy
            objcet representing the strategy to be used for broadcasting
            changes. This strategy will override any previously set broadcast
            strategy. The strategy should not be None.
        """
        raise NotImplementedError()

    def remove_ontology_change_listener(self, listener):
        """Removes a previously added listener.

        :param listener: The owlapy.model.OWLOntologyChangeListener object to be
            removed
        """
        raise NotImplementedError()

    def make_load_import_request(self, declaration, configuration):
        """Requests that the manager loads an imported ontology that is
        described by an imports statement. This method is generally used by
        parsers and other kinds of loaders. For simply loading an ontology, use
        the loadOntologyXXX methods. The method respects the list of ignored
        imports in the specified configuration. In other words, if this methods
        is called for an ignored import as specified by the configuration
        object then the import won't be loaded.

        :param declaration: The owlapy.model.OWLImportsDeclaration that
            describes the import to be loaded.
        :param configuration: The owlapy.model.OWLOntologyLoaderConfiguration
            object that passes arguments to the mechanism used for loading.
        """
        raise NotImplementedError()

    def add_missing_import_listener(self, listener):
        """In the case where silent missing imports handling is enabled, a
        listener can be attached via this method so that there is a mechanism
        that allows clients to be informed of the reason when an import cannot
        be loaded.

        :param listener: The owlapy.model.MissingImportListener object to be
            added.
        """
        raise NotImplementedError()

    def remove_missing_import_listener(self, listener):
        """Removes a previously added missing import listener.

        :param listener: The owlapy.model.MissingImportListener object to be
            removed.
        """
        raise NotImplementedError()

    def add_ontology_loader_listener(self, listener):
        """Adds an ontology loaded listener to this manager.

        :param listener: The owlapy.model.OWLOntologyLoaderListener object to be
            added.
        """
        raise NotImplementedError()

    def remove_ontology_loader_listener(self, listener):
        """Removes a previously added ontology loaded listener.

        :param listener: The owlapy.model.OWLOntologyLoaderListener object to be
            removed.
        """
        raise NotImplementedError()

    def add_ontology_change_progress_listener(self, listener):
        """Adds an ontology change progress listener.

        :param listener: The owlapy.model.OWLOntologyChangeProgressListener
            object to be added.
        """
        raise NotImplementedError()

    def remove_ontology_change_progress_listener(self, listener):
        """Removes a previously added ontology change listener.

        :param listener: The owlapy.model.OWLOntologyChangeProgressListener
            object to be removed.
        """
        raise NotImplementedError()
