#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from scriptgen import StringBuilder, BlockBuilder

from scriptgen.templates.csharp import \
    csharp_autogen, \
    csharp_block, \
    csharp_class, \
    csharp_comment, \
    csharp_constructor, \
    csharp_doc, \
    csharp_for_loop, \
    csharp_foreach_loop, \
    csharp_if, \
    csharp_method, \
    csharp_namespace, \
    csharp_parameters, \
    csharp_region, \
    csharp_switch, \
    csharp_try_catch, \
    csharp_usings


class CSharpTemplateTestCase(TestCase):

    def test_csharp_autogen(self):
        from datetime import datetime
        tolerance = 9
        autogen_str = str(csharp_autogen())
        utcnow_iso = datetime.utcnow().isoformat()
        expected_str = f"""// Auto-generated: {utcnow_iso}
"""
        self.assertEqual(expected_str[:-tolerance], autogen_str[:-tolerance])

    def test_csharp_block(self):
        block_str = str(csharp_block())
        expected_str = """{
}
"""
        self.assertEqual(expected_str, block_str)

    def test_csharp_class(self):
        class_str = str(csharp_class(
            "ClassName",
            access_modifier="public partial",
            base_class_name="BaseClassName",
            interface_names=["IInterface1", "Interface2"]
        ))
        expected_str = """public partial class ClassName : BaseClassName, IInterface1, Interface2
{
}
"""
        self.assertEqual(expected_str, class_str)

    def test_csharp_comment(self):
        comment_str = str(csharp_comment("a", "b"))
        expected_str = """// a
// b
"""
        self.assertEqual(expected_str, comment_str)

    def test_csharp_constructor_no_parameters(self):
        constructor_str = str(csharp_constructor(
            "ClassName",
            access_modifier="public"
        ))
        expected_str = """public ClassName()
{
}
"""
        self.assertEqual(expected_str, constructor_str)

    def test_csharp_constructor_single_parameters(self):
        constructor_str = str(csharp_constructor(
            "ClassName",
            access_modifier="public",
            parameters=["int a"]
        ))
        expected_str = """public ClassName(int a)
{
}
"""
        self.assertEqual(expected_str, constructor_str)

    def test_csharp_constructor_multiple_parameters(self):
        constructor_str = str(csharp_constructor(
            "ClassName",
            access_modifier="public",
            parameters=["int a", "string b"]
        ))
        expected_str = """public ClassName(
    int a,
    string b
)
{
}
"""
        self.assertEqual(expected_str, constructor_str)

    def test_csharp_doc(self):
        doc_str = str(csharp_doc("a", "b"))
        expected_str = """/// <summary>
///     a
///     b
/// </summary>
"""
        self.assertEqual(expected_str, doc_str)

    def test_csharp_for_loop(self):
        for_loop_str = str(csharp_for_loop(
            condition_max="5"
        ))
        expected_str = """for (var i = 0; i < 5; ++i)
{
}
"""
        self.assertEqual(expected_str, for_loop_str)

    def test_csharp_foreach_loop(self):
        foreach_loop_str = str(csharp_foreach_loop(
            enumerable_name="list"
        ))
        expected_str = """foreach (var v in list)
{
}
"""
        self.assertEqual(expected_str, foreach_loop_str)

    def test_csharp_if(self):
        cs_if = csharp_if("true")
        cs_if.wl("int x;")
        if_str = str(cs_if)
        expected_str = """if (true)
{
    int x;
}
"""
        self.assertEqual(expected_str, if_str)

    def test_csharp_method_no_parameters(self):
        cs_method = csharp_method(
            "MethodName",
            access_modifier="public",
            return_type="int"
        )
        cs_method.wl("return 0;")
        method_str = str(cs_method)
        expected_str = """public int MethodName()
{
    return 0;
}
"""
        self.assertEqual(expected_str, method_str)

    def test_csharp_method_single_parameters(self):
        cs_method = csharp_method(
            "MethodName",
            access_modifier="public",
            return_type="int",
            parameters=["int i"]
        )
        cs_method.wl("return i;")
        method_str = str(cs_method)
        expected_str = """public int MethodName(int i)
{
    return i;
}
"""
        self.assertEqual(expected_str, method_str)

    def test_csharp_method_multiple_parameters(self):
        cs_method = csharp_method(
            "MethodName",
            access_modifier="public",
            return_type="int",
            parameters=["int a", "int b"]
        )
        cs_method.wl("return a + b;")
        method_str = str(cs_method)
        expected_str = """public int MethodName(
    int a,
    int b
)
{
    return a + b;
}
"""
        self.assertEqual(expected_str, method_str)

    def test_csharp_namespace(self):
        namespace_str = str(csharp_namespace("NamespaceName"))
        expected_str = """namespace NamespaceName
{
}
"""
        self.assertEqual(expected_str, namespace_str)

    def test_csharp_no_parameters(self):
        parameters_str = str(csharp_parameters([]))
        expected_str = """"""
        self.assertEqual(parameters_str, expected_str)

    def test_csharp_single_parameters(self):
        parameters_str = str(csharp_parameters(["int a"]))
        expected_str = """int a"""
        self.assertEqual(expected_str, parameters_str)

    def test_csharp_multiple_parameters(self):
        parameters_str = str(csharp_parameters(["int a", "int b"]))
        expected_str = """
    int a,
    int b
"""
        self.assertEqual(expected_str, parameters_str)

    def test_csharp_region(self):
        region_str = str(csharp_region("RegionName"))
        expected_str = """#region RegionName


#endregion RegionName
"""
        self.assertEqual(expected_str, region_str)

    def test_csharp_switch(self):
        bb = BlockBuilder()
        bb.wl("x += 3;")
        bb.wl("x *= 2;")
        switch_str = str(csharp_switch(
            "s",
            [
                ("\"hello\"", "x += 1;"),
                ("\"world\"", bb)
            ]
        ))
        expected_str = """switch (s)
{
    case "hello":
        x += 1;
        break;
    case "world":
        x += 3;
        x *= 2;
        break;
}
"""
        self.assertEqual(expected_str, switch_str)

    def test_csharp_switch_with_str_default_case(self):
        bb = BlockBuilder()
        bb.wl("x += 3;")
        bb.wl("x *= 2;")
        switch_str = str(csharp_switch(
            "s",
            [
                ("\"hello\"", "x += 1;"),
                ("\"world\"", bb)
            ],
            "x = 0;"
        ))
        expected_str = """switch (s)
{
    case "hello":
        x += 1;
        break;
    case "world":
        x += 3;
        x *= 2;
        break;
    default:
        x = 0;
        break;
}
"""
        self.assertEqual(expected_str, switch_str)

    def test_csharp_switch_with_block_default_case(self):
        bb = BlockBuilder()
        bb.wl("x += 3;")
        bb.wl("x *= 2;")
        dft_bb = BlockBuilder()
        dft_bb.wl("x = 0;")
        dft_bb.wl("y = 0;")
        switch_str = str(csharp_switch(
            "s",
            [
                ("\"hello\"", "x += 1;"),
                ("\"world\"", bb)
            ],
            dft_bb
        ))
        expected_str = """switch (s)
{
    case "hello":
        x += 1;
        break;
    case "world":
        x += 3;
        x *= 2;
        break;
    default:
        x = 0;
        y = 0;
        break;
}
"""
        self.assertEqual(expected_str, switch_str)

    def test_csharp_try_catch(self):
        cs_tc, cs_try, cs_catch = csharp_try_catch()
        cs_try.wl("// a")
        cs_catch.wl("// b")
        cs_tc_str = str(cs_tc)
        expected_str = """try
{
    // a
}
catch (Exception ex)
{
    // b
}
"""
        self.assertEqual(expected_str, cs_tc_str)

    def test_csharp_usings(self):
        usings_str = str(csharp_usings("System", SysIo="System.IO"))
        expected_str = """using System;
using SysIo = System.IO;
"""
        self.assertEqual(expected_str, usings_str)
