# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KernelEventAdditionalDetails(object):
    """
    Provides additional information about the kernel event.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KernelEventAdditionalDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vmcore:
            The value to assign to the vmcore property of this KernelEventAdditionalDetails.
        :type vmcore: oci.os_management_hub.models.VmcoreDetails

        """
        self.swagger_types = {
            'vmcore': 'VmcoreDetails'
        }

        self.attribute_map = {
            'vmcore': 'vmcore'
        }

        self._vmcore = None

    @property
    def vmcore(self):
        """
        **[Required]** Gets the vmcore of this KernelEventAdditionalDetails.

        :return: The vmcore of this KernelEventAdditionalDetails.
        :rtype: oci.os_management_hub.models.VmcoreDetails
        """
        return self._vmcore

    @vmcore.setter
    def vmcore(self, vmcore):
        """
        Sets the vmcore of this KernelEventAdditionalDetails.

        :param vmcore: The vmcore of this KernelEventAdditionalDetails.
        :type: oci.os_management_hub.models.VmcoreDetails
        """
        self._vmcore = vmcore

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
