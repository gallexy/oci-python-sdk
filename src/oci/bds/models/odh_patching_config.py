# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OdhPatchingConfig(object):
    """
    Detailed configurations for defining the behavior when installing ODH patches. If not provided, nodes will be patched with down time.
    """

    #: A constant which can be used with the patching_config_strategy property of a OdhPatchingConfig.
    #: This constant has a value of "DOWNTIME_BASED"
    PATCHING_CONFIG_STRATEGY_DOWNTIME_BASED = "DOWNTIME_BASED"

    #: A constant which can be used with the patching_config_strategy property of a OdhPatchingConfig.
    #: This constant has a value of "BATCHING_BASED"
    PATCHING_CONFIG_STRATEGY_BATCHING_BASED = "BATCHING_BASED"

    #: A constant which can be used with the patching_config_strategy property of a OdhPatchingConfig.
    #: This constant has a value of "DOMAIN_BASED"
    PATCHING_CONFIG_STRATEGY_DOMAIN_BASED = "DOMAIN_BASED"

    def __init__(self, **kwargs):
        """
        Initializes a new OdhPatchingConfig object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.bds.models.DowntimeBasedOdhPatchingConfig`
        * :class:`~oci.bds.models.DomainBasedOdhPatchingConfig`
        * :class:`~oci.bds.models.BatchingBasedOdhPatchingConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param patching_config_strategy:
            The value to assign to the patching_config_strategy property of this OdhPatchingConfig.
            Allowed values for this property are: "DOWNTIME_BASED", "BATCHING_BASED", "DOMAIN_BASED"
        :type patching_config_strategy: str

        """
        self.swagger_types = {
            'patching_config_strategy': 'str'
        }

        self.attribute_map = {
            'patching_config_strategy': 'patchingConfigStrategy'
        }

        self._patching_config_strategy = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['patchingConfigStrategy']

        if type == 'DOWNTIME_BASED':
            return 'DowntimeBasedOdhPatchingConfig'

        if type == 'DOMAIN_BASED':
            return 'DomainBasedOdhPatchingConfig'

        if type == 'BATCHING_BASED':
            return 'BatchingBasedOdhPatchingConfig'
        else:
            return 'OdhPatchingConfig'

    @property
    def patching_config_strategy(self):
        """
        **[Required]** Gets the patching_config_strategy of this OdhPatchingConfig.
        Type of strategy used for detailed patching configuration

        Allowed values for this property are: "DOWNTIME_BASED", "BATCHING_BASED", "DOMAIN_BASED"


        :return: The patching_config_strategy of this OdhPatchingConfig.
        :rtype: str
        """
        return self._patching_config_strategy

    @patching_config_strategy.setter
    def patching_config_strategy(self, patching_config_strategy):
        """
        Sets the patching_config_strategy of this OdhPatchingConfig.
        Type of strategy used for detailed patching configuration


        :param patching_config_strategy: The patching_config_strategy of this OdhPatchingConfig.
        :type: str
        """
        allowed_values = ["DOWNTIME_BASED", "BATCHING_BASED", "DOMAIN_BASED"]
        if not value_allowed_none_or_none_sentinel(patching_config_strategy, allowed_values):
            raise ValueError(
                f"Invalid value for `patching_config_strategy`, must be None or one of {allowed_values}"
            )
        self._patching_config_strategy = patching_config_strategy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
