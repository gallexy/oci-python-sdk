# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ToolSummary(object):
    """
    Summary information of a Tool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ToolSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ToolSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ToolSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ToolSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ToolSummary.
        :type time_updated: datetime

        :param display_name:
            The value to assign to the display_name property of this ToolSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ToolSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ToolSummary.
        :type compartment_id: str

        :param agent_id:
            The value to assign to the agent_id property of this ToolSummary.
        :type agent_id: str

        :param tool_config:
            The value to assign to the tool_config property of this ToolSummary.
        :type tool_config: oci.generative_ai_agent.models.ToolConfig

        :param metadata:
            The value to assign to the metadata property of this ToolSummary.
        :type metadata: dict(str, str)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ToolSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ToolSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ToolSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'agent_id': 'str',
            'tool_config': 'ToolConfig',
            'metadata': 'dict(str, str)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'agent_id': 'agentId',
            'tool_config': 'toolConfig',
            'metadata': 'metadata',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._agent_id = None
        self._tool_config = None
        self._metadata = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ToolSummary.
        The `OCID`__ of the Tool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ToolSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ToolSummary.
        The `OCID`__ of the Tool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ToolSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ToolSummary.
        The current state of the agent.


        :return: The lifecycle_state of this ToolSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ToolSummary.
        The current state of the agent.


        :param lifecycle_state: The lifecycle_state of this ToolSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ToolSummary.
        The date and time the Tool was created, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ToolSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ToolSummary.
        The date and time the Tool was created, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ToolSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ToolSummary.
        The date and time the Tool was updated, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ToolSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ToolSummary.
        The date and time the Tool was updated, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ToolSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def display_name(self):
        """
        Gets the display_name of this ToolSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this ToolSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ToolSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this ToolSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ToolSummary.
        Description about the Tool.


        :return: The description of this ToolSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ToolSummary.
        Description about the Tool.


        :param description: The description of this ToolSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ToolSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ToolSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ToolSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ToolSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def agent_id(self):
        """
        **[Required]** Gets the agent_id of this ToolSummary.
        The OCID of the agent that this Tool is attached to.


        :return: The agent_id of this ToolSummary.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this ToolSummary.
        The OCID of the agent that this Tool is attached to.


        :param agent_id: The agent_id of this ToolSummary.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def tool_config(self):
        """
        **[Required]** Gets the tool_config of this ToolSummary.

        :return: The tool_config of this ToolSummary.
        :rtype: oci.generative_ai_agent.models.ToolConfig
        """
        return self._tool_config

    @tool_config.setter
    def tool_config(self, tool_config):
        """
        Sets the tool_config of this ToolSummary.

        :param tool_config: The tool_config of this ToolSummary.
        :type: oci.generative_ai_agent.models.ToolConfig
        """
        self._tool_config = tool_config

    @property
    def metadata(self):
        """
        Gets the metadata of this ToolSummary.
        Key-value pairs to allow additional configurations.


        :return: The metadata of this ToolSummary.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this ToolSummary.
        Key-value pairs to allow additional configurations.


        :param metadata: The metadata of this ToolSummary.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ToolSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ToolSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ToolSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ToolSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ToolSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ToolSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ToolSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ToolSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ToolSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ToolSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ToolSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ToolSummary.
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
