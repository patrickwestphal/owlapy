from .hasaddaxioms import HasAddAxioms
from .hasapplychanges import HasApplyChanges
from .hascontainsontology import HasContainsOntology
from .hasdatafactory import HasDataFactory
from .hasgetontologybyid import HasGetOntologyById
from .owlontologysetprovider import OWLOntologySetProvider


class OWLOntologyManager(OWLOntologySetProvider, HasDataFactory,
                         HasGetOntologyById, HasApplyChanges, HasAddAxioms,
                         HasContainsOntology):
    """TODO: implement"""

    def __init__(self, data_factory):
        """
        :param data_factory: an owlapy.model.OWLDataFactory object
        """
        self.owl_data_factory = data_factory
