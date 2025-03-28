# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppExtensionRadiusAppApp(object):
    """
    This extension defines attributes specific to Apps that represent instances of Radius App.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppExtensionRadiusAppApp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param client_ip:
            The value to assign to the client_ip property of this AppExtensionRadiusAppApp.
        :type client_ip: str

        :param port:
            The value to assign to the port property of this AppExtensionRadiusAppApp.
        :type port: str

        :param secret_key:
            The value to assign to the secret_key property of this AppExtensionRadiusAppApp.
        :type secret_key: str

        :param secret_key_temporary:
            The value to assign to the secret_key_temporary property of this AppExtensionRadiusAppApp.
        :type secret_key_temporary: str

        :param include_group_in_response:
            The value to assign to the include_group_in_response property of this AppExtensionRadiusAppApp.
        :type include_group_in_response: bool

        :param capture_client_ip:
            The value to assign to the capture_client_ip property of this AppExtensionRadiusAppApp.
        :type capture_client_ip: bool

        :param type_of_radius_app:
            The value to assign to the type_of_radius_app property of this AppExtensionRadiusAppApp.
        :type type_of_radius_app: str

        :param end_user_ip_attribute:
            The value to assign to the end_user_ip_attribute property of this AppExtensionRadiusAppApp.
        :type end_user_ip_attribute: str

        :param radius_vendor_specific_id:
            The value to assign to the radius_vendor_specific_id property of this AppExtensionRadiusAppApp.
        :type radius_vendor_specific_id: str

        :param country_code_response_attribute_id:
            The value to assign to the country_code_response_attribute_id property of this AppExtensionRadiusAppApp.
        :type country_code_response_attribute_id: str

        :param group_membership_radius_attribute:
            The value to assign to the group_membership_radius_attribute property of this AppExtensionRadiusAppApp.
        :type group_membership_radius_attribute: str

        :param response_format:
            The value to assign to the response_format property of this AppExtensionRadiusAppApp.
        :type response_format: str

        :param response_format_delimiter:
            The value to assign to the response_format_delimiter property of this AppExtensionRadiusAppApp.
        :type response_format_delimiter: str

        :param group_name_format:
            The value to assign to the group_name_format property of this AppExtensionRadiusAppApp.
        :type group_name_format: str

        :param password_and_otp_together:
            The value to assign to the password_and_otp_together property of this AppExtensionRadiusAppApp.
        :type password_and_otp_together: bool

        :param group_membership_to_return:
            The value to assign to the group_membership_to_return property of this AppExtensionRadiusAppApp.
        :type group_membership_to_return: list[oci.identity_domains.models.AppGroupMembershipToReturn]

        """
        self.swagger_types = {
            'client_ip': 'str',
            'port': 'str',
            'secret_key': 'str',
            'secret_key_temporary': 'str',
            'include_group_in_response': 'bool',
            'capture_client_ip': 'bool',
            'type_of_radius_app': 'str',
            'end_user_ip_attribute': 'str',
            'radius_vendor_specific_id': 'str',
            'country_code_response_attribute_id': 'str',
            'group_membership_radius_attribute': 'str',
            'response_format': 'str',
            'response_format_delimiter': 'str',
            'group_name_format': 'str',
            'password_and_otp_together': 'bool',
            'group_membership_to_return': 'list[AppGroupMembershipToReturn]'
        }
        self.attribute_map = {
            'client_ip': 'clientIP',
            'port': 'port',
            'secret_key': 'secretKey',
            'secret_key_temporary': 'secretKeyTemporary',
            'include_group_in_response': 'includeGroupInResponse',
            'capture_client_ip': 'captureClientIp',
            'type_of_radius_app': 'typeOfRadiusApp',
            'end_user_ip_attribute': 'endUserIPAttribute',
            'radius_vendor_specific_id': 'radiusVendorSpecificId',
            'country_code_response_attribute_id': 'countryCodeResponseAttributeId',
            'group_membership_radius_attribute': 'groupMembershipRadiusAttribute',
            'response_format': 'responseFormat',
            'response_format_delimiter': 'responseFormatDelimiter',
            'group_name_format': 'groupNameFormat',
            'password_and_otp_together': 'passwordAndOtpTogether',
            'group_membership_to_return': 'groupMembershipToReturn'
        }
        self._client_ip = None
        self._port = None
        self._secret_key = None
        self._secret_key_temporary = None
        self._include_group_in_response = None
        self._capture_client_ip = None
        self._type_of_radius_app = None
        self._end_user_ip_attribute = None
        self._radius_vendor_specific_id = None
        self._country_code_response_attribute_id = None
        self._group_membership_radius_attribute = None
        self._response_format = None
        self._response_format_delimiter = None
        self._group_name_format = None
        self._password_and_otp_together = None
        self._group_membership_to_return = None

    @property
    def client_ip(self):
        """
        **[Required]** Gets the client_ip of this AppExtensionRadiusAppApp.
        This is the IP address of the RADIUS Client like Oracle Database server. It can be only IP address and not hostname.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :return: The client_ip of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """
        Sets the client_ip of this AppExtensionRadiusAppApp.
        This is the IP address of the RADIUS Client like Oracle Database server. It can be only IP address and not hostname.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :param client_ip: The client_ip of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._client_ip = client_ip

    @property
    def port(self):
        """
        **[Required]** Gets the port of this AppExtensionRadiusAppApp.
        This is the port of RADIUS Proxy which RADIUS client will connect to.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :return: The port of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this AppExtensionRadiusAppApp.
        This is the port of RADIUS Proxy which RADIUS client will connect to.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :param port: The port of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._port = port

    @property
    def secret_key(self):
        """
        **[Required]** Gets the secret_key of this AppExtensionRadiusAppApp.
        Secret key used to secure communication between RADIUS Proxy and RADIUS client

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :return: The secret_key of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """
        Sets the secret_key of this AppExtensionRadiusAppApp.
        Secret key used to secure communication between RADIUS Proxy and RADIUS client

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :param secret_key: The secret_key of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._secret_key = secret_key

    @property
    def secret_key_temporary(self):
        """
        Gets the secret_key_temporary of this AppExtensionRadiusAppApp.
        Secret key used to secure communication between RADIUS Proxy and RADIUS client. This will be available only for few releases for an internal migration requirement. Use secretKey attribute instead of this attribute for all other requirements.

        **Added In:** 2306131901

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsSensitive: encrypt
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: never
         - type: string


        :return: The secret_key_temporary of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._secret_key_temporary

    @secret_key_temporary.setter
    def secret_key_temporary(self, secret_key_temporary):
        """
        Sets the secret_key_temporary of this AppExtensionRadiusAppApp.
        Secret key used to secure communication between RADIUS Proxy and RADIUS client. This will be available only for few releases for an internal migration requirement. Use secretKey attribute instead of this attribute for all other requirements.

        **Added In:** 2306131901

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsSensitive: encrypt
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: never
         - type: string


        :param secret_key_temporary: The secret_key_temporary of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._secret_key_temporary = secret_key_temporary

    @property
    def include_group_in_response(self):
        """
        **[Required]** Gets the include_group_in_response of this AppExtensionRadiusAppApp.
        Indicates to include groups in RADIUS response

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean


        :return: The include_group_in_response of this AppExtensionRadiusAppApp.
        :rtype: bool
        """
        return self._include_group_in_response

    @include_group_in_response.setter
    def include_group_in_response(self, include_group_in_response):
        """
        Sets the include_group_in_response of this AppExtensionRadiusAppApp.
        Indicates to include groups in RADIUS response

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean


        :param include_group_in_response: The include_group_in_response of this AppExtensionRadiusAppApp.
        :type: bool
        """
        self._include_group_in_response = include_group_in_response

    @property
    def capture_client_ip(self):
        """
        Gets the capture_client_ip of this AppExtensionRadiusAppApp.
        If true, capture the client IP address from the RADIUS request packet. IP Address is used for auditing, policy-evaluation and country-code calculation.

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean


        :return: The capture_client_ip of this AppExtensionRadiusAppApp.
        :rtype: bool
        """
        return self._capture_client_ip

    @capture_client_ip.setter
    def capture_client_ip(self, capture_client_ip):
        """
        Sets the capture_client_ip of this AppExtensionRadiusAppApp.
        If true, capture the client IP address from the RADIUS request packet. IP Address is used for auditing, policy-evaluation and country-code calculation.

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean


        :param capture_client_ip: The capture_client_ip of this AppExtensionRadiusAppApp.
        :type: bool
        """
        self._capture_client_ip = capture_client_ip

    @property
    def type_of_radius_app(self):
        """
        Gets the type_of_radius_app of this AppExtensionRadiusAppApp.
        Value consists of type of RADIUS App. Type can be Oracle Database, VPN etc

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :return: The type_of_radius_app of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._type_of_radius_app

    @type_of_radius_app.setter
    def type_of_radius_app(self, type_of_radius_app):
        """
        Sets the type_of_radius_app of this AppExtensionRadiusAppApp.
        Value consists of type of RADIUS App. Type can be Oracle Database, VPN etc

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :param type_of_radius_app: The type_of_radius_app of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._type_of_radius_app = type_of_radius_app

    @property
    def end_user_ip_attribute(self):
        """
        Gets the end_user_ip_attribute of this AppExtensionRadiusAppApp.
        The name of the attribute that contains the Internet Protocol address of the end-user.

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :return: The end_user_ip_attribute of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._end_user_ip_attribute

    @end_user_ip_attribute.setter
    def end_user_ip_attribute(self, end_user_ip_attribute):
        """
        Sets the end_user_ip_attribute of this AppExtensionRadiusAppApp.
        The name of the attribute that contains the Internet Protocol address of the end-user.

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :param end_user_ip_attribute: The end_user_ip_attribute of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._end_user_ip_attribute = end_user_ip_attribute

    @property
    def radius_vendor_specific_id(self):
        """
        Gets the radius_vendor_specific_id of this AppExtensionRadiusAppApp.
        ID used to identify a particular vendor.

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :return: The radius_vendor_specific_id of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._radius_vendor_specific_id

    @radius_vendor_specific_id.setter
    def radius_vendor_specific_id(self, radius_vendor_specific_id):
        """
        Sets the radius_vendor_specific_id of this AppExtensionRadiusAppApp.
        ID used to identify a particular vendor.

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :param radius_vendor_specific_id: The radius_vendor_specific_id of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._radius_vendor_specific_id = radius_vendor_specific_id

    @property
    def country_code_response_attribute_id(self):
        """
        Gets the country_code_response_attribute_id of this AppExtensionRadiusAppApp.
        Vendor-specific identifier of the attribute in the RADIUS response that will contain the end-user's country code. This is an integer-value in the range 1 to 255

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :return: The country_code_response_attribute_id of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._country_code_response_attribute_id

    @country_code_response_attribute_id.setter
    def country_code_response_attribute_id(self, country_code_response_attribute_id):
        """
        Sets the country_code_response_attribute_id of this AppExtensionRadiusAppApp.
        Vendor-specific identifier of the attribute in the RADIUS response that will contain the end-user's country code. This is an integer-value in the range 1 to 255

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :param country_code_response_attribute_id: The country_code_response_attribute_id of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._country_code_response_attribute_id = country_code_response_attribute_id

    @property
    def group_membership_radius_attribute(self):
        """
        Gets the group_membership_radius_attribute of this AppExtensionRadiusAppApp.
        RADIUS attribute that RADIUS-enabled system uses to pass the group membership

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :return: The group_membership_radius_attribute of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._group_membership_radius_attribute

    @group_membership_radius_attribute.setter
    def group_membership_radius_attribute(self, group_membership_radius_attribute):
        """
        Sets the group_membership_radius_attribute of this AppExtensionRadiusAppApp.
        RADIUS attribute that RADIUS-enabled system uses to pass the group membership

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :param group_membership_radius_attribute: The group_membership_radius_attribute of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._group_membership_radius_attribute = group_membership_radius_attribute

    @property
    def response_format(self):
        """
        Gets the response_format of this AppExtensionRadiusAppApp.
        Configure the responseFormat based on vendor in order to pass it to RADIUS infra

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :return: The response_format of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._response_format

    @response_format.setter
    def response_format(self, response_format):
        """
        Sets the response_format of this AppExtensionRadiusAppApp.
        Configure the responseFormat based on vendor in order to pass it to RADIUS infra

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :param response_format: The response_format of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._response_format = response_format

    @property
    def response_format_delimiter(self):
        """
        Gets the response_format_delimiter of this AppExtensionRadiusAppApp.
        The delimiter used if group membership responseFormat is a delimited list instead of repeating attributes

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :return: The response_format_delimiter of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._response_format_delimiter

    @response_format_delimiter.setter
    def response_format_delimiter(self, response_format_delimiter):
        """
        Sets the response_format_delimiter of this AppExtensionRadiusAppApp.
        The delimiter used if group membership responseFormat is a delimited list instead of repeating attributes

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :param response_format_delimiter: The response_format_delimiter of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._response_format_delimiter = response_format_delimiter

    @property
    def group_name_format(self):
        """
        Gets the group_name_format of this AppExtensionRadiusAppApp.
        Configure the groupNameFormat based on vendor in order to pass it to RADIUS infra

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :return: The group_name_format of this AppExtensionRadiusAppApp.
        :rtype: str
        """
        return self._group_name_format

    @group_name_format.setter
    def group_name_format(self, group_name_format):
        """
        Sets the group_name_format of this AppExtensionRadiusAppApp.
        Configure the groupNameFormat based on vendor in order to pass it to RADIUS infra

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :param group_name_format: The group_name_format of this AppExtensionRadiusAppApp.
        :type: str
        """
        self._group_name_format = group_name_format

    @property
    def password_and_otp_together(self):
        """
        Gets the password_and_otp_together of this AppExtensionRadiusAppApp.
        Indicates if password and OTP are passed in the same sign-in request or not.

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean


        :return: The password_and_otp_together of this AppExtensionRadiusAppApp.
        :rtype: bool
        """
        return self._password_and_otp_together

    @password_and_otp_together.setter
    def password_and_otp_together(self, password_and_otp_together):
        """
        Sets the password_and_otp_together of this AppExtensionRadiusAppApp.
        Indicates if password and OTP are passed in the same sign-in request or not.

        **Added In:** 2205120021

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean


        :param password_and_otp_together: The password_and_otp_together of this AppExtensionRadiusAppApp.
        :type: bool
        """
        self._password_and_otp_together = password_and_otp_together

    @property
    def group_membership_to_return(self):
        """
        Gets the group_membership_to_return of this AppExtensionRadiusAppApp.
        In a successful authentication response, Oracle Identity Cloud Service will pass user's group information restricted to groups persisted in this attribute, in the specified RADIUS attribute.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsCompositeKey: [value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :return: The group_membership_to_return of this AppExtensionRadiusAppApp.
        :rtype: list[oci.identity_domains.models.AppGroupMembershipToReturn]
        """
        return self._group_membership_to_return

    @group_membership_to_return.setter
    def group_membership_to_return(self, group_membership_to_return):
        """
        Sets the group_membership_to_return of this AppExtensionRadiusAppApp.
        In a successful authentication response, Oracle Identity Cloud Service will pass user's group information restricted to groups persisted in this attribute, in the specified RADIUS attribute.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsCompositeKey: [value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :param group_membership_to_return: The group_membership_to_return of this AppExtensionRadiusAppApp.
        :type: list[oci.identity_domains.models.AppGroupMembershipToReturn]
        """
        self._group_membership_to_return = group_membership_to_return

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
