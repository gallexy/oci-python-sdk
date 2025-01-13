# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DifferenceColumnSummary(object):
    """
    Summary of a SDM masking policy difference column.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DifferenceColumnSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DifferenceColumnSummary.
        :type key: str

        :param difference_type:
            The value to assign to the difference_type property of this DifferenceColumnSummary.
        :type difference_type: str

        :param sensitive_columnkey:
            The value to assign to the sensitive_columnkey property of this DifferenceColumnSummary.
        :type sensitive_columnkey: str

        :param masking_columnkey:
            The value to assign to the masking_columnkey property of this DifferenceColumnSummary.
        :type masking_columnkey: str

        :param schema_name:
            The value to assign to the schema_name property of this DifferenceColumnSummary.
        :type schema_name: str

        :param object_name:
            The value to assign to the object_name property of this DifferenceColumnSummary.
        :type object_name: str

        :param column_name:
            The value to assign to the column_name property of this DifferenceColumnSummary.
        :type column_name: str

        :param sensitive_type_id:
            The value to assign to the sensitive_type_id property of this DifferenceColumnSummary.
        :type sensitive_type_id: str

        :param planned_action:
            The value to assign to the planned_action property of this DifferenceColumnSummary.
        :type planned_action: str

        :param sync_status:
            The value to assign to the sync_status property of this DifferenceColumnSummary.
        :type sync_status: str

        :param time_last_synced:
            The value to assign to the time_last_synced property of this DifferenceColumnSummary.
        :type time_last_synced: datetime

        """
        self.swagger_types = {
            'key': 'str',
            'difference_type': 'str',
            'sensitive_columnkey': 'str',
            'masking_columnkey': 'str',
            'schema_name': 'str',
            'object_name': 'str',
            'column_name': 'str',
            'sensitive_type_id': 'str',
            'planned_action': 'str',
            'sync_status': 'str',
            'time_last_synced': 'datetime'
        }

        self.attribute_map = {
            'key': 'key',
            'difference_type': 'differenceType',
            'sensitive_columnkey': 'sensitiveColumnkey',
            'masking_columnkey': 'maskingColumnkey',
            'schema_name': 'schemaName',
            'object_name': 'objectName',
            'column_name': 'columnName',
            'sensitive_type_id': 'sensitiveTypeId',
            'planned_action': 'plannedAction',
            'sync_status': 'syncStatus',
            'time_last_synced': 'timeLastSynced'
        }

        self._key = None
        self._difference_type = None
        self._sensitive_columnkey = None
        self._masking_columnkey = None
        self._schema_name = None
        self._object_name = None
        self._column_name = None
        self._sensitive_type_id = None
        self._planned_action = None
        self._sync_status = None
        self._time_last_synced = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this DifferenceColumnSummary.
        The unique key that identifies the SDM masking policy difference column.


        :return: The key of this DifferenceColumnSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DifferenceColumnSummary.
        The unique key that identifies the SDM masking policy difference column.


        :param key: The key of this DifferenceColumnSummary.
        :type: str
        """
        self._key = key

    @property
    def difference_type(self):
        """
        **[Required]** Gets the difference_type of this DifferenceColumnSummary.
        The type of the SDM masking policy difference column. It can be one of the following three types:
        NEW: A new sensitive column in the sensitive data model that is not in the masking policy.
        DELETED: A column that is present in the masking policy but has been deleted from the sensitive data model.
        MODIFIED: A column that is present in the masking policy as well as the sensitive data model but some of its attributes have been modified.


        :return: The difference_type of this DifferenceColumnSummary.
        :rtype: str
        """
        return self._difference_type

    @difference_type.setter
    def difference_type(self, difference_type):
        """
        Sets the difference_type of this DifferenceColumnSummary.
        The type of the SDM masking policy difference column. It can be one of the following three types:
        NEW: A new sensitive column in the sensitive data model that is not in the masking policy.
        DELETED: A column that is present in the masking policy but has been deleted from the sensitive data model.
        MODIFIED: A column that is present in the masking policy as well as the sensitive data model but some of its attributes have been modified.


        :param difference_type: The difference_type of this DifferenceColumnSummary.
        :type: str
        """
        self._difference_type = difference_type

    @property
    def sensitive_columnkey(self):
        """
        Gets the sensitive_columnkey of this DifferenceColumnSummary.
        The unique key that identifies the sensitive column represented by the SDM masking policy difference column.


        :return: The sensitive_columnkey of this DifferenceColumnSummary.
        :rtype: str
        """
        return self._sensitive_columnkey

    @sensitive_columnkey.setter
    def sensitive_columnkey(self, sensitive_columnkey):
        """
        Sets the sensitive_columnkey of this DifferenceColumnSummary.
        The unique key that identifies the sensitive column represented by the SDM masking policy difference column.


        :param sensitive_columnkey: The sensitive_columnkey of this DifferenceColumnSummary.
        :type: str
        """
        self._sensitive_columnkey = sensitive_columnkey

    @property
    def masking_columnkey(self):
        """
        Gets the masking_columnkey of this DifferenceColumnSummary.
        The unique key that identifies the masking column represented by the SDM masking policy difference column.


        :return: The masking_columnkey of this DifferenceColumnSummary.
        :rtype: str
        """
        return self._masking_columnkey

    @masking_columnkey.setter
    def masking_columnkey(self, masking_columnkey):
        """
        Sets the masking_columnkey of this DifferenceColumnSummary.
        The unique key that identifies the masking column represented by the SDM masking policy difference column.


        :param masking_columnkey: The masking_columnkey of this DifferenceColumnSummary.
        :type: str
        """
        self._masking_columnkey = masking_columnkey

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this DifferenceColumnSummary.
        The database schema that contains the difference column.


        :return: The schema_name of this DifferenceColumnSummary.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this DifferenceColumnSummary.
        The database schema that contains the difference column.


        :param schema_name: The schema_name of this DifferenceColumnSummary.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this DifferenceColumnSummary.
        The database object that contains the difference column.


        :return: The object_name of this DifferenceColumnSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this DifferenceColumnSummary.
        The database object that contains the difference column.


        :param object_name: The object_name of this DifferenceColumnSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def column_name(self):
        """
        **[Required]** Gets the column_name of this DifferenceColumnSummary.
        The name of the difference column.


        :return: The column_name of this DifferenceColumnSummary.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this DifferenceColumnSummary.
        The name of the difference column.


        :param column_name: The column_name of this DifferenceColumnSummary.
        :type: str
        """
        self._column_name = column_name

    @property
    def sensitive_type_id(self):
        """
        Gets the sensitive_type_id of this DifferenceColumnSummary.
        The OCID of the sensitive type associated with the difference column.


        :return: The sensitive_type_id of this DifferenceColumnSummary.
        :rtype: str
        """
        return self._sensitive_type_id

    @sensitive_type_id.setter
    def sensitive_type_id(self, sensitive_type_id):
        """
        Sets the sensitive_type_id of this DifferenceColumnSummary.
        The OCID of the sensitive type associated with the difference column.


        :param sensitive_type_id: The sensitive_type_id of this DifferenceColumnSummary.
        :type: str
        """
        self._sensitive_type_id = sensitive_type_id

    @property
    def planned_action(self):
        """
        **[Required]** Gets the planned_action of this DifferenceColumnSummary.
        Specifies how to process the difference column. It's set to SYNC by default. Use the PatchSdmMaskingPolicyDifferenceColumns operation to update this attribute. You can choose one of the following options:
        SYNC: To sync the difference column and update the masking policy to reflect the changes.
        NO_SYNC: To not sync the difference column so that it doesn't change the masking policy.
        After specifying the planned action, you can use the ApplySdmMaskingPolicyDifference operation to automatically process the difference columns.


        :return: The planned_action of this DifferenceColumnSummary.
        :rtype: str
        """
        return self._planned_action

    @planned_action.setter
    def planned_action(self, planned_action):
        """
        Sets the planned_action of this DifferenceColumnSummary.
        Specifies how to process the difference column. It's set to SYNC by default. Use the PatchSdmMaskingPolicyDifferenceColumns operation to update this attribute. You can choose one of the following options:
        SYNC: To sync the difference column and update the masking policy to reflect the changes.
        NO_SYNC: To not sync the difference column so that it doesn't change the masking policy.
        After specifying the planned action, you can use the ApplySdmMaskingPolicyDifference operation to automatically process the difference columns.


        :param planned_action: The planned_action of this DifferenceColumnSummary.
        :type: str
        """
        self._planned_action = planned_action

    @property
    def sync_status(self):
        """
        **[Required]** Gets the sync_status of this DifferenceColumnSummary.
        Indicates if the difference column has been processed.Use GetDifferenceColumn operation to track whether the difference column has
        already been processed and applied to the masking policy.


        :return: The sync_status of this DifferenceColumnSummary.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """
        Sets the sync_status of this DifferenceColumnSummary.
        Indicates if the difference column has been processed.Use GetDifferenceColumn operation to track whether the difference column has
        already been processed and applied to the masking policy.


        :param sync_status: The sync_status of this DifferenceColumnSummary.
        :type: str
        """
        self._sync_status = sync_status

    @property
    def time_last_synced(self):
        """
        Gets the time_last_synced of this DifferenceColumnSummary.
        The date and time the SDM masking policy difference column was last synced, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_last_synced of this DifferenceColumnSummary.
        :rtype: datetime
        """
        return self._time_last_synced

    @time_last_synced.setter
    def time_last_synced(self, time_last_synced):
        """
        Sets the time_last_synced of this DifferenceColumnSummary.
        The date and time the SDM masking policy difference column was last synced, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_last_synced: The time_last_synced of this DifferenceColumnSummary.
        :type: datetime
        """
        self._time_last_synced = time_last_synced

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
