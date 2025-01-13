# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalingPolicyDetails(object):
    """
    Details for an autoscaling policy to enable on the model deployment.
    Each autoscaling configuration can have one autoscaling policy.
    In a threshold-based autoscaling policy, an autoscaling action is triggered when a performance metric meets
    or exceeds a threshold.
    """

    #: A constant which can be used with the auto_scaling_policy_type property of a AutoScalingPolicyDetails.
    #: This constant has a value of "THRESHOLD"
    AUTO_SCALING_POLICY_TYPE_THRESHOLD = "THRESHOLD"

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalingPolicyDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_science.models.ThresholdBasedAutoScalingPolicyDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param auto_scaling_policy_type:
            The value to assign to the auto_scaling_policy_type property of this AutoScalingPolicyDetails.
            Allowed values for this property are: "THRESHOLD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type auto_scaling_policy_type: str

        """
        self.swagger_types = {
            'auto_scaling_policy_type': 'str'
        }

        self.attribute_map = {
            'auto_scaling_policy_type': 'autoScalingPolicyType'
        }

        self._auto_scaling_policy_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['autoScalingPolicyType']

        if type == 'THRESHOLD':
            return 'ThresholdBasedAutoScalingPolicyDetails'
        else:
            return 'AutoScalingPolicyDetails'

    @property
    def auto_scaling_policy_type(self):
        """
        **[Required]** Gets the auto_scaling_policy_type of this AutoScalingPolicyDetails.
        The type of autoscaling policy.

        Allowed values for this property are: "THRESHOLD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The auto_scaling_policy_type of this AutoScalingPolicyDetails.
        :rtype: str
        """
        return self._auto_scaling_policy_type

    @auto_scaling_policy_type.setter
    def auto_scaling_policy_type(self, auto_scaling_policy_type):
        """
        Sets the auto_scaling_policy_type of this AutoScalingPolicyDetails.
        The type of autoscaling policy.


        :param auto_scaling_policy_type: The auto_scaling_policy_type of this AutoScalingPolicyDetails.
        :type: str
        """
        allowed_values = ["THRESHOLD"]
        if not value_allowed_none_or_none_sentinel(auto_scaling_policy_type, allowed_values):
            auto_scaling_policy_type = 'UNKNOWN_ENUM_VALUE'
        self._auto_scaling_policy_type = auto_scaling_policy_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
