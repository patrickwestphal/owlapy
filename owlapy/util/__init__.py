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


def str_compare_to(str1, str2):
    len1 = 0 if str1 is None else len(str1)
    len2 = 0 if str2 is None else len(str2)

    lim = min(len1, len2)

    for i in range(lim):
        char1 = str1[i]
        char2 = str2[i]

        if not char1 == char2:
            return ord(char1) - ord(char2)

    return len1 - len2


def accept_default(obj, visitor):
    visitor.visit(obj)


def accept_default_ex(obj, visitor):
    return visitor.visit(obj)
