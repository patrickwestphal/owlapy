

escape = {
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp;',
    '"': '&quot;',
    '\'': '&apos;'
}

OWL_PROCESSING_INSTRUCTION_NAME = 'owl'


def is_xml_name_start_character(code_point):
    """Determines if a character is an XML name start character.

    http://www.w3.org/TR/REC-xml/:
    NameStartChar ::=   ":" | [A-Z] | "_" | [a-z] | [#xC0-#xD6] | [#xD8-#xF6]
        | [#xF8-#x2FF] | [#x370-#x37D] | [#x37F-#x1FFF] | [#x200C-#x200D]
        | [#x2070-#x218F] | [#x2C00-#x2FEF] | [#x3001-#xD7FF] | [#xF900-#xFDCF]
        | [#xFDF0-#xFFFD] | [#x10000-#xEFFFF]

    :param code_point: The code point or string representation of the
        character to be tested. For UTF-16 characters the code point
        corresponds to the value of the char  that represents the character.
    :return: boolean indicating whether the input is an XML name start
        character
    """
    if isinstance(code_point, str):
        code_point = ord(code_point)

    return code_point == ord(':') or \
        ord('A') <= code_point <= ord('Z') or \
        code_point == ord('_') or \
        ord('a') <= code_point <= ord('z') or \
        0xC0 <= code_point <= 0xD6 or \
        0xD8 <= code_point <= 0xF6 or \
        0xD8 <= code_point <= 0xF6 or \
        0xF8 <= code_point <= 0x2FF or \
        0x370 <= code_point <= 0x37D or \
        0x37F <= code_point <= 0x1FFF or \
        0x200C <= code_point <= 0x200D or \
        0x2070 <= code_point <= 0x218F or \
        0x2C00 <= code_point <= 0x2FEF or \
        0x3001 <= code_point <= 0xD7FF or \
        0xF900 <= code_point <= 0xFDCF or \
        0xFDF0 <= code_point <= 0xFFFD or \
        0x10000 <= code_point <= 0xEFFFF


def is_xml_name_char(code_point):
    """Determines if a character is an XML name character.

    http://www.w3.org/TR/REC-xml/:
    NameChar ::= NameStartChar | "-" | "." | [0-9] | #xB7 | [#x0300-#x036F]
        | [#x203F-#x2040]

    :param code_point: The code point or string representation of the
        character to be tested. For UTF-8 and UTF-16 characters the code point
        corresponds to the value of the char that represents the character.
    :return: boolean indicating whether the input is an XML name character
    """
    if isinstance(code_point, str):
        code_point = ord(code_point)

    return is_xml_name_start_character(code_point) or \
        code_point == ord('-') or \
        code_point == ord('.') or \
        0x30 <= code_point <= 0x39 or \
        code_point == 0xB7 or \
        0x300 <= code_point <= 0x36F or \
        0x203F <= code_point <= 0x2040


def is_nc_name_start_char(code_point):
    """Determines if a character is an NCName (Non-Colonised Name) start
    character.


    :param code_point: The code point or string representation of the character
        to be tested. For UTF-8 and UTF-16 characters the code point
        corresponds to the value of the char that represents the character.
    :return: boolean indicating whether the input is a NCName start character
    """
    if isinstance(code_point, str):
        code_point = ord(code_point)

    return code_point != ord(':') and is_xml_name_start_character(code_point)


def is_nc_name_char(code_point):
    """Determines if a character is an NCName (Non-Colonised Name) character.

    :param code_point: The code point or string representation of the character
        to be tested. For UTF-8 and UTF-16 characters the code point
        corresponds to the value of the char that represents the character.
    :return: boolean indicating whether is a NCName character
    """
    if isinstance(code_point, str):
        code_point = ord(code_point)

    return code_point != ord(':') and is_xml_name_char(code_point)


def is_nc_name(s):
    """Determines if a string is an NCName (Non-Colonised Name). A
    NCName is a string which starts with an NCName start character and is
    followed by zero or more NCName characters.

    :param s: The string to be tested.
    :return: boolean determining whether an input string is an NCName
    """
    if not s:
        return False

    if not is_nc_name_start_char(s[0]):
        return False

    for char in s[1:]:
        if not is_nc_name_char(char):
            return False

    return True


def is_qname(s):
    """Determines if a string is a QName. A QName is either an NCName
    (LocalName), or an NCName followed by a colon followed by another NCName
    (where the first NCName is referred to as the 'Prefix Name' and the second
    NCName is referred to as the 'Local Name' - i.e. PrefixName:LocalName).

    :param s: The string to be tested
    :return: a boolean indicating whether the input is a QName
    """
    if not s:
        return False

    found_colon = False
    in_nc_name = False

    for char in s:
        if char == ':':
            if found_colon:  # found second colon --> invalid
                return False

            found_colon = True

            if not in_nc_name:
                # since qnames must have a prefix and must not start with colon
                return False

            # reset since second part after colon will be considered
            in_nc_name = False

        else:  # char is not ':'
            if not in_nc_name:  # reading first char
                if not is_xml_name_start_character(char):
                    return False

                # read first char --> are now *in* string under test
                in_nc_name = True

            else:  # first char already read
                if not is_xml_name_char(char):
                    # found invalid char inside string under test
                    return False

    if found_colon and not in_nc_name:  # e.g. foo:
        return False

    return True


def has_nc_name_suffix(s):
    """Determines if a string has a suffix that is an NCName.

    :param s: The string to be tested
    :return: boolean indicating whether the input has a NCName suffix
    """
    return get_nc_name_suffix_index(s) != -1


def get_nc_name_suffix_index(s):
    """Gets the index of the longest NCName that is the suffix of a character
    sequence.

    :param s: The string to be tested
    :return: The index of the longest suffix of the input string that is an
        NCName, or -1 if the input string does not have a suffix that is an
        NCName.
    """
    # return -1 in case of bNodes or None input
    if (s is None) or (s and s.startswith('_:')):
        return -1

    idx = -1
    i = len(s) - 1

    while i > -1:
        char = s[i]
        if is_nc_name_start_char(char):
            print('%s: %s' % (char, is_nc_name_start_char(char)))
            idx = i

        if not is_nc_name_char(char):
            break

        i -= 1

    return idx


def get_nc_name_suffix(s):
    """Get the longest NCName that is a suffix of a string.

    :param s: The input string.
    :return: The string which is the longest suffix of the input string that
        is an NCName, or None if the input string does not have a suffix that
        is an NCName.
    """
    if s and s.startswith('_:'):  # in case s is a blank node identifier
        return None

    local_part_start_idx = get_nc_name_suffix_index(s)

    if local_part_start_idx > -1:
        return s[local_part_start_idx:]
    else:
        return None


def get_nc_name_prefix(s):
    """Utility to get the part of a string that is not the NCName fragment.

    :param s: The input string
    :return: the prefix split at the last non-NCName character, or the whole
        input if no NCName is found
    """
    if s and s.startswith('_:'):  # in case s is a blank node identifier
        return s

    local_part_start_idx = get_nc_name_suffix_index(s)

    if local_part_start_idx > -1:
        return s[0:local_part_start_idx]

    else:
        return s


def escape_xml(s):
    """Escapes a string so that it is valid XML.

    :param s: The input string
    :return: The escaped version of the input string
    """
    if s is None:
        return None

    escaped_s = ''

    for char in s:
        escaped_s += escape.get(char, char)

    return escaped_s
