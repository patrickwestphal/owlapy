import unittest
from owlapy.model.entitytype import EntityType
from owlapy.model.iri import IRI


class TestEntityTypes(unittest.TestCase):
    def test___init__(self):
        self.assertEqual('Class', EntityType.CLASS.name_)
        self.assertEqual('Class', EntityType.CLASS.short_form)
        self.assertEqual('Class', EntityType.CLASS.print_name)
        self.assertEqual('Classes', EntityType.CLASS.plural_print_name)
        class_iri = IRI('http://www.w3.org/2002/07/owl#Class')
        self.assertEqual(class_iri, EntityType.CLASS.iri)

        self.assertEqual('ObjectProperty', EntityType.OBJECT_PROPERTY.name_)
        self.assertEqual('ObjectProperty',
                         EntityType.OBJECT_PROPERTY.short_form)
        self.assertEqual('Object property',
                         EntityType.OBJECT_PROPERTY.print_name)
        self.assertEqual('Object properties',
                         EntityType.OBJECT_PROPERTY.plural_print_name)
        class_iri = IRI('http://www.w3.org/2002/07/owl#ObjectProperty')
        self.assertEqual(class_iri, EntityType.OBJECT_PROPERTY.iri)

        self.assertEqual('AnnotationProperty',
                         EntityType.ANNOTATION_PROPERTY.name_)
        self.assertEqual('AnnotationProperty',
                         EntityType.ANNOTATION_PROPERTY.short_form)
        self.assertEqual('Annotation property',
                         EntityType.ANNOTATION_PROPERTY.print_name)
        self.assertEqual('Annotation properties',
                         EntityType.ANNOTATION_PROPERTY.plural_print_name)
        class_iri = IRI('http://www.w3.org/2002/07/owl#AnnotationProperty')
        self.assertEqual(class_iri, EntityType.ANNOTATION_PROPERTY.iri)

        self.assertEqual('NamedIndividual', EntityType.NAMED_INDIVIDUAL.name_)
        self.assertEqual('NamedIndividual',
                         EntityType.NAMED_INDIVIDUAL.short_form)
        self.assertEqual('Named individual',
                         EntityType.NAMED_INDIVIDUAL.print_name)
        self.assertEqual('Named individuals',
                         EntityType.NAMED_INDIVIDUAL.plural_print_name)
        class_iri = IRI('http://www.w3.org/2002/07/owl#NamedIndividual')
        self.assertEqual(class_iri, EntityType.NAMED_INDIVIDUAL.iri)

        self.assertEqual('Datatype', EntityType.DATATYPE.name_)
        self.assertEqual('Datatype', EntityType.DATATYPE.short_form)
        self.assertEqual('Datatype', EntityType.DATATYPE.print_name)
        self.assertEqual('Datatypes', EntityType.DATATYPE.plural_print_name)
        class_iri = IRI('http://www.w3.org/2000/01/rdf-schema#Datatype')
        self.assertEqual(class_iri, EntityType.DATATYPE.iri)

    def test___str__(self):
        self.assertEqual('Datatype',
                         str(EntityType.DATATYPE))

    def test_prefixed_name_class(self):
        self.assertEqual(EntityType.CLASS.prefixed_name, 'owl:Class')

    def test_prefixed_name_obj_property(self):
        self.assertEqual(EntityType.OBJECT_PROPERTY.prefixed_name,
                         'owl:ObjectProperty')

    def test_prefixed_name_data_property(self):
        self.assertEqual(EntityType.DATA_PROPERTY.prefixed_name,
                         'owl:DatatypeProperty')

    def test_prefixed_name_annotation_property(self):
        self.assertEqual(EntityType.ANNOTATION_PROPERTY.prefixed_name,
                         'owl:AnnotationProperty')

    def test_prefixed_name_named_individual(self):
        self.assertEqual(EntityType.NAMED_INDIVIDUAL.prefixed_name,
                         'owl:NamedIndividual')

    def test_prefixed_name_datatype(self):
        self.assertEqual(EntityType.DATATYPE.prefixed_name, 'rdfs:Datatype')

    def test_iri_class(self):
        self.assertEqual(EntityType.CLASS.iri,
                         IRI('http://www.w3.org/2002/07/owl#Class'))

    def test_iri_obj_property(self):
        self.assertEqual(EntityType.OBJECT_PROPERTY.iri,
                         IRI('http://www.w3.org/2002/07/owl#ObjectProperty'))

    def test_iri_data_property(self):
        self.assertEqual(EntityType.DATA_PROPERTY.iri,
                         IRI('http://www.w3.org/2002/07/owl#DatatypeProperty'))

    def test_iri_annotation_property(self):
        self.assertEqual(EntityType.ANNOTATION_PROPERTY.iri,
                         IRI('http://www.w3.org/2002/07/owl#AnnotationProperty'))

    def test_iri_named_individual(self):
        self.assertEqual(EntityType.NAMED_INDIVIDUAL.iri,
                         IRI('http://www.w3.org/2002/07/owl#NamedIndividual'))

    def test_iri_datatype(self):
        self.assertEqual(EntityType.DATATYPE.iri,
                         IRI('http://www.w3.org/2000/01/rdf-schema#Datatype'))

    def test_values(self):
        self.assertIn(EntityType.CLASS, EntityType.values)
        self.assertIn(EntityType.OBJECT_PROPERTY, EntityType.values)
        self.assertIn(EntityType.DATA_PROPERTY, EntityType.values)
        self.assertIn(EntityType.ANNOTATION_PROPERTY, EntityType.values)
        self.assertIn(EntityType.NAMED_INDIVIDUAL, EntityType.values)
        self.assertIn(EntityType.DATATYPE, EntityType.values)
