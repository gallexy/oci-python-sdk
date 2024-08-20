# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SchedulerDefinitionSummary(object):
    """
    Summary of the SchedulerDefinition.
    """

    #: A constant which can be used with the action_group_types property of a SchedulerDefinitionSummary.
    #: This constant has a value of "PRODUCT"
    ACTION_GROUP_TYPES_PRODUCT = "PRODUCT"

    #: A constant which can be used with the action_group_types property of a SchedulerDefinitionSummary.
    #: This constant has a value of "ENVIRONMENT"
    ACTION_GROUP_TYPES_ENVIRONMENT = "ENVIRONMENT"

    def __init__(self, **kwargs):
        """
        Initializes a new SchedulerDefinitionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SchedulerDefinitionSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this SchedulerDefinitionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this SchedulerDefinitionSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SchedulerDefinitionSummary.
        :type compartment_id: str

        :param resource_region:
            The value to assign to the resource_region property of this SchedulerDefinitionSummary.
        :type resource_region: str

        :param time_created:
            The value to assign to the time_created property of this SchedulerDefinitionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SchedulerDefinitionSummary.
        :type time_updated: datetime

        :param time_of_next_run:
            The value to assign to the time_of_next_run property of this SchedulerDefinitionSummary.
        :type time_of_next_run: datetime

        :param schedule:
            The value to assign to the schedule property of this SchedulerDefinitionSummary.
        :type schedule: oci.fleet_apps_management.models.Schedule

        :param count_of_affected_action_groups:
            The value to assign to the count_of_affected_action_groups property of this SchedulerDefinitionSummary.
        :type count_of_affected_action_groups: int

        :param count_of_affected_resources:
            The value to assign to the count_of_affected_resources property of this SchedulerDefinitionSummary.
        :type count_of_affected_resources: int

        :param count_of_affected_targets:
            The value to assign to the count_of_affected_targets property of this SchedulerDefinitionSummary.
        :type count_of_affected_targets: int

        :param action_group_types:
            The value to assign to the action_group_types property of this SchedulerDefinitionSummary.
            Allowed values for items in this list are: "PRODUCT", "ENVIRONMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action_group_types: list[str]

        :param application_types:
            The value to assign to the application_types property of this SchedulerDefinitionSummary.
        :type application_types: list[str]

        :param products:
            The value to assign to the products property of this SchedulerDefinitionSummary.
        :type products: list[str]

        :param lifecycle_operations:
            The value to assign to the lifecycle_operations property of this SchedulerDefinitionSummary.
        :type lifecycle_operations: list[str]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SchedulerDefinitionSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SchedulerDefinitionSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SchedulerDefinitionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SchedulerDefinitionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SchedulerDefinitionSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'resource_region': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_of_next_run': 'datetime',
            'schedule': 'Schedule',
            'count_of_affected_action_groups': 'int',
            'count_of_affected_resources': 'int',
            'count_of_affected_targets': 'int',
            'action_group_types': 'list[str]',
            'application_types': 'list[str]',
            'products': 'list[str]',
            'lifecycle_operations': 'list[str]',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'resource_region': 'resourceRegion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_of_next_run': 'timeOfNextRun',
            'schedule': 'schedule',
            'count_of_affected_action_groups': 'countOfAffectedActionGroups',
            'count_of_affected_resources': 'countOfAffectedResources',
            'count_of_affected_targets': 'countOfAffectedTargets',
            'action_group_types': 'actionGroupTypes',
            'application_types': 'applicationTypes',
            'products': 'products',
            'lifecycle_operations': 'lifecycleOperations',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._resource_region = None
        self._time_created = None
        self._time_updated = None
        self._time_of_next_run = None
        self._schedule = None
        self._count_of_affected_action_groups = None
        self._count_of_affected_resources = None
        self._count_of_affected_targets = None
        self._action_group_types = None
        self._application_types = None
        self._products = None
        self._lifecycle_operations = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SchedulerDefinitionSummary.
        The OCID of the resource.


        :return: The id of this SchedulerDefinitionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SchedulerDefinitionSummary.
        The OCID of the resource.


        :param id: The id of this SchedulerDefinitionSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SchedulerDefinitionSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this SchedulerDefinitionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SchedulerDefinitionSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this SchedulerDefinitionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this SchedulerDefinitionSummary.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :return: The description of this SchedulerDefinitionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SchedulerDefinitionSummary.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :param description: The description of this SchedulerDefinitionSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SchedulerDefinitionSummary.
        Tenancy OCID


        :return: The compartment_id of this SchedulerDefinitionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SchedulerDefinitionSummary.
        Tenancy OCID


        :param compartment_id: The compartment_id of this SchedulerDefinitionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resource_region(self):
        """
        Gets the resource_region of this SchedulerDefinitionSummary.
        Associated region


        :return: The resource_region of this SchedulerDefinitionSummary.
        :rtype: str
        """
        return self._resource_region

    @resource_region.setter
    def resource_region(self, resource_region):
        """
        Sets the resource_region of this SchedulerDefinitionSummary.
        Associated region


        :param resource_region: The resource_region of this SchedulerDefinitionSummary.
        :type: str
        """
        self._resource_region = resource_region

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SchedulerDefinitionSummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this SchedulerDefinitionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SchedulerDefinitionSummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this SchedulerDefinitionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this SchedulerDefinitionSummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this SchedulerDefinitionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SchedulerDefinitionSummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this SchedulerDefinitionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_of_next_run(self):
        """
        Gets the time_of_next_run of this SchedulerDefinitionSummary.
        Scheduled date for the next run of the Job.


        :return: The time_of_next_run of this SchedulerDefinitionSummary.
        :rtype: datetime
        """
        return self._time_of_next_run

    @time_of_next_run.setter
    def time_of_next_run(self, time_of_next_run):
        """
        Sets the time_of_next_run of this SchedulerDefinitionSummary.
        Scheduled date for the next run of the Job.


        :param time_of_next_run: The time_of_next_run of this SchedulerDefinitionSummary.
        :type: datetime
        """
        self._time_of_next_run = time_of_next_run

    @property
    def schedule(self):
        """
        Gets the schedule of this SchedulerDefinitionSummary.

        :return: The schedule of this SchedulerDefinitionSummary.
        :rtype: oci.fleet_apps_management.models.Schedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this SchedulerDefinitionSummary.

        :param schedule: The schedule of this SchedulerDefinitionSummary.
        :type: oci.fleet_apps_management.models.Schedule
        """
        self._schedule = schedule

    @property
    def count_of_affected_action_groups(self):
        """
        Gets the count_of_affected_action_groups of this SchedulerDefinitionSummary.
        Count of Action Groups affected by the Schedule.


        :return: The count_of_affected_action_groups of this SchedulerDefinitionSummary.
        :rtype: int
        """
        return self._count_of_affected_action_groups

    @count_of_affected_action_groups.setter
    def count_of_affected_action_groups(self, count_of_affected_action_groups):
        """
        Sets the count_of_affected_action_groups of this SchedulerDefinitionSummary.
        Count of Action Groups affected by the Schedule.


        :param count_of_affected_action_groups: The count_of_affected_action_groups of this SchedulerDefinitionSummary.
        :type: int
        """
        self._count_of_affected_action_groups = count_of_affected_action_groups

    @property
    def count_of_affected_resources(self):
        """
        Gets the count_of_affected_resources of this SchedulerDefinitionSummary.
        Count of Resources affected by the Schedule


        :return: The count_of_affected_resources of this SchedulerDefinitionSummary.
        :rtype: int
        """
        return self._count_of_affected_resources

    @count_of_affected_resources.setter
    def count_of_affected_resources(self, count_of_affected_resources):
        """
        Sets the count_of_affected_resources of this SchedulerDefinitionSummary.
        Count of Resources affected by the Schedule


        :param count_of_affected_resources: The count_of_affected_resources of this SchedulerDefinitionSummary.
        :type: int
        """
        self._count_of_affected_resources = count_of_affected_resources

    @property
    def count_of_affected_targets(self):
        """
        Gets the count_of_affected_targets of this SchedulerDefinitionSummary.
        Count of Targets affected by the Schedule


        :return: The count_of_affected_targets of this SchedulerDefinitionSummary.
        :rtype: int
        """
        return self._count_of_affected_targets

    @count_of_affected_targets.setter
    def count_of_affected_targets(self, count_of_affected_targets):
        """
        Sets the count_of_affected_targets of this SchedulerDefinitionSummary.
        Count of Targets affected by the Schedule


        :param count_of_affected_targets: The count_of_affected_targets of this SchedulerDefinitionSummary.
        :type: int
        """
        self._count_of_affected_targets = count_of_affected_targets

    @property
    def action_group_types(self):
        """
        Gets the action_group_types of this SchedulerDefinitionSummary.
        All ActionGroup Types part of the schedule.

        Allowed values for items in this list are: "PRODUCT", "ENVIRONMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action_group_types of this SchedulerDefinitionSummary.
        :rtype: list[str]
        """
        return self._action_group_types

    @action_group_types.setter
    def action_group_types(self, action_group_types):
        """
        Sets the action_group_types of this SchedulerDefinitionSummary.
        All ActionGroup Types part of the schedule.


        :param action_group_types: The action_group_types of this SchedulerDefinitionSummary.
        :type: list[str]
        """
        allowed_values = ["PRODUCT", "ENVIRONMENT"]
        if action_group_types:
            action_group_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in action_group_types]
        self._action_group_types = action_group_types

    @property
    def application_types(self):
        """
        Gets the application_types of this SchedulerDefinitionSummary.
        All application types part of the schedule for ENVIRONMENT ActionGroup Type.


        :return: The application_types of this SchedulerDefinitionSummary.
        :rtype: list[str]
        """
        return self._application_types

    @application_types.setter
    def application_types(self, application_types):
        """
        Sets the application_types of this SchedulerDefinitionSummary.
        All application types part of the schedule for ENVIRONMENT ActionGroup Type.


        :param application_types: The application_types of this SchedulerDefinitionSummary.
        :type: list[str]
        """
        self._application_types = application_types

    @property
    def products(self):
        """
        Gets the products of this SchedulerDefinitionSummary.
        All products part of the schedule for PRODUCT ActionGroup Type.


        :return: The products of this SchedulerDefinitionSummary.
        :rtype: list[str]
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this SchedulerDefinitionSummary.
        All products part of the schedule for PRODUCT ActionGroup Type.


        :param products: The products of this SchedulerDefinitionSummary.
        :type: list[str]
        """
        self._products = products

    @property
    def lifecycle_operations(self):
        """
        Gets the lifecycle_operations of this SchedulerDefinitionSummary.
        All LifeCycle Operations part of the schedule


        :return: The lifecycle_operations of this SchedulerDefinitionSummary.
        :rtype: list[str]
        """
        return self._lifecycle_operations

    @lifecycle_operations.setter
    def lifecycle_operations(self, lifecycle_operations):
        """
        Sets the lifecycle_operations of this SchedulerDefinitionSummary.
        All LifeCycle Operations part of the schedule


        :param lifecycle_operations: The lifecycle_operations of this SchedulerDefinitionSummary.
        :type: list[str]
        """
        self._lifecycle_operations = lifecycle_operations

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SchedulerDefinitionSummary.
        The current state of the SchedulerDefinition.


        :return: The lifecycle_state of this SchedulerDefinitionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SchedulerDefinitionSummary.
        The current state of the SchedulerDefinition.


        :param lifecycle_state: The lifecycle_state of this SchedulerDefinitionSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this SchedulerDefinitionSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this SchedulerDefinitionSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SchedulerDefinitionSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this SchedulerDefinitionSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SchedulerDefinitionSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this SchedulerDefinitionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SchedulerDefinitionSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this SchedulerDefinitionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SchedulerDefinitionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this SchedulerDefinitionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SchedulerDefinitionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this SchedulerDefinitionSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SchedulerDefinitionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this SchedulerDefinitionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SchedulerDefinitionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this SchedulerDefinitionSummary.
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
