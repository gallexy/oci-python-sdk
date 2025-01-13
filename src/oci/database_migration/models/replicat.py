# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Replicat(object):
    """
    Parameters for Replicat processes.
    """

    #: A constant which can be used with the performance_profile property of a Replicat.
    #: This constant has a value of "LOW"
    PERFORMANCE_PROFILE_LOW = "LOW"

    #: A constant which can be used with the performance_profile property of a Replicat.
    #: This constant has a value of "HIGH"
    PERFORMANCE_PROFILE_HIGH = "HIGH"

    def __init__(self, **kwargs):
        """
        Initializes a new Replicat object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param performance_profile:
            The value to assign to the performance_profile property of this Replicat.
            Allowed values for this property are: "LOW", "HIGH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type performance_profile: str

        """
        self.swagger_types = {
            'performance_profile': 'str'
        }

        self.attribute_map = {
            'performance_profile': 'performanceProfile'
        }

        self._performance_profile = None

    @property
    def performance_profile(self):
        """
        Gets the performance_profile of this Replicat.
        Replicat performance.

        Allowed values for this property are: "LOW", "HIGH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The performance_profile of this Replicat.
        :rtype: str
        """
        return self._performance_profile

    @performance_profile.setter
    def performance_profile(self, performance_profile):
        """
        Sets the performance_profile of this Replicat.
        Replicat performance.


        :param performance_profile: The performance_profile of this Replicat.
        :type: str
        """
        allowed_values = ["LOW", "HIGH"]
        if not value_allowed_none_or_none_sentinel(performance_profile, allowed_values):
            performance_profile = 'UNKNOWN_ENUM_VALUE'
        self._performance_profile = performance_profile

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
