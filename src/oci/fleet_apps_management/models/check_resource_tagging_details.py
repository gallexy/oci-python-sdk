# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CheckResourceTaggingDetails(object):
    """
    Request to check resource tagging.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CheckResourceTaggingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CheckResourceTaggingDetails.
        :type compartment_id: str

        :param fleet_display_name:
            The value to assign to the fleet_display_name property of this CheckResourceTaggingDetails.
        :type fleet_display_name: str

        :param resource_ids:
            The value to assign to the resource_ids property of this CheckResourceTaggingDetails.
        :type resource_ids: list[str]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'fleet_display_name': 'str',
            'resource_ids': 'list[str]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'fleet_display_name': 'fleetDisplayName',
            'resource_ids': 'resourceIds'
        }

        self._compartment_id = None
        self._fleet_display_name = None
        self._resource_ids = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CheckResourceTaggingDetails.
        Tenancy OCID


        :return: The compartment_id of this CheckResourceTaggingDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CheckResourceTaggingDetails.
        Tenancy OCID


        :param compartment_id: The compartment_id of this CheckResourceTaggingDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def fleet_display_name(self):
        """
        Gets the fleet_display_name of this CheckResourceTaggingDetails.
        Fleet Display Name.


        :return: The fleet_display_name of this CheckResourceTaggingDetails.
        :rtype: str
        """
        return self._fleet_display_name

    @fleet_display_name.setter
    def fleet_display_name(self, fleet_display_name):
        """
        Sets the fleet_display_name of this CheckResourceTaggingDetails.
        Fleet Display Name.


        :param fleet_display_name: The fleet_display_name of this CheckResourceTaggingDetails.
        :type: str
        """
        self._fleet_display_name = fleet_display_name

    @property
    def resource_ids(self):
        """
        **[Required]** Gets the resource_ids of this CheckResourceTaggingDetails.
        Resource OCIDS that need to be verified if a tag can be enabled for them.


        :return: The resource_ids of this CheckResourceTaggingDetails.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """
        Sets the resource_ids of this CheckResourceTaggingDetails.
        Resource OCIDS that need to be verified if a tag can be enabled for them.


        :param resource_ids: The resource_ids of this CheckResourceTaggingDetails.
        :type: list[str]
        """
        self._resource_ids = resource_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
