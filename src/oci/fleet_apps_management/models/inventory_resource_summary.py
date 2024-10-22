# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InventoryResourceSummary(object):
    """
    InventoryResource Search Summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InventoryResourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this InventoryResourceSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this InventoryResourceSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this InventoryResourceSummary.
        :type display_name: str

        :param type:
            The value to assign to the type property of this InventoryResourceSummary.
        :type type: str

        :param resource_compartment_id:
            The value to assign to the resource_compartment_id property of this InventoryResourceSummary.
        :type resource_compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this InventoryResourceSummary.
        :type availability_domain: str

        :param resource_region:
            The value to assign to the resource_region property of this InventoryResourceSummary.
        :type resource_region: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InventoryResourceSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this InventoryResourceSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this InventoryResourceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this InventoryResourceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this InventoryResourceSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'type': 'str',
            'resource_compartment_id': 'str',
            'availability_domain': 'str',
            'resource_region': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'type': 'type',
            'resource_compartment_id': 'resourceCompartmentId',
            'availability_domain': 'availabilityDomain',
            'resource_region': 'resourceRegion',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._type = None
        self._resource_compartment_id = None
        self._availability_domain = None
        self._resource_region = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InventoryResourceSummary.
        The OCID of the resource.


        :return: The id of this InventoryResourceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InventoryResourceSummary.
        The OCID of the resource.


        :param id: The id of this InventoryResourceSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this InventoryResourceSummary.
        OCID of the compartment to which the resource belongs to.


        :return: The compartment_id of this InventoryResourceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InventoryResourceSummary.
        OCID of the compartment to which the resource belongs to.


        :param compartment_id: The compartment_id of this InventoryResourceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this InventoryResourceSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this InventoryResourceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InventoryResourceSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this InventoryResourceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this InventoryResourceSummary.
        Type of the Resource.


        :return: The type of this InventoryResourceSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InventoryResourceSummary.
        Type of the Resource.


        :param type: The type of this InventoryResourceSummary.
        :type: str
        """
        self._type = type

    @property
    def resource_compartment_id(self):
        """
        Gets the resource_compartment_id of this InventoryResourceSummary.
        Compartment Id of the resource.


        :return: The resource_compartment_id of this InventoryResourceSummary.
        :rtype: str
        """
        return self._resource_compartment_id

    @resource_compartment_id.setter
    def resource_compartment_id(self, resource_compartment_id):
        """
        Sets the resource_compartment_id of this InventoryResourceSummary.
        Compartment Id of the resource.


        :param resource_compartment_id: The resource_compartment_id of this InventoryResourceSummary.
        :type: str
        """
        self._resource_compartment_id = resource_compartment_id

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this InventoryResourceSummary.
        Availability Domain of the resource.


        :return: The availability_domain of this InventoryResourceSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this InventoryResourceSummary.
        Availability Domain of the resource.


        :param availability_domain: The availability_domain of this InventoryResourceSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def resource_region(self):
        """
        Gets the resource_region of this InventoryResourceSummary.
        The region the resource belongs to.


        :return: The resource_region of this InventoryResourceSummary.
        :rtype: str
        """
        return self._resource_region

    @resource_region.setter
    def resource_region(self, resource_region):
        """
        Sets the resource_region of this InventoryResourceSummary.
        The region the resource belongs to.


        :param resource_region: The resource_region of this InventoryResourceSummary.
        :type: str
        """
        self._resource_region = resource_region

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this InventoryResourceSummary.
        The current state of the Resource.


        :return: The lifecycle_state of this InventoryResourceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InventoryResourceSummary.
        The current state of the Resource.


        :param lifecycle_state: The lifecycle_state of this InventoryResourceSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this InventoryResourceSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this InventoryResourceSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this InventoryResourceSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this InventoryResourceSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this InventoryResourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this InventoryResourceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this InventoryResourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this InventoryResourceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this InventoryResourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this InventoryResourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this InventoryResourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this InventoryResourceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this InventoryResourceSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this InventoryResourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this InventoryResourceSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this InventoryResourceSummary.
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
