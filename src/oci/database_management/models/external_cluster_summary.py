# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalClusterSummary(object):
    """
    The summary of an external cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalClusterSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalClusterSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalClusterSummary.
        :type display_name: str

        :param component_name:
            The value to assign to the component_name property of this ExternalClusterSummary.
        :type component_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalClusterSummary.
        :type compartment_id: str

        :param external_db_system_id:
            The value to assign to the external_db_system_id property of this ExternalClusterSummary.
        :type external_db_system_id: str

        :param external_connector_id:
            The value to assign to the external_connector_id property of this ExternalClusterSummary.
        :type external_connector_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalClusterSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalClusterSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ExternalClusterSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExternalClusterSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExternalClusterSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ExternalClusterSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ExternalClusterSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'component_name': 'str',
            'compartment_id': 'str',
            'external_db_system_id': 'str',
            'external_connector_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'component_name': 'componentName',
            'compartment_id': 'compartmentId',
            'external_db_system_id': 'externalDbSystemId',
            'external_connector_id': 'externalConnectorId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._component_name = None
        self._compartment_id = None
        self._external_db_system_id = None
        self._external_connector_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExternalClusterSummary.
        The `OCID`__ of the external cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExternalClusterSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalClusterSummary.
        The `OCID`__ of the external cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExternalClusterSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExternalClusterSummary.
        The user-friendly name for the external cluster. The name does not have to be unique.


        :return: The display_name of this ExternalClusterSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExternalClusterSummary.
        The user-friendly name for the external cluster. The name does not have to be unique.


        :param display_name: The display_name of this ExternalClusterSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def component_name(self):
        """
        **[Required]** Gets the component_name of this ExternalClusterSummary.
        The name of the external cluster.


        :return: The component_name of this ExternalClusterSummary.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """
        Sets the component_name of this ExternalClusterSummary.
        The name of the external cluster.


        :param component_name: The component_name of this ExternalClusterSummary.
        :type: str
        """
        self._component_name = component_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExternalClusterSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalClusterSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalClusterSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalClusterSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def external_db_system_id(self):
        """
        **[Required]** Gets the external_db_system_id of this ExternalClusterSummary.
        The `OCID`__ of the external DB system that the cluster is a part of.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_db_system_id of this ExternalClusterSummary.
        :rtype: str
        """
        return self._external_db_system_id

    @external_db_system_id.setter
    def external_db_system_id(self, external_db_system_id):
        """
        Sets the external_db_system_id of this ExternalClusterSummary.
        The `OCID`__ of the external DB system that the cluster is a part of.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_db_system_id: The external_db_system_id of this ExternalClusterSummary.
        :type: str
        """
        self._external_db_system_id = external_db_system_id

    @property
    def external_connector_id(self):
        """
        Gets the external_connector_id of this ExternalClusterSummary.
        The `OCID`__ of the external connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_connector_id of this ExternalClusterSummary.
        :rtype: str
        """
        return self._external_connector_id

    @external_connector_id.setter
    def external_connector_id(self, external_connector_id):
        """
        Sets the external_connector_id of this ExternalClusterSummary.
        The `OCID`__ of the external connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_connector_id: The external_connector_id of this ExternalClusterSummary.
        :type: str
        """
        self._external_connector_id = external_connector_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExternalClusterSummary.
        The current lifecycle state of the external cluster.


        :return: The lifecycle_state of this ExternalClusterSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExternalClusterSummary.
        The current lifecycle state of the external cluster.


        :param lifecycle_state: The lifecycle_state of this ExternalClusterSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExternalClusterSummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExternalClusterSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExternalClusterSummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExternalClusterSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ExternalClusterSummary.
        The date and time the external cluster was created.


        :return: The time_created of this ExternalClusterSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExternalClusterSummary.
        The date and time the external cluster was created.


        :param time_created: The time_created of this ExternalClusterSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ExternalClusterSummary.
        The date and time the external cluster was last updated.


        :return: The time_updated of this ExternalClusterSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ExternalClusterSummary.
        The date and time the external cluster was last updated.


        :param time_updated: The time_updated of this ExternalClusterSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ExternalClusterSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ExternalClusterSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExternalClusterSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ExternalClusterSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ExternalClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ExternalClusterSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExternalClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ExternalClusterSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ExternalClusterSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ExternalClusterSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ExternalClusterSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ExternalClusterSummary.
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
