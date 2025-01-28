# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMySqlDatabaseConnectorDetails(object):
    """
    Update Details of external database connector.
    """

    #: A constant which can be used with the credential_type property of a UpdateMySqlDatabaseConnectorDetails.
    #: This constant has a value of "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS"
    CREDENTIAL_TYPE_MYSQL_EXTERNAL_NON_SSL_CREDENTIALS = "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS"

    #: A constant which can be used with the credential_type property of a UpdateMySqlDatabaseConnectorDetails.
    #: This constant has a value of "MYSQL_EXTERNAL_SSL_CREDENTIALS"
    CREDENTIAL_TYPE_MYSQL_EXTERNAL_SSL_CREDENTIALS = "MYSQL_EXTERNAL_SSL_CREDENTIALS"

    #: A constant which can be used with the credential_type property of a UpdateMySqlDatabaseConnectorDetails.
    #: This constant has a value of "MYSQL_EXTERNAL_SOCKET_CREDENTIALS"
    CREDENTIAL_TYPE_MYSQL_EXTERNAL_SOCKET_CREDENTIALS = "MYSQL_EXTERNAL_SOCKET_CREDENTIALS"

    #: A constant which can be used with the network_protocol property of a UpdateMySqlDatabaseConnectorDetails.
    #: This constant has a value of "TCP"
    NETWORK_PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the network_protocol property of a UpdateMySqlDatabaseConnectorDetails.
    #: This constant has a value of "TCPS"
    NETWORK_PROTOCOL_TCPS = "TCPS"

    #: A constant which can be used with the network_protocol property of a UpdateMySqlDatabaseConnectorDetails.
    #: This constant has a value of "SOCKETS"
    NETWORK_PROTOCOL_SOCKETS = "SOCKETS"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMySqlDatabaseConnectorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateMySqlDatabaseConnectorDetails.
        :type display_name: str

        :param macs_agent_id:
            The value to assign to the macs_agent_id property of this UpdateMySqlDatabaseConnectorDetails.
        :type macs_agent_id: str

        :param host_name:
            The value to assign to the host_name property of this UpdateMySqlDatabaseConnectorDetails.
        :type host_name: str

        :param port:
            The value to assign to the port property of this UpdateMySqlDatabaseConnectorDetails.
        :type port: int

        :param credential_type:
            The value to assign to the credential_type property of this UpdateMySqlDatabaseConnectorDetails.
            Allowed values for this property are: "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SOCKET_CREDENTIALS"
        :type credential_type: str

        :param ssl_secret_id:
            The value to assign to the ssl_secret_id property of this UpdateMySqlDatabaseConnectorDetails.
        :type ssl_secret_id: str

        :param network_protocol:
            The value to assign to the network_protocol property of this UpdateMySqlDatabaseConnectorDetails.
            Allowed values for this property are: "TCP", "TCPS", "SOCKETS"
        :type network_protocol: str

        :param external_database_id:
            The value to assign to the external_database_id property of this UpdateMySqlDatabaseConnectorDetails.
        :type external_database_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'macs_agent_id': 'str',
            'host_name': 'str',
            'port': 'int',
            'credential_type': 'str',
            'ssl_secret_id': 'str',
            'network_protocol': 'str',
            'external_database_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'macs_agent_id': 'macsAgentId',
            'host_name': 'hostName',
            'port': 'port',
            'credential_type': 'credentialType',
            'ssl_secret_id': 'sslSecretId',
            'network_protocol': 'networkProtocol',
            'external_database_id': 'externalDatabaseId'
        }

        self._display_name = None
        self._macs_agent_id = None
        self._host_name = None
        self._port = None
        self._credential_type = None
        self._ssl_secret_id = None
        self._network_protocol = None
        self._external_database_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateMySqlDatabaseConnectorDetails.
        External MySQL Database Connector Name.


        :return: The display_name of this UpdateMySqlDatabaseConnectorDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateMySqlDatabaseConnectorDetails.
        External MySQL Database Connector Name.


        :param display_name: The display_name of this UpdateMySqlDatabaseConnectorDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def macs_agent_id(self):
        """
        **[Required]** Gets the macs_agent_id of this UpdateMySqlDatabaseConnectorDetails.
        Agent Id of the MACS agent.


        :return: The macs_agent_id of this UpdateMySqlDatabaseConnectorDetails.
        :rtype: str
        """
        return self._macs_agent_id

    @macs_agent_id.setter
    def macs_agent_id(self, macs_agent_id):
        """
        Sets the macs_agent_id of this UpdateMySqlDatabaseConnectorDetails.
        Agent Id of the MACS agent.


        :param macs_agent_id: The macs_agent_id of this UpdateMySqlDatabaseConnectorDetails.
        :type: str
        """
        self._macs_agent_id = macs_agent_id

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this UpdateMySqlDatabaseConnectorDetails.
        Host name for Connector.


        :return: The host_name of this UpdateMySqlDatabaseConnectorDetails.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this UpdateMySqlDatabaseConnectorDetails.
        Host name for Connector.


        :param host_name: The host_name of this UpdateMySqlDatabaseConnectorDetails.
        :type: str
        """
        self._host_name = host_name

    @property
    def port(self):
        """
        **[Required]** Gets the port of this UpdateMySqlDatabaseConnectorDetails.
        Port number to connect to External MySQL Database.


        :return: The port of this UpdateMySqlDatabaseConnectorDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateMySqlDatabaseConnectorDetails.
        Port number to connect to External MySQL Database.


        :param port: The port of this UpdateMySqlDatabaseConnectorDetails.
        :type: int
        """
        self._port = port

    @property
    def credential_type(self):
        """
        Gets the credential_type of this UpdateMySqlDatabaseConnectorDetails.
        Type of the credential.

        Allowed values for this property are: "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SOCKET_CREDENTIALS"


        :return: The credential_type of this UpdateMySqlDatabaseConnectorDetails.
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """
        Sets the credential_type of this UpdateMySqlDatabaseConnectorDetails.
        Type of the credential.


        :param credential_type: The credential_type of this UpdateMySqlDatabaseConnectorDetails.
        :type: str
        """
        allowed_values = ["MYSQL_EXTERNAL_NON_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SOCKET_CREDENTIALS"]
        if not value_allowed_none_or_none_sentinel(credential_type, allowed_values):
            raise ValueError(
                f"Invalid value for `credential_type`, must be None or one of {allowed_values}"
            )
        self._credential_type = credential_type

    @property
    def ssl_secret_id(self):
        """
        **[Required]** Gets the ssl_secret_id of this UpdateMySqlDatabaseConnectorDetails.
        If using existing SSL secret to connect, OCID for the secret resource.


        :return: The ssl_secret_id of this UpdateMySqlDatabaseConnectorDetails.
        :rtype: str
        """
        return self._ssl_secret_id

    @ssl_secret_id.setter
    def ssl_secret_id(self, ssl_secret_id):
        """
        Sets the ssl_secret_id of this UpdateMySqlDatabaseConnectorDetails.
        If using existing SSL secret to connect, OCID for the secret resource.


        :param ssl_secret_id: The ssl_secret_id of this UpdateMySqlDatabaseConnectorDetails.
        :type: str
        """
        self._ssl_secret_id = ssl_secret_id

    @property
    def network_protocol(self):
        """
        **[Required]** Gets the network_protocol of this UpdateMySqlDatabaseConnectorDetails.
        Protocol to be used to connect to External MySQL Database; TCP, TCP with SSL or Socket.

        Allowed values for this property are: "TCP", "TCPS", "SOCKETS"


        :return: The network_protocol of this UpdateMySqlDatabaseConnectorDetails.
        :rtype: str
        """
        return self._network_protocol

    @network_protocol.setter
    def network_protocol(self, network_protocol):
        """
        Sets the network_protocol of this UpdateMySqlDatabaseConnectorDetails.
        Protocol to be used to connect to External MySQL Database; TCP, TCP with SSL or Socket.


        :param network_protocol: The network_protocol of this UpdateMySqlDatabaseConnectorDetails.
        :type: str
        """
        allowed_values = ["TCP", "TCPS", "SOCKETS"]
        if not value_allowed_none_or_none_sentinel(network_protocol, allowed_values):
            raise ValueError(
                f"Invalid value for `network_protocol`, must be None or one of {allowed_values}"
            )
        self._network_protocol = network_protocol

    @property
    def external_database_id(self):
        """
        Gets the external_database_id of this UpdateMySqlDatabaseConnectorDetails.
        OCID of MySQL Database resource.


        :return: The external_database_id of this UpdateMySqlDatabaseConnectorDetails.
        :rtype: str
        """
        return self._external_database_id

    @external_database_id.setter
    def external_database_id(self, external_database_id):
        """
        Sets the external_database_id of this UpdateMySqlDatabaseConnectorDetails.
        OCID of MySQL Database resource.


        :param external_database_id: The external_database_id of this UpdateMySqlDatabaseConnectorDetails.
        :type: str
        """
        self._external_database_id = external_database_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
