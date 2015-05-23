from .iri import IRI
from .owlobjectproperty import OWLObjectProperty


class OWLDataFactory(object):
    """TODO: implement"""

    def __init__(self, cache=True, use_compression=False):
        # TODO: implement
        pass

    def get_owl_object_property(self, foo):
        """FIXME: this is just a dummy"""
        return OWLObjectProperty(IRI('http://ex.org/justADummyProp'))