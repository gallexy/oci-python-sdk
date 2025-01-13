# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePropertyDetails(object):
    """
    The information to be updated.
    """

    #: A constant which can be used with the selection property of a UpdatePropertyDetails.
    #: This constant has a value of "SINGLE_CHOICE"
    SELECTION_SINGLE_CHOICE = "SINGLE_CHOICE"

    #: A constant which can be used with the selection property of a UpdatePropertyDetails.
    #: This constant has a value of "MULTI_CHOICE"
    SELECTION_MULTI_CHOICE = "MULTI_CHOICE"

    #: A constant which can be used with the selection property of a UpdatePropertyDetails.
    #: This constant has a value of "DEFAULT_TEXT"
    SELECTION_DEFAULT_TEXT = "DEFAULT_TEXT"

    #: A constant which can be used with the value_type property of a UpdatePropertyDetails.
    #: This constant has a value of "STRING"
    VALUE_TYPE_STRING = "STRING"

    #: A constant which can be used with the value_type property of a UpdatePropertyDetails.
    #: This constant has a value of "NUMERIC"
    VALUE_TYPE_NUMERIC = "NUMERIC"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePropertyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdatePropertyDetails.
        :type display_name: str

        :param selection:
            The value to assign to the selection property of this UpdatePropertyDetails.
            Allowed values for this property are: "SINGLE_CHOICE", "MULTI_CHOICE", "DEFAULT_TEXT"
        :type selection: str

        :param value_type:
            The value to assign to the value_type property of this UpdatePropertyDetails.
            Allowed values for this property are: "STRING", "NUMERIC"
        :type value_type: str

        :param values:
            The value to assign to the values property of this UpdatePropertyDetails.
        :type values: list[str]

        """
        self.swagger_types = {
            'display_name': 'str',
            'selection': 'str',
            'value_type': 'str',
            'values': 'list[str]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'selection': 'selection',
            'value_type': 'valueType',
            'values': 'values'
        }

        self._display_name = None
        self._selection = None
        self._value_type = None
        self._values = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdatePropertyDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this UpdatePropertyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdatePropertyDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this UpdatePropertyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def selection(self):
        """
        Gets the selection of this UpdatePropertyDetails.
        Text selection of the property.

        Allowed values for this property are: "SINGLE_CHOICE", "MULTI_CHOICE", "DEFAULT_TEXT"


        :return: The selection of this UpdatePropertyDetails.
        :rtype: str
        """
        return self._selection

    @selection.setter
    def selection(self, selection):
        """
        Sets the selection of this UpdatePropertyDetails.
        Text selection of the property.


        :param selection: The selection of this UpdatePropertyDetails.
        :type: str
        """
        allowed_values = ["SINGLE_CHOICE", "MULTI_CHOICE", "DEFAULT_TEXT"]
        if not value_allowed_none_or_none_sentinel(selection, allowed_values):
            raise ValueError(
                f"Invalid value for `selection`, must be None or one of {allowed_values}"
            )
        self._selection = selection

    @property
    def value_type(self):
        """
        Gets the value_type of this UpdatePropertyDetails.
        Format of the value.

        Allowed values for this property are: "STRING", "NUMERIC"


        :return: The value_type of this UpdatePropertyDetails.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this UpdatePropertyDetails.
        Format of the value.


        :param value_type: The value_type of this UpdatePropertyDetails.
        :type: str
        """
        allowed_values = ["STRING", "NUMERIC"]
        if not value_allowed_none_or_none_sentinel(value_type, allowed_values):
            raise ValueError(
                f"Invalid value for `value_type`, must be None or one of {allowed_values}"
            )
        self._value_type = value_type

    @property
    def values(self):
        """
        Gets the values of this UpdatePropertyDetails.
        Values of the property (must be a single value if selection = 'SINGLE_CHOICE').


        :return: The values of this UpdatePropertyDetails.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this UpdatePropertyDetails.
        Values of the property (must be a single value if selection = 'SINGLE_CHOICE').


        :param values: The values of this UpdatePropertyDetails.
        :type: list[str]
        """
        self._values = values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
