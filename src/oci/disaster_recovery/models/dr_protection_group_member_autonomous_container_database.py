# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125

from .dr_protection_group_member import DrProtectionGroupMember
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrProtectionGroupMemberAutonomousContainerDatabase(DrProtectionGroupMember):
    """
    The properties for an Autonomous Container Database member of a DR protection group.
    """

    #: A constant which can be used with the connection_string_type property of a DrProtectionGroupMemberAutonomousContainerDatabase.
    #: This constant has a value of "SNAPSHOT_SERVICE"
    CONNECTION_STRING_TYPE_SNAPSHOT_SERVICE = "SNAPSHOT_SERVICE"

    #: A constant which can be used with the connection_string_type property of a DrProtectionGroupMemberAutonomousContainerDatabase.
    #: This constant has a value of "PRIMARY_SERVICE"
    CONNECTION_STRING_TYPE_PRIMARY_SERVICE = "PRIMARY_SERVICE"

    def __init__(self, **kwargs):
        """
        Initializes a new DrProtectionGroupMemberAutonomousContainerDatabase object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.DrProtectionGroupMemberAutonomousContainerDatabase.member_type` attribute
        of this class is ``AUTONOMOUS_CONTAINER_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_id:
            The value to assign to the member_id property of this DrProtectionGroupMemberAutonomousContainerDatabase.
        :type member_id: str

        :param member_type:
            The value to assign to the member_type property of this DrProtectionGroupMemberAutonomousContainerDatabase.
            Allowed values for this property are: "COMPUTE_INSTANCE", "COMPUTE_INSTANCE_MOVABLE", "COMPUTE_INSTANCE_NON_MOVABLE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE", "AUTONOMOUS_CONTAINER_DATABASE", "LOAD_BALANCER", "NETWORK_LOAD_BALANCER", "FILE_SYSTEM", "OBJECT_STORAGE_BUCKET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type member_type: str

        :param connection_string_type:
            The value to assign to the connection_string_type property of this DrProtectionGroupMemberAutonomousContainerDatabase.
            Allowed values for this property are: "SNAPSHOT_SERVICE", "PRIMARY_SERVICE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_string_type: str

        """
        self.swagger_types = {
            'member_id': 'str',
            'member_type': 'str',
            'connection_string_type': 'str'
        }

        self.attribute_map = {
            'member_id': 'memberId',
            'member_type': 'memberType',
            'connection_string_type': 'connectionStringType'
        }

        self._member_id = None
        self._member_type = None
        self._connection_string_type = None
        self._member_type = 'AUTONOMOUS_CONTAINER_DATABASE'

    @property
    def connection_string_type(self):
        """
        Gets the connection_string_type of this DrProtectionGroupMemberAutonomousContainerDatabase.
        The type of connection strings used to connect to an Autonomous Container Database snapshot standby created during a DR Drill operation.
        See https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbcl/index.html for information about these service types.

        Allowed values for this property are: "SNAPSHOT_SERVICE", "PRIMARY_SERVICE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connection_string_type of this DrProtectionGroupMemberAutonomousContainerDatabase.
        :rtype: str
        """
        return self._connection_string_type

    @connection_string_type.setter
    def connection_string_type(self, connection_string_type):
        """
        Sets the connection_string_type of this DrProtectionGroupMemberAutonomousContainerDatabase.
        The type of connection strings used to connect to an Autonomous Container Database snapshot standby created during a DR Drill operation.
        See https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbcl/index.html for information about these service types.


        :param connection_string_type: The connection_string_type of this DrProtectionGroupMemberAutonomousContainerDatabase.
        :type: str
        """
        allowed_values = ["SNAPSHOT_SERVICE", "PRIMARY_SERVICE"]
        if not value_allowed_none_or_none_sentinel(connection_string_type, allowed_values):
            connection_string_type = 'UNKNOWN_ENUM_VALUE'
        self._connection_string_type = connection_string_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
