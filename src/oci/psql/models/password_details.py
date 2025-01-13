# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PasswordDetails(object):
    """
    Details for the database system password.
    Password can be passed as `VaultSecretPasswordDetails` or `PlainTextPasswordDetails`.
    """

    #: A constant which can be used with the password_type property of a PasswordDetails.
    #: This constant has a value of "PLAIN_TEXT"
    PASSWORD_TYPE_PLAIN_TEXT = "PLAIN_TEXT"

    #: A constant which can be used with the password_type property of a PasswordDetails.
    #: This constant has a value of "VAULT_SECRET"
    PASSWORD_TYPE_VAULT_SECRET = "VAULT_SECRET"

    def __init__(self, **kwargs):
        """
        Initializes a new PasswordDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.psql.models.PlainTextPasswordDetails`
        * :class:`~oci.psql.models.VaultSecretPasswordDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password_type:
            The value to assign to the password_type property of this PasswordDetails.
            Allowed values for this property are: "PLAIN_TEXT", "VAULT_SECRET"
        :type password_type: str

        """
        self.swagger_types = {
            'password_type': 'str'
        }

        self.attribute_map = {
            'password_type': 'passwordType'
        }

        self._password_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['passwordType']

        if type == 'PLAIN_TEXT':
            return 'PlainTextPasswordDetails'

        if type == 'VAULT_SECRET':
            return 'VaultSecretPasswordDetails'
        else:
            return 'PasswordDetails'

    @property
    def password_type(self):
        """
        **[Required]** Gets the password_type of this PasswordDetails.
        The password type.

        Allowed values for this property are: "PLAIN_TEXT", "VAULT_SECRET"


        :return: The password_type of this PasswordDetails.
        :rtype: str
        """
        return self._password_type

    @password_type.setter
    def password_type(self, password_type):
        """
        Sets the password_type of this PasswordDetails.
        The password type.


        :param password_type: The password_type of this PasswordDetails.
        :type: str
        """
        allowed_values = ["PLAIN_TEXT", "VAULT_SECRET"]
        if not value_allowed_none_or_none_sentinel(password_type, allowed_values):
            raise ValueError(
                f"Invalid value for `password_type`, must be None or one of {allowed_values}"
            )
        self._password_type = password_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
