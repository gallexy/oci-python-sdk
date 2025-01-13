# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SchedulingPlanSummary(object):
    """
    Details of a Scheduling Plan.
    """

    #: A constant which can be used with the lifecycle_state property of a SchedulingPlanSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SchedulingPlanSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a SchedulingPlanSummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a SchedulingPlanSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SchedulingPlanSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a SchedulingPlanSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SchedulingPlanSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the plan_intent property of a SchedulingPlanSummary.
    #: This constant has a value of "EXADATA_INFRASTRUCTURE_FULL_SOFTWARE_UPDATE"
    PLAN_INTENT_EXADATA_INFRASTRUCTURE_FULL_SOFTWARE_UPDATE = "EXADATA_INFRASTRUCTURE_FULL_SOFTWARE_UPDATE"

    #: A constant which can be used with the service_type property of a SchedulingPlanSummary.
    #: This constant has a value of "EXACC"
    SERVICE_TYPE_EXACC = "EXACC"

    #: A constant which can be used with the service_type property of a SchedulingPlanSummary.
    #: This constant has a value of "EXACS"
    SERVICE_TYPE_EXACS = "EXACS"

    #: A constant which can be used with the service_type property of a SchedulingPlanSummary.
    #: This constant has a value of "FPPPCS"
    SERVICE_TYPE_FPPPCS = "FPPPCS"

    def __init__(self, **kwargs):
        """
        Initializes a new SchedulingPlanSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SchedulingPlanSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SchedulingPlanSummary.
        :type compartment_id: str

        :param scheduling_policy_id:
            The value to assign to the scheduling_policy_id property of this SchedulingPlanSummary.
        :type scheduling_policy_id: str

        :param resource_id:
            The value to assign to the resource_id property of this SchedulingPlanSummary.
        :type resource_id: str

        :param display_name:
            The value to assign to the display_name property of this SchedulingPlanSummary.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SchedulingPlanSummary.
            Allowed values for this property are: "CREATING", "NEEDS_ATTENTION", "AVAILABLE", "UPDATING", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SchedulingPlanSummary.
        :type lifecycle_details: str

        :param is_using_recommended_scheduled_actions:
            The value to assign to the is_using_recommended_scheduled_actions property of this SchedulingPlanSummary.
        :type is_using_recommended_scheduled_actions: bool

        :param plan_intent:
            The value to assign to the plan_intent property of this SchedulingPlanSummary.
            Allowed values for this property are: "EXADATA_INFRASTRUCTURE_FULL_SOFTWARE_UPDATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type plan_intent: str

        :param estimated_time_in_mins:
            The value to assign to the estimated_time_in_mins property of this SchedulingPlanSummary.
        :type estimated_time_in_mins: int

        :param service_type:
            The value to assign to the service_type property of this SchedulingPlanSummary.
            Allowed values for this property are: "EXACC", "EXACS", "FPPPCS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type service_type: str

        :param time_created:
            The value to assign to the time_created property of this SchedulingPlanSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SchedulingPlanSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SchedulingPlanSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SchedulingPlanSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SchedulingPlanSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'scheduling_policy_id': 'str',
            'resource_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'is_using_recommended_scheduled_actions': 'bool',
            'plan_intent': 'str',
            'estimated_time_in_mins': 'int',
            'service_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'scheduling_policy_id': 'schedulingPolicyId',
            'resource_id': 'resourceId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'is_using_recommended_scheduled_actions': 'isUsingRecommendedScheduledActions',
            'plan_intent': 'planIntent',
            'estimated_time_in_mins': 'estimatedTimeInMins',
            'service_type': 'serviceType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._scheduling_policy_id = None
        self._resource_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._is_using_recommended_scheduled_actions = None
        self._plan_intent = None
        self._estimated_time_in_mins = None
        self._service_type = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SchedulingPlanSummary.
        The `OCID`__ of the Scheduling Plan.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this SchedulingPlanSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SchedulingPlanSummary.
        The `OCID`__ of the Scheduling Plan.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this SchedulingPlanSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SchedulingPlanSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this SchedulingPlanSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SchedulingPlanSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this SchedulingPlanSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def scheduling_policy_id(self):
        """
        **[Required]** Gets the scheduling_policy_id of this SchedulingPlanSummary.
        The `OCID`__ of the Scheduling Policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The scheduling_policy_id of this SchedulingPlanSummary.
        :rtype: str
        """
        return self._scheduling_policy_id

    @scheduling_policy_id.setter
    def scheduling_policy_id(self, scheduling_policy_id):
        """
        Sets the scheduling_policy_id of this SchedulingPlanSummary.
        The `OCID`__ of the Scheduling Policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param scheduling_policy_id: The scheduling_policy_id of this SchedulingPlanSummary.
        :type: str
        """
        self._scheduling_policy_id = scheduling_policy_id

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this SchedulingPlanSummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The resource_id of this SchedulingPlanSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this SchedulingPlanSummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param resource_id: The resource_id of this SchedulingPlanSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def display_name(self):
        """
        Gets the display_name of this SchedulingPlanSummary.
        The display name of the Scheduling Plan.


        :return: The display_name of this SchedulingPlanSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SchedulingPlanSummary.
        The display name of the Scheduling Plan.


        :param display_name: The display_name of this SchedulingPlanSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SchedulingPlanSummary.
        The current state of the Scheduling Plan. Valid states are CREATING, NEEDS_ATTENTION, AVAILABLE, UPDATING, FAILED, DELETING and DELETED.

        Allowed values for this property are: "CREATING", "NEEDS_ATTENTION", "AVAILABLE", "UPDATING", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SchedulingPlanSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SchedulingPlanSummary.
        The current state of the Scheduling Plan. Valid states are CREATING, NEEDS_ATTENTION, AVAILABLE, UPDATING, FAILED, DELETING and DELETED.


        :param lifecycle_state: The lifecycle_state of this SchedulingPlanSummary.
        :type: str
        """
        allowed_values = ["CREATING", "NEEDS_ATTENTION", "AVAILABLE", "UPDATING", "FAILED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this SchedulingPlanSummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this SchedulingPlanSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SchedulingPlanSummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this SchedulingPlanSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def is_using_recommended_scheduled_actions(self):
        """
        Gets the is_using_recommended_scheduled_actions of this SchedulingPlanSummary.
        If true, recommended scheduled actions will be generated for the scheduling plan.


        :return: The is_using_recommended_scheduled_actions of this SchedulingPlanSummary.
        :rtype: bool
        """
        return self._is_using_recommended_scheduled_actions

    @is_using_recommended_scheduled_actions.setter
    def is_using_recommended_scheduled_actions(self, is_using_recommended_scheduled_actions):
        """
        Sets the is_using_recommended_scheduled_actions of this SchedulingPlanSummary.
        If true, recommended scheduled actions will be generated for the scheduling plan.


        :param is_using_recommended_scheduled_actions: The is_using_recommended_scheduled_actions of this SchedulingPlanSummary.
        :type: bool
        """
        self._is_using_recommended_scheduled_actions = is_using_recommended_scheduled_actions

    @property
    def plan_intent(self):
        """
        Gets the plan_intent of this SchedulingPlanSummary.
        The current intent the Scheduling Plan. Valid states is EXADATA_INFRASTRUCTURE_FULL_SOFTWARE_UPDATE.

        Allowed values for this property are: "EXADATA_INFRASTRUCTURE_FULL_SOFTWARE_UPDATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The plan_intent of this SchedulingPlanSummary.
        :rtype: str
        """
        return self._plan_intent

    @plan_intent.setter
    def plan_intent(self, plan_intent):
        """
        Sets the plan_intent of this SchedulingPlanSummary.
        The current intent the Scheduling Plan. Valid states is EXADATA_INFRASTRUCTURE_FULL_SOFTWARE_UPDATE.


        :param plan_intent: The plan_intent of this SchedulingPlanSummary.
        :type: str
        """
        allowed_values = ["EXADATA_INFRASTRUCTURE_FULL_SOFTWARE_UPDATE"]
        if not value_allowed_none_or_none_sentinel(plan_intent, allowed_values):
            plan_intent = 'UNKNOWN_ENUM_VALUE'
        self._plan_intent = plan_intent

    @property
    def estimated_time_in_mins(self):
        """
        Gets the estimated_time_in_mins of this SchedulingPlanSummary.
        The estimated time for the Scheduling Plan.


        :return: The estimated_time_in_mins of this SchedulingPlanSummary.
        :rtype: int
        """
        return self._estimated_time_in_mins

    @estimated_time_in_mins.setter
    def estimated_time_in_mins(self, estimated_time_in_mins):
        """
        Sets the estimated_time_in_mins of this SchedulingPlanSummary.
        The estimated time for the Scheduling Plan.


        :param estimated_time_in_mins: The estimated_time_in_mins of this SchedulingPlanSummary.
        :type: int
        """
        self._estimated_time_in_mins = estimated_time_in_mins

    @property
    def service_type(self):
        """
        **[Required]** Gets the service_type of this SchedulingPlanSummary.
        The service type of the Scheduling Plan.

        Allowed values for this property are: "EXACC", "EXACS", "FPPPCS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The service_type of this SchedulingPlanSummary.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """
        Sets the service_type of this SchedulingPlanSummary.
        The service type of the Scheduling Plan.


        :param service_type: The service_type of this SchedulingPlanSummary.
        :type: str
        """
        allowed_values = ["EXACC", "EXACS", "FPPPCS"]
        if not value_allowed_none_or_none_sentinel(service_type, allowed_values):
            service_type = 'UNKNOWN_ENUM_VALUE'
        self._service_type = service_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SchedulingPlanSummary.
        The date and time the Scheduling Plan Resource was created.


        :return: The time_created of this SchedulingPlanSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SchedulingPlanSummary.
        The date and time the Scheduling Plan Resource was created.


        :param time_created: The time_created of this SchedulingPlanSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this SchedulingPlanSummary.
        The date and time the Scheduling Plan Resource was updated.


        :return: The time_updated of this SchedulingPlanSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SchedulingPlanSummary.
        The date and time the Scheduling Plan Resource was updated.


        :param time_updated: The time_updated of this SchedulingPlanSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SchedulingPlanSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SchedulingPlanSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SchedulingPlanSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SchedulingPlanSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SchedulingPlanSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SchedulingPlanSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SchedulingPlanSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SchedulingPlanSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SchedulingPlanSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this SchedulingPlanSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SchedulingPlanSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this SchedulingPlanSummary.
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
