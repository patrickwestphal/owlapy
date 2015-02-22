import os
import re

from urllib import parse as p

from rdflib import URIRef

from owlapy.io import xmlutils
from owlapy.vocab import Namespaces


class IRI(object):
    # TODO: make immutable? (if, then fix length and hash)
    # TODO: path normalization (i.e. /foo/../bar --> /bar)

    # taken from http://developer.classpath.org/doc/java/net/URI-source.html
    _iri_regex = '^(([^:/?#]+):)?((//([^/?#]*))?([^?#]*)(\\?([^#]*))?)?(#(.*))?'
    # Index of scheme component in parsed IRI
    _m_scheme_idx = 2
    # Index of scheme-specific-part in parsed IRI
    _m_scheme_specific_idx = 3
    # Index of authority component in parsed IRI
    _m_auth_idx = 5
    # Index of path component in parsed IRI
    _m_path_idx = 6
    # Index of query component in parsed IRI
    _m_query_idx = 8
    # Index of fragment component in parsed IRI
    _m_fragment_idx = 10

    # TODO: add IRI validation
    def __init__(self, iri_str_or_uri, fragment=None):
        """Constructs an IRI which is built from the concatenation of the
        specified prefix and suffix.

        :param iri_str_or_uri: a string containing the IRI prefix or the whole
            iri identifier or an rdflib.URIRef object
        :param fragment: an optional string containing the local part a.k.a.
            remainder a.k.a. fragment a.k.a. suffix of the IRI
        """
        if isinstance(iri_str_or_uri, URIRef):
            iri_str_or_uri = str(iri_str_or_uri)
        if not fragment:
            self.prefix = xmlutils.get_nc_name_prefix(iri_str_or_uri)
            self.remainder = xmlutils.get_nc_name_suffix(iri_str_or_uri)
        else:
            self.prefix = iri_str_or_uri
            self.remainder = fragment

        self.namespace = self.prefix

    @property
    def _iri_str(self):
        if self.remainder is None:
            return self.prefix
        else:
            return self.prefix + self.remainder

    def __len__(self):
        prefix_len = 0 if self.prefix is None else len(self.prefix)
        suffix_len = 0 if self.remainder is None else len(self.remainder)

        return prefix_len + suffix_len

    def __getitem__(self, item):
        if isinstance(item, slice):
            res = ''
            start = item.start if item.start is not None else 0
            stop = item.stop if item.stop is not None else len(self)
            step = item.step if item.step is not None else 1

            for i in range(start, stop, step):
                res += self[i]

            return res
        else:
            while item < 0:
                item += len(self)
            prefix_len = len(self.prefix)
            if item < prefix_len:
                return self.prefix[item]
            else:
                return self.remainder[item-prefix_len]

    def __eq__(self, other):
        if not isinstance(other, IRI):
            return False

        self_iri_str = self._iri_str
        other_iri_str = other._iri_str

        return self_iri_str == other_iri_str

    def __str__(self):
        return self._iri_str

    def __repr__(self):
        return self._iri_str

    def __hash__(self):
        return hash(self.prefix + self.remainder)

    def to_uri(self):
        """Obtains this IRI as a rdflib URI.

        :return: an rdflib.URIRef object
        """
        return URIRef(self._iri_str)

    def is_absolute(self):
        """Determines if this IRI is absolute

        :return: boolean indicating whether this IRI is absolute
        """
        colon_index = self.prefix.find(':')

        if colon_index == -1:
            return False

        for i in range(colon_index):
            char = self.prefix[i]

            if not char.isalnum() and char not in ['.', '+', '-']:
                return False

        return True

    def get_scheme(self):
        """Returns the scheme part of this IRI, so e.g. http, https, ftp ...

        :return: the IRI scheme, e.g., http, urn...
        """
        colon_index = self.prefix.find(':')

        if colon_index == -1:
            return None

        return self.prefix[:colon_index]

    def resolve(self, s):
        """Resolves the given IRI identifier string against this IRI

        :param s: the IRI string to be resolved
        :return: an IRI object resolved against this IRI unless this IRI is
            opaque
        """
        if not s:
            return IRI(self._iri_str)

        if not self.is_absolute():
            return IRI(s)

        s_iri = IRI(s)
        s_parts = IRI._parse_iri_str(s)
        self_parts = IRI._parse_iri_str(self._iri_str)

        # test if s is an opaque IRI string, i.e. whether
        # - the scheme part is not empty/None and
        # - the scheme-specific part does not start with a '/'
        # (see http://developer.classpath.org/doc/java/net/URI-source.html)
        s_is_opaque = False
        if s_parts['scheme'] and not s_parts['scheme_specific'].startswith('/'):
            s_is_opaque = True

        if s_iri.is_absolute() or s_is_opaque:
            return s_iri

        # if (fragment != null && path != null && path.equals("") &&
        #       scheme == null && authority == null && query == null)
        #   return new URI(this.scheme, this.schemeSpecificPart, fragment);
        if s_parts['fragment'] is not None and \
                s_parts['path'] == '' and s_parts['scheme'] is None and \
                s_parts['auth'] is None and s_parts['query'] is None:

            iri_str = '%s:%s#%s' % (self_parts['scheme'],
                                    self_parts['scheme_specific'],
                                    s_parts['fragment'])
            return IRI(iri_str)

        if s_parts['auth'] is None:
            s_parts['auth'] = self_parts['auth']

            if not s_parts['path']:
                s_parts['path'] = self_parts['path']

            elif not s_parts['path'].startswith('/'):
                self_path = self_parts['path'][:]
                self_last_slash_idx = self_path.rfind('/')

                if self_last_slash_idx >= 0:
                    self_path = self_path[:self_last_slash_idx]

                # 1) strip off all leading dot paths
                while s_parts['path'].startswith('../') or \
                        s_parts['path'].startswith('./'):
                    # strip of leading dots (../) in s path and adjust self
                    # path accordingly
                    while s_parts['path'].startswith('../'):
                        self_last_slash_idx = self_path.rfind('/')

                        if self_last_slash_idx >= 0:
                            self_path = self_path[:self_last_slash_idx]

                        s_parts['path'] = s_parts['path'][3:]

                    # strip off single leading dot (./) in s path
                    while s_parts['path'].startswith('./'):
                        s_parts['path'] = s_parts['path'][2:]

                # 2) check if the remainder is only dots
                if s_parts['path'] == '..':
                    s_parts['path'] = ''

                    self_last_slash_idx = self_path.rfind('/')

                    if self_last_slash_idx >= 0:
                        self_path = self_path[:self_last_slash_idx]

                if s_parts['path'] == '.':
                    s_parts['path'] = ''

                s_parts['path'] = self_path + '/' + s_parts['path']

        iri_str = '%s://%s%s' % (self_parts['scheme'], s_parts['auth'],
                                 s_parts['path'])
        if s_parts['query'] is not None:
            iri_str += '?' + s_parts['query']

        if s_parts['fragment'] is not None:
            iri_str += '#' + s_parts['fragment']
        return IRI(iri_str)

    @classmethod
    def _parse_iri_str(cls, s):
        """Parses an IRI string and separates it into its parts, i.e. scheme,
        authority, path, ...

        :return:
        """
        m = re.search(cls._iri_regex, s)

        return {
            'scheme': m.group(cls._m_scheme_idx),
            'scheme_specific': m.group(cls._m_scheme_specific_idx),
            'auth': m.group(cls._m_auth_idx),
            'path': m.group(cls._m_path_idx),
            'query': m.group(cls._m_query_idx),
            'fragment': m.group(cls._m_fragment_idx)
        }

    def is_reserved_vocabulary(self):
        """Determines if this IRI is in the reserved vocabulary. An IRI is in
        the reserved vocabulary if it starts with
        - <http://www.w3.org/1999/02/22-rdf-syntax-ns#> or
        - <http://www.w3.org/2000/01/rdf-schema#> or
        - <http://www.w3.org/2001/XMLSchema#> or
        - <http://www.w3.org/2002/07/owl#>

        :return: boolean indicating whether the IRI is in the reserved
            vocabulary
        """
        return Namespaces.OWL.in_namespace(self.prefix) or \
            Namespaces.RDF.in_namespace(self.prefix) or \
            Namespaces.RDFS.in_namespace(self.prefix) or \
            Namespaces.XSD.in_namespace(self.prefix)

    def is_thing(self):
        """Determines if this IRI is equal to owl:Thing

        :return: boolean indicating whether this IRI is equal to
            <http://www.w3.org/2002/07/owl#Thing>
        """
        return self.remainder is not None and self.remainder == 'Thing' and \
            Namespaces.OWL.in_namespace(self.prefix)

    def is_nothing(self):
        """Determines if this IRI is equal to owl:Nothing

        :return: boolean indicating whether this IRI is equal to
            <http://www.w3.org/2002/07/owl#Nothing>
        """
        return self.remainder is not None and self.remainder == 'Nothing' and \
            Namespaces.OWL.in_namespace(self.prefix)

    def is_plain_literal(self):
        """Determines if this IRI is equal to rdf:PlainLiteral

        :return: boolean indicating whether this IRI is equal to
            <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral>
        """
        return self.remainder == 'PlainLiteral' and \
            Namespaces.RDF.in_namespace(self.prefix)

    def to_quoted_string(self):
        """:return: This IRI surrounded by angled brackets"""
        return '<%s>' % self._iri_str

    @classmethod
    def create(cls, iri_or_file_or_uri, suffix=None):
        """Creates an IRI from the specified string, file, URI or URL

        :param iri_or_file_or_uri: an IRI string representing the IRI
            prefix or the whole IRI, or a file, or a URI

        :param suffix: in case the first argument is a string, this argument is
            interpreted as IRI suffix and the first one as IRI prefix
        :return: an IRI object
        """
        if isinstance(iri_or_file_or_uri, str) and \
                not isinstance(iri_or_file_or_uri, URIRef):
            if suffix:
                # first argument is interpreted as prefix, second argument as
                # suffix
                return IRI(iri_or_file_or_uri, suffix)

        elif hasattr(iri_or_file_or_uri, 'read') and \
                hasattr(iri_or_file_or_uri, 'name'):
            # it's file like
            path = iri_or_file_or_uri.name.split(os.path.sep)
            quoted_path = []

            for sub_path in path:
                quoted_path.append(p.quote_plus(sub_path))

            file_name = 'file://' + os.path.sep.join(quoted_path)
            return IRI(file_name)

        # works in case of iri string and URIRef
        return IRI(iri_or_file_or_uri)

    def generate_document_iri(self):
        """TODO: comment

        :return: TODO
        """
        # public static IRI generateDocumentIRI() {
        raise NotImplementedError()

    def prefixed_by(self, prefix):
        """TODO: comment

        :param prefix: TODO
        :return: TODO
        """
        # public String prefixedBy(String prefix) {
        raise NotImplementedError()

    def get_short_form(self):
        """TODO: comment

        :return: TODO
        """
        # public String getShortForm() {
        raise NotImplementedError()

    def accept(self, visitor):
        """TODO: comment

        :param visitor:
        :return:
        """
        # public void accept(OWLObjectVisitor visitor) {
        # public <O> O accept(OWLObjectVisitorEx<O> visitor) {
        # public void accept(OWLAnnotationSubjectVisitor visitor) {
        # public <E> E accept(OWLAnnotationSubjectVisitorEx<E> visitor) {
        # public void accept(OWLAnnotationValueVisitor visitor) {
        # public <O> O accept(OWLAnnotationValueVisitorEx<O> visitor) {
        # from interfaces:
        # void accept(OWLAnnotationValueVisitor visitor);
        # <O> O accept(OWLAnnotationValueVisitorEx<O> visitor);
        # void accept(OWLAnnotationSubjectVisitor visitor);
        # <O> O accept(OWLAnnotationSubjectVisitorEx<O> visitor);
        raise NotImplementedError()

    def get_data_properties_in_signature(self):
        """TODO: comment

        :return: TODO
        """
        # public Set<OWLDataProperty> getDataPropertiesInSignature() {
        raise NotImplementedError()

    def get_individuals_in_signature(self):
        """TODO: comment

        :return: TODO
        """
        # public Set<OWLNamedIndividual> getIndividualsInSignature() {
        raise NotImplementedError()

    def get_object_properties_in_signature(self):
        """TODO: comment

        :return: TODO
        """
        # public Set<OWLObjectProperty> getObjectPropertiesInSignature() {
        raise NotImplementedError()

    def get_signature(self):
        """TODO: comment

        :return: TODO
        """
        # public Set<OWLEntity> getSignature() {
        raise NotImplementedError()

    def contains_entity_in_signature(self):
        """TODO: comment

        :return: TODO
        """
        # public boolean containsEntityInSignature(OWLEntity owlEntity) {
        raise NotImplementedError()

    def get_anonymous_individuals(self):
        """TODO: comment

        :return: TODO
        """
        # public Set<OWLAnonymousIndividual> getAnonymousIndividuals() {
        raise NotImplementedError()

    def get_datatypes_in_signature(self):
        """TODO: comment

        :return: TODO
        """
        # public Set<OWLDatatype> getDatatypesInSignature() {
        raise NotImplementedError()

    def get_nested_class_expressions(self):
        """TODO: comment

        :return: TODO
        """
        # public Set<OWLClassExpression> getNestedClassExpressions() {
        raise NotImplementedError()

    def is_top_entity(self):
        """TODO: comment

        :return: TODO
        """
        # public boolean isTopEntity() {
        raise NotImplementedError()

    def is_bottom_entity(self):
        """TODO: comment

        :return: TODO
        """
        # public boolean isBottomEntity() {
        raise NotImplementedError()
