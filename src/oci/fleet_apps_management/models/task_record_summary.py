# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaskRecordSummary(object):
    """
    Summary of the TaskRecord.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TaskRecordSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TaskRecordSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this TaskRecordSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TaskRecordSummary.
        :type description: str

        :param type:
            The value to assign to the type property of this TaskRecordSummary.
        :type type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TaskRecordSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this TaskRecordSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TaskRecordSummary.
        :type time_updated: datetime

        :param details:
            The value to assign to the details property of this TaskRecordSummary.
        :type details: oci.fleet_apps_management.models.Details

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TaskRecordSummary.
        :type lifecycle_details: str

        :param version:
            The value to assign to the version property of this TaskRecordSummary.
        :type version: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TaskRecordSummary.
        :type compartment_id: str

        :param resource_region:
            The value to assign to the resource_region property of this TaskRecordSummary.
        :type resource_region: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TaskRecordSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TaskRecordSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this TaskRecordSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'type': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'details': 'Details',
            'lifecycle_details': 'str',
            'version': 'str',
            'compartment_id': 'str',
            'resource_region': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'type': 'type',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'details': 'details',
            'lifecycle_details': 'lifecycleDetails',
            'version': 'version',
            'compartment_id': 'compartmentId',
            'resource_region': 'resourceRegion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._type = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._details = None
        self._lifecycle_details = None
        self._version = None
        self._compartment_id = None
        self._resource_region = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TaskRecordSummary.
        The OCID of the resource.


        :return: The id of this TaskRecordSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TaskRecordSummary.
        The OCID of the resource.


        :param id: The id of this TaskRecordSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this TaskRecordSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this TaskRecordSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TaskRecordSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this TaskRecordSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this TaskRecordSummary.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :return: The description of this TaskRecordSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TaskRecordSummary.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :param description: The description of this TaskRecordSummary.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        **[Required]** Gets the type of this TaskRecordSummary.
        Task type.


        :return: The type of this TaskRecordSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TaskRecordSummary.
        Task type.


        :param type: The type of this TaskRecordSummary.
        :type: str
        """
        self._type = type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this TaskRecordSummary.
        The current state of the TaskRecord.


        :return: The lifecycle_state of this TaskRecordSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TaskRecordSummary.
        The current state of the TaskRecord.


        :param lifecycle_state: The lifecycle_state of this TaskRecordSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this TaskRecordSummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this TaskRecordSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TaskRecordSummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this TaskRecordSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this TaskRecordSummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this TaskRecordSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TaskRecordSummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this TaskRecordSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def details(self):
        """
        **[Required]** Gets the details of this TaskRecordSummary.

        :return: The details of this TaskRecordSummary.
        :rtype: oci.fleet_apps_management.models.Details
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this TaskRecordSummary.

        :param details: The details of this TaskRecordSummary.
        :type: oci.fleet_apps_management.models.Details
        """
        self._details = details

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TaskRecordSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this TaskRecordSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TaskRecordSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this TaskRecordSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def version(self):
        """
        Gets the version of this TaskRecordSummary.
        The version of the task


        :return: The version of this TaskRecordSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this TaskRecordSummary.
        The version of the task


        :param version: The version of this TaskRecordSummary.
        :type: str
        """
        self._version = version

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TaskRecordSummary.
        OCID of the compartment to which the resource belongs to.


        :return: The compartment_id of this TaskRecordSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TaskRecordSummary.
        OCID of the compartment to which the resource belongs to.


        :param compartment_id: The compartment_id of this TaskRecordSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resource_region(self):
        """
        Gets the resource_region of this TaskRecordSummary.
        Associated region


        :return: The resource_region of this TaskRecordSummary.
        :rtype: str
        """
        return self._resource_region

    @resource_region.setter
    def resource_region(self, resource_region):
        """
        Sets the resource_region of this TaskRecordSummary.
        Associated region


        :param resource_region: The resource_region of this TaskRecordSummary.
        :type: str
        """
        self._resource_region = resource_region

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TaskRecordSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this TaskRecordSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TaskRecordSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this TaskRecordSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TaskRecordSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this TaskRecordSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TaskRecordSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this TaskRecordSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this TaskRecordSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this TaskRecordSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this TaskRecordSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this TaskRecordSummary.
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
