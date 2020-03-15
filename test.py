#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from unittest import TestLoader, TextTestRunner

import tests


def set_logger_level(level):
    from funity import __name__ as module_name
    logging.basicConfig()
    logging.getLogger(module_name).setLevel(level)


if __name__ == '__main__':

    set_logger_level(logging.INFO)

    loader = TestLoader()
    suite = loader.loadTestsFromModule(tests)
    test_runner = TextTestRunner()
    test_runner.run(suite)
