class HasAddAxioms(object):
    """Marker class"""

    def add_axioms(self, ont, axioms):
        """A convenience method that adds a set of axioms to an ontology. The
        appropriate AddAxiom change objects are automatically generated.

        :param ont: The owlapy.model.OWLOntology object to which the axioms
            should be added.
        :param axioms: The set of owlapy.model.OWLAxiom objects to be added
        :return: A list of ontology changes that represent the changes which
            took place in order to add the axioms.
        """
        raise NotImplementedError()
