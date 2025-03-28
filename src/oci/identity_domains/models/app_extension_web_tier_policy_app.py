# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppExtensionWebTierPolicyApp(object):
    """
    WebTier Policy
    """

    #: A constant which can be used with the web_tier_policy_az_control property of a AppExtensionWebTierPolicyApp.
    #: This constant has a value of "server"
    WEB_TIER_POLICY_AZ_CONTROL_SERVER = "server"

    #: A constant which can be used with the web_tier_policy_az_control property of a AppExtensionWebTierPolicyApp.
    #: This constant has a value of "local"
    WEB_TIER_POLICY_AZ_CONTROL_LOCAL = "local"

    def __init__(self, **kwargs):
        """
        Initializes a new AppExtensionWebTierPolicyApp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param web_tier_policy_json:
            The value to assign to the web_tier_policy_json property of this AppExtensionWebTierPolicyApp.
        :type web_tier_policy_json: str

        :param web_tier_policy_az_control:
            The value to assign to the web_tier_policy_az_control property of this AppExtensionWebTierPolicyApp.
            Allowed values for this property are: "server", "local", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type web_tier_policy_az_control: str

        :param resource_ref:
            The value to assign to the resource_ref property of this AppExtensionWebTierPolicyApp.
        :type resource_ref: bool

        """
        self.swagger_types = {
            'web_tier_policy_json': 'str',
            'web_tier_policy_az_control': 'str',
            'resource_ref': 'bool'
        }
        self.attribute_map = {
            'web_tier_policy_json': 'webTierPolicyJson',
            'web_tier_policy_az_control': 'webTierPolicyAZControl',
            'resource_ref': 'resourceRef'
        }
        self._web_tier_policy_json = None
        self._web_tier_policy_az_control = None
        self._resource_ref = None

    @property
    def web_tier_policy_json(self):
        """
        Gets the web_tier_policy_json of this AppExtensionWebTierPolicyApp.
        Store the web tier policy for an application as a string in Javascript Object Notification (JSON) format.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The web_tier_policy_json of this AppExtensionWebTierPolicyApp.
        :rtype: str
        """
        return self._web_tier_policy_json

    @web_tier_policy_json.setter
    def web_tier_policy_json(self, web_tier_policy_json):
        """
        Sets the web_tier_policy_json of this AppExtensionWebTierPolicyApp.
        Store the web tier policy for an application as a string in Javascript Object Notification (JSON) format.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param web_tier_policy_json: The web_tier_policy_json of this AppExtensionWebTierPolicyApp.
        :type: str
        """
        self._web_tier_policy_json = web_tier_policy_json

    @property
    def web_tier_policy_az_control(self):
        """
        Gets the web_tier_policy_az_control of this AppExtensionWebTierPolicyApp.
        Webtier policy AZ Control

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "server", "local", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The web_tier_policy_az_control of this AppExtensionWebTierPolicyApp.
        :rtype: str
        """
        return self._web_tier_policy_az_control

    @web_tier_policy_az_control.setter
    def web_tier_policy_az_control(self, web_tier_policy_az_control):
        """
        Sets the web_tier_policy_az_control of this AppExtensionWebTierPolicyApp.
        Webtier policy AZ Control

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param web_tier_policy_az_control: The web_tier_policy_az_control of this AppExtensionWebTierPolicyApp.
        :type: str
        """
        allowed_values = ["server", "local"]
        if not value_allowed_none_or_none_sentinel(web_tier_policy_az_control, allowed_values):
            web_tier_policy_az_control = 'UNKNOWN_ENUM_VALUE'
        self._web_tier_policy_az_control = web_tier_policy_az_control

    @property
    def resource_ref(self):
        """
        Gets the resource_ref of this AppExtensionWebTierPolicyApp.
        If this Attribute is true, resource ref id and resource ref name attributes will we included in wtp json response.

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The resource_ref of this AppExtensionWebTierPolicyApp.
        :rtype: bool
        """
        return self._resource_ref

    @resource_ref.setter
    def resource_ref(self, resource_ref):
        """
        Sets the resource_ref of this AppExtensionWebTierPolicyApp.
        If this Attribute is true, resource ref id and resource ref name attributes will we included in wtp json response.

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param resource_ref: The resource_ref of this AppExtensionWebTierPolicyApp.
        :type: bool
        """
        self._resource_ref = resource_ref

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
