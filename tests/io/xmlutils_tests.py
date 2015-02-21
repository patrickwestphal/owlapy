import unittest

from owlapy.io.xmlutils import *


class TestXMLUtils(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # <is_xml_name_start_character tests> -------------------------------------
    # NameStartChar ::= ":" ...
    def test_is_xml_name_start_character_01(self):
        self.assertTrue(is_xml_name_start_character(':'))
        self.assertTrue(is_xml_name_start_character(ord(':')))

    # ... | [A-Z] ...
    def test_is_xml_name_start_character_02(self):
        self.assertTrue(is_xml_name_start_character('A'))
        self.assertTrue(is_xml_name_start_character(ord('A')))
        self.assertTrue(is_xml_name_start_character('G'))
        self.assertTrue(is_xml_name_start_character(ord('G')))
        self.assertTrue(is_xml_name_start_character('P'))
        self.assertTrue(is_xml_name_start_character(ord('P')))
        self.assertTrue(is_xml_name_start_character('Z'))
        self.assertTrue(is_xml_name_start_character(ord('Z')))

    # ... | "_" ...
    def test_is_xml_name_start_character_03(self):
        self.assertTrue(is_xml_name_start_character('_'))
        self.assertTrue(is_xml_name_start_character(ord('_')))

    # ... | [a-z] ...
    def test_is_xml_name_start_character_04(self):
        self.assertTrue(is_xml_name_start_character('a'))
        self.assertTrue(is_xml_name_start_character(ord('a')))
        self.assertTrue(is_xml_name_start_character('g'))
        self.assertTrue(is_xml_name_start_character(ord('g')))
        self.assertTrue(is_xml_name_start_character('p'))
        self.assertTrue(is_xml_name_start_character(ord('p')))
        self.assertTrue(is_xml_name_start_character('z'))
        self.assertTrue(is_xml_name_start_character(ord('z')))

    # ... | [#xC0-#xD6] ...
    def test_is_xml_name_start_character_05(self):
        self.assertTrue(is_xml_name_start_character('\u00c0'))
        self.assertTrue(is_xml_name_start_character(0xC0))
        self.assertTrue(is_xml_name_start_character('\u00cf'))
        self.assertTrue(is_xml_name_start_character(0xCF))
        self.assertTrue(is_xml_name_start_character('\u00d0'))
        self.assertTrue(is_xml_name_start_character(0xD0))
        self.assertTrue(is_xml_name_start_character('\u00d6'))
        self.assertTrue(is_xml_name_start_character(0xD6))

    # ... | [#xD8-#xF6] ...
    def test_is_xml_name_start_character_06(self):
        self.assertTrue(is_xml_name_start_character('\u00d8'))
        self.assertTrue(is_xml_name_start_character(0xD8))
        self.assertTrue(is_xml_name_start_character('\u00df'))
        self.assertTrue(is_xml_name_start_character(0xDF))
        self.assertTrue(is_xml_name_start_character('\u00f6'))
        self.assertTrue(is_xml_name_start_character(0xF6))

    # ... | [#xF8-#x2FF] ...
    def test_is_xml_name_start_character_07(self):
        self.assertTrue(is_xml_name_start_character('\u00f8'))
        self.assertTrue(is_xml_name_start_character(0xF8))
        self.assertTrue(is_xml_name_start_character('\u01ff'))
        self.assertTrue(is_xml_name_start_character(0x1FF))
        self.assertTrue(is_xml_name_start_character('\u02f6'))
        self.assertTrue(is_xml_name_start_character(0x2F6))
        self.assertTrue(is_xml_name_start_character('\u02ff'))
        self.assertTrue(is_xml_name_start_character(0x2FF))

    # ... | [#x370-#x37D] ...
    def test_is_xml_name_start_character_08(self):
        self.assertTrue(is_xml_name_start_character('\u0370'))
        self.assertTrue(is_xml_name_start_character(0x370))
        self.assertTrue(is_xml_name_start_character('\u0377'))
        self.assertTrue(is_xml_name_start_character(0x377))
        self.assertTrue(is_xml_name_start_character('\u0370'))
        self.assertTrue(is_xml_name_start_character(0x370))

    # ... | [#x37F-#x1FFF] ...
    def test_is_xml_name_start_character_09(self):
        self.assertTrue(is_xml_name_start_character('\u037F'))
        self.assertTrue(is_xml_name_start_character(0x37F))
        self.assertTrue(is_xml_name_start_character('\u0577'))
        self.assertTrue(is_xml_name_start_character(0x577))
        self.assertTrue(is_xml_name_start_character('\u0890'))
        self.assertTrue(is_xml_name_start_character(0x890))
        self.assertTrue(is_xml_name_start_character('\u1FFF'))
        self.assertTrue(is_xml_name_start_character(0x1FFF))

    # ... | [#x200C-#x200D] ...
    def test_is_xml_name_start_character_10(self):
        self.assertTrue(is_xml_name_start_character('\u200c'))
        self.assertTrue(is_xml_name_start_character(0x200C))
        self.assertTrue(is_xml_name_start_character('\u200d'))
        self.assertTrue(is_xml_name_start_character(0x200D))

    # ... | [#x2070-#x218F] ...
    def test_is_xml_name_start_character_11(self):
        self.assertTrue(is_xml_name_start_character('\u2070'))
        self.assertTrue(is_xml_name_start_character(0x2070))
        self.assertTrue(is_xml_name_start_character('\u2100'))
        self.assertTrue(is_xml_name_start_character(0x2100))
        self.assertTrue(is_xml_name_start_character('\u218f'))
        self.assertTrue(is_xml_name_start_character(0x218F))

    # ... | [#x2C00-#x2FEF] ...
    def test_is_xml_name_start_character_12(self):
        self.assertTrue(is_xml_name_start_character('\u2c00'))
        self.assertTrue(is_xml_name_start_character(0x2C00))
        self.assertTrue(is_xml_name_start_character('\u2d00'))
        self.assertTrue(is_xml_name_start_character(0x2D00))
        self.assertTrue(is_xml_name_start_character('\u2e00'))
        self.assertTrue(is_xml_name_start_character(0x2e00))
        self.assertTrue(is_xml_name_start_character('\u2fef'))
        self.assertTrue(is_xml_name_start_character(0x2FEF))

    # ... | [#x3001-#xD7FF] ...
    def test_is_xml_name_start_character_13(self):
        self.assertTrue(is_xml_name_start_character('\u3001'))
        self.assertTrue(is_xml_name_start_character(0x3001))
        self.assertTrue(is_xml_name_start_character('\u4444'))
        self.assertTrue(is_xml_name_start_character(0x4444))
        self.assertTrue(is_xml_name_start_character('\u8888'))
        self.assertTrue(is_xml_name_start_character(0x8888))
        self.assertTrue(is_xml_name_start_character('\ud7ff'))
        self.assertTrue(is_xml_name_start_character(0xD7FF))

    # ... | [#xF900-#xFDCF] ...
    def test_is_xml_name_start_character_14(self):
        self.assertTrue(is_xml_name_start_character('\uf900'))
        self.assertTrue(is_xml_name_start_character(0xF900))
        self.assertTrue(is_xml_name_start_character('\ufafa'))
        self.assertTrue(is_xml_name_start_character(0xFAFA))
        self.assertTrue(is_xml_name_start_character('\ufdcf'))
        self.assertTrue(is_xml_name_start_character(0xFDCF))

    # ... | [#xFDF0-#xFFFD] ...
    def test_is_xml_name_start_character_15(self):
        self.assertTrue(is_xml_name_start_character('\ufdf0'))
        self.assertTrue(is_xml_name_start_character(0xFDF0))
        self.assertTrue(is_xml_name_start_character('\ufefe'))
        self.assertTrue(is_xml_name_start_character(0xFEFE))
        self.assertTrue(is_xml_name_start_character('\ufffd'))
        self.assertTrue(is_xml_name_start_character(0xFFFD))

    # ... | [#x10000-#xEFFFF]
    def test_is_xml_name_start_character_16(self):
        self.assertTrue(is_xml_name_start_character('\U00010000'))
        self.assertTrue(is_xml_name_start_character(0x10000))
        self.assertTrue(is_xml_name_start_character('\U0007ffff'))
        self.assertTrue(is_xml_name_start_character(0x7FFFF))
        self.assertTrue(is_xml_name_start_character('\U000effff'))
        self.assertTrue(is_xml_name_start_character(0xEFFFF))
    # </is_xml_name_start_character tests> ------------------------------------

    # <is_xml_name_char tests> ------------------------------------------------
    # NameChar ::= NameStartChar ...
    def test_is_xml_name_char_01(self):
        self.assertTrue(is_xml_name_char('_'))
        self.assertTrue(is_xml_name_char(ord('_')))
        self.assertTrue(is_xml_name_char('\u2100'))
        self.assertTrue(is_xml_name_char(0x2100))
        self.assertTrue(is_xml_name_char('\ufdcf'))
        self.assertTrue(is_xml_name_char(0xFDCF))
        self.assertTrue(is_xml_name_char('\U000effff'))
        self.assertTrue(is_xml_name_char(0xEFFFF))

    # ... | "-" ...
    def test_is_xml_name_char_02(self):
        self.assertTrue(is_xml_name_char('-'))
        self.assertTrue(is_xml_name_char(ord('-')))

    # ... | "." ...
    def test_is_xml_name_char_03(self):
        self.assertTrue(is_xml_name_char('.'))
        self.assertTrue(is_xml_name_char(ord('.')))

    # ... | [0-9] ...
    def test_is_xml_name_char_04(self):
        self.assertTrue(is_xml_name_char('0'))
        self.assertTrue(is_xml_name_char(0x30))
        self.assertTrue(is_xml_name_char('1'))
        self.assertTrue(is_xml_name_char(0x31))
        self.assertTrue(is_xml_name_char('3'))
        self.assertTrue(is_xml_name_char(0x33))
        self.assertTrue(is_xml_name_char('5'))
        self.assertTrue(is_xml_name_char(0x35))
        self.assertTrue(is_xml_name_char('7'))
        self.assertTrue(is_xml_name_char(0x37))
        self.assertTrue(is_xml_name_char('9'))
        self.assertTrue(is_xml_name_char(0x39))

    # ... | #xB7 ...
    def test_is_xml_name_char_05(self):
        self.assertTrue(is_xml_name_char('\u00b7'))
        self.assertTrue(is_xml_name_char(0xB7))

    # ... | [#x0300-#x036F] ...
    def test_is_xml_name_char_06(self):
        self.assertTrue(is_xml_name_char('\u0300'))
        self.assertTrue(is_xml_name_char(0x300))
        self.assertTrue(is_xml_name_char('\u0333'))
        self.assertTrue(is_xml_name_char(0x333))
        self.assertTrue(is_xml_name_char('\u036f'))
        self.assertTrue(is_xml_name_char(0x36F))

    # ... | [#x203F-#x2040]
    def test_is_xml_name_char_07(self):
        self.assertTrue(is_xml_name_char('\u203f'))
        self.assertTrue(is_xml_name_char(0x203F))
        self.assertTrue(is_xml_name_char('\u2040'))
        self.assertTrue(is_xml_name_char(0x2040))
    # </is_xml_name_char tests> -----------------------------------------------

    # <is_nc_name_start_char tests> -------------------------------------------
    def test_is_nc_name_start_char(self):
        self.assertFalse(is_nc_name_start_char(':'))
        self.assertFalse(is_nc_name_start_char(ord(':')))
        self.assertTrue(is_nc_name_start_char('\u0377'))
        self.assertTrue(is_nc_name_start_char(0x377))
        self.assertTrue(is_nc_name_start_char('\u4444'))
        self.assertTrue(is_nc_name_start_char(0x4444))
    # <is_nc_name_start_char tests> -------------------------------------------

    # <is_nc_name_char tests> -------------------------------------------------
    def test_is_nc_name_char(self):
        self.assertFalse(is_nc_name_char(':'))
        self.assertFalse(is_nc_name_char(ord(':')))
        self.assertTrue(is_nc_name_char('5'))
        self.assertTrue(is_nc_name_char(0x35))
        self.assertTrue(is_nc_name_char('\u203f'))
        self.assertTrue(is_nc_name_char(0x203F))
    # </is_nc_name_char tests> ------------------------------------------------

    # <is_nc_name tests> ------------------------------------------------------
    # None input
    def test_is_nc_name_01(self):
        self.assertFalse(is_nc_name(None))

    # empty string input
    def test_is_nc_name_02(self):
        self.assertFalse(is_nc_name(''))

    # single char not being nc start char
    def test_is_nc_name_03(self):
        self.assertFalse(is_nc_name('6'))

    # single char being nc start char
    def test_is_nc_name_04(self):
        self.assertTrue(is_nc_name('a'))
        self.assertTrue(is_nc_name('_'))

    # string with invalid start char
    def test_is_nc_name_05(self):
        self.assertFalse(is_nc_name('2invalid'))

    # string containing invalid non-start char
    def test_is_nc_name_06(self):
        self.assertFalse(is_nc_name('abc<34'))

    # valid strings
    def test_is_nc_name_07(self):
        self.assertTrue(is_nc_name('abcdef'))
        self.assertTrue(is_nc_name('_abcdef'))
        self.assertTrue(is_nc_name('_abc123'))
    # <is_nc_name tests> ------------------------------------------------------

    # <is_qname tests> --------------------------------------------------------
    # non-colonised/invalid: None
    def test_is_qname_01(self):
        self.assertFalse(is_qname(None))

    # non-colonised/invalid: empty string
    def test_is_qname_02(self):
        self.assertFalse('')

    # non-colonised/invalid: single char not being valid start char
    def test_is_qname_03(self):
        self.assertFalse(is_qname('5'))

    # non-colonised/valid: single char being valid start char
    def test_is_qname_04(self):
        self.assertTrue(is_qname('a'))

    # non-colonised/invalid: str with invalid char inside
    def test_is_qname_05(self):
        self.assertFalse(is_qname('i<3lin'))

    # non-colonised/valid: valid str
    def test_is_qname_06(self):
        self.assertTrue(is_qname('abc234'))
        self.assertTrue(is_qname('_abc234'))

    # colonised/invalid: single colon (empty prefix and empty local part)
    def test_is_qname_07(self):
        self.assertFalse(is_qname(':'))

    # colonised/invalid: empty prefix
    def test_is_qname_08(self):
        self.assertFalse(is_qname(':a'))

    # colonised/invalid: empty local part
    def test_is_qname_09(self):
        self.assertFalse(is_qname('a:'))

    # colonised/invalid: str with invalid start char in prefix
    def test_is_qname_10(self):
        self.assertFalse(is_qname('5foo:bar'))

    # colonised/invalid: str with invalid start char in local part
    def test_is_qname_11(self):
        self.assertFalse(is_qname('foo:5bar'))

    # colonised/invalid: str with invalid char inside prefix
    def test_is_qname_12(self):
        self.assertFalse(is_qname('fo<o:bar'))

    # colonised/invalid: str with invalid char inside local part
    def test_is_qname_13(self):
        self.assertFalse(is_qname('foo:b<ar'))

    # # colonised/valid: valid str
    def test_is_qname_14(self):
        self.assertTrue(is_qname('foo:bar'))
    # </is_qname tests> -------------------------------------------------------

    # <has_nc_name_suffix tests> ----------------------------------------------
    # no: no nc name at all
    def test_has_nc_name_suffix_01(self):
        self.assertFalse(has_nc_name_suffix('<<<<<>>>>'))

    # yes: input is nc name
    def test_has_nc_name_suffix_02(self):
        self.assertTrue(has_nc_name_suffix('foo'))

    # no: <prefix> <nc_name> <suffix>
    def test_has_nc_name_suffix_03(self):
        self.assertFalse(has_nc_name_suffix('foo:bar>>>'))

    # yes: <prefix> <nc_name>
    def test_has_nc_name_suffix_04(self):
        self.assertTrue(has_nc_name_suffix('foo:bar'))
    # </has_nc_name_suffix tests> ---------------------------------------------

    # <get_nc_name_suffix_index tests> ----------------------------------------
    # -1: does not contain an nc name at all
    def test_get_nc_name_suffix_index_01(self):
        self.assertEqual(-1, get_nc_name_suffix_index('<<<>>>>'))

    # -1: blank node
    def test_get_nc_name_suffix_index_02(self):
        self.assertEqual(-1, get_nc_name_suffix_index('_:2356'))

    # 0: input is nc name
    def test_get_nc_name_suffix_index_03(self):
        self.assertEqual(0, get_nc_name_suffix_index('foo'))

    # -1: <prefix> <nc_name> <suffix>
    def test_get_nc_name_suffix_index_04(self):
        self.assertEqual(-1, get_nc_name_suffix_index('foo:bar>>>'))

    # >0: <prefix> <nc_name>
    def test_get_nc_name_suffix_index_05(self):
        prefix = 'foo:'
        self.assertEqual(len(prefix), get_nc_name_suffix_index(prefix + 'bar'))
    # </get_nc_name_suffix_index tests> ---------------------------------------

    # <get_nc_name_suffix tests> ----------------------------------------------
    # input is None
    def test_get_nc_name_suffix_01(self):
        self.assertIsNone(get_nc_name_suffix(None))

    # input is empty string
    def test_get_nc_name_suffix_02(self):
        self.assertIsNone(get_nc_name_suffix(''))

    # input is blank node
    def test_get_nc_name_suffix_03(self):
        self.assertIsNone(get_nc_name_suffix('_:2345'))

    # input has no nc name suffix (<non_nc_name>)
    def test_get_nc_name_suffix_04(self):
        self.assertIsNone(get_nc_name_suffix('<<<<<<>>>>>'))

    # input has no nc name suffix (<prefix> <nc_name> <non_nc_name_suffix>)
    def test_get_nc_name_suffix_05(self):
        self.assertIsNone(get_nc_name_suffix('foo:bar>>>'))

    # input is nc name
    def test_get_nc_name_suffix_06(self):
        s = 'foo'
        self.assertEqual(s, get_nc_name_suffix(s))

    # input has nc name suffix
    def test_get_nc_name_suffix_07(self):
        s = 'bar'
        self.assertEqual(s, get_nc_name_suffix('foo:' + s))
    # </get_nc_name_suffix tests> ---------------------------------------------

    # <get_nc_name_prefix tests> ----------------------------------------------
    # input is None
    def test_get_nc_name_prefix_01(self):
        s = None
        self.assertEqual(s, get_nc_name_prefix(s))

    # input is empty string
    def test_get_nc_name_prefix_02(self):
        s = ''
        self.assertEqual(s, get_nc_name_prefix(s))

    # input is blank node identifier
    def test_get_nc_name_prefix_03(self):
        s = '_:2345'
        self.assertEqual(s, get_nc_name_prefix(s))

    # input has empty prefix
    def test_get_nc_name_prefix_04(self):
        self.assertEqual('', get_nc_name_prefix('foo'))

    # input has non-empty prefix
    def test_get_nc_name_prefix_05(self):
        prefix = 'foo:'
        self.assertEqual(prefix, get_nc_name_prefix(prefix + 'bar'))
    # </get_nc_name_prefix tests> ---------------------------------------------

    # <escape_xml tests> ------------------------------------------------------
    # input is None
    def test_escape_xml_01(self):
        s = None
        self.assertEqual(s, escape_xml(s))

    # input is empty
    def test_escape_xml_02(self):
        s = ''
        self.assertEqual(s, escape_xml(s))

    # input contains '<'
    def test_escape_xml_03(self):
        s = '123 < 456'
        escaped_s = '123 &lt; 456'
        self.assertEqual(escaped_s, escape_xml(s))

    # input contains '>'
    def test_escape_xml_04(self):
        s = '456 >> 12'
        escaped_s = '456 &gt;&gt; 12'
        self.assertEqual(escaped_s, escape_xml(s))

    # input contains '&'
    def test_escape_xml_05(self):
        s = 'foo & bar'
        escaped_s = 'foo &amp; bar'
        self.assertEqual(escaped_s, escape_xml(s))

    # input contains '"'
    def test_escape_xml_06(self):
        s = 'foo "bar"'
        escaped_s = 'foo &quot;bar&quot;'
        self.assertEqual(escaped_s, escape_xml(s))

    # input contains "'"
    def test_escape_xml_07(self):
        s = 'foo\'s bar'
        escaped_s = 'foo&apos;s bar'
        self.assertEqual(escaped_s, escape_xml(s))

    # input contains no char to be escaped
    def test_escape_xml_08(self):
        s = 'nothing to escape here'
        self.assertEqual(s, escape_xml(s))
    # </escape_xml tests> -----------------------------------------------------
