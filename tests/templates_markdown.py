#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from scriptgen.templates.markdown import \
    markdown_autogen, \
    markdown_code_block, \
    markdown_comment, \
    markdown_inline


class MarkdownTemplateTestCase(TestCase):

    def test_markdown_autogen(self):
        from datetime import datetime
        tolerance = 9
        autogen_str = str(markdown_autogen())
        utcnow_iso = datetime.utcnow().isoformat()
        expected_str = f"""
[//]: # (Auto-generated: {utcnow_iso})

"""
        self.assertEqual(expected_str.strip()[:-tolerance], autogen_str.strip()[:-tolerance])

    def test_markdown_code_block(self):
        md_code_block = markdown_code_block(
            language="python"
        )
        md_code_block.wl("import os")
        md_code_block.nl()
        md_code_block.wl('print("Hello World!")')
        code_block_str = str(md_code_block)
        expected_str = """```python
import os

print("Hello World!")
```
"""
        self.assertEqual(expected_str, code_block_str)

    def test_csharp_comment(self):
        comment_str = str(markdown_comment("a", "b"))
        expected_str = """
[//]: # (a)
[//]: # (b)

"""
        self.assertEqual(expected_str, comment_str)

    def test_markdown_inline(self):
        inline_str = markdown_inline("lorem", "*")
        expected_str = "*lorem*"
        self.assertEqual(expected_str, inline_str)
