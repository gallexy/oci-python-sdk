# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20191001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VerifyAddressReceipt(object):
    """
    Address verficiation result
    """

    #: A constant which can be used with the quality property of a VerifyAddressReceipt.
    #: This constant has a value of "EXCELLENT"
    QUALITY_EXCELLENT = "EXCELLENT"

    #: A constant which can be used with the quality property of a VerifyAddressReceipt.
    #: This constant has a value of "GOOD"
    QUALITY_GOOD = "GOOD"

    #: A constant which can be used with the quality property of a VerifyAddressReceipt.
    #: This constant has a value of "AVERAGE"
    QUALITY_AVERAGE = "AVERAGE"

    #: A constant which can be used with the quality property of a VerifyAddressReceipt.
    #: This constant has a value of "POOR"
    QUALITY_POOR = "POOR"

    #: A constant which can be used with the quality property of a VerifyAddressReceipt.
    #: This constant has a value of "BAD"
    QUALITY_BAD = "BAD"

    #: A constant which can be used with the verification_code property of a VerifyAddressReceipt.
    #: This constant has a value of "VERIFIED"
    VERIFICATION_CODE_VERIFIED = "VERIFIED"

    #: A constant which can be used with the verification_code property of a VerifyAddressReceipt.
    #: This constant has a value of "PARTIALLY_VERIFIED"
    VERIFICATION_CODE_PARTIALLY_VERIFIED = "PARTIALLY_VERIFIED"

    #: A constant which can be used with the verification_code property of a VerifyAddressReceipt.
    #: This constant has a value of "AMBIGUOUS"
    VERIFICATION_CODE_AMBIGUOUS = "AMBIGUOUS"

    #: A constant which can be used with the verification_code property of a VerifyAddressReceipt.
    #: This constant has a value of "REVERTED"
    VERIFICATION_CODE_REVERTED = "REVERTED"

    #: A constant which can be used with the verification_code property of a VerifyAddressReceipt.
    #: This constant has a value of "UNVERIFIED"
    VERIFICATION_CODE_UNVERIFIED = "UNVERIFIED"

    def __init__(self, **kwargs):
        """
        Initializes a new VerifyAddressReceipt object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param address:
            The value to assign to the address property of this VerifyAddressReceipt.
        :type address: oci.osp_gateway.models.Address

        :param quality:
            The value to assign to the quality property of this VerifyAddressReceipt.
            Allowed values for this property are: "EXCELLENT", "GOOD", "AVERAGE", "POOR", "BAD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type quality: str

        :param verification_code:
            The value to assign to the verification_code property of this VerifyAddressReceipt.
            Allowed values for this property are: "VERIFIED", "PARTIALLY_VERIFIED", "AMBIGUOUS", "REVERTED", "UNVERIFIED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type verification_code: str

        """
        self.swagger_types = {
            'address': 'Address',
            'quality': 'str',
            'verification_code': 'str'
        }
        self.attribute_map = {
            'address': 'address',
            'quality': 'quality',
            'verification_code': 'verificationCode'
        }
        self._address = None
        self._quality = None
        self._verification_code = None

    @property
    def address(self):
        """
        **[Required]** Gets the address of this VerifyAddressReceipt.

        :return: The address of this VerifyAddressReceipt.
        :rtype: oci.osp_gateway.models.Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this VerifyAddressReceipt.

        :param address: The address of this VerifyAddressReceipt.
        :type: oci.osp_gateway.models.Address
        """
        self._address = address

    @property
    def quality(self):
        """
        **[Required]** Gets the quality of this VerifyAddressReceipt.
        Address quality type.

        Allowed values for this property are: "EXCELLENT", "GOOD", "AVERAGE", "POOR", "BAD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The quality of this VerifyAddressReceipt.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """
        Sets the quality of this VerifyAddressReceipt.
        Address quality type.


        :param quality: The quality of this VerifyAddressReceipt.
        :type: str
        """
        allowed_values = ["EXCELLENT", "GOOD", "AVERAGE", "POOR", "BAD"]
        if not value_allowed_none_or_none_sentinel(quality, allowed_values):
            quality = 'UNKNOWN_ENUM_VALUE'
        self._quality = quality

    @property
    def verification_code(self):
        """
        **[Required]** Gets the verification_code of this VerifyAddressReceipt.
        Address verification code.

        Allowed values for this property are: "VERIFIED", "PARTIALLY_VERIFIED", "AMBIGUOUS", "REVERTED", "UNVERIFIED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The verification_code of this VerifyAddressReceipt.
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """
        Sets the verification_code of this VerifyAddressReceipt.
        Address verification code.


        :param verification_code: The verification_code of this VerifyAddressReceipt.
        :type: str
        """
        allowed_values = ["VERIFIED", "PARTIALLY_VERIFIED", "AMBIGUOUS", "REVERTED", "UNVERIFIED"]
        if not value_allowed_none_or_none_sentinel(verification_code, allowed_values):
            verification_code = 'UNKNOWN_ENUM_VALUE'
        self._verification_code = verification_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
