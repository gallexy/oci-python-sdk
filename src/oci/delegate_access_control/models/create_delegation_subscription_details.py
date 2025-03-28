# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230801


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDelegationSubscriptionDetails(object):
    """
    Details for creating the Delegation Subscription.
    """

    #: A constant which can be used with the subscribed_service_type property of a CreateDelegationSubscriptionDetails.
    #: This constant has a value of "TROUBLESHOOTING"
    SUBSCRIBED_SERVICE_TYPE_TROUBLESHOOTING = "TROUBLESHOOTING"

    #: A constant which can be used with the subscribed_service_type property of a CreateDelegationSubscriptionDetails.
    #: This constant has a value of "ASSISTED_PATCHING"
    SUBSCRIBED_SERVICE_TYPE_ASSISTED_PATCHING = "ASSISTED_PATCHING"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDelegationSubscriptionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDelegationSubscriptionDetails.
        :type compartment_id: str

        :param service_provider_id:
            The value to assign to the service_provider_id property of this CreateDelegationSubscriptionDetails.
        :type service_provider_id: str

        :param description:
            The value to assign to the description property of this CreateDelegationSubscriptionDetails.
        :type description: str

        :param subscribed_service_type:
            The value to assign to the subscribed_service_type property of this CreateDelegationSubscriptionDetails.
            Allowed values for this property are: "TROUBLESHOOTING", "ASSISTED_PATCHING"
        :type subscribed_service_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDelegationSubscriptionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDelegationSubscriptionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'service_provider_id': 'str',
            'description': 'str',
            'subscribed_service_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'service_provider_id': 'serviceProviderId',
            'description': 'description',
            'subscribed_service_type': 'subscribedServiceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._compartment_id = None
        self._service_provider_id = None
        self._description = None
        self._subscribed_service_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDelegationSubscriptionDetails.
        The OCID of the compartment that contains the Delegation Control.


        :return: The compartment_id of this CreateDelegationSubscriptionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDelegationSubscriptionDetails.
        The OCID of the compartment that contains the Delegation Control.


        :param compartment_id: The compartment_id of this CreateDelegationSubscriptionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def service_provider_id(self):
        """
        **[Required]** Gets the service_provider_id of this CreateDelegationSubscriptionDetails.
        Unique identifier of the Service Provider.


        :return: The service_provider_id of this CreateDelegationSubscriptionDetails.
        :rtype: str
        """
        return self._service_provider_id

    @service_provider_id.setter
    def service_provider_id(self, service_provider_id):
        """
        Sets the service_provider_id of this CreateDelegationSubscriptionDetails.
        Unique identifier of the Service Provider.


        :param service_provider_id: The service_provider_id of this CreateDelegationSubscriptionDetails.
        :type: str
        """
        self._service_provider_id = service_provider_id

    @property
    def description(self):
        """
        Gets the description of this CreateDelegationSubscriptionDetails.
        Description of the Delegation Subscription.


        :return: The description of this CreateDelegationSubscriptionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDelegationSubscriptionDetails.
        Description of the Delegation Subscription.


        :param description: The description of this CreateDelegationSubscriptionDetails.
        :type: str
        """
        self._description = description

    @property
    def subscribed_service_type(self):
        """
        **[Required]** Gets the subscribed_service_type of this CreateDelegationSubscriptionDetails.
        Subscribed Service Provider Service Type.

        Allowed values for this property are: "TROUBLESHOOTING", "ASSISTED_PATCHING"


        :return: The subscribed_service_type of this CreateDelegationSubscriptionDetails.
        :rtype: str
        """
        return self._subscribed_service_type

    @subscribed_service_type.setter
    def subscribed_service_type(self, subscribed_service_type):
        """
        Sets the subscribed_service_type of this CreateDelegationSubscriptionDetails.
        Subscribed Service Provider Service Type.


        :param subscribed_service_type: The subscribed_service_type of this CreateDelegationSubscriptionDetails.
        :type: str
        """
        allowed_values = ["TROUBLESHOOTING", "ASSISTED_PATCHING"]
        if not value_allowed_none_or_none_sentinel(subscribed_service_type, allowed_values):
            raise ValueError(
                f"Invalid value for `subscribed_service_type`, must be None or one of {allowed_values}"
            )
        self._subscribed_service_type = subscribed_service_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDelegationSubscriptionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDelegationSubscriptionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDelegationSubscriptionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDelegationSubscriptionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDelegationSubscriptionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDelegationSubscriptionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDelegationSubscriptionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDelegationSubscriptionDetails.
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
