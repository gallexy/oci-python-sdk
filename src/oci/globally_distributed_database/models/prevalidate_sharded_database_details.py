# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230301


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrevalidateShardedDatabaseDetails(object):
    """
    Input for prevalidate sharded database API to validate various operations payload.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrevalidateShardedDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param prevalidate_sharded_database_details:
            The value to assign to the prevalidate_sharded_database_details property of this PrevalidateShardedDatabaseDetails.
        :type prevalidate_sharded_database_details: oci.globally_distributed_database.models.PrevalidatePayload

        """
        self.swagger_types = {
            'prevalidate_sharded_database_details': 'PrevalidatePayload'
        }

        self.attribute_map = {
            'prevalidate_sharded_database_details': 'prevalidateShardedDatabaseDetails'
        }

        self._prevalidate_sharded_database_details = None

    @property
    def prevalidate_sharded_database_details(self):
        """
        **[Required]** Gets the prevalidate_sharded_database_details of this PrevalidateShardedDatabaseDetails.

        :return: The prevalidate_sharded_database_details of this PrevalidateShardedDatabaseDetails.
        :rtype: oci.globally_distributed_database.models.PrevalidatePayload
        """
        return self._prevalidate_sharded_database_details

    @prevalidate_sharded_database_details.setter
    def prevalidate_sharded_database_details(self, prevalidate_sharded_database_details):
        """
        Sets the prevalidate_sharded_database_details of this PrevalidateShardedDatabaseDetails.

        :param prevalidate_sharded_database_details: The prevalidate_sharded_database_details of this PrevalidateShardedDatabaseDetails.
        :type: oci.globally_distributed_database.models.PrevalidatePayload
        """
        self._prevalidate_sharded_database_details = prevalidate_sharded_database_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
