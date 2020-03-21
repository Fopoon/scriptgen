#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from scriptgen.templates.xml import \
    XmlElementBuilder, \
    xml_autogen, \
    xml_comment, \
    xml_declaration


class XmlTemplateTestCase(TestCase):

    def test_xml_autogen(self):
        from datetime import datetime
        tolerance = 9
        autogen_str = str(xml_autogen())
        utcnow_iso = datetime.utcnow().isoformat()
        expected_str = f"""<!-- Auto-generated: {utcnow_iso} -->
"""
        self.assertEqual(expected_str[:-tolerance], autogen_str[:-tolerance])

    def test_xml_comment(self):
        comment_str = str(xml_comment("a", "b"))
        expected_str = """<!-- a -->
<!-- b -->
"""
        self.assertEqual(expected_str, comment_str)

    def test_xml_declaration(self):
        declaration_str = str(xml_declaration(
            version="2.0",
            encoding="UTF-16"
        ))
        expected_str = """<?xml version="2.0" encoding="UTF-16" ?>
"""
        self.assertEqual(expected_str, declaration_str)

    def test_xml_element_builder_no_attributes_no_content(self):

        element_str = str(XmlElementBuilder(
            "root",
            attributes=None,
            content=None
        ))

        expected_str = """<root />
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_one_attributes_no_content(self):
        element_str = str(XmlElementBuilder(
            "root",
            attributes={
                "attrb": "value"
            },
            content=None
        ))

        expected_str = """<root attrb="value" />
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_many_attributes_no_content(self):
        element_str = str(XmlElementBuilder(
            "root",
            attributes={
                "attrb1": "value",
                "attrb2": "value"
            },
            content=None
        ))

        expected_str = """<root
    attrb1="value"
    attrb2="value" />
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_no_attributes_str_content(self):

        element_str = str(XmlElementBuilder(
            "root",
            attributes=None,
            content="value"
        ))

        expected_str = """<root>value</root>
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_one_attributes_str_content(self):
        element_str = str(XmlElementBuilder(
            "root",
            attributes={
                "attrb": "value"
            },
            content="value"
        ))

        expected_str = """<root attrb="value">value</root>
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_many_attributes_str_content(self):
        element_str = str(XmlElementBuilder(
            "root",
            attributes={
                "attrb1": "value",
                "attrb2": "value"
            },
            content="value"
        ))

        expected_str = """<root
    attrb1="value"
    attrb2="value">
    value
</root>
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_no_attributes_element_content(self):

        element_str = str(XmlElementBuilder(
            "root",
            attributes=None,
            content=[
                XmlElementBuilder("child")
            ]
        ))

        expected_str = """<root>
    <child />
</root>
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_one_attributes_element_content(self):
        element_str = str(XmlElementBuilder(
            "root",
            attributes={
                "attrb": "value"
            },
            content=[
                XmlElementBuilder("child")
            ]
        ))

        expected_str = """<root attrb="value">
    <child />
</root>
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_many_attributes_element_content(self):
        element_str = str(XmlElementBuilder(
            "root",
            attributes={
                "attrb1": "value",
                "attrb2": "value"
            },
            content=[
                XmlElementBuilder("child")
            ]
        ))

        expected_str = """<root
    attrb1="value"
    attrb2="value">
    <child />
</root>
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_no_attributes_elements_content(self):

        element_str = str(XmlElementBuilder(
            "root",
            attributes=None,
            content=[
                XmlElementBuilder("child1"),
                XmlElementBuilder("child2")
            ]
        ))

        expected_str = """<root>
    <child1 />
    <child2 />
</root>
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_one_attributes_elements_content(self):
        element_str = str(XmlElementBuilder(
            "root",
            attributes={
                "attrb": "value"
            },
            content=[
                XmlElementBuilder("child1"),
                XmlElementBuilder("child2")
            ]
        ))

        expected_str = """<root attrb="value">
    <child1 />
    <child2 />
</root>
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_many_attributes_elements_content(self):
        element_str = str(XmlElementBuilder(
            "root",
            attributes={
                "attrb1": "value",
                "attrb2": "value"
            },
            content=[
                XmlElementBuilder("child1"),
                XmlElementBuilder("child2")
            ]
        ))

        expected_str = """<root
    attrb1="value"
    attrb2="value">
    <child1 />
    <child2 />
</root>
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_no_attributes_nested_element_content(self):

        element_str = str(XmlElementBuilder(
            "root",
            attributes=None,
            content=[
                XmlElementBuilder(
                    "child",
                    content=[
                        XmlElementBuilder("grandchild")
                    ]
                )
            ]
        ))

        expected_str = """<root>
    <child>
        <grandchild />
    </child>
</root>
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_one_attributes_nested_element_content(self):
        element_str = str(XmlElementBuilder(
            "root",
            attributes={
                "attrb": "value"
            },
            content=[
                XmlElementBuilder(
                    "child",
                    content=[
                        XmlElementBuilder("grandchild")
                    ]
                )
            ]
        ))

        expected_str = """<root attrb="value">
    <child>
        <grandchild />
    </child>
</root>
"""
        self.assertEqual(expected_str, element_str)

    def test_xml_element_builder_many_attributes_nested_element_content(self):
        element_str = str(XmlElementBuilder(
            "root",
            attributes={
                "attrb1": "value",
                "attrb2": "value"
            },
            content=[
                XmlElementBuilder(
                    "child",
                    content=[
                        XmlElementBuilder("grandchild")
                    ]
                )
            ]
        ))

        expected_str = """<root
    attrb1="value"
    attrb2="value">
    <child>
        <grandchild />
    </child>
</root>
"""
        self.assertEqual(expected_str, element_str)
