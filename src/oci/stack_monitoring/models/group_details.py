# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GroupDetails(object):
    """
    User Group object
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this GroupDetails.
        :type name: str

        :param domain:
            The value to assign to the domain property of this GroupDetails.
        :type domain: str

        :param stack_monitoring_role:
            The value to assign to the stack_monitoring_role property of this GroupDetails.
        :type stack_monitoring_role: str

        """
        self.swagger_types = {
            'name': 'str',
            'domain': 'str',
            'stack_monitoring_role': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'domain': 'domain',
            'stack_monitoring_role': 'stackMonitoringRole'
        }
        self._name = None
        self._domain = None
        self._stack_monitoring_role = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this GroupDetails.
        Name of user Group


        :return: The name of this GroupDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GroupDetails.
        Name of user Group


        :param name: The name of this GroupDetails.
        :type: str
        """
        self._name = name

    @property
    def domain(self):
        """
        Gets the domain of this GroupDetails.
        Identity domain name


        :return: The domain of this GroupDetails.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this GroupDetails.
        Identity domain name


        :param domain: The domain of this GroupDetails.
        :type: str
        """
        self._domain = domain

    @property
    def stack_monitoring_role(self):
        """
        **[Required]** Gets the stack_monitoring_role of this GroupDetails.
        Role assigned to user group in context of Stack Monitoring service. Access role can be for example: ADMINISTRATOR, OPERATOR, VIEWER, any other access role


        :return: The stack_monitoring_role of this GroupDetails.
        :rtype: str
        """
        return self._stack_monitoring_role

    @stack_monitoring_role.setter
    def stack_monitoring_role(self, stack_monitoring_role):
        """
        Sets the stack_monitoring_role of this GroupDetails.
        Role assigned to user group in context of Stack Monitoring service. Access role can be for example: ADMINISTRATOR, OPERATOR, VIEWER, any other access role


        :param stack_monitoring_role: The stack_monitoring_role of this GroupDetails.
        :type: str
        """
        self._stack_monitoring_role = stack_monitoring_role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
