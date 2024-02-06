# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtRiskScores(object):
    """
    The risk score pertaining to the user.

    **Added In:** 18.1.6

    **SCIM++ Properties:**
    - caseExact: false
    - idcsCompositeKey: [value]
    - multiValued: true
    - mutability: readWrite
    - required: false
    - returned: request
    - type: complex
    - uniqueness: none
    """

    #: A constant which can be used with the risk_level property of a UserExtRiskScores.
    #: This constant has a value of "LOW"
    RISK_LEVEL_LOW = "LOW"

    #: A constant which can be used with the risk_level property of a UserExtRiskScores.
    #: This constant has a value of "MEDIUM"
    RISK_LEVEL_MEDIUM = "MEDIUM"

    #: A constant which can be used with the risk_level property of a UserExtRiskScores.
    #: This constant has a value of "HIGH"
    RISK_LEVEL_HIGH = "HIGH"

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtRiskScores object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UserExtRiskScores.
        :type value: str

        :param ref:
            The value to assign to the ref property of this UserExtRiskScores.
        :type ref: str

        :param source:
            The value to assign to the source property of this UserExtRiskScores.
        :type source: str

        :param status:
            The value to assign to the status property of this UserExtRiskScores.
        :type status: str

        :param score:
            The value to assign to the score property of this UserExtRiskScores.
        :type score: int

        :param risk_level:
            The value to assign to the risk_level property of this UserExtRiskScores.
            Allowed values for this property are: "LOW", "MEDIUM", "HIGH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type risk_level: str

        :param last_update_timestamp:
            The value to assign to the last_update_timestamp property of this UserExtRiskScores.
        :type last_update_timestamp: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'source': 'str',
            'status': 'str',
            'score': 'int',
            'risk_level': 'str',
            'last_update_timestamp': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'source': 'source',
            'status': 'status',
            'score': 'score',
            'risk_level': 'riskLevel',
            'last_update_timestamp': 'lastUpdateTimestamp'
        }

        self._value = None
        self._ref = None
        self._source = None
        self._status = None
        self._score = None
        self._risk_level = None
        self._last_update_timestamp = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this UserExtRiskScores.
        Risk Provider Profile: Identifier for the provider service from which the risk score was received.

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this UserExtRiskScores.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserExtRiskScores.
        Risk Provider Profile: Identifier for the provider service from which the risk score was received.

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this UserExtRiskScores.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this UserExtRiskScores.
        Risk Provider Profile URI: URI that corresponds to risk source identifier.

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: reference
         - uniqueness: none


        :return: The ref of this UserExtRiskScores.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this UserExtRiskScores.
        Risk Provider Profile URI: URI that corresponds to risk source identifier.

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: reference
         - uniqueness: none


        :param ref: The ref of this UserExtRiskScores.
        :type: str
        """
        self._ref = ref

    @property
    def source(self):
        """
        Gets the source of this UserExtRiskScores.
        Risk Provider Profile Source

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The source of this UserExtRiskScores.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this UserExtRiskScores.
        Risk Provider Profile Source

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param source: The source of this UserExtRiskScores.
        :type: str
        """
        self._source = source

    @property
    def status(self):
        """
        Gets the status of this UserExtRiskScores.
        Risk Provider Profile status

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The status of this UserExtRiskScores.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UserExtRiskScores.
        Risk Provider Profile status

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param status: The status of this UserExtRiskScores.
        :type: str
        """
        self._status = status

    @property
    def score(self):
        """
        **[Required]** Gets the score of this UserExtRiskScores.
        Risk Score value

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: integer
         - uniqueness: none
         - idcsMaxValue: 100
         - idcsMinValue: 0


        :return: The score of this UserExtRiskScores.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this UserExtRiskScores.
        Risk Score value

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: integer
         - uniqueness: none
         - idcsMaxValue: 100
         - idcsMinValue: 0


        :param score: The score of this UserExtRiskScores.
        :type: int
        """
        self._score = score

    @property
    def risk_level(self):
        """
        **[Required]** Gets the risk_level of this UserExtRiskScores.
        Risk Level

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none

        Allowed values for this property are: "LOW", "MEDIUM", "HIGH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The risk_level of this UserExtRiskScores.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this UserExtRiskScores.
        Risk Level

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param risk_level: The risk_level of this UserExtRiskScores.
        :type: str
        """
        allowed_values = ["LOW", "MEDIUM", "HIGH"]
        if not value_allowed_none_or_none_sentinel(risk_level, allowed_values):
            risk_level = 'UNKNOWN_ENUM_VALUE'
        self._risk_level = risk_level

    @property
    def last_update_timestamp(self):
        """
        **[Required]** Gets the last_update_timestamp of this UserExtRiskScores.
        Last update timestamp for the risk score

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: dateTime
         - uniqueness: none


        :return: The last_update_timestamp of this UserExtRiskScores.
        :rtype: str
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """
        Sets the last_update_timestamp of this UserExtRiskScores.
        Last update timestamp for the risk score

        **Added In:** 18.1.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: dateTime
         - uniqueness: none


        :param last_update_timestamp: The last_update_timestamp of this UserExtRiskScores.
        :type: str
        """
        self._last_update_timestamp = last_update_timestamp

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other