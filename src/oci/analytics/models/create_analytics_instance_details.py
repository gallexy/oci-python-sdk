# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190331


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAnalyticsInstanceDetails(object):
    """
    Input payload to create an Anaytics instance.
    """

    #: A constant which can be used with the feature_set property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "SELF_SERVICE_ANALYTICS"
    FEATURE_SET_SELF_SERVICE_ANALYTICS = "SELF_SERVICE_ANALYTICS"

    #: A constant which can be used with the feature_set property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "ENTERPRISE_ANALYTICS"
    FEATURE_SET_ENTERPRISE_ANALYTICS = "ENTERPRISE_ANALYTICS"

    #: A constant which can be used with the license_type property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_TYPE_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_type property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_TYPE_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the update_channel property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "REGULAR"
    UPDATE_CHANNEL_REGULAR = "REGULAR"

    #: A constant which can be used with the update_channel property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "EARLY"
    UPDATE_CHANNEL_EARLY = "EARLY"

    #: A constant which can be used with the update_channel property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "PHASE_2"
    UPDATE_CHANNEL_PHASE_2 = "PHASE_2"

    #: A constant which can be used with the update_channel property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "PHASE_1"
    UPDATE_CHANNEL_PHASE_1 = "PHASE_1"

    #: A constant which can be used with the feature_bundle property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "FAW_PAID"
    FEATURE_BUNDLE_FAW_PAID = "FAW_PAID"

    #: A constant which can be used with the feature_bundle property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "FAW_FREE"
    FEATURE_BUNDLE_FAW_FREE = "FAW_FREE"

    #: A constant which can be used with the feature_bundle property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "EE_EMBEDDED"
    FEATURE_BUNDLE_EE_EMBEDDED = "EE_EMBEDDED"

    #: A constant which can be used with the feature_bundle property of a CreateAnalyticsInstanceDetails.
    #: This constant has a value of "SE_EMBEDDED"
    FEATURE_BUNDLE_SE_EMBEDDED = "SE_EMBEDDED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAnalyticsInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateAnalyticsInstanceDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateAnalyticsInstanceDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAnalyticsInstanceDetails.
        :type compartment_id: str

        :param feature_set:
            The value to assign to the feature_set property of this CreateAnalyticsInstanceDetails.
            Allowed values for this property are: "SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS"
        :type feature_set: str

        :param capacity:
            The value to assign to the capacity property of this CreateAnalyticsInstanceDetails.
        :type capacity: oci.analytics.models.Capacity

        :param license_type:
            The value to assign to the license_type property of this CreateAnalyticsInstanceDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_type: str

        :param email_notification:
            The value to assign to the email_notification property of this CreateAnalyticsInstanceDetails.
        :type email_notification: str

        :param network_endpoint_details:
            The value to assign to the network_endpoint_details property of this CreateAnalyticsInstanceDetails.
        :type network_endpoint_details: oci.analytics.models.NetworkEndpointDetails

        :param idcs_access_token:
            The value to assign to the idcs_access_token property of this CreateAnalyticsInstanceDetails.
        :type idcs_access_token: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAnalyticsInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAnalyticsInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param update_channel:
            The value to assign to the update_channel property of this CreateAnalyticsInstanceDetails.
            Allowed values for this property are: "REGULAR", "EARLY", "PHASE_2", "PHASE_1"
        :type update_channel: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateAnalyticsInstanceDetails.
        :type kms_key_id: str

        :param domain_id:
            The value to assign to the domain_id property of this CreateAnalyticsInstanceDetails.
        :type domain_id: str

        :param admin_user:
            The value to assign to the admin_user property of this CreateAnalyticsInstanceDetails.
        :type admin_user: str

        :param feature_bundle:
            The value to assign to the feature_bundle property of this CreateAnalyticsInstanceDetails.
            Allowed values for this property are: "FAW_PAID", "FAW_FREE", "EE_EMBEDDED", "SE_EMBEDDED"
        :type feature_bundle: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'feature_set': 'str',
            'capacity': 'Capacity',
            'license_type': 'str',
            'email_notification': 'str',
            'network_endpoint_details': 'NetworkEndpointDetails',
            'idcs_access_token': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'update_channel': 'str',
            'kms_key_id': 'str',
            'domain_id': 'str',
            'admin_user': 'str',
            'feature_bundle': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'feature_set': 'featureSet',
            'capacity': 'capacity',
            'license_type': 'licenseType',
            'email_notification': 'emailNotification',
            'network_endpoint_details': 'networkEndpointDetails',
            'idcs_access_token': 'idcsAccessToken',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'update_channel': 'updateChannel',
            'kms_key_id': 'kmsKeyId',
            'domain_id': 'domainId',
            'admin_user': 'adminUser',
            'feature_bundle': 'featureBundle'
        }
        self._name = None
        self._description = None
        self._compartment_id = None
        self._feature_set = None
        self._capacity = None
        self._license_type = None
        self._email_notification = None
        self._network_endpoint_details = None
        self._idcs_access_token = None
        self._defined_tags = None
        self._freeform_tags = None
        self._update_channel = None
        self._kms_key_id = None
        self._domain_id = None
        self._admin_user = None
        self._feature_bundle = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateAnalyticsInstanceDetails.
        The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.


        :return: The name of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateAnalyticsInstanceDetails.
        The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.


        :param name: The name of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateAnalyticsInstanceDetails.
        Optional description.


        :return: The description of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAnalyticsInstanceDetails.
        Optional description.


        :param description: The description of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAnalyticsInstanceDetails.
        The OCID of the compartment.


        :return: The compartment_id of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAnalyticsInstanceDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def feature_set(self):
        """
        **[Required]** Gets the feature_set of this CreateAnalyticsInstanceDetails.
        Analytics feature set.

        Allowed values for this property are: "SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS"


        :return: The feature_set of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._feature_set

    @feature_set.setter
    def feature_set(self, feature_set):
        """
        Sets the feature_set of this CreateAnalyticsInstanceDetails.
        Analytics feature set.


        :param feature_set: The feature_set of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        allowed_values = ["SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS"]
        if not value_allowed_none_or_none_sentinel(feature_set, allowed_values):
            raise ValueError(
                f"Invalid value for `feature_set`, must be None or one of {allowed_values}"
            )
        self._feature_set = feature_set

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this CreateAnalyticsInstanceDetails.

        :return: The capacity of this CreateAnalyticsInstanceDetails.
        :rtype: oci.analytics.models.Capacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this CreateAnalyticsInstanceDetails.

        :param capacity: The capacity of this CreateAnalyticsInstanceDetails.
        :type: oci.analytics.models.Capacity
        """
        self._capacity = capacity

    @property
    def license_type(self):
        """
        **[Required]** Gets the license_type of this CreateAnalyticsInstanceDetails.
        The license used for the service.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_type of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this CreateAnalyticsInstanceDetails.
        The license used for the service.


        :param license_type: The license_type of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_type, allowed_values):
            raise ValueError(
                f"Invalid value for `license_type`, must be None or one of {allowed_values}"
            )
        self._license_type = license_type

    @property
    def email_notification(self):
        """
        Gets the email_notification of this CreateAnalyticsInstanceDetails.
        Email address receiving notifications.


        :return: The email_notification of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """
        Sets the email_notification of this CreateAnalyticsInstanceDetails.
        Email address receiving notifications.


        :param email_notification: The email_notification of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        self._email_notification = email_notification

    @property
    def network_endpoint_details(self):
        """
        Gets the network_endpoint_details of this CreateAnalyticsInstanceDetails.

        :return: The network_endpoint_details of this CreateAnalyticsInstanceDetails.
        :rtype: oci.analytics.models.NetworkEndpointDetails
        """
        return self._network_endpoint_details

    @network_endpoint_details.setter
    def network_endpoint_details(self, network_endpoint_details):
        """
        Sets the network_endpoint_details of this CreateAnalyticsInstanceDetails.

        :param network_endpoint_details: The network_endpoint_details of this CreateAnalyticsInstanceDetails.
        :type: oci.analytics.models.NetworkEndpointDetails
        """
        self._network_endpoint_details = network_endpoint_details

    @property
    def idcs_access_token(self):
        """
        Gets the idcs_access_token of this CreateAnalyticsInstanceDetails.
        IDCS access token identifying a stripe and service administrator user.


        :return: The idcs_access_token of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._idcs_access_token

    @idcs_access_token.setter
    def idcs_access_token(self, idcs_access_token):
        """
        Sets the idcs_access_token of this CreateAnalyticsInstanceDetails.
        IDCS access token identifying a stripe and service administrator user.


        :param idcs_access_token: The idcs_access_token of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        self._idcs_access_token = idcs_access_token

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAnalyticsInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAnalyticsInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAnalyticsInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAnalyticsInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAnalyticsInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAnalyticsInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAnalyticsInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAnalyticsInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def update_channel(self):
        """
        Gets the update_channel of this CreateAnalyticsInstanceDetails.
        Analytics instance update channel.

        Allowed values for this property are: "REGULAR", "EARLY", "PHASE_2", "PHASE_1"


        :return: The update_channel of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._update_channel

    @update_channel.setter
    def update_channel(self, update_channel):
        """
        Sets the update_channel of this CreateAnalyticsInstanceDetails.
        Analytics instance update channel.


        :param update_channel: The update_channel of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        allowed_values = ["REGULAR", "EARLY", "PHASE_2", "PHASE_1"]
        if not value_allowed_none_or_none_sentinel(update_channel, allowed_values):
            raise ValueError(
                f"Invalid value for `update_channel`, must be None or one of {allowed_values}"
            )
        self._update_channel = update_channel

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this CreateAnalyticsInstanceDetails.
        OCID of the OCI Vault Key encrypting the customer data stored in this Analytics instance. A null value indicates Oracle managed default encryption.


        :return: The kms_key_id of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CreateAnalyticsInstanceDetails.
        OCID of the OCI Vault Key encrypting the customer data stored in this Analytics instance. A null value indicates Oracle managed default encryption.


        :param kms_key_id: The kms_key_id of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def domain_id(self):
        """
        Gets the domain_id of this CreateAnalyticsInstanceDetails.
        domain id for which the user is authorized.


        :return: The domain_id of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """
        Sets the domain_id of this CreateAnalyticsInstanceDetails.
        domain id for which the user is authorized.


        :param domain_id: The domain_id of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def admin_user(self):
        """
        Gets the admin_user of this CreateAnalyticsInstanceDetails.
        user name of the authorized user.


        :return: The admin_user of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._admin_user

    @admin_user.setter
    def admin_user(self, admin_user):
        """
        Sets the admin_user of this CreateAnalyticsInstanceDetails.
        user name of the authorized user.


        :param admin_user: The admin_user of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        self._admin_user = admin_user

    @property
    def feature_bundle(self):
        """
        Gets the feature_bundle of this CreateAnalyticsInstanceDetails.
        The feature set of an Analytics instance.

        Allowed values for this property are: "FAW_PAID", "FAW_FREE", "EE_EMBEDDED", "SE_EMBEDDED"


        :return: The feature_bundle of this CreateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._feature_bundle

    @feature_bundle.setter
    def feature_bundle(self, feature_bundle):
        """
        Sets the feature_bundle of this CreateAnalyticsInstanceDetails.
        The feature set of an Analytics instance.


        :param feature_bundle: The feature_bundle of this CreateAnalyticsInstanceDetails.
        :type: str
        """
        allowed_values = ["FAW_PAID", "FAW_FREE", "EE_EMBEDDED", "SE_EMBEDDED"]
        if not value_allowed_none_or_none_sentinel(feature_bundle, allowed_values):
            raise ValueError(
                f"Invalid value for `feature_bundle`, must be None or one of {allowed_values}"
            )
        self._feature_bundle = feature_bundle

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
