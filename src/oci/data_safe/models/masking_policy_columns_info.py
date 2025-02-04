# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskingPolicyColumnsInfo(object):
    """
    maskingPolicyColumnsInfo object has details of column group with schema details.
    """

    #: A constant which can be used with the object_type property of a MaskingPolicyColumnsInfo.
    #: This constant has a value of "TABLE"
    OBJECT_TYPE_TABLE = "TABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new MaskingPolicyColumnsInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schema_name:
            The value to assign to the schema_name property of this MaskingPolicyColumnsInfo.
        :type schema_name: str

        :param object_type:
            The value to assign to the object_type property of this MaskingPolicyColumnsInfo.
            Allowed values for this property are: "TABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type object_type: str

        :param object_name:
            The value to assign to the object_name property of this MaskingPolicyColumnsInfo.
        :type object_name: str

        :param referential_column_group:
            The value to assign to the referential_column_group property of this MaskingPolicyColumnsInfo.
        :type referential_column_group: list[str]

        """
        self.swagger_types = {
            'schema_name': 'str',
            'object_type': 'str',
            'object_name': 'str',
            'referential_column_group': 'list[str]'
        }

        self.attribute_map = {
            'schema_name': 'schemaName',
            'object_type': 'objectType',
            'object_name': 'objectName',
            'referential_column_group': 'referentialColumnGroup'
        }

        self._schema_name = None
        self._object_type = None
        self._object_name = None
        self._referential_column_group = None

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this MaskingPolicyColumnsInfo.
        The name of the schema that contains the database column(s).


        :return: The schema_name of this MaskingPolicyColumnsInfo.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this MaskingPolicyColumnsInfo.
        The name of the schema that contains the database column(s).


        :param schema_name: The schema_name of this MaskingPolicyColumnsInfo.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def object_type(self):
        """
        **[Required]** Gets the object_type of this MaskingPolicyColumnsInfo.
        The type of the database object that contains the masking policy.

        Allowed values for this property are: "TABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The object_type of this MaskingPolicyColumnsInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this MaskingPolicyColumnsInfo.
        The type of the database object that contains the masking policy.


        :param object_type: The object_type of this MaskingPolicyColumnsInfo.
        :type: str
        """
        allowed_values = ["TABLE"]
        if not value_allowed_none_or_none_sentinel(object_type, allowed_values):
            object_type = 'UNKNOWN_ENUM_VALUE'
        self._object_type = object_type

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this MaskingPolicyColumnsInfo.
        The name of the object (table or editioning view) that contains the database column(s).


        :return: The object_name of this MaskingPolicyColumnsInfo.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this MaskingPolicyColumnsInfo.
        The name of the object (table or editioning view) that contains the database column(s).


        :param object_name: The object_name of this MaskingPolicyColumnsInfo.
        :type: str
        """
        self._object_name = object_name

    @property
    def referential_column_group(self):
        """
        **[Required]** Gets the referential_column_group of this MaskingPolicyColumnsInfo.
        Group of columns in referential relation. Order needs to be maintained in the elements of the parent/child array listing.


        :return: The referential_column_group of this MaskingPolicyColumnsInfo.
        :rtype: list[str]
        """
        return self._referential_column_group

    @referential_column_group.setter
    def referential_column_group(self, referential_column_group):
        """
        Sets the referential_column_group of this MaskingPolicyColumnsInfo.
        Group of columns in referential relation. Order needs to be maintained in the elements of the parent/child array listing.


        :param referential_column_group: The referential_column_group of this MaskingPolicyColumnsInfo.
        :type: list[str]
        """
        self._referential_column_group = referential_column_group

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
