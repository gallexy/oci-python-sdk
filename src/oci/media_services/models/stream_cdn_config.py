# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20211101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StreamCdnConfig(object):
    """
    Configuration used for integrating with a CDN.
    """

    #: A constant which can be used with the lifecycle_state property of a StreamCdnConfig.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a StreamCdnConfig.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a StreamCdnConfig.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new StreamCdnConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this StreamCdnConfig.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this StreamCdnConfig.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this StreamCdnConfig.
        :type compartment_id: str

        :param distribution_channel_id:
            The value to assign to the distribution_channel_id property of this StreamCdnConfig.
        :type distribution_channel_id: str

        :param is_enabled:
            The value to assign to the is_enabled property of this StreamCdnConfig.
        :type is_enabled: bool

        :param config:
            The value to assign to the config property of this StreamCdnConfig.
        :type config: oci.media_services.models.StreamCdnConfigSection

        :param time_created:
            The value to assign to the time_created property of this StreamCdnConfig.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this StreamCdnConfig.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this StreamCdnConfig.
            Allowed values for this property are: "ACTIVE", "NEEDS_ATTENTION", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecyle_details:
            The value to assign to the lifecyle_details property of this StreamCdnConfig.
        :type lifecyle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this StreamCdnConfig.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this StreamCdnConfig.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this StreamCdnConfig.
        :type system_tags: dict(str, dict(str, object))

        :param locks:
            The value to assign to the locks property of this StreamCdnConfig.
        :type locks: list[oci.media_services.models.ResourceLock]

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'distribution_channel_id': 'str',
            'is_enabled': 'bool',
            'config': 'StreamCdnConfigSection',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecyle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'locks': 'list[ResourceLock]'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'distribution_channel_id': 'distributionChannelId',
            'is_enabled': 'isEnabled',
            'config': 'config',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecyle_details': 'lifecyleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'locks': 'locks'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._distribution_channel_id = None
        self._is_enabled = None
        self._config = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecyle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._locks = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this StreamCdnConfig.
        Unique identifier that is immutable on creation.


        :return: The id of this StreamCdnConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StreamCdnConfig.
        Unique identifier that is immutable on creation.


        :param id: The id of this StreamCdnConfig.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this StreamCdnConfig.
        The CDN Configuration identifier or display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this StreamCdnConfig.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this StreamCdnConfig.
        The CDN Configuration identifier or display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this StreamCdnConfig.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this StreamCdnConfig.
        Compartment Identifier.


        :return: The compartment_id of this StreamCdnConfig.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this StreamCdnConfig.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this StreamCdnConfig.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def distribution_channel_id(self):
        """
        **[Required]** Gets the distribution_channel_id of this StreamCdnConfig.
        Distribution Channel Identifier.


        :return: The distribution_channel_id of this StreamCdnConfig.
        :rtype: str
        """
        return self._distribution_channel_id

    @distribution_channel_id.setter
    def distribution_channel_id(self, distribution_channel_id):
        """
        Sets the distribution_channel_id of this StreamCdnConfig.
        Distribution Channel Identifier.


        :param distribution_channel_id: The distribution_channel_id of this StreamCdnConfig.
        :type: str
        """
        self._distribution_channel_id = distribution_channel_id

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this StreamCdnConfig.
        Whether publishing to CDN is enabled.


        :return: The is_enabled of this StreamCdnConfig.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this StreamCdnConfig.
        Whether publishing to CDN is enabled.


        :param is_enabled: The is_enabled of this StreamCdnConfig.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def config(self):
        """
        **[Required]** Gets the config of this StreamCdnConfig.

        :return: The config of this StreamCdnConfig.
        :rtype: oci.media_services.models.StreamCdnConfigSection
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this StreamCdnConfig.

        :param config: The config of this StreamCdnConfig.
        :type: oci.media_services.models.StreamCdnConfigSection
        """
        self._config = config

    @property
    def time_created(self):
        """
        Gets the time_created of this StreamCdnConfig.
        The time when the CDN Config was created. An RFC3339 formatted datetime string.


        :return: The time_created of this StreamCdnConfig.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this StreamCdnConfig.
        The time when the CDN Config was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this StreamCdnConfig.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this StreamCdnConfig.
        The time when the CDN Config was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this StreamCdnConfig.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this StreamCdnConfig.
        The time when the CDN Config was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this StreamCdnConfig.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this StreamCdnConfig.
        The current state of the CDN Configuration.

        Allowed values for this property are: "ACTIVE", "NEEDS_ATTENTION", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this StreamCdnConfig.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this StreamCdnConfig.
        The current state of the CDN Configuration.


        :param lifecycle_state: The lifecycle_state of this StreamCdnConfig.
        :type: str
        """
        allowed_values = ["ACTIVE", "NEEDS_ATTENTION", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecyle_details(self):
        """
        Gets the lifecyle_details of this StreamCdnConfig.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecyle_details of this StreamCdnConfig.
        :rtype: str
        """
        return self._lifecyle_details

    @lifecyle_details.setter
    def lifecyle_details(self, lifecyle_details):
        """
        Sets the lifecyle_details of this StreamCdnConfig.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecyle_details: The lifecyle_details of this StreamCdnConfig.
        :type: str
        """
        self._lifecyle_details = lifecyle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this StreamCdnConfig.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this StreamCdnConfig.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this StreamCdnConfig.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this StreamCdnConfig.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this StreamCdnConfig.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this StreamCdnConfig.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this StreamCdnConfig.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this StreamCdnConfig.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this StreamCdnConfig.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this StreamCdnConfig.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this StreamCdnConfig.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this StreamCdnConfig.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def locks(self):
        """
        Gets the locks of this StreamCdnConfig.
        Locks associated with this resource.


        :return: The locks of this StreamCdnConfig.
        :rtype: list[oci.media_services.models.ResourceLock]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """
        Sets the locks of this StreamCdnConfig.
        Locks associated with this resource.


        :param locks: The locks of this StreamCdnConfig.
        :type: list[oci.media_services.models.ResourceLock]
        """
        self._locks = locks

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
