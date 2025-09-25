# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import os
import pathlib
import tempfile
import uuid
from io import BytesIO
from typing import Any

import PIL.Image
import requests

from .utils import _is_package_available


logger = logging.getLogger(__name__)


class AgentType:
    """
    Abstract class to be reimplemented to define types that can be returned by agents.

    These objects serve three purposes:

    - They behave as they were the type they're meant to be, e.g., a string for text, a PIL.Image.Image for images
    - They can be stringified: str(object) in order to return a string defining the object
    - They should be displayed correctly in ipython notebooks/colab/jupyter
    """

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self.to_string()

    def to_raw(self):
        logger.error(
            "This is a raw AgentType of unknown type. Display in notebooks and string conversion will be unreliable"
        )
        return self._value

    def to_string(self) -> str:
        logger.error(
            "This is a raw AgentType of unknown type. Display in notebooks and string conversion will be unreliable"
        )
        return str(self._value)


class AgentText(AgentType, str):
    """
    Text type returned by the agent. Behaves as a string.
    """

    def to_raw(self):
        return self._value

    def to_string(self):
        return str(self._value)

_AGENT_TYPE_MAPPING = {"string": AgentText}


def handle_agent_input_types(*args, **kwargs):
    args = [(arg.to_raw() if isinstance(arg, AgentType) else arg) for arg in args]
    kwargs = {k: (v.to_raw() if isinstance(v, AgentType) else v) for k, v in kwargs.items()}
    return args, kwargs


def handle_agent_output_types(output: Any, output_type: str | None = None) -> Any:
    if output_type in _AGENT_TYPE_MAPPING:
        # If the class has defined outputs, we can map directly according to the class definition
        decoded_outputs = _AGENT_TYPE_MAPPING[output_type](output)
        return decoded_outputs

    # If the class does not have defined output, then we map according to the type
    if isinstance(output, str):
        return AgentText(output)

    return output


__all__ = ["AgentType", "AgentText"]
