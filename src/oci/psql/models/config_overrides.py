# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigOverrides(object):
    """
    Configuration overrides for a PostgreSQL instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigOverrides object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_key:
            The value to assign to the config_key property of this ConfigOverrides.
        :type config_key: str

        :param overriden_config_value:
            The value to assign to the overriden_config_value property of this ConfigOverrides.
        :type overriden_config_value: str

        """
        self.swagger_types = {
            'config_key': 'str',
            'overriden_config_value': 'str'
        }

        self.attribute_map = {
            'config_key': 'configKey',
            'overriden_config_value': 'overridenConfigValue'
        }

        self._config_key = None
        self._overriden_config_value = None

    @property
    def config_key(self):
        """
        **[Required]** Gets the config_key of this ConfigOverrides.
        Configuration variable name.


        :return: The config_key of this ConfigOverrides.
        :rtype: str
        """
        return self._config_key

    @config_key.setter
    def config_key(self, config_key):
        """
        Sets the config_key of this ConfigOverrides.
        Configuration variable name.


        :param config_key: The config_key of this ConfigOverrides.
        :type: str
        """
        self._config_key = config_key

    @property
    def overriden_config_value(self):
        """
        **[Required]** Gets the overriden_config_value of this ConfigOverrides.
        User-selected variable value.


        :return: The overriden_config_value of this ConfigOverrides.
        :rtype: str
        """
        return self._overriden_config_value

    @overriden_config_value.setter
    def overriden_config_value(self, overriden_config_value):
        """
        Sets the overriden_config_value of this ConfigOverrides.
        User-selected variable value.


        :param overriden_config_value: The overriden_config_value of this ConfigOverrides.
        :type: str
        """
        self._overriden_config_value = overriden_config_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
