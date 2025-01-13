# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AdhocQueryDetails(object):
    """
    Detailed information about the adhoc query.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AdhocQueryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param query:
            The value to assign to the query property of this AdhocQueryDetails.
        :type query: str

        :param adhoc_query_resources:
            The value to assign to the adhoc_query_resources property of this AdhocQueryDetails.
        :type adhoc_query_resources: list[oci.cloud_guard.models.AdhocQueryResource]

        """
        self.swagger_types = {
            'query': 'str',
            'adhoc_query_resources': 'list[AdhocQueryResource]'
        }

        self.attribute_map = {
            'query': 'query',
            'adhoc_query_resources': 'adhocQueryResources'
        }

        self._query = None
        self._adhoc_query_resources = None

    @property
    def query(self):
        """
        **[Required]** Gets the query of this AdhocQueryDetails.
        The adhoc query expression that is run


        :return: The query of this AdhocQueryDetails.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this AdhocQueryDetails.
        The adhoc query expression that is run


        :param query: The query of this AdhocQueryDetails.
        :type: str
        """
        self._query = query

    @property
    def adhoc_query_resources(self):
        """
        **[Required]** Gets the adhoc_query_resources of this AdhocQueryDetails.
        Target information in which adhoc query will be run


        :return: The adhoc_query_resources of this AdhocQueryDetails.
        :rtype: list[oci.cloud_guard.models.AdhocQueryResource]
        """
        return self._adhoc_query_resources

    @adhoc_query_resources.setter
    def adhoc_query_resources(self, adhoc_query_resources):
        """
        Sets the adhoc_query_resources of this AdhocQueryDetails.
        Target information in which adhoc query will be run


        :param adhoc_query_resources: The adhoc_query_resources of this AdhocQueryDetails.
        :type: list[oci.cloud_guard.models.AdhocQueryResource]
        """
        self._adhoc_query_resources = adhoc_query_resources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
