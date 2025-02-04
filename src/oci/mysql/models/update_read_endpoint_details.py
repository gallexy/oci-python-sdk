# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190415


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateReadEndpointDetails(object):
    """
    Read Endpoint details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateReadEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateReadEndpointDetails.
        :type is_enabled: bool

        :param read_endpoint_ip_address:
            The value to assign to the read_endpoint_ip_address property of this UpdateReadEndpointDetails.
        :type read_endpoint_ip_address: str

        :param read_endpoint_hostname_label:
            The value to assign to the read_endpoint_hostname_label property of this UpdateReadEndpointDetails.
        :type read_endpoint_hostname_label: str

        :param exclude_ips:
            The value to assign to the exclude_ips property of this UpdateReadEndpointDetails.
        :type exclude_ips: list[str]

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'read_endpoint_ip_address': 'str',
            'read_endpoint_hostname_label': 'str',
            'exclude_ips': 'list[str]'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'read_endpoint_ip_address': 'readEndpointIpAddress',
            'read_endpoint_hostname_label': 'readEndpointHostnameLabel',
            'exclude_ips': 'excludeIps'
        }

        self._is_enabled = None
        self._read_endpoint_ip_address = None
        self._read_endpoint_hostname_label = None
        self._exclude_ips = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateReadEndpointDetails.
        Specifies if the DB System read endpoint is enabled or not.


        :return: The is_enabled of this UpdateReadEndpointDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateReadEndpointDetails.
        Specifies if the DB System read endpoint is enabled or not.


        :param is_enabled: The is_enabled of this UpdateReadEndpointDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def read_endpoint_ip_address(self):
        """
        Gets the read_endpoint_ip_address of this UpdateReadEndpointDetails.
        The IP address the DB System read endpoint is configured to listen on.
        A private IP address of your choice to assign to the read endpoint of the DB System.
        Must be an available IP address within the subnet's CIDR. If you don't specify a value,
        Oracle automatically assigns a private IP address from the subnet. This should be a
        \"dotted-quad\" style IPv4 address.


        :return: The read_endpoint_ip_address of this UpdateReadEndpointDetails.
        :rtype: str
        """
        return self._read_endpoint_ip_address

    @read_endpoint_ip_address.setter
    def read_endpoint_ip_address(self, read_endpoint_ip_address):
        """
        Sets the read_endpoint_ip_address of this UpdateReadEndpointDetails.
        The IP address the DB System read endpoint is configured to listen on.
        A private IP address of your choice to assign to the read endpoint of the DB System.
        Must be an available IP address within the subnet's CIDR. If you don't specify a value,
        Oracle automatically assigns a private IP address from the subnet. This should be a
        \"dotted-quad\" style IPv4 address.


        :param read_endpoint_ip_address: The read_endpoint_ip_address of this UpdateReadEndpointDetails.
        :type: str
        """
        self._read_endpoint_ip_address = read_endpoint_ip_address

    @property
    def read_endpoint_hostname_label(self):
        """
        Gets the read_endpoint_hostname_label of this UpdateReadEndpointDetails.
        The hostname for the read endpoint of the DB System. Used for DNS.

        The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\").

        Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.


        :return: The read_endpoint_hostname_label of this UpdateReadEndpointDetails.
        :rtype: str
        """
        return self._read_endpoint_hostname_label

    @read_endpoint_hostname_label.setter
    def read_endpoint_hostname_label(self, read_endpoint_hostname_label):
        """
        Sets the read_endpoint_hostname_label of this UpdateReadEndpointDetails.
        The hostname for the read endpoint of the DB System. Used for DNS.

        The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\").

        Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.


        :param read_endpoint_hostname_label: The read_endpoint_hostname_label of this UpdateReadEndpointDetails.
        :type: str
        """
        self._read_endpoint_hostname_label = read_endpoint_hostname_label

    @property
    def exclude_ips(self):
        """
        Gets the exclude_ips of this UpdateReadEndpointDetails.
        A list of IP addresses of read replicas that are excluded from serving read requests.


        :return: The exclude_ips of this UpdateReadEndpointDetails.
        :rtype: list[str]
        """
        return self._exclude_ips

    @exclude_ips.setter
    def exclude_ips(self, exclude_ips):
        """
        Sets the exclude_ips of this UpdateReadEndpointDetails.
        A list of IP addresses of read replicas that are excluded from serving read requests.


        :param exclude_ips: The exclude_ips of this UpdateReadEndpointDetails.
        :type: list[str]
        """
        self._exclude_ips = exclude_ips

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
