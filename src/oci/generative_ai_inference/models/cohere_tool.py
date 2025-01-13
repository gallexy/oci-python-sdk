# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CohereTool(object):
    """
    A definition of tool (function).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CohereTool object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CohereTool.
        :type name: str

        :param description:
            The value to assign to the description property of this CohereTool.
        :type description: str

        :param parameter_definitions:
            The value to assign to the parameter_definitions property of this CohereTool.
        :type parameter_definitions: dict(str, CohereParameterDefinition)

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'parameter_definitions': 'dict(str, CohereParameterDefinition)'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'parameter_definitions': 'parameterDefinitions'
        }

        self._name = None
        self._description = None
        self._parameter_definitions = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CohereTool.
        The name of the tool to be called. Valid names contain only the characters a-z, A-Z, 0-9, _ and must not begin with a digit.


        :return: The name of this CohereTool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CohereTool.
        The name of the tool to be called. Valid names contain only the characters a-z, A-Z, 0-9, _ and must not begin with a digit.


        :param name: The name of this CohereTool.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CohereTool.
        The description of what the tool does, the model uses the description to choose when and how to call the function.


        :return: The description of this CohereTool.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CohereTool.
        The description of what the tool does, the model uses the description to choose when and how to call the function.


        :param description: The description of this CohereTool.
        :type: str
        """
        self._description = description

    @property
    def parameter_definitions(self):
        """
        Gets the parameter_definitions of this CohereTool.
        The input parameters of the tool.


        :return: The parameter_definitions of this CohereTool.
        :rtype: dict(str, CohereParameterDefinition)
        """
        return self._parameter_definitions

    @parameter_definitions.setter
    def parameter_definitions(self, parameter_definitions):
        """
        Sets the parameter_definitions of this CohereTool.
        The input parameters of the tool.


        :param parameter_definitions: The parameter_definitions of this CohereTool.
        :type: dict(str, CohereParameterDefinition)
        """
        self._parameter_definitions = parameter_definitions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
