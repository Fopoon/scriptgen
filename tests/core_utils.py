#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from scriptgen import \
    diff_lines, \
    diff_text, \
    interpolate_text


class UtilsTestCase(TestCase):

    def test_diff_lines(self):
        lines_1 = ["a", "b", "c"]
        lines_2 = ["a", "b", "d"]
        diff = diff_lines(lines_1, lines_2)
        self.assertListEqual(["c → d"], diff)

    def test_diff_text(self):
        text_1 = """a
b
c"""
        text_2 = """a
b
d"""
        diff = diff_text(text_1, text_2)
        self.assertListEqual(["c → d"], diff)

    def test_interpolate_text(self):
        text = "Hello World! My name is ${full_name}."
        expressions = {
            "${full_name}": "John Doe"
        }
        interpolated_text = interpolate_text(text, expressions)
        self.assertEqual("Hello World! My name is John Doe.", interpolated_text)
