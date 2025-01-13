# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EndpointResponse(object):
    """
    An object containing details of a REST response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EndpointResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content_type:
            The value to assign to the content_type property of this EndpointResponse.
        :type content_type: str

        :param example:
            The value to assign to the example property of this EndpointResponse.
        :type example: str

        """
        self.swagger_types = {
            'content_type': 'str',
            'example': 'str'
        }

        self.attribute_map = {
            'content_type': 'contentType',
            'example': 'example'
        }

        self._content_type = None
        self._example = None

    @property
    def content_type(self):
        """
        Gets the content_type of this EndpointResponse.
        The response content type.


        :return: The content_type of this EndpointResponse.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this EndpointResponse.
        The response content type.


        :param content_type: The content_type of this EndpointResponse.
        :type: str
        """
        self._content_type = content_type

    @property
    def example(self):
        """
        Gets the example of this EndpointResponse.
        A sample response.


        :return: The example of this EndpointResponse.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        """
        Sets the example of this EndpointResponse.
        A sample response.


        :param example: The example of this EndpointResponse.
        :type: str
        """
        self._example = example

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
