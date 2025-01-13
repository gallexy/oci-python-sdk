# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .enable_database_insight_details import EnableDatabaseInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableMacsManagedCloudDatabaseInsightDetails(EnableDatabaseInsightDetails):
    """
    The information about database to be analyzed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnableMacsManagedCloudDatabaseInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.EnableMacsManagedCloudDatabaseInsightDetails.entity_source` attribute
        of this class is ``MACS_MANAGED_CLOUD_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this EnableMacsManagedCloudDatabaseInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE", "MDS_MYSQL_DATABASE_SYSTEM", "MACS_MANAGED_CLOUD_DATABASE"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type compartment_id: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type management_agent_id: str

        :param connection_details:
            The value to assign to the connection_details property of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type connection_details: oci.opsi.models.ConnectionDetails

        :param connection_credential_details:
            The value to assign to the connection_credential_details property of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type connection_credential_details: oci.opsi.models.CredentialDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'entity_source': 'str',
            'compartment_id': 'str',
            'management_agent_id': 'str',
            'connection_details': 'ConnectionDetails',
            'connection_credential_details': 'CredentialDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'management_agent_id': 'managementAgentId',
            'connection_details': 'connectionDetails',
            'connection_credential_details': 'connectionCredentialDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._entity_source = None
        self._compartment_id = None
        self._management_agent_id = None
        self._connection_details = None
        self._connection_credential_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._entity_source = 'MACS_MANAGED_CLOUD_DATABASE'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EnableMacsManagedCloudDatabaseInsightDetails.
        The compartment `OCID`__ of the External Database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this EnableMacsManagedCloudDatabaseInsightDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EnableMacsManagedCloudDatabaseInsightDetails.
        The compartment `OCID`__ of the External Database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def management_agent_id(self):
        """
        **[Required]** Gets the management_agent_id of this EnableMacsManagedCloudDatabaseInsightDetails.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this EnableMacsManagedCloudDatabaseInsightDetails.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this EnableMacsManagedCloudDatabaseInsightDetails.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def connection_details(self):
        """
        **[Required]** Gets the connection_details of this EnableMacsManagedCloudDatabaseInsightDetails.

        :return: The connection_details of this EnableMacsManagedCloudDatabaseInsightDetails.
        :rtype: oci.opsi.models.ConnectionDetails
        """
        return self._connection_details

    @connection_details.setter
    def connection_details(self, connection_details):
        """
        Sets the connection_details of this EnableMacsManagedCloudDatabaseInsightDetails.

        :param connection_details: The connection_details of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type: oci.opsi.models.ConnectionDetails
        """
        self._connection_details = connection_details

    @property
    def connection_credential_details(self):
        """
        **[Required]** Gets the connection_credential_details of this EnableMacsManagedCloudDatabaseInsightDetails.

        :return: The connection_credential_details of this EnableMacsManagedCloudDatabaseInsightDetails.
        :rtype: oci.opsi.models.CredentialDetails
        """
        return self._connection_credential_details

    @connection_credential_details.setter
    def connection_credential_details(self, connection_credential_details):
        """
        Sets the connection_credential_details of this EnableMacsManagedCloudDatabaseInsightDetails.

        :param connection_credential_details: The connection_credential_details of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type: oci.opsi.models.CredentialDetails
        """
        self._connection_credential_details = connection_credential_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this EnableMacsManagedCloudDatabaseInsightDetails.
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
