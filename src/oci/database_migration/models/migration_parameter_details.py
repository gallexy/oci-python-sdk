# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrationParameterDetails(object):
    """
    Migration parameter details object.
    """

    #: A constant which can be used with the data_type property of a MigrationParameterDetails.
    #: This constant has a value of "STRING"
    DATA_TYPE_STRING = "STRING"

    #: A constant which can be used with the data_type property of a MigrationParameterDetails.
    #: This constant has a value of "INTEGER"
    DATA_TYPE_INTEGER = "INTEGER"

    #: A constant which can be used with the data_type property of a MigrationParameterDetails.
    #: This constant has a value of "FLOAT"
    DATA_TYPE_FLOAT = "FLOAT"

    #: A constant which can be used with the data_type property of a MigrationParameterDetails.
    #: This constant has a value of "BOOLEAN"
    DATA_TYPE_BOOLEAN = "BOOLEAN"

    def __init__(self, **kwargs):
        """
        Initializes a new MigrationParameterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this MigrationParameterDetails.
        :type value: str

        :param name:
            The value to assign to the name property of this MigrationParameterDetails.
        :type name: str

        :param data_type:
            The value to assign to the data_type property of this MigrationParameterDetails.
            Allowed values for this property are: "STRING", "INTEGER", "FLOAT", "BOOLEAN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_type: str

        """
        self.swagger_types = {
            'value': 'str',
            'name': 'str',
            'data_type': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'name': 'name',
            'data_type': 'dataType'
        }

        self._value = None
        self._name = None
        self._data_type = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this MigrationParameterDetails.
        If a STRING data type then the value should be an array of characters,
        if a INTEGER data type then the value should be an integer value,
        if a FLOAT data type then the value should be an float value,
        if a BOOLEAN data type then the value should be TRUE or FALSE.


        :return: The value of this MigrationParameterDetails.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this MigrationParameterDetails.
        If a STRING data type then the value should be an array of characters,
        if a INTEGER data type then the value should be an integer value,
        if a FLOAT data type then the value should be an float value,
        if a BOOLEAN data type then the value should be TRUE or FALSE.


        :param value: The value of this MigrationParameterDetails.
        :type: str
        """
        self._value = value

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MigrationParameterDetails.
        Parameter name.


        :return: The name of this MigrationParameterDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MigrationParameterDetails.
        Parameter name.


        :param name: The name of this MigrationParameterDetails.
        :type: str
        """
        self._name = name

    @property
    def data_type(self):
        """
        **[Required]** Gets the data_type of this MigrationParameterDetails.
        Parameter data type.

        Allowed values for this property are: "STRING", "INTEGER", "FLOAT", "BOOLEAN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_type of this MigrationParameterDetails.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this MigrationParameterDetails.
        Parameter data type.


        :param data_type: The data_type of this MigrationParameterDetails.
        :type: str
        """
        allowed_values = ["STRING", "INTEGER", "FLOAT", "BOOLEAN"]
        if not value_allowed_none_or_none_sentinel(data_type, allowed_values):
            data_type = 'UNKNOWN_ENUM_VALUE'
        self._data_type = data_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
