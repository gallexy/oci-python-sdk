# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseEncryptionKeyDetails(object):
    """
    Details of the Autonomous Database encryption key.
    """

    #: A constant which can be used with the provider property of a AutonomousDatabaseEncryptionKeyDetails.
    #: This constant has a value of "AWS"
    PROVIDER_AWS = "AWS"

    #: A constant which can be used with the provider property of a AutonomousDatabaseEncryptionKeyDetails.
    #: This constant has a value of "AZURE"
    PROVIDER_AZURE = "AZURE"

    #: A constant which can be used with the provider property of a AutonomousDatabaseEncryptionKeyDetails.
    #: This constant has a value of "OCI"
    PROVIDER_OCI = "OCI"

    #: A constant which can be used with the provider property of a AutonomousDatabaseEncryptionKeyDetails.
    #: This constant has a value of "ORACLE_MANAGED"
    PROVIDER_ORACLE_MANAGED = "ORACLE_MANAGED"

    #: A constant which can be used with the provider property of a AutonomousDatabaseEncryptionKeyDetails.
    #: This constant has a value of "OKV"
    PROVIDER_OKV = "OKV"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseEncryptionKeyDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.OkvKeyDetails`
        * :class:`~oci.database.models.AzureKeyDetails`
        * :class:`~oci.database.models.AwsKeyDetails`
        * :class:`~oci.database.models.OciKeyDetails`
        * :class:`~oci.database.models.OracleManagedKeyDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param provider:
            The value to assign to the provider property of this AutonomousDatabaseEncryptionKeyDetails.
            Allowed values for this property are: "AWS", "AZURE", "OCI", "ORACLE_MANAGED", "OKV", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type provider: str

        """
        self.swagger_types = {
            'provider': 'str'
        }

        self.attribute_map = {
            'provider': 'provider'
        }

        self._provider = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['provider']

        if type == 'OKV':
            return 'OkvKeyDetails'

        if type == 'AZURE':
            return 'AzureKeyDetails'

        if type == 'AWS':
            return 'AwsKeyDetails'

        if type == 'OCI':
            return 'OciKeyDetails'

        if type == 'ORACLE_MANAGED':
            return 'OracleManagedKeyDetails'
        else:
            return 'AutonomousDatabaseEncryptionKeyDetails'

    @property
    def provider(self):
        """
        Gets the provider of this AutonomousDatabaseEncryptionKeyDetails.
        The provider for the Autonomous Database encryption key.

        Allowed values for this property are: "AWS", "AZURE", "OCI", "ORACLE_MANAGED", "OKV", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The provider of this AutonomousDatabaseEncryptionKeyDetails.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this AutonomousDatabaseEncryptionKeyDetails.
        The provider for the Autonomous Database encryption key.


        :param provider: The provider of this AutonomousDatabaseEncryptionKeyDetails.
        :type: str
        """
        allowed_values = ["AWS", "AZURE", "OCI", "ORACLE_MANAGED", "OKV"]
        if not value_allowed_none_or_none_sentinel(provider, allowed_values):
            provider = 'UNKNOWN_ENUM_VALUE'
        self._provider = provider

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
