# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200202


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementAgentInstallKeySummary(object):
    """
    The summary of the Agent Install Key details.
    """

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentInstallKeySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentInstallKeySummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentInstallKeySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentInstallKeySummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentInstallKeySummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentInstallKeySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentInstallKeySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentInstallKeySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementAgentInstallKeySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagementAgentInstallKeySummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ManagementAgentInstallKeySummary.
        :type display_name: str

        :param created_by_principal_id:
            The value to assign to the created_by_principal_id property of this ManagementAgentInstallKeySummary.
        :type created_by_principal_id: str

        :param allowed_key_install_count:
            The value to assign to the allowed_key_install_count property of this ManagementAgentInstallKeySummary.
        :type allowed_key_install_count: int

        :param current_key_install_count:
            The value to assign to the current_key_install_count property of this ManagementAgentInstallKeySummary.
        :type current_key_install_count: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagementAgentInstallKeySummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ManagementAgentInstallKeySummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ManagementAgentInstallKeySummary.
        :type time_created: datetime

        :param time_expires:
            The value to assign to the time_expires property of this ManagementAgentInstallKeySummary.
        :type time_expires: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagementAgentInstallKeySummary.
        :type compartment_id: str

        :param is_unlimited:
            The value to assign to the is_unlimited property of this ManagementAgentInstallKeySummary.
        :type is_unlimited: bool

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'created_by_principal_id': 'str',
            'allowed_key_install_count': 'int',
            'current_key_install_count': 'int',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_expires': 'datetime',
            'compartment_id': 'str',
            'is_unlimited': 'bool'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'created_by_principal_id': 'createdByPrincipalId',
            'allowed_key_install_count': 'allowedKeyInstallCount',
            'current_key_install_count': 'currentKeyInstallCount',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_expires': 'timeExpires',
            'compartment_id': 'compartmentId',
            'is_unlimited': 'isUnlimited'
        }
        self._id = None
        self._display_name = None
        self._created_by_principal_id = None
        self._allowed_key_install_count = None
        self._current_key_install_count = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_expires = None
        self._compartment_id = None
        self._is_unlimited = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagementAgentInstallKeySummary.
        Agent Install Key identifier


        :return: The id of this ManagementAgentInstallKeySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagementAgentInstallKeySummary.
        Agent Install Key identifier


        :param id: The id of this ManagementAgentInstallKeySummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this ManagementAgentInstallKeySummary.
        Management Agent Install Key Name


        :return: The display_name of this ManagementAgentInstallKeySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagementAgentInstallKeySummary.
        Management Agent Install Key Name


        :param display_name: The display_name of this ManagementAgentInstallKeySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def created_by_principal_id(self):
        """
        Gets the created_by_principal_id of this ManagementAgentInstallKeySummary.
        Principal id of user who created the Agent Install key


        :return: The created_by_principal_id of this ManagementAgentInstallKeySummary.
        :rtype: str
        """
        return self._created_by_principal_id

    @created_by_principal_id.setter
    def created_by_principal_id(self, created_by_principal_id):
        """
        Sets the created_by_principal_id of this ManagementAgentInstallKeySummary.
        Principal id of user who created the Agent Install key


        :param created_by_principal_id: The created_by_principal_id of this ManagementAgentInstallKeySummary.
        :type: str
        """
        self._created_by_principal_id = created_by_principal_id

    @property
    def allowed_key_install_count(self):
        """
        Gets the allowed_key_install_count of this ManagementAgentInstallKeySummary.
        Total number of install for this keys


        :return: The allowed_key_install_count of this ManagementAgentInstallKeySummary.
        :rtype: int
        """
        return self._allowed_key_install_count

    @allowed_key_install_count.setter
    def allowed_key_install_count(self, allowed_key_install_count):
        """
        Sets the allowed_key_install_count of this ManagementAgentInstallKeySummary.
        Total number of install for this keys


        :param allowed_key_install_count: The allowed_key_install_count of this ManagementAgentInstallKeySummary.
        :type: int
        """
        self._allowed_key_install_count = allowed_key_install_count

    @property
    def current_key_install_count(self):
        """
        Gets the current_key_install_count of this ManagementAgentInstallKeySummary.
        Total number of install for this keys


        :return: The current_key_install_count of this ManagementAgentInstallKeySummary.
        :rtype: int
        """
        return self._current_key_install_count

    @current_key_install_count.setter
    def current_key_install_count(self, current_key_install_count):
        """
        Sets the current_key_install_count of this ManagementAgentInstallKeySummary.
        Total number of install for this keys


        :param current_key_install_count: The current_key_install_count of this ManagementAgentInstallKeySummary.
        :type: int
        """
        self._current_key_install_count = current_key_install_count

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ManagementAgentInstallKeySummary.
        Status of Key

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ManagementAgentInstallKeySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagementAgentInstallKeySummary.
        Status of Key


        :param lifecycle_state: The lifecycle_state of this ManagementAgentInstallKeySummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ManagementAgentInstallKeySummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this ManagementAgentInstallKeySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ManagementAgentInstallKeySummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this ManagementAgentInstallKeySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        Gets the time_created of this ManagementAgentInstallKeySummary.
        The time when Management Agent install Key was created. An RFC3339 formatted date time string


        :return: The time_created of this ManagementAgentInstallKeySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagementAgentInstallKeySummary.
        The time when Management Agent install Key was created. An RFC3339 formatted date time string


        :param time_created: The time_created of this ManagementAgentInstallKeySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_expires(self):
        """
        Gets the time_expires of this ManagementAgentInstallKeySummary.
        date after which key would expire after creation


        :return: The time_expires of this ManagementAgentInstallKeySummary.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this ManagementAgentInstallKeySummary.
        date after which key would expire after creation


        :param time_expires: The time_expires of this ManagementAgentInstallKeySummary.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagementAgentInstallKeySummary.
        Compartment Identifier


        :return: The compartment_id of this ManagementAgentInstallKeySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagementAgentInstallKeySummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this ManagementAgentInstallKeySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_unlimited(self):
        """
        Gets the is_unlimited of this ManagementAgentInstallKeySummary.
        If set to true, the install key has no expiration date or usage limit. Properties allowedKeyInstallCount and timeExpires are ignored if set to true. Defaults to false.


        :return: The is_unlimited of this ManagementAgentInstallKeySummary.
        :rtype: bool
        """
        return self._is_unlimited

    @is_unlimited.setter
    def is_unlimited(self, is_unlimited):
        """
        Sets the is_unlimited of this ManagementAgentInstallKeySummary.
        If set to true, the install key has no expiration date or usage limit. Properties allowedKeyInstallCount and timeExpires are ignored if set to true. Defaults to false.


        :param is_unlimited: The is_unlimited of this ManagementAgentInstallKeySummary.
        :type: bool
        """
        self._is_unlimited = is_unlimited

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
