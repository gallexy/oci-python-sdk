# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTargetDatabaseDetails(object):
    """
    The details used to register the database in Data Safe and to create the Data Safe target database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTargetDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateTargetDatabaseDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateTargetDatabaseDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateTargetDatabaseDetails.
        :type description: str

        :param database_details:
            The value to assign to the database_details property of this CreateTargetDatabaseDetails.
        :type database_details: oci.data_safe.models.DatabaseDetails

        :param credentials:
            The value to assign to the credentials property of this CreateTargetDatabaseDetails.
        :type credentials: oci.data_safe.models.Credentials

        :param tls_config:
            The value to assign to the tls_config property of this CreateTargetDatabaseDetails.
        :type tls_config: oci.data_safe.models.TlsConfig

        :param connection_option:
            The value to assign to the connection_option property of this CreateTargetDatabaseDetails.
        :type connection_option: oci.data_safe.models.ConnectionOption

        :param peer_target_database_details:
            The value to assign to the peer_target_database_details property of this CreateTargetDatabaseDetails.
        :type peer_target_database_details: list[oci.data_safe.models.CreatePeerTargetDatabaseDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateTargetDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateTargetDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'database_details': 'DatabaseDetails',
            'credentials': 'Credentials',
            'tls_config': 'TlsConfig',
            'connection_option': 'ConnectionOption',
            'peer_target_database_details': 'list[CreatePeerTargetDatabaseDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'database_details': 'databaseDetails',
            'credentials': 'credentials',
            'tls_config': 'tlsConfig',
            'connection_option': 'connectionOption',
            'peer_target_database_details': 'peerTargetDatabaseDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._database_details = None
        self._credentials = None
        self._tls_config = None
        self._connection_option = None
        self._peer_target_database_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateTargetDatabaseDetails.
        The OCID of the compartment in which to create the Data Safe target database.


        :return: The compartment_id of this CreateTargetDatabaseDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateTargetDatabaseDetails.
        The OCID of the compartment in which to create the Data Safe target database.


        :param compartment_id: The compartment_id of this CreateTargetDatabaseDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateTargetDatabaseDetails.
        The display name of the target database in Data Safe. The name is modifiable and does not need to be unique.


        :return: The display_name of this CreateTargetDatabaseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateTargetDatabaseDetails.
        The display name of the target database in Data Safe. The name is modifiable and does not need to be unique.


        :param display_name: The display_name of this CreateTargetDatabaseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateTargetDatabaseDetails.
        The description of the target database in Data Safe.


        :return: The description of this CreateTargetDatabaseDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTargetDatabaseDetails.
        The description of the target database in Data Safe.


        :param description: The description of this CreateTargetDatabaseDetails.
        :type: str
        """
        self._description = description

    @property
    def database_details(self):
        """
        **[Required]** Gets the database_details of this CreateTargetDatabaseDetails.

        :return: The database_details of this CreateTargetDatabaseDetails.
        :rtype: oci.data_safe.models.DatabaseDetails
        """
        return self._database_details

    @database_details.setter
    def database_details(self, database_details):
        """
        Sets the database_details of this CreateTargetDatabaseDetails.

        :param database_details: The database_details of this CreateTargetDatabaseDetails.
        :type: oci.data_safe.models.DatabaseDetails
        """
        self._database_details = database_details

    @property
    def credentials(self):
        """
        Gets the credentials of this CreateTargetDatabaseDetails.

        :return: The credentials of this CreateTargetDatabaseDetails.
        :rtype: oci.data_safe.models.Credentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this CreateTargetDatabaseDetails.

        :param credentials: The credentials of this CreateTargetDatabaseDetails.
        :type: oci.data_safe.models.Credentials
        """
        self._credentials = credentials

    @property
    def tls_config(self):
        """
        Gets the tls_config of this CreateTargetDatabaseDetails.

        :return: The tls_config of this CreateTargetDatabaseDetails.
        :rtype: oci.data_safe.models.TlsConfig
        """
        return self._tls_config

    @tls_config.setter
    def tls_config(self, tls_config):
        """
        Sets the tls_config of this CreateTargetDatabaseDetails.

        :param tls_config: The tls_config of this CreateTargetDatabaseDetails.
        :type: oci.data_safe.models.TlsConfig
        """
        self._tls_config = tls_config

    @property
    def connection_option(self):
        """
        Gets the connection_option of this CreateTargetDatabaseDetails.

        :return: The connection_option of this CreateTargetDatabaseDetails.
        :rtype: oci.data_safe.models.ConnectionOption
        """
        return self._connection_option

    @connection_option.setter
    def connection_option(self, connection_option):
        """
        Sets the connection_option of this CreateTargetDatabaseDetails.

        :param connection_option: The connection_option of this CreateTargetDatabaseDetails.
        :type: oci.data_safe.models.ConnectionOption
        """
        self._connection_option = connection_option

    @property
    def peer_target_database_details(self):
        """
        Gets the peer_target_database_details of this CreateTargetDatabaseDetails.
        The details of the database to be registered as a peer target database.


        :return: The peer_target_database_details of this CreateTargetDatabaseDetails.
        :rtype: list[oci.data_safe.models.CreatePeerTargetDatabaseDetails]
        """
        return self._peer_target_database_details

    @peer_target_database_details.setter
    def peer_target_database_details(self, peer_target_database_details):
        """
        Sets the peer_target_database_details of this CreateTargetDatabaseDetails.
        The details of the database to be registered as a peer target database.


        :param peer_target_database_details: The peer_target_database_details of this CreateTargetDatabaseDetails.
        :type: list[oci.data_safe.models.CreatePeerTargetDatabaseDetails]
        """
        self._peer_target_database_details = peer_target_database_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateTargetDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateTargetDatabaseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateTargetDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateTargetDatabaseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateTargetDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateTargetDatabaseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateTargetDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateTargetDatabaseDetails.
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
