# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230301

from .prevalidate_payload import PrevalidatePayload
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrevalidatePatchPayload(PrevalidatePayload):
    """
    Payload to prevalidate patch sharded database operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrevalidatePatchPayload object with values from keyword arguments. The default value of the :py:attr:`~oci.globally_distributed_database.models.PrevalidatePatchPayload.operation` attribute
        of this class is ``PATCH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this PrevalidatePatchPayload.
            Allowed values for this property are: "CREATE", "PATCH"
        :type operation: str

        :param prevalidate_payload:
            The value to assign to the prevalidate_payload property of this PrevalidatePatchPayload.
        :type prevalidate_payload: oci.globally_distributed_database.models.PatchShardedDatabaseDetails

        :param sharded_database_id:
            The value to assign to the sharded_database_id property of this PrevalidatePatchPayload.
        :type sharded_database_id: str

        """
        self.swagger_types = {
            'operation': 'str',
            'prevalidate_payload': 'PatchShardedDatabaseDetails',
            'sharded_database_id': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'prevalidate_payload': 'prevalidatePayload',
            'sharded_database_id': 'shardedDatabaseId'
        }

        self._operation = None
        self._prevalidate_payload = None
        self._sharded_database_id = None
        self._operation = 'PATCH'

    @property
    def prevalidate_payload(self):
        """
        **[Required]** Gets the prevalidate_payload of this PrevalidatePatchPayload.

        :return: The prevalidate_payload of this PrevalidatePatchPayload.
        :rtype: oci.globally_distributed_database.models.PatchShardedDatabaseDetails
        """
        return self._prevalidate_payload

    @prevalidate_payload.setter
    def prevalidate_payload(self, prevalidate_payload):
        """
        Sets the prevalidate_payload of this PrevalidatePatchPayload.

        :param prevalidate_payload: The prevalidate_payload of this PrevalidatePatchPayload.
        :type: oci.globally_distributed_database.models.PatchShardedDatabaseDetails
        """
        self._prevalidate_payload = prevalidate_payload

    @property
    def sharded_database_id(self):
        """
        **[Required]** Gets the sharded_database_id of this PrevalidatePatchPayload.
        Sharded database identifier


        :return: The sharded_database_id of this PrevalidatePatchPayload.
        :rtype: str
        """
        return self._sharded_database_id

    @sharded_database_id.setter
    def sharded_database_id(self, sharded_database_id):
        """
        Sets the sharded_database_id of this PrevalidatePatchPayload.
        Sharded database identifier


        :param sharded_database_id: The sharded_database_id of this PrevalidatePatchPayload.
        :type: str
        """
        self._sharded_database_id = sharded_database_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
