# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220919


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetAsset(object):
    """
    Description of the target asset.
    """

    #: A constant which can be used with the lifecycle_state property of a TargetAsset.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a TargetAsset.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a TargetAsset.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a TargetAsset.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetAsset.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a TargetAsset.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TargetAsset.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the type property of a TargetAsset.
    #: This constant has a value of "INSTANCE"
    TYPE_INSTANCE = "INSTANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetAsset object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_migrations.models.VmTargetAsset`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TargetAsset.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this TargetAsset.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TargetAsset.
            Allowed values for this property are: "CREATING", "UPDATING", "NEEDS_ATTENTION", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TargetAsset.
        :type lifecycle_details: str

        :param migration_plan_id:
            The value to assign to the migration_plan_id property of this TargetAsset.
        :type migration_plan_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TargetAsset.
        :type compartment_id: str

        :param created_resource_id:
            The value to assign to the created_resource_id property of this TargetAsset.
        :type created_resource_id: str

        :param type:
            The value to assign to the type property of this TargetAsset.
            Allowed values for this property are: "INSTANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param is_excluded_from_execution:
            The value to assign to the is_excluded_from_execution property of this TargetAsset.
        :type is_excluded_from_execution: bool

        :param compatibility_messages:
            The value to assign to the compatibility_messages property of this TargetAsset.
        :type compatibility_messages: list[oci.cloud_migrations.models.CompatibilityMessage]

        :param estimated_cost:
            The value to assign to the estimated_cost property of this TargetAsset.
        :type estimated_cost: oci.cloud_migrations.models.CostEstimation

        :param time_created:
            The value to assign to the time_created property of this TargetAsset.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TargetAsset.
        :type time_updated: datetime

        :param time_assessed:
            The value to assign to the time_assessed property of this TargetAsset.
        :type time_assessed: datetime

        :param migration_asset:
            The value to assign to the migration_asset property of this TargetAsset.
        :type migration_asset: oci.cloud_migrations.models.MigrationAsset

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'migration_plan_id': 'str',
            'compartment_id': 'str',
            'created_resource_id': 'str',
            'type': 'str',
            'is_excluded_from_execution': 'bool',
            'compatibility_messages': 'list[CompatibilityMessage]',
            'estimated_cost': 'CostEstimation',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_assessed': 'datetime',
            'migration_asset': 'MigrationAsset'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'migration_plan_id': 'migrationPlanId',
            'compartment_id': 'compartmentId',
            'created_resource_id': 'createdResourceId',
            'type': 'type',
            'is_excluded_from_execution': 'isExcludedFromExecution',
            'compatibility_messages': 'compatibilityMessages',
            'estimated_cost': 'estimatedCost',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_assessed': 'timeAssessed',
            'migration_asset': 'migrationAsset'
        }

        self._id = None
        self._display_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._migration_plan_id = None
        self._compartment_id = None
        self._created_resource_id = None
        self._type = None
        self._is_excluded_from_execution = None
        self._compatibility_messages = None
        self._estimated_cost = None
        self._time_created = None
        self._time_updated = None
        self._time_assessed = None
        self._migration_asset = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'INSTANCE':
            return 'VmTargetAsset'
        else:
            return 'TargetAsset'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TargetAsset.
        Unique identifier that is immutable on creation.


        :return: The id of this TargetAsset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TargetAsset.
        Unique identifier that is immutable on creation.


        :param id: The id of this TargetAsset.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this TargetAsset.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this TargetAsset.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TargetAsset.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this TargetAsset.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this TargetAsset.
        The current state of the target asset.

        Allowed values for this property are: "CREATING", "UPDATING", "NEEDS_ATTENTION", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TargetAsset.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TargetAsset.
        The current state of the target asset.


        :param lifecycle_state: The lifecycle_state of this TargetAsset.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "NEEDS_ATTENTION", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TargetAsset.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this TargetAsset.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TargetAsset.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this TargetAsset.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def migration_plan_id(self):
        """
        **[Required]** Gets the migration_plan_id of this TargetAsset.
        OCID of the associated migration plan.


        :return: The migration_plan_id of this TargetAsset.
        :rtype: str
        """
        return self._migration_plan_id

    @migration_plan_id.setter
    def migration_plan_id(self, migration_plan_id):
        """
        Sets the migration_plan_id of this TargetAsset.
        OCID of the associated migration plan.


        :param migration_plan_id: The migration_plan_id of this TargetAsset.
        :type: str
        """
        self._migration_plan_id = migration_plan_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this TargetAsset.
        Compartment identifier


        :return: The compartment_id of this TargetAsset.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TargetAsset.
        Compartment identifier


        :param compartment_id: The compartment_id of this TargetAsset.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def created_resource_id(self):
        """
        Gets the created_resource_id of this TargetAsset.
        Created resource identifier


        :return: The created_resource_id of this TargetAsset.
        :rtype: str
        """
        return self._created_resource_id

    @created_resource_id.setter
    def created_resource_id(self, created_resource_id):
        """
        Sets the created_resource_id of this TargetAsset.
        Created resource identifier


        :param created_resource_id: The created_resource_id of this TargetAsset.
        :type: str
        """
        self._created_resource_id = created_resource_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this TargetAsset.
        The type of target asset.

        Allowed values for this property are: "INSTANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this TargetAsset.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TargetAsset.
        The type of target asset.


        :param type: The type of this TargetAsset.
        :type: str
        """
        allowed_values = ["INSTANCE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def is_excluded_from_execution(self):
        """
        **[Required]** Gets the is_excluded_from_execution of this TargetAsset.
        A boolean indicating whether the asset should be migrated.


        :return: The is_excluded_from_execution of this TargetAsset.
        :rtype: bool
        """
        return self._is_excluded_from_execution

    @is_excluded_from_execution.setter
    def is_excluded_from_execution(self, is_excluded_from_execution):
        """
        Sets the is_excluded_from_execution of this TargetAsset.
        A boolean indicating whether the asset should be migrated.


        :param is_excluded_from_execution: The is_excluded_from_execution of this TargetAsset.
        :type: bool
        """
        self._is_excluded_from_execution = is_excluded_from_execution

    @property
    def compatibility_messages(self):
        """
        Gets the compatibility_messages of this TargetAsset.
        Messages about the compatibility issues.


        :return: The compatibility_messages of this TargetAsset.
        :rtype: list[oci.cloud_migrations.models.CompatibilityMessage]
        """
        return self._compatibility_messages

    @compatibility_messages.setter
    def compatibility_messages(self, compatibility_messages):
        """
        Sets the compatibility_messages of this TargetAsset.
        Messages about the compatibility issues.


        :param compatibility_messages: The compatibility_messages of this TargetAsset.
        :type: list[oci.cloud_migrations.models.CompatibilityMessage]
        """
        self._compatibility_messages = compatibility_messages

    @property
    def estimated_cost(self):
        """
        **[Required]** Gets the estimated_cost of this TargetAsset.

        :return: The estimated_cost of this TargetAsset.
        :rtype: oci.cloud_migrations.models.CostEstimation
        """
        return self._estimated_cost

    @estimated_cost.setter
    def estimated_cost(self, estimated_cost):
        """
        Sets the estimated_cost of this TargetAsset.

        :param estimated_cost: The estimated_cost of this TargetAsset.
        :type: oci.cloud_migrations.models.CostEstimation
        """
        self._estimated_cost = estimated_cost

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this TargetAsset.
        The time when the target asset was created. An RFC3339 formatted datetime string.


        :return: The time_created of this TargetAsset.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TargetAsset.
        The time when the target asset was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this TargetAsset.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this TargetAsset.
        The time when the target asset was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this TargetAsset.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TargetAsset.
        The time when the target asset was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this TargetAsset.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_assessed(self):
        """
        **[Required]** Gets the time_assessed of this TargetAsset.
        The time when the assessment was done. An RFC3339 formatted datetime string.


        :return: The time_assessed of this TargetAsset.
        :rtype: datetime
        """
        return self._time_assessed

    @time_assessed.setter
    def time_assessed(self, time_assessed):
        """
        Sets the time_assessed of this TargetAsset.
        The time when the assessment was done. An RFC3339 formatted datetime string.


        :param time_assessed: The time_assessed of this TargetAsset.
        :type: datetime
        """
        self._time_assessed = time_assessed

    @property
    def migration_asset(self):
        """
        Gets the migration_asset of this TargetAsset.

        :return: The migration_asset of this TargetAsset.
        :rtype: oci.cloud_migrations.models.MigrationAsset
        """
        return self._migration_asset

    @migration_asset.setter
    def migration_asset(self, migration_asset):
        """
        Sets the migration_asset of this TargetAsset.

        :param migration_asset: The migration_asset of this TargetAsset.
        :type: oci.cloud_migrations.models.MigrationAsset
        """
        self._migration_asset = migration_asset

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
