# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330

from .config import Config
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoPromoteConfigDetails(Config):
    """
    A configuration of the AUTO_PROMOTE type, consists of a resource type and a boolean value
    that determines if this resource needs to be automatically promoted/discovered.
    For example, when a Management Agent registration event occurs and if isEnabled is TRUE for
    a HOST resource type, a HOST resource will be automatically discovered using that Management Agent.
    """

    #: A constant which can be used with the resource_type property of a AutoPromoteConfigDetails.
    #: This constant has a value of "HOST"
    RESOURCE_TYPE_HOST = "HOST"

    def __init__(self, **kwargs):
        """
        Initializes a new AutoPromoteConfigDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.stack_monitoring.models.AutoPromoteConfigDetails.config_type` attribute
        of this class is ``AUTO_PROMOTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutoPromoteConfigDetails.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AutoPromoteConfigDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this AutoPromoteConfigDetails.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this AutoPromoteConfigDetails.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AutoPromoteConfigDetails.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutoPromoteConfigDetails.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param config_type:
            The value to assign to the config_type property of this AutoPromoteConfigDetails.
            Allowed values for this property are: "AUTO_PROMOTE", "COMPUTE_AUTO_ACTIVATE_PLUGIN", "LICENSE_AUTO_ASSIGN", "LICENSE_ENTERPRISE_EXTENSIBILITY", "ONBOARD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type config_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AutoPromoteConfigDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AutoPromoteConfigDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AutoPromoteConfigDetails.
        :type system_tags: dict(str, dict(str, object))

        :param resource_type:
            The value to assign to the resource_type property of this AutoPromoteConfigDetails.
            Allowed values for this property are: "HOST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this AutoPromoteConfigDetails.
        :type is_enabled: bool

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'config_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'resource_type': 'str',
            'is_enabled': 'bool'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'config_type': 'configType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'resource_type': 'resourceType',
            'is_enabled': 'isEnabled'
        }
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._config_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._resource_type = None
        self._is_enabled = None
        self._config_type = 'AUTO_PROMOTE'

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this AutoPromoteConfigDetails.
        The type of resource to configure for automatic promotion.

        Allowed values for this property are: "HOST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_type of this AutoPromoteConfigDetails.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this AutoPromoteConfigDetails.
        The type of resource to configure for automatic promotion.


        :param resource_type: The resource_type of this AutoPromoteConfigDetails.
        :type: str
        """
        allowed_values = ["HOST"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            resource_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_type = resource_type

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this AutoPromoteConfigDetails.
        True if automatic promotion is enabled, false if it is not enabled.


        :return: The is_enabled of this AutoPromoteConfigDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AutoPromoteConfigDetails.
        True if automatic promotion is enabled, false if it is not enabled.


        :param is_enabled: The is_enabled of this AutoPromoteConfigDetails.
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
