# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221208


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCccInfrastructureDetails(object):
    """
    The configuration details for creating Compute Cloud@Customer infrastructure.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCccInfrastructureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateCccInfrastructureDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateCccInfrastructureDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCccInfrastructureDetails.
        :type compartment_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateCccInfrastructureDetails.
        :type subnet_id: str

        :param connection_state:
            The value to assign to the connection_state property of this CreateCccInfrastructureDetails.
        :type connection_state: str

        :param connection_details:
            The value to assign to the connection_details property of this CreateCccInfrastructureDetails.
        :type connection_details: str

        :param ccc_upgrade_schedule_id:
            The value to assign to the ccc_upgrade_schedule_id property of this CreateCccInfrastructureDetails.
        :type ccc_upgrade_schedule_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCccInfrastructureDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCccInfrastructureDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'subnet_id': 'str',
            'connection_state': 'str',
            'connection_details': 'str',
            'ccc_upgrade_schedule_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'subnet_id': 'subnetId',
            'connection_state': 'connectionState',
            'connection_details': 'connectionDetails',
            'ccc_upgrade_schedule_id': 'cccUpgradeScheduleId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._subnet_id = None
        self._connection_state = None
        self._connection_details = None
        self._ccc_upgrade_schedule_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateCccInfrastructureDetails.
        The name that will be used to display the Compute Cloud@Customer infrastructure
        in the Oracle Cloud Infrastructure console. Does not have to be unique and can be changed.
        Avoid entering confidential information.


        :return: The display_name of this CreateCccInfrastructureDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCccInfrastructureDetails.
        The name that will be used to display the Compute Cloud@Customer infrastructure
        in the Oracle Cloud Infrastructure console. Does not have to be unique and can be changed.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateCccInfrastructureDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateCccInfrastructureDetails.
        A mutable client-meaningful text description of the Compute Cloud@Customer infrastructure.
        Avoid entering confidential information.


        :return: The description of this CreateCccInfrastructureDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateCccInfrastructureDetails.
        A mutable client-meaningful text description of the Compute Cloud@Customer infrastructure.
        Avoid entering confidential information.


        :param description: The description of this CreateCccInfrastructureDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCccInfrastructureDetails.
        The compartment `OCID`__ associated with
        the infrastructure.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateCccInfrastructureDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCccInfrastructureDetails.
        The compartment `OCID`__ associated with
        the infrastructure.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateCccInfrastructureDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateCccInfrastructureDetails.
        Identifier for network subnet that will be used to communicate with Compute Cloud@Customer infrastructure.


        :return: The subnet_id of this CreateCccInfrastructureDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateCccInfrastructureDetails.
        Identifier for network subnet that will be used to communicate with Compute Cloud@Customer infrastructure.


        :param subnet_id: The subnet_id of this CreateCccInfrastructureDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def connection_state(self):
        """
        Gets the connection_state of this CreateCccInfrastructureDetails.
        The current connection state of the Compute Cloud@Customer infrastructure. This value
        will default to REJECT if the value is not provided. The only valid value at creation
        time is REJECT.


        :return: The connection_state of this CreateCccInfrastructureDetails.
        :rtype: str
        """
        return self._connection_state

    @connection_state.setter
    def connection_state(self, connection_state):
        """
        Sets the connection_state of this CreateCccInfrastructureDetails.
        The current connection state of the Compute Cloud@Customer infrastructure. This value
        will default to REJECT if the value is not provided. The only valid value at creation
        time is REJECT.


        :param connection_state: The connection_state of this CreateCccInfrastructureDetails.
        :type: str
        """
        self._connection_state = connection_state

    @property
    def connection_details(self):
        """
        Gets the connection_details of this CreateCccInfrastructureDetails.
        A message describing the current connection state in more detail.


        :return: The connection_details of this CreateCccInfrastructureDetails.
        :rtype: str
        """
        return self._connection_details

    @connection_details.setter
    def connection_details(self, connection_details):
        """
        Sets the connection_details of this CreateCccInfrastructureDetails.
        A message describing the current connection state in more detail.


        :param connection_details: The connection_details of this CreateCccInfrastructureDetails.
        :type: str
        """
        self._connection_details = connection_details

    @property
    def ccc_upgrade_schedule_id(self):
        """
        Gets the ccc_upgrade_schedule_id of this CreateCccInfrastructureDetails.
        Schedule used for upgrades. If no schedule is associated with the infrastructure,
        it can be upgraded at any time.


        :return: The ccc_upgrade_schedule_id of this CreateCccInfrastructureDetails.
        :rtype: str
        """
        return self._ccc_upgrade_schedule_id

    @ccc_upgrade_schedule_id.setter
    def ccc_upgrade_schedule_id(self, ccc_upgrade_schedule_id):
        """
        Sets the ccc_upgrade_schedule_id of this CreateCccInfrastructureDetails.
        Schedule used for upgrades. If no schedule is associated with the infrastructure,
        it can be upgraded at any time.


        :param ccc_upgrade_schedule_id: The ccc_upgrade_schedule_id of this CreateCccInfrastructureDetails.
        :type: str
        """
        self._ccc_upgrade_schedule_id = ccc_upgrade_schedule_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCccInfrastructureDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateCccInfrastructureDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCccInfrastructureDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateCccInfrastructureDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCccInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateCccInfrastructureDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCccInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateCccInfrastructureDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
