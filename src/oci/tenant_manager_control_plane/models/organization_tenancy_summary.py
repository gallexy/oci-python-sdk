# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230401


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OrganizationTenancySummary(object):
    """
    An organization tenancy summary entity.
    """

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancySummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the role property of a OrganizationTenancySummary.
    #: This constant has a value of "PARENT"
    ROLE_PARENT = "PARENT"

    #: A constant which can be used with the role property of a OrganizationTenancySummary.
    #: This constant has a value of "CHILD"
    ROLE_CHILD = "CHILD"

    #: A constant which can be used with the role property of a OrganizationTenancySummary.
    #: This constant has a value of "NONE"
    ROLE_NONE = "NONE"

    #: A constant which can be used with the governance_status property of a OrganizationTenancySummary.
    #: This constant has a value of "OPTED_IN"
    GOVERNANCE_STATUS_OPTED_IN = "OPTED_IN"

    #: A constant which can be used with the governance_status property of a OrganizationTenancySummary.
    #: This constant has a value of "OPTED_OUT"
    GOVERNANCE_STATUS_OPTED_OUT = "OPTED_OUT"

    def __init__(self, **kwargs):
        """
        Initializes a new OrganizationTenancySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenancy_id:
            The value to assign to the tenancy_id property of this OrganizationTenancySummary.
        :type tenancy_id: str

        :param name:
            The value to assign to the name property of this OrganizationTenancySummary.
        :type name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OrganizationTenancySummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param role:
            The value to assign to the role property of this OrganizationTenancySummary.
            Allowed values for this property are: "PARENT", "CHILD", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param time_joined:
            The value to assign to the time_joined property of this OrganizationTenancySummary.
        :type time_joined: datetime

        :param time_left:
            The value to assign to the time_left property of this OrganizationTenancySummary.
        :type time_left: datetime

        :param is_approved_for_transfer:
            The value to assign to the is_approved_for_transfer property of this OrganizationTenancySummary.
        :type is_approved_for_transfer: bool

        :param governance_status:
            The value to assign to the governance_status property of this OrganizationTenancySummary.
            Allowed values for this property are: "OPTED_IN", "OPTED_OUT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type governance_status: str

        :param system_tags:
            The value to assign to the system_tags property of this OrganizationTenancySummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'tenancy_id': 'str',
            'name': 'str',
            'lifecycle_state': 'str',
            'role': 'str',
            'time_joined': 'datetime',
            'time_left': 'datetime',
            'is_approved_for_transfer': 'bool',
            'governance_status': 'str',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'tenancy_id': 'tenancyId',
            'name': 'name',
            'lifecycle_state': 'lifecycleState',
            'role': 'role',
            'time_joined': 'timeJoined',
            'time_left': 'timeLeft',
            'is_approved_for_transfer': 'isApprovedForTransfer',
            'governance_status': 'governanceStatus',
            'system_tags': 'systemTags'
        }
        self._tenancy_id = None
        self._name = None
        self._lifecycle_state = None
        self._role = None
        self._time_joined = None
        self._time_left = None
        self._is_approved_for_transfer = None
        self._governance_status = None
        self._system_tags = None

    @property
    def tenancy_id(self):
        """
        **[Required]** Gets the tenancy_id of this OrganizationTenancySummary.
        OCID of the tenancy.


        :return: The tenancy_id of this OrganizationTenancySummary.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this OrganizationTenancySummary.
        OCID of the tenancy.


        :param tenancy_id: The tenancy_id of this OrganizationTenancySummary.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def name(self):
        """
        Gets the name of this OrganizationTenancySummary.
        Name of the tenancy.


        :return: The name of this OrganizationTenancySummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrganizationTenancySummary.
        Name of the tenancy.


        :param name: The name of this OrganizationTenancySummary.
        :type: str
        """
        self._name = name

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OrganizationTenancySummary.
        Lifecycle state of the organization tenancy.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OrganizationTenancySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OrganizationTenancySummary.
        Lifecycle state of the organization tenancy.


        :param lifecycle_state: The lifecycle_state of this OrganizationTenancySummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED", "DELETING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def role(self):
        """
        Gets the role of this OrganizationTenancySummary.
        Role of the organization tenancy.

        Allowed values for this property are: "PARENT", "CHILD", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this OrganizationTenancySummary.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this OrganizationTenancySummary.
        Role of the organization tenancy.


        :param role: The role of this OrganizationTenancySummary.
        :type: str
        """
        allowed_values = ["PARENT", "CHILD", "NONE"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def time_joined(self):
        """
        Gets the time_joined of this OrganizationTenancySummary.
        Date and time when the tenancy joined the organization.


        :return: The time_joined of this OrganizationTenancySummary.
        :rtype: datetime
        """
        return self._time_joined

    @time_joined.setter
    def time_joined(self, time_joined):
        """
        Sets the time_joined of this OrganizationTenancySummary.
        Date and time when the tenancy joined the organization.


        :param time_joined: The time_joined of this OrganizationTenancySummary.
        :type: datetime
        """
        self._time_joined = time_joined

    @property
    def time_left(self):
        """
        Gets the time_left of this OrganizationTenancySummary.
        Date and time when the tenancy left the organization.


        :return: The time_left of this OrganizationTenancySummary.
        :rtype: datetime
        """
        return self._time_left

    @time_left.setter
    def time_left(self, time_left):
        """
        Sets the time_left of this OrganizationTenancySummary.
        Date and time when the tenancy left the organization.


        :param time_left: The time_left of this OrganizationTenancySummary.
        :type: datetime
        """
        self._time_left = time_left

    @property
    def is_approved_for_transfer(self):
        """
        Gets the is_approved_for_transfer of this OrganizationTenancySummary.
        Parameter to indicate the tenancy is approved for transfer to another organization.


        :return: The is_approved_for_transfer of this OrganizationTenancySummary.
        :rtype: bool
        """
        return self._is_approved_for_transfer

    @is_approved_for_transfer.setter
    def is_approved_for_transfer(self, is_approved_for_transfer):
        """
        Sets the is_approved_for_transfer of this OrganizationTenancySummary.
        Parameter to indicate the tenancy is approved for transfer to another organization.


        :param is_approved_for_transfer: The is_approved_for_transfer of this OrganizationTenancySummary.
        :type: bool
        """
        self._is_approved_for_transfer = is_approved_for_transfer

    @property
    def governance_status(self):
        """
        **[Required]** Gets the governance_status of this OrganizationTenancySummary.
        The governance status of the tenancy.

        Allowed values for this property are: "OPTED_IN", "OPTED_OUT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The governance_status of this OrganizationTenancySummary.
        :rtype: str
        """
        return self._governance_status

    @governance_status.setter
    def governance_status(self, governance_status):
        """
        Sets the governance_status of this OrganizationTenancySummary.
        The governance status of the tenancy.


        :param governance_status: The governance_status of this OrganizationTenancySummary.
        :type: str
        """
        allowed_values = ["OPTED_IN", "OPTED_OUT"]
        if not value_allowed_none_or_none_sentinel(governance_status, allowed_values):
            governance_status = 'UNKNOWN_ENUM_VALUE'
        self._governance_status = governance_status

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OrganizationTenancySummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OrganizationTenancySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OrganizationTenancySummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OrganizationTenancySummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
