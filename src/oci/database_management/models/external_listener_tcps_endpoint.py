# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .external_listener_endpoint import ExternalListenerEndpoint
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalListenerTcpsEndpoint(ExternalListenerEndpoint):
    """
    A `TCPS`-based protocol address.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalListenerTcpsEndpoint object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalListenerTcpsEndpoint.protocol` attribute
        of this class is ``TCPS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this ExternalListenerTcpsEndpoint.
            Allowed values for this property are: "IPC", "TCP", "TCPS"
        :type protocol: str

        :param services:
            The value to assign to the services property of this ExternalListenerTcpsEndpoint.
        :type services: list[str]

        :param host:
            The value to assign to the host property of this ExternalListenerTcpsEndpoint.
        :type host: str

        :param port:
            The value to assign to the port property of this ExternalListenerTcpsEndpoint.
        :type port: int

        """
        self.swagger_types = {
            'protocol': 'str',
            'services': 'list[str]',
            'host': 'str',
            'port': 'int'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'services': 'services',
            'host': 'host',
            'port': 'port'
        }

        self._protocol = None
        self._services = None
        self._host = None
        self._port = None
        self._protocol = 'TCPS'

    @property
    def host(self):
        """
        **[Required]** Gets the host of this ExternalListenerTcpsEndpoint.
        The host name or IP address.


        :return: The host of this ExternalListenerTcpsEndpoint.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this ExternalListenerTcpsEndpoint.
        The host name or IP address.


        :param host: The host of this ExternalListenerTcpsEndpoint.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        **[Required]** Gets the port of this ExternalListenerTcpsEndpoint.
        The port number.


        :return: The port of this ExternalListenerTcpsEndpoint.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ExternalListenerTcpsEndpoint.
        The port number.


        :param port: The port of this ExternalListenerTcpsEndpoint.
        :type: int
        """
        self._port = port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other