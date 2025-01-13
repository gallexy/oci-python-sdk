# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Index(object):
    """
    OCI OpenSearch index details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Index object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Index.
        :type name: str

        :param schema:
            The value to assign to the schema property of this Index.
        :type schema: oci.generative_ai_agent.models.IndexSchema

        """
        self.swagger_types = {
            'name': 'str',
            'schema': 'IndexSchema'
        }

        self.attribute_map = {
            'name': 'name',
            'schema': 'schema'
        }

        self._name = None
        self._schema = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Index.
        The index name in opensearch.


        :return: The name of this Index.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Index.
        The index name in opensearch.


        :param name: The name of this Index.
        :type: str
        """
        self._name = name

    @property
    def schema(self):
        """
        **[Required]** Gets the schema of this Index.

        :return: The schema of this Index.
        :rtype: oci.generative_ai_agent.models.IndexSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this Index.

        :param schema: The schema of this Index.
        :type: oci.generative_ai_agent.models.IndexSchema
        """
        self._schema = schema

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
