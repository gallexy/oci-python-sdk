# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .launch_instance_licensing_config import LaunchInstanceLicensingConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchInstanceWindowsLicensingConfig(LaunchInstanceLicensingConfig):
    """
    The default windows licensing config.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchInstanceWindowsLicensingConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.LaunchInstanceWindowsLicensingConfig.type` attribute
        of this class is ``WINDOWS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this LaunchInstanceWindowsLicensingConfig.
            Allowed values for this property are: "WINDOWS"
        :type type: str

        :param license_type:
            The value to assign to the license_type property of this LaunchInstanceWindowsLicensingConfig.
            Allowed values for this property are: "OCI_PROVIDED", "BRING_YOUR_OWN_LICENSE"
        :type license_type: str

        """
        self.swagger_types = {
            'type': 'str',
            'license_type': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'license_type': 'licenseType'
        }

        self._type = None
        self._license_type = None
        self._type = 'WINDOWS'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
