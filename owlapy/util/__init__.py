def get_annotation_axioms(entity, ontologies):
    """
    :param entity: an owlapy.model.OWLEntity object to look for
    :param ontologies: a list/set of owlapy.model.OWLOntology objects to search
    :return: a set of annotation axioms containing the given entity
    """
    result = set()

    for ontology in ontologies:
        result = result.union(
            ontology.get_annotation_assertion_axioms(entity.iri))

    return result


def get_annotations(entity, ontologies, annotation_property=None):
    """
    :param entity: an owlapy.model.OWLEntity object to look for
    :param ontologies: a list/set of owlapy.model.OWLOntology objects to search
    :param annotation_property: an owlapy.model.OWLAnnotationProperty object to
        match
    :return: a set of annotations of the input entity
    """
    result = set()
    annotation_axioms = get_annotation_axioms(entity, ontologies)

    if annotation_property:
        for axiom in annotation_axioms:
            if axiom.get_annotation().property == annotation_property:
                result.add(axiom.get_annotation)

    else:
        for axiom in annotation_axioms:
            result.add(axiom.get_annotation())

    return result
