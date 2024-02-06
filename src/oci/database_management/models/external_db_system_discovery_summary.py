# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalDbSystemDiscoverySummary(object):
    """
    The summary of an external DB system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalDbSystemDiscoverySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalDbSystemDiscoverySummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalDbSystemDiscoverySummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalDbSystemDiscoverySummary.
        :type compartment_id: str

        :param agent_id:
            The value to assign to the agent_id property of this ExternalDbSystemDiscoverySummary.
        :type agent_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalDbSystemDiscoverySummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalDbSystemDiscoverySummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ExternalDbSystemDiscoverySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExternalDbSystemDiscoverySummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'agent_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'agent_id': 'agentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._agent_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExternalDbSystemDiscoverySummary.
        The `OCID`__ of the external DB system discovery.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExternalDbSystemDiscoverySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalDbSystemDiscoverySummary.
        The `OCID`__ of the external DB system discovery.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExternalDbSystemDiscoverySummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExternalDbSystemDiscoverySummary.
        The user-friendly name for the DB system. The name does not have to be unique.


        :return: The display_name of this ExternalDbSystemDiscoverySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExternalDbSystemDiscoverySummary.
        The user-friendly name for the DB system. The name does not have to be unique.


        :param display_name: The display_name of this ExternalDbSystemDiscoverySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExternalDbSystemDiscoverySummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalDbSystemDiscoverySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalDbSystemDiscoverySummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalDbSystemDiscoverySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def agent_id(self):
        """
        **[Required]** Gets the agent_id of this ExternalDbSystemDiscoverySummary.
        The `OCID`__ of the management agent
        used for the external DB system discovery.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The agent_id of this ExternalDbSystemDiscoverySummary.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this ExternalDbSystemDiscoverySummary.
        The `OCID`__ of the management agent
        used for the external DB system discovery.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param agent_id: The agent_id of this ExternalDbSystemDiscoverySummary.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExternalDbSystemDiscoverySummary.
        The current lifecycle state of the external DB system discovery resource.


        :return: The lifecycle_state of this ExternalDbSystemDiscoverySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExternalDbSystemDiscoverySummary.
        The current lifecycle state of the external DB system discovery resource.


        :param lifecycle_state: The lifecycle_state of this ExternalDbSystemDiscoverySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExternalDbSystemDiscoverySummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExternalDbSystemDiscoverySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExternalDbSystemDiscoverySummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExternalDbSystemDiscoverySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ExternalDbSystemDiscoverySummary.
        The date and time the external DB system discovery was created.


        :return: The time_created of this ExternalDbSystemDiscoverySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExternalDbSystemDiscoverySummary.
        The date and time the external DB system discovery was created.


        :param time_created: The time_created of this ExternalDbSystemDiscoverySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ExternalDbSystemDiscoverySummary.
        The date and time the external DB system discovery was last updated.


        :return: The time_updated of this ExternalDbSystemDiscoverySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ExternalDbSystemDiscoverySummary.
        The date and time the external DB system discovery was last updated.


        :param time_updated: The time_updated of this ExternalDbSystemDiscoverySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other