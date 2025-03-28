# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .configuration_item_metadata import ConfigurationItemMetadata
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BasicConfigurationItemMetadata(ConfigurationItemMetadata):
    """
    Basic configuration item metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BasicConfigurationItemMetadata object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.BasicConfigurationItemMetadata.config_item_type` attribute
        of this class is ``BASIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_item_type:
            The value to assign to the config_item_type property of this BasicConfigurationItemMetadata.
            Allowed values for this property are: "BASIC"
        :type config_item_type: str

        :param display_name:
            The value to assign to the display_name property of this BasicConfigurationItemMetadata.
        :type display_name: str

        :param description:
            The value to assign to the description property of this BasicConfigurationItemMetadata.
        :type description: str

        :param data_type:
            The value to assign to the data_type property of this BasicConfigurationItemMetadata.
        :type data_type: str

        :param unit_details:
            The value to assign to the unit_details property of this BasicConfigurationItemMetadata.
        :type unit_details: oci.opsi.models.ConfigurationItemUnitDetails

        :param value_input_details:
            The value to assign to the value_input_details property of this BasicConfigurationItemMetadata.
        :type value_input_details: oci.opsi.models.ConfigurationItemAllowedValueDetails

        """
        self.swagger_types = {
            'config_item_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'data_type': 'str',
            'unit_details': 'ConfigurationItemUnitDetails',
            'value_input_details': 'ConfigurationItemAllowedValueDetails'
        }
        self.attribute_map = {
            'config_item_type': 'configItemType',
            'display_name': 'displayName',
            'description': 'description',
            'data_type': 'dataType',
            'unit_details': 'unitDetails',
            'value_input_details': 'valueInputDetails'
        }
        self._config_item_type = None
        self._display_name = None
        self._description = None
        self._data_type = None
        self._unit_details = None
        self._value_input_details = None
        self._config_item_type = 'BASIC'

    @property
    def display_name(self):
        """
        Gets the display_name of this BasicConfigurationItemMetadata.
        User-friendly display name for the configuration item.


        :return: The display_name of this BasicConfigurationItemMetadata.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BasicConfigurationItemMetadata.
        User-friendly display name for the configuration item.


        :param display_name: The display_name of this BasicConfigurationItemMetadata.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this BasicConfigurationItemMetadata.
        Description of configuration item .


        :return: The description of this BasicConfigurationItemMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BasicConfigurationItemMetadata.
        Description of configuration item .


        :param description: The description of this BasicConfigurationItemMetadata.
        :type: str
        """
        self._description = description

    @property
    def data_type(self):
        """
        Gets the data_type of this BasicConfigurationItemMetadata.
        Data type of configuration item.
        Examples: STRING, BOOLEAN, NUMBER


        :return: The data_type of this BasicConfigurationItemMetadata.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this BasicConfigurationItemMetadata.
        Data type of configuration item.
        Examples: STRING, BOOLEAN, NUMBER


        :param data_type: The data_type of this BasicConfigurationItemMetadata.
        :type: str
        """
        self._data_type = data_type

    @property
    def unit_details(self):
        """
        Gets the unit_details of this BasicConfigurationItemMetadata.

        :return: The unit_details of this BasicConfigurationItemMetadata.
        :rtype: oci.opsi.models.ConfigurationItemUnitDetails
        """
        return self._unit_details

    @unit_details.setter
    def unit_details(self, unit_details):
        """
        Sets the unit_details of this BasicConfigurationItemMetadata.

        :param unit_details: The unit_details of this BasicConfigurationItemMetadata.
        :type: oci.opsi.models.ConfigurationItemUnitDetails
        """
        self._unit_details = unit_details

    @property
    def value_input_details(self):
        """
        Gets the value_input_details of this BasicConfigurationItemMetadata.

        :return: The value_input_details of this BasicConfigurationItemMetadata.
        :rtype: oci.opsi.models.ConfigurationItemAllowedValueDetails
        """
        return self._value_input_details

    @value_input_details.setter
    def value_input_details(self, value_input_details):
        """
        Sets the value_input_details of this BasicConfigurationItemMetadata.

        :param value_input_details: The value_input_details of this BasicConfigurationItemMetadata.
        :type: oci.opsi.models.ConfigurationItemAllowedValueDetails
        """
        self._value_input_details = value_input_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
