# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudGateMappingUpstreamServerGroup(object):
    """
    Reference to upstream block for this mapping

    **Added In:** 20.1.3

    **SCIM++ Properties:**
    - caseExact: false
    - multiValued: false
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloudGateMappingUpstreamServerGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this CloudGateMappingUpstreamServerGroup.
        :type value: str

        :param ref:
            The value to assign to the ref property of this CloudGateMappingUpstreamServerGroup.
        :type ref: str

        :param ssl:
            The value to assign to the ssl property of this CloudGateMappingUpstreamServerGroup.
        :type ssl: bool

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'ssl': 'bool'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'ssl': 'ssl'
        }

        self._value = None
        self._ref = None
        self._ssl = None

    @property
    def value(self):
        """
        Gets the value of this CloudGateMappingUpstreamServerGroup.
        The id of the upstream block entry.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this CloudGateMappingUpstreamServerGroup.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CloudGateMappingUpstreamServerGroup.
        The id of the upstream block entry.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this CloudGateMappingUpstreamServerGroup.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this CloudGateMappingUpstreamServerGroup.
        The URI to the upstream block entry

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this CloudGateMappingUpstreamServerGroup.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this CloudGateMappingUpstreamServerGroup.
        The URI to the upstream block entry

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this CloudGateMappingUpstreamServerGroup.
        :type: str
        """
        self._ref = ref

    @property
    def ssl(self):
        """
        Gets the ssl of this CloudGateMappingUpstreamServerGroup.
        SSL flag for the Upstream Block

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The ssl of this CloudGateMappingUpstreamServerGroup.
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """
        Sets the ssl of this CloudGateMappingUpstreamServerGroup.
        SSL flag for the Upstream Block

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param ssl: The ssl of this CloudGateMappingUpstreamServerGroup.
        :type: bool
        """
        self._ssl = ssl

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
