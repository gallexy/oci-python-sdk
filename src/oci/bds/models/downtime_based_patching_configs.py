# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531

from .patching_configs import PatchingConfigs
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DowntimeBasedPatchingConfigs(PatchingConfigs):
    """
    Patching configurations which allows downtime. This patching config will patch and reboot all the nodes in parallel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DowntimeBasedPatchingConfigs object with values from keyword arguments. The default value of the :py:attr:`~oci.bds.models.DowntimeBasedPatchingConfigs.patching_config_strategy` attribute
        of this class is ``DOWNTIME_BASED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param patching_config_strategy:
            The value to assign to the patching_config_strategy property of this DowntimeBasedPatchingConfigs.
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
        self._patching_config_strategy = 'DOWNTIME_BASED'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
