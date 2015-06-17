class OWLOntologyManagerProperties(object):

    def __init__(self):
        self.restore_defaults()

    def restore_defaults(self):
        self.load_annotation_axioms = True
        self.treat_dublin_core_vocabulary_as_built_in_vocabulary = True
