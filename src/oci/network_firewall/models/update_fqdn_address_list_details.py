# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501

from .update_address_list_details import UpdateAddressListDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFqdnAddressListDetails(UpdateAddressListDetails):
    """
    The request details to be updated in the address List for the policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFqdnAddressListDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.network_firewall.models.UpdateFqdnAddressListDetails.type` attribute
        of this class is ``FQDN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateFqdnAddressListDetails.
            Allowed values for this property are: "FQDN", "IP"
        :type type: str

        :param addresses:
            The value to assign to the addresses property of this UpdateFqdnAddressListDetails.
        :type addresses: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'addresses': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'addresses': 'addresses'
        }

        self._type = None
        self._addresses = None
        self._type = 'FQDN'

    @property
    def addresses(self):
        """
        **[Required]** Gets the addresses of this UpdateFqdnAddressListDetails.
        List of FQDN addresses.


        :return: The addresses of this UpdateFqdnAddressListDetails.
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this UpdateFqdnAddressListDetails.
        List of FQDN addresses.


        :param addresses: The addresses of this UpdateFqdnAddressListDetails.
        :type: list[str]
        """
        self._addresses = addresses

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
