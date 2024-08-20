# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .database_connection_string_details import DatabaseConnectionStringDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BasicDatabaseConnectionStringDetails(DatabaseConnectionStringDetails):
    """
    The details of the Oracle Database basic connection string.
    """

    #: A constant which can be used with the protocol property of a BasicDatabaseConnectionStringDetails.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the protocol property of a BasicDatabaseConnectionStringDetails.
    #: This constant has a value of "TCPS"
    PROTOCOL_TCPS = "TCPS"

    def __init__(self, **kwargs):
        """
        Initializes a new BasicDatabaseConnectionStringDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.BasicDatabaseConnectionStringDetails.connection_type` attribute
        of this class is ``BASIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this BasicDatabaseConnectionStringDetails.
            Allowed values for this property are: "BASIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param service:
            The value to assign to the service property of this BasicDatabaseConnectionStringDetails.
        :type service: str

        :param port:
            The value to assign to the port property of this BasicDatabaseConnectionStringDetails.
        :type port: int

        :param protocol:
            The value to assign to the protocol property of this BasicDatabaseConnectionStringDetails.
            Allowed values for this property are: "TCP", "TCPS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'service': 'str',
            'port': 'int',
            'protocol': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'service': 'service',
            'port': 'port',
            'protocol': 'protocol'
        }

        self._connection_type = None
        self._service = None
        self._port = None
        self._protocol = None
        self._connection_type = 'BASIC'

    @property
    def service(self):
        """
        **[Required]** Gets the service of this BasicDatabaseConnectionStringDetails.
        The service name of the database.


        :return: The service of this BasicDatabaseConnectionStringDetails.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this BasicDatabaseConnectionStringDetails.
        The service name of the database.


        :param service: The service of this BasicDatabaseConnectionStringDetails.
        :type: str
        """
        self._service = service

    @property
    def port(self):
        """
        **[Required]** Gets the port of this BasicDatabaseConnectionStringDetails.
        The port number used to connect to the database.


        :return: The port of this BasicDatabaseConnectionStringDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this BasicDatabaseConnectionStringDetails.
        The port number used to connect to the database.


        :param port: The port of this BasicDatabaseConnectionStringDetails.
        :type: int
        """
        self._port = port

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this BasicDatabaseConnectionStringDetails.
        The protocol used to connect to the database.

        Allowed values for this property are: "TCP", "TCPS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this BasicDatabaseConnectionStringDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this BasicDatabaseConnectionStringDetails.
        The protocol used to connect to the database.


        :param protocol: The protocol of this BasicDatabaseConnectionStringDetails.
        :type: str
        """
        allowed_values = ["TCP", "TCPS"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
