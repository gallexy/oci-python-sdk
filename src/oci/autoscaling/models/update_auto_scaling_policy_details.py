# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAutoScalingPolicyDetails(object):
    """
    UpdateAutoScalingPolicyDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAutoScalingPolicyDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.autoscaling.models.UpdateThresholdPolicyDetails`
        * :class:`~oci.autoscaling.models.UpdateScheduledPolicyDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAutoScalingPolicyDetails.
        :type display_name: str

        :param capacity:
            The value to assign to the capacity property of this UpdateAutoScalingPolicyDetails.
        :type capacity: Capacity

        :param policy_type:
            The value to assign to the policy_type property of this UpdateAutoScalingPolicyDetails.
        :type policy_type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateAutoScalingPolicyDetails.
        :type is_enabled: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'capacity': 'Capacity',
            'policy_type': 'str',
            'is_enabled': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'capacity': 'capacity',
            'policy_type': 'policyType',
            'is_enabled': 'isEnabled'
        }

        self._display_name = None
        self._capacity = None
        self._policy_type = None
        self._is_enabled = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['policyType']

        if type == 'threshold':
            return 'UpdateThresholdPolicyDetails'

        if type == 'scheduled':
            return 'UpdateScheduledPolicyDetails'
        else:
            return 'UpdateAutoScalingPolicyDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAutoScalingPolicyDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this UpdateAutoScalingPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAutoScalingPolicyDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateAutoScalingPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def capacity(self):
        """
        Gets the capacity of this UpdateAutoScalingPolicyDetails.
        The capacity requirements of the autoscaling policy.


        :return: The capacity of this UpdateAutoScalingPolicyDetails.
        :rtype: Capacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this UpdateAutoScalingPolicyDetails.
        The capacity requirements of the autoscaling policy.


        :param capacity: The capacity of this UpdateAutoScalingPolicyDetails.
        :type: Capacity
        """
        self._capacity = capacity

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this UpdateAutoScalingPolicyDetails.
        Indicates the type of autoscaling policy.


        :return: The policy_type of this UpdateAutoScalingPolicyDetails.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this UpdateAutoScalingPolicyDetails.
        Indicates the type of autoscaling policy.


        :param policy_type: The policy_type of this UpdateAutoScalingPolicyDetails.
        :type: str
        """
        self._policy_type = policy_type

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateAutoScalingPolicyDetails.
        Boolean field indicating whether this policy is enabled or not.


        :return: The is_enabled of this UpdateAutoScalingPolicyDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateAutoScalingPolicyDetails.
        Boolean field indicating whether this policy is enabled or not.


        :param is_enabled: The is_enabled of this UpdateAutoScalingPolicyDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
