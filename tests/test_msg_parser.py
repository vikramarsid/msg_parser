#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tests for `msg_parser` package."""
import os
import unittest

from msg_parser.cli import create_parser
from msg_parser.msg_parser import MsOxMessage

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
TEST_FILES = os.path.join(SCRIPT_PATH, "files")

TEST_NESTED_MSG = os.path.join(TEST_FILES, "outer.msg")
TEST_ATTACHED_EML = os.path.join(TEST_FILES, "other.msg")
TEST_COMPLETE_MSG = os.path.join(TEST_FILES, "complete.msg")


class TextMessageParsing(unittest.TestCase):

    def test_command_line_interface(self):
        """Test the CLI."""
        parsed = create_parser(
            ['-i', TEST_COMPLETE_MSG,
             '--json'])
        self.assertTrue(parsed.json_output)

    def test_msg_parsing_1(self):
        ms_msg = MsOxMessage(TEST_COMPLETE_MSG)
        self.assertTrue(ms_msg.get_properties())

    def test_msg_parsing_2(self):
        ms_msg = MsOxMessage(TEST_ATTACHED_EML)
        self.assertTrue(ms_msg.get_properties())

    def test_msg_parsing_3(self):
        ms_msg = MsOxMessage(TEST_NESTED_MSG)
        self.assertTrue(ms_msg.get_properties())

    def test_json_output(self):
        ms_msg = MsOxMessage(TEST_COMPLETE_MSG)
        self.assertTrue(ms_msg.get_message_as_json())

    def test_save_as_eml_1(self):
        ms_msg = MsOxMessage(TEST_COMPLETE_MSG)
        self.assertTrue(ms_msg.save_email_file(TEST_FILES))

    def test_save_as_eml_2(self):
        ms_msg = MsOxMessage(TEST_ATTACHED_EML)
        self.assertTrue(ms_msg.save_email_file(TEST_FILES))

    def test_save_as_eml_3(self):
        ms_msg = MsOxMessage(TEST_NESTED_MSG)
        self.assertTrue(ms_msg.save_email_file(TEST_FILES))
