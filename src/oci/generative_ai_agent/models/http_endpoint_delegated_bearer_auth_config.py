# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531

from .http_endpoint_auth_config import HttpEndpointAuthConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HttpEndpointDelegatedBearerAuthConfig(HttpEndpointAuthConfig):
    """
    Specifies Bearer Token Authentication, where the same Bearer token received as part of the Agent Chat API request is used to invoke
    the external endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HttpEndpointDelegatedBearerAuthConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_agent.models.HttpEndpointDelegatedBearerAuthConfig.http_endpoint_auth_config_type` attribute
        of this class is ``HTTP_ENDPOINT_DELEGATED_BEARER_AUTH_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param http_endpoint_auth_config_type:
            The value to assign to the http_endpoint_auth_config_type property of this HttpEndpointDelegatedBearerAuthConfig.
            Allowed values for this property are: "HTTP_ENDPOINT_NO_AUTH_CONFIG", "HTTP_ENDPOINT_DELEGATED_BEARER_AUTH_CONFIG", "HTTP_ENDPOINT_OCI_RESOURCE_PRINCIPAL_AUTH_CONFIG", "HTTP_ENDPOINT_IDCS_AUTH_CONFIG"
        :type http_endpoint_auth_config_type: str

        """
        self.swagger_types = {
            'http_endpoint_auth_config_type': 'str'
        }
        self.attribute_map = {
            'http_endpoint_auth_config_type': 'httpEndpointAuthConfigType'
        }
        self._http_endpoint_auth_config_type = None
        self._http_endpoint_auth_config_type = 'HTTP_ENDPOINT_DELEGATED_BEARER_AUTH_CONFIG'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
