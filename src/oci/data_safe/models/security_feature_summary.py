# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityFeatureSummary(object):
    """
    The details of database security feature usage available on a given compartment.
    """

    #: A constant which can be used with the unified_audit property of a SecurityFeatureSummary.
    #: This constant has a value of "ENABLED"
    UNIFIED_AUDIT_ENABLED = "ENABLED"

    #: A constant which can be used with the unified_audit property of a SecurityFeatureSummary.
    #: This constant has a value of "DISABLED"
    UNIFIED_AUDIT_DISABLED = "DISABLED"

    #: A constant which can be used with the unified_audit property of a SecurityFeatureSummary.
    #: This constant has a value of "NONE"
    UNIFIED_AUDIT_NONE = "NONE"

    #: A constant which can be used with the fine_grained_audit property of a SecurityFeatureSummary.
    #: This constant has a value of "ENABLED"
    FINE_GRAINED_AUDIT_ENABLED = "ENABLED"

    #: A constant which can be used with the fine_grained_audit property of a SecurityFeatureSummary.
    #: This constant has a value of "DISABLED"
    FINE_GRAINED_AUDIT_DISABLED = "DISABLED"

    #: A constant which can be used with the fine_grained_audit property of a SecurityFeatureSummary.
    #: This constant has a value of "NONE"
    FINE_GRAINED_AUDIT_NONE = "NONE"

    #: A constant which can be used with the traditional_audit property of a SecurityFeatureSummary.
    #: This constant has a value of "ENABLED"
    TRADITIONAL_AUDIT_ENABLED = "ENABLED"

    #: A constant which can be used with the traditional_audit property of a SecurityFeatureSummary.
    #: This constant has a value of "DISABLED"
    TRADITIONAL_AUDIT_DISABLED = "DISABLED"

    #: A constant which can be used with the traditional_audit property of a SecurityFeatureSummary.
    #: This constant has a value of "NONE"
    TRADITIONAL_AUDIT_NONE = "NONE"

    #: A constant which can be used with the database_vault property of a SecurityFeatureSummary.
    #: This constant has a value of "ENABLED"
    DATABASE_VAULT_ENABLED = "ENABLED"

    #: A constant which can be used with the database_vault property of a SecurityFeatureSummary.
    #: This constant has a value of "DISABLED"
    DATABASE_VAULT_DISABLED = "DISABLED"

    #: A constant which can be used with the database_vault property of a SecurityFeatureSummary.
    #: This constant has a value of "NONE"
    DATABASE_VAULT_NONE = "NONE"

    #: A constant which can be used with the privilege_analysis property of a SecurityFeatureSummary.
    #: This constant has a value of "ENABLED"
    PRIVILEGE_ANALYSIS_ENABLED = "ENABLED"

    #: A constant which can be used with the privilege_analysis property of a SecurityFeatureSummary.
    #: This constant has a value of "DISABLED"
    PRIVILEGE_ANALYSIS_DISABLED = "DISABLED"

    #: A constant which can be used with the privilege_analysis property of a SecurityFeatureSummary.
    #: This constant has a value of "NONE"
    PRIVILEGE_ANALYSIS_NONE = "NONE"

    #: A constant which can be used with the tablespace_encryption property of a SecurityFeatureSummary.
    #: This constant has a value of "ENABLED"
    TABLESPACE_ENCRYPTION_ENABLED = "ENABLED"

    #: A constant which can be used with the tablespace_encryption property of a SecurityFeatureSummary.
    #: This constant has a value of "DISABLED"
    TABLESPACE_ENCRYPTION_DISABLED = "DISABLED"

    #: A constant which can be used with the tablespace_encryption property of a SecurityFeatureSummary.
    #: This constant has a value of "NONE"
    TABLESPACE_ENCRYPTION_NONE = "NONE"

    #: A constant which can be used with the column_encryption property of a SecurityFeatureSummary.
    #: This constant has a value of "ENABLED"
    COLUMN_ENCRYPTION_ENABLED = "ENABLED"

    #: A constant which can be used with the column_encryption property of a SecurityFeatureSummary.
    #: This constant has a value of "DISABLED"
    COLUMN_ENCRYPTION_DISABLED = "DISABLED"

    #: A constant which can be used with the column_encryption property of a SecurityFeatureSummary.
    #: This constant has a value of "NONE"
    COLUMN_ENCRYPTION_NONE = "NONE"

    #: A constant which can be used with the network_encryption property of a SecurityFeatureSummary.
    #: This constant has a value of "ENABLED"
    NETWORK_ENCRYPTION_ENABLED = "ENABLED"

    #: A constant which can be used with the network_encryption property of a SecurityFeatureSummary.
    #: This constant has a value of "DISABLED"
    NETWORK_ENCRYPTION_DISABLED = "DISABLED"

    #: A constant which can be used with the network_encryption property of a SecurityFeatureSummary.
    #: This constant has a value of "NONE"
    NETWORK_ENCRYPTION_NONE = "NONE"

    #: A constant which can be used with the password_authentication property of a SecurityFeatureSummary.
    #: This constant has a value of "ENABLED"
    PASSWORD_AUTHENTICATION_ENABLED = "ENABLED"

    #: A constant which can be used with the password_authentication property of a SecurityFeatureSummary.
    #: This constant has a value of "DISABLED"
    PASSWORD_AUTHENTICATION_DISABLED = "DISABLED"

    #: A constant which can be used with the password_authentication property of a SecurityFeatureSummary.
    #: This constant has a value of "NONE"
    PASSWORD_AUTHENTICATION_NONE = "NONE"

    #: A constant which can be used with the global_authentication property of a SecurityFeatureSummary.
    #: This constant has a value of "ENABLED"
    GLOBAL_AUTHENTICATION_ENABLED = "ENABLED"

    #: A constant which can be used with the global_authentication property of a SecurityFeatureSummary.
    #: This constant has a value of "DISABLED"
    GLOBAL_AUTHENTICATION_DISABLED = "DISABLED"

    #: A constant which can be used with the global_authentication property of a SecurityFeatureSummary.
    #: This constant has a value of "NONE"
    GLOBAL_AUTHENTICATION_NONE = "NONE"

    #: A constant which can be used with the external_authentication property of a SecurityFeatureSummary.
    #: This constant has a value of "ENABLED"
    EXTERNAL_AUTHENTICATION_ENABLED = "ENABLED"

    #: A constant which can be used with the external_authentication property of a SecurityFeatureSummary.
    #: This constant has a value of "DISABLED"
    EXTERNAL_AUTHENTICATION_DISABLED = "DISABLED"

    #: A constant which can be used with the external_authentication property of a SecurityFeatureSummary.
    #: This constant has a value of "NONE"
    EXTERNAL_AUTHENTICATION_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityFeatureSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this SecurityFeatureSummary.
        :type compartment_id: str

        :param target_id:
            The value to assign to the target_id property of this SecurityFeatureSummary.
        :type target_id: str

        :param assessment_id:
            The value to assign to the assessment_id property of this SecurityFeatureSummary.
        :type assessment_id: str

        :param unified_audit:
            The value to assign to the unified_audit property of this SecurityFeatureSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unified_audit: str

        :param fine_grained_audit:
            The value to assign to the fine_grained_audit property of this SecurityFeatureSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type fine_grained_audit: str

        :param traditional_audit:
            The value to assign to the traditional_audit property of this SecurityFeatureSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type traditional_audit: str

        :param database_vault:
            The value to assign to the database_vault property of this SecurityFeatureSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_vault: str

        :param privilege_analysis:
            The value to assign to the privilege_analysis property of this SecurityFeatureSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type privilege_analysis: str

        :param tablespace_encryption:
            The value to assign to the tablespace_encryption property of this SecurityFeatureSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type tablespace_encryption: str

        :param column_encryption:
            The value to assign to the column_encryption property of this SecurityFeatureSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type column_encryption: str

        :param network_encryption:
            The value to assign to the network_encryption property of this SecurityFeatureSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type network_encryption: str

        :param password_authentication:
            The value to assign to the password_authentication property of this SecurityFeatureSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type password_authentication: str

        :param global_authentication:
            The value to assign to the global_authentication property of this SecurityFeatureSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type global_authentication: str

        :param external_authentication:
            The value to assign to the external_authentication property of this SecurityFeatureSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type external_authentication: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SecurityFeatureSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SecurityFeatureSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'target_id': 'str',
            'assessment_id': 'str',
            'unified_audit': 'str',
            'fine_grained_audit': 'str',
            'traditional_audit': 'str',
            'database_vault': 'str',
            'privilege_analysis': 'str',
            'tablespace_encryption': 'str',
            'column_encryption': 'str',
            'network_encryption': 'str',
            'password_authentication': 'str',
            'global_authentication': 'str',
            'external_authentication': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'target_id': 'targetId',
            'assessment_id': 'assessmentId',
            'unified_audit': 'unifiedAudit',
            'fine_grained_audit': 'fineGrainedAudit',
            'traditional_audit': 'traditionalAudit',
            'database_vault': 'databaseVault',
            'privilege_analysis': 'privilegeAnalysis',
            'tablespace_encryption': 'tablespaceEncryption',
            'column_encryption': 'columnEncryption',
            'network_encryption': 'networkEncryption',
            'password_authentication': 'passwordAuthentication',
            'global_authentication': 'globalAuthentication',
            'external_authentication': 'externalAuthentication',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._target_id = None
        self._assessment_id = None
        self._unified_audit = None
        self._fine_grained_audit = None
        self._traditional_audit = None
        self._database_vault = None
        self._privilege_analysis = None
        self._tablespace_encryption = None
        self._column_encryption = None
        self._network_encryption = None
        self._password_authentication = None
        self._global_authentication = None
        self._external_authentication = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SecurityFeatureSummary.
        The OCID of the compartment.


        :return: The compartment_id of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SecurityFeatureSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this SecurityFeatureSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this SecurityFeatureSummary.
        The OCID of the target database.


        :return: The target_id of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this SecurityFeatureSummary.
        The OCID of the target database.


        :param target_id: The target_id of this SecurityFeatureSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def assessment_id(self):
        """
        **[Required]** Gets the assessment_id of this SecurityFeatureSummary.
        The OCID of the assessment that generates this security feature usage result.


        :return: The assessment_id of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._assessment_id

    @assessment_id.setter
    def assessment_id(self, assessment_id):
        """
        Sets the assessment_id of this SecurityFeatureSummary.
        The OCID of the assessment that generates this security feature usage result.


        :param assessment_id: The assessment_id of this SecurityFeatureSummary.
        :type: str
        """
        self._assessment_id = assessment_id

    @property
    def unified_audit(self):
        """
        **[Required]** Gets the unified_audit of this SecurityFeatureSummary.
        The usage of security feature - Unified Audit.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unified_audit of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._unified_audit

    @unified_audit.setter
    def unified_audit(self, unified_audit):
        """
        Sets the unified_audit of this SecurityFeatureSummary.
        The usage of security feature - Unified Audit.


        :param unified_audit: The unified_audit of this SecurityFeatureSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(unified_audit, allowed_values):
            unified_audit = 'UNKNOWN_ENUM_VALUE'
        self._unified_audit = unified_audit

    @property
    def fine_grained_audit(self):
        """
        **[Required]** Gets the fine_grained_audit of this SecurityFeatureSummary.
        The usage of security feature - Fine Grained Audit.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The fine_grained_audit of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._fine_grained_audit

    @fine_grained_audit.setter
    def fine_grained_audit(self, fine_grained_audit):
        """
        Sets the fine_grained_audit of this SecurityFeatureSummary.
        The usage of security feature - Fine Grained Audit.


        :param fine_grained_audit: The fine_grained_audit of this SecurityFeatureSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(fine_grained_audit, allowed_values):
            fine_grained_audit = 'UNKNOWN_ENUM_VALUE'
        self._fine_grained_audit = fine_grained_audit

    @property
    def traditional_audit(self):
        """
        **[Required]** Gets the traditional_audit of this SecurityFeatureSummary.
        The usage of security feature - Traditional Audit.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The traditional_audit of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._traditional_audit

    @traditional_audit.setter
    def traditional_audit(self, traditional_audit):
        """
        Sets the traditional_audit of this SecurityFeatureSummary.
        The usage of security feature - Traditional Audit.


        :param traditional_audit: The traditional_audit of this SecurityFeatureSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(traditional_audit, allowed_values):
            traditional_audit = 'UNKNOWN_ENUM_VALUE'
        self._traditional_audit = traditional_audit

    @property
    def database_vault(self):
        """
        **[Required]** Gets the database_vault of this SecurityFeatureSummary.
        The usage of security feature - Database Vault.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_vault of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._database_vault

    @database_vault.setter
    def database_vault(self, database_vault):
        """
        Sets the database_vault of this SecurityFeatureSummary.
        The usage of security feature - Database Vault.


        :param database_vault: The database_vault of this SecurityFeatureSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(database_vault, allowed_values):
            database_vault = 'UNKNOWN_ENUM_VALUE'
        self._database_vault = database_vault

    @property
    def privilege_analysis(self):
        """
        **[Required]** Gets the privilege_analysis of this SecurityFeatureSummary.
        The usage of security feature - Privilege Analysis.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The privilege_analysis of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._privilege_analysis

    @privilege_analysis.setter
    def privilege_analysis(self, privilege_analysis):
        """
        Sets the privilege_analysis of this SecurityFeatureSummary.
        The usage of security feature - Privilege Analysis.


        :param privilege_analysis: The privilege_analysis of this SecurityFeatureSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(privilege_analysis, allowed_values):
            privilege_analysis = 'UNKNOWN_ENUM_VALUE'
        self._privilege_analysis = privilege_analysis

    @property
    def tablespace_encryption(self):
        """
        **[Required]** Gets the tablespace_encryption of this SecurityFeatureSummary.
        The usage of security feature - Tablespace Encryption.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The tablespace_encryption of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._tablespace_encryption

    @tablespace_encryption.setter
    def tablespace_encryption(self, tablespace_encryption):
        """
        Sets the tablespace_encryption of this SecurityFeatureSummary.
        The usage of security feature - Tablespace Encryption.


        :param tablespace_encryption: The tablespace_encryption of this SecurityFeatureSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(tablespace_encryption, allowed_values):
            tablespace_encryption = 'UNKNOWN_ENUM_VALUE'
        self._tablespace_encryption = tablespace_encryption

    @property
    def column_encryption(self):
        """
        **[Required]** Gets the column_encryption of this SecurityFeatureSummary.
        The usage of security feature - Column Encryption.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The column_encryption of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._column_encryption

    @column_encryption.setter
    def column_encryption(self, column_encryption):
        """
        Sets the column_encryption of this SecurityFeatureSummary.
        The usage of security feature - Column Encryption.


        :param column_encryption: The column_encryption of this SecurityFeatureSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(column_encryption, allowed_values):
            column_encryption = 'UNKNOWN_ENUM_VALUE'
        self._column_encryption = column_encryption

    @property
    def network_encryption(self):
        """
        **[Required]** Gets the network_encryption of this SecurityFeatureSummary.
        The usage of security feature - Network Encryption.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The network_encryption of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._network_encryption

    @network_encryption.setter
    def network_encryption(self, network_encryption):
        """
        Sets the network_encryption of this SecurityFeatureSummary.
        The usage of security feature - Network Encryption.


        :param network_encryption: The network_encryption of this SecurityFeatureSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(network_encryption, allowed_values):
            network_encryption = 'UNKNOWN_ENUM_VALUE'
        self._network_encryption = network_encryption

    @property
    def password_authentication(self):
        """
        **[Required]** Gets the password_authentication of this SecurityFeatureSummary.
        The usage of security feature - Password Authentication.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The password_authentication of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._password_authentication

    @password_authentication.setter
    def password_authentication(self, password_authentication):
        """
        Sets the password_authentication of this SecurityFeatureSummary.
        The usage of security feature - Password Authentication.


        :param password_authentication: The password_authentication of this SecurityFeatureSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(password_authentication, allowed_values):
            password_authentication = 'UNKNOWN_ENUM_VALUE'
        self._password_authentication = password_authentication

    @property
    def global_authentication(self):
        """
        **[Required]** Gets the global_authentication of this SecurityFeatureSummary.
        The usage of security feature - Global Authentication.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The global_authentication of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._global_authentication

    @global_authentication.setter
    def global_authentication(self, global_authentication):
        """
        Sets the global_authentication of this SecurityFeatureSummary.
        The usage of security feature - Global Authentication.


        :param global_authentication: The global_authentication of this SecurityFeatureSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(global_authentication, allowed_values):
            global_authentication = 'UNKNOWN_ENUM_VALUE'
        self._global_authentication = global_authentication

    @property
    def external_authentication(self):
        """
        **[Required]** Gets the external_authentication of this SecurityFeatureSummary.
        The usage of security feature - External Authentication.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The external_authentication of this SecurityFeatureSummary.
        :rtype: str
        """
        return self._external_authentication

    @external_authentication.setter
    def external_authentication(self, external_authentication):
        """
        Sets the external_authentication of this SecurityFeatureSummary.
        The usage of security feature - External Authentication.


        :param external_authentication: The external_authentication of this SecurityFeatureSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(external_authentication, allowed_values):
            external_authentication = 'UNKNOWN_ENUM_VALUE'
        self._external_authentication = external_authentication

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SecurityFeatureSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SecurityFeatureSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SecurityFeatureSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SecurityFeatureSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SecurityFeatureSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SecurityFeatureSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SecurityFeatureSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SecurityFeatureSummary.
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
