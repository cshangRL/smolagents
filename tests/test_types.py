# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#

import os
import tempfile
import unittest
import uuid

from smolagents.agent_types import AgentText

from .utils.markers import require_soundfile, require_torch


def get_new_path(suffix="") -> str:
    directory = tempfile.mkdtemp()
    return os.path.join(directory, str(uuid.uuid4()) + suffix)


class AgentTextTests(unittest.TestCase):
    def test_from_string(self):
        string = "Hey!"
        agent_type = AgentText(string)

        self.assertEqual(string, agent_type.to_string())
        self.assertEqual(string, agent_type.to_raw())
