# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNetworkLoadBalancerDetails(object):
    """
    Configuration details to update a network load balancer.

    **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the nlb_ip_version property of a UpdateNetworkLoadBalancerDetails.
    #: This constant has a value of "IPV4"
    NLB_IP_VERSION_IPV4 = "IPV4"

    #: A constant which can be used with the nlb_ip_version property of a UpdateNetworkLoadBalancerDetails.
    #: This constant has a value of "IPV4_AND_IPV6"
    NLB_IP_VERSION_IPV4_AND_IPV6 = "IPV4_AND_IPV6"

    #: A constant which can be used with the nlb_ip_version property of a UpdateNetworkLoadBalancerDetails.
    #: This constant has a value of "IPV6"
    NLB_IP_VERSION_IPV6 = "IPV6"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNetworkLoadBalancerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateNetworkLoadBalancerDetails.
        :type display_name: str

        :param is_preserve_source_destination:
            The value to assign to the is_preserve_source_destination property of this UpdateNetworkLoadBalancerDetails.
        :type is_preserve_source_destination: bool

        :param is_symmetric_hash_enabled:
            The value to assign to the is_symmetric_hash_enabled property of this UpdateNetworkLoadBalancerDetails.
        :type is_symmetric_hash_enabled: bool

        :param nlb_ip_version:
            The value to assign to the nlb_ip_version property of this UpdateNetworkLoadBalancerDetails.
            Allowed values for this property are: "IPV4", "IPV4_AND_IPV6", "IPV6"
        :type nlb_ip_version: str

        :param subnet_ipv6_cidr:
            The value to assign to the subnet_ipv6_cidr property of this UpdateNetworkLoadBalancerDetails.
        :type subnet_ipv6_cidr: str

        :param assigned_ipv6:
            The value to assign to the assigned_ipv6 property of this UpdateNetworkLoadBalancerDetails.
        :type assigned_ipv6: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateNetworkLoadBalancerDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateNetworkLoadBalancerDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'is_preserve_source_destination': 'bool',
            'is_symmetric_hash_enabled': 'bool',
            'nlb_ip_version': 'str',
            'subnet_ipv6_cidr': 'str',
            'assigned_ipv6': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'is_preserve_source_destination': 'isPreserveSourceDestination',
            'is_symmetric_hash_enabled': 'isSymmetricHashEnabled',
            'nlb_ip_version': 'nlbIpVersion',
            'subnet_ipv6_cidr': 'subnetIpv6Cidr',
            'assigned_ipv6': 'assignedIpv6',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._is_preserve_source_destination = None
        self._is_symmetric_hash_enabled = None
        self._nlb_ip_version = None
        self._subnet_ipv6_cidr = None
        self._assigned_ipv6 = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateNetworkLoadBalancerDetails.
        The user-friendly display name for the network load balancer, which does not have to be unique and can be changed.
        Avoid entering confidential information.

        Example: `example_network_load_balancer`


        :return: The display_name of this UpdateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateNetworkLoadBalancerDetails.
        The user-friendly display name for the network load balancer, which does not have to be unique and can be changed.
        Avoid entering confidential information.

        Example: `example_network_load_balancer`


        :param display_name: The display_name of this UpdateNetworkLoadBalancerDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_preserve_source_destination(self):
        """
        Gets the is_preserve_source_destination of this UpdateNetworkLoadBalancerDetails.
        This parameter can be enabled only if backends are compute OCIDs. When enabled, the skipSourceDestinationCheck parameter is automatically
        enabled on the load balancer VNIC, and packets are sent to the backend with the entire IP header intact.


        :return: The is_preserve_source_destination of this UpdateNetworkLoadBalancerDetails.
        :rtype: bool
        """
        return self._is_preserve_source_destination

    @is_preserve_source_destination.setter
    def is_preserve_source_destination(self, is_preserve_source_destination):
        """
        Sets the is_preserve_source_destination of this UpdateNetworkLoadBalancerDetails.
        This parameter can be enabled only if backends are compute OCIDs. When enabled, the skipSourceDestinationCheck parameter is automatically
        enabled on the load balancer VNIC, and packets are sent to the backend with the entire IP header intact.


        :param is_preserve_source_destination: The is_preserve_source_destination of this UpdateNetworkLoadBalancerDetails.
        :type: bool
        """
        self._is_preserve_source_destination = is_preserve_source_destination

    @property
    def is_symmetric_hash_enabled(self):
        """
        Gets the is_symmetric_hash_enabled of this UpdateNetworkLoadBalancerDetails.
        This can only be enabled when NLB is working in transparent mode with source destination header preservation enabled.
        This removes the additional dependency from NLB backends(like Firewalls) to perform SNAT.


        :return: The is_symmetric_hash_enabled of this UpdateNetworkLoadBalancerDetails.
        :rtype: bool
        """
        return self._is_symmetric_hash_enabled

    @is_symmetric_hash_enabled.setter
    def is_symmetric_hash_enabled(self, is_symmetric_hash_enabled):
        """
        Sets the is_symmetric_hash_enabled of this UpdateNetworkLoadBalancerDetails.
        This can only be enabled when NLB is working in transparent mode with source destination header preservation enabled.
        This removes the additional dependency from NLB backends(like Firewalls) to perform SNAT.


        :param is_symmetric_hash_enabled: The is_symmetric_hash_enabled of this UpdateNetworkLoadBalancerDetails.
        :type: bool
        """
        self._is_symmetric_hash_enabled = is_symmetric_hash_enabled

    @property
    def nlb_ip_version(self):
        """
        Gets the nlb_ip_version of this UpdateNetworkLoadBalancerDetails.
        IP version associated with the NLB.

        Allowed values for this property are: "IPV4", "IPV4_AND_IPV6", "IPV6"


        :return: The nlb_ip_version of this UpdateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._nlb_ip_version

    @nlb_ip_version.setter
    def nlb_ip_version(self, nlb_ip_version):
        """
        Sets the nlb_ip_version of this UpdateNetworkLoadBalancerDetails.
        IP version associated with the NLB.


        :param nlb_ip_version: The nlb_ip_version of this UpdateNetworkLoadBalancerDetails.
        :type: str
        """
        allowed_values = ["IPV4", "IPV4_AND_IPV6", "IPV6"]
        if not value_allowed_none_or_none_sentinel(nlb_ip_version, allowed_values):
            raise ValueError(
                f"Invalid value for `nlb_ip_version`, must be None or one of {allowed_values}"
            )
        self._nlb_ip_version = nlb_ip_version

    @property
    def subnet_ipv6_cidr(self):
        """
        Gets the subnet_ipv6_cidr of this UpdateNetworkLoadBalancerDetails.
        IPv6 subnet prefix selection. If Ipv6 subnet prefix is passed, Nlb Ipv6 Address would be assign within the cidr block. NLB has to be dual or single stack ipv6 to support this.


        :return: The subnet_ipv6_cidr of this UpdateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._subnet_ipv6_cidr

    @subnet_ipv6_cidr.setter
    def subnet_ipv6_cidr(self, subnet_ipv6_cidr):
        """
        Sets the subnet_ipv6_cidr of this UpdateNetworkLoadBalancerDetails.
        IPv6 subnet prefix selection. If Ipv6 subnet prefix is passed, Nlb Ipv6 Address would be assign within the cidr block. NLB has to be dual or single stack ipv6 to support this.


        :param subnet_ipv6_cidr: The subnet_ipv6_cidr of this UpdateNetworkLoadBalancerDetails.
        :type: str
        """
        self._subnet_ipv6_cidr = subnet_ipv6_cidr

    @property
    def assigned_ipv6(self):
        """
        Gets the assigned_ipv6 of this UpdateNetworkLoadBalancerDetails.
        IPv6 address to be assigned to the network load balancer being created.
        This IP address has to be part of one of the prefixes supported by the subnet.
        Example: \"2607:9b80:9a0a:9a7e:abcd:ef01:2345:6789\"


        :return: The assigned_ipv6 of this UpdateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._assigned_ipv6

    @assigned_ipv6.setter
    def assigned_ipv6(self, assigned_ipv6):
        """
        Sets the assigned_ipv6 of this UpdateNetworkLoadBalancerDetails.
        IPv6 address to be assigned to the network load balancer being created.
        This IP address has to be part of one of the prefixes supported by the subnet.
        Example: \"2607:9b80:9a0a:9a7e:abcd:ef01:2345:6789\"


        :param assigned_ipv6: The assigned_ipv6 of this UpdateNetworkLoadBalancerDetails.
        :type: str
        """
        self._assigned_ipv6 = assigned_ipv6

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateNetworkLoadBalancerDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateNetworkLoadBalancerDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateNetworkLoadBalancerDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateNetworkLoadBalancerDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateNetworkLoadBalancerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateNetworkLoadBalancerDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateNetworkLoadBalancerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateNetworkLoadBalancerDetails.
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
