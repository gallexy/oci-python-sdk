# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RealtimeMessageResultTranscriptionToken(object):
    """
    Individual transcription tokens.
    """

    #: A constant which can be used with the type property of a RealtimeMessageResultTranscriptionToken.
    #: This constant has a value of "WORD"
    TYPE_WORD = "WORD"

    #: A constant which can be used with the type property of a RealtimeMessageResultTranscriptionToken.
    #: This constant has a value of "PUNCTUATION"
    TYPE_PUNCTUATION = "PUNCTUATION"

    def __init__(self, **kwargs):
        """
        Initializes a new RealtimeMessageResultTranscriptionToken object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param token:
            The value to assign to the token property of this RealtimeMessageResultTranscriptionToken.
        :type token: str

        :param start_time_in_ms:
            The value to assign to the start_time_in_ms property of this RealtimeMessageResultTranscriptionToken.
        :type start_time_in_ms: int

        :param end_time_in_ms:
            The value to assign to the end_time_in_ms property of this RealtimeMessageResultTranscriptionToken.
        :type end_time_in_ms: int

        :param confidence:
            The value to assign to the confidence property of this RealtimeMessageResultTranscriptionToken.
        :type confidence: float

        :param type:
            The value to assign to the type property of this RealtimeMessageResultTranscriptionToken.
            Allowed values for this property are: "WORD", "PUNCTUATION"
        :type type: str

        """
        self.swagger_types = {
            'token': 'str',
            'start_time_in_ms': 'int',
            'end_time_in_ms': 'int',
            'confidence': 'float',
            'type': 'str'
        }
        self.attribute_map = {
            'token': 'token',
            'start_time_in_ms': 'startTimeInMs',
            'end_time_in_ms': 'endTimeInMs',
            'confidence': 'confidence',
            'type': 'type'
        }
        self._token = None
        self._start_time_in_ms = None
        self._end_time_in_ms = None
        self._confidence = None
        self._type = None

    @property
    def token(self):
        """
        **[Required]** Gets the token of this RealtimeMessageResultTranscriptionToken.
        Transcription token.


        :return: The token of this RealtimeMessageResultTranscriptionToken.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this RealtimeMessageResultTranscriptionToken.
        Transcription token.


        :param token: The token of this RealtimeMessageResultTranscriptionToken.
        :type: str
        """
        self._token = token

    @property
    def start_time_in_ms(self):
        """
        **[Required]** Gets the start_time_in_ms of this RealtimeMessageResultTranscriptionToken.
        Start time in milliseconds for the transcription token.


        :return: The start_time_in_ms of this RealtimeMessageResultTranscriptionToken.
        :rtype: int
        """
        return self._start_time_in_ms

    @start_time_in_ms.setter
    def start_time_in_ms(self, start_time_in_ms):
        """
        Sets the start_time_in_ms of this RealtimeMessageResultTranscriptionToken.
        Start time in milliseconds for the transcription token.


        :param start_time_in_ms: The start_time_in_ms of this RealtimeMessageResultTranscriptionToken.
        :type: int
        """
        self._start_time_in_ms = start_time_in_ms

    @property
    def end_time_in_ms(self):
        """
        **[Required]** Gets the end_time_in_ms of this RealtimeMessageResultTranscriptionToken.
        End time in milliseconds for the transcription token.


        :return: The end_time_in_ms of this RealtimeMessageResultTranscriptionToken.
        :rtype: int
        """
        return self._end_time_in_ms

    @end_time_in_ms.setter
    def end_time_in_ms(self, end_time_in_ms):
        """
        Sets the end_time_in_ms of this RealtimeMessageResultTranscriptionToken.
        End time in milliseconds for the transcription token.


        :param end_time_in_ms: The end_time_in_ms of this RealtimeMessageResultTranscriptionToken.
        :type: int
        """
        self._end_time_in_ms = end_time_in_ms

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this RealtimeMessageResultTranscriptionToken.
        Confidence score for the transcription token.


        :return: The confidence of this RealtimeMessageResultTranscriptionToken.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this RealtimeMessageResultTranscriptionToken.
        Confidence score for the transcription token.


        :param confidence: The confidence of this RealtimeMessageResultTranscriptionToken.
        :type: float
        """
        self._confidence = confidence

    @property
    def type(self):
        """
        **[Required]** Gets the type of this RealtimeMessageResultTranscriptionToken.
        Type of the transcription token.

        Allowed values for this property are: "WORD", "PUNCTUATION"


        :return: The type of this RealtimeMessageResultTranscriptionToken.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RealtimeMessageResultTranscriptionToken.
        Type of the transcription token.


        :param type: The type of this RealtimeMessageResultTranscriptionToken.
        :type: str
        """
        allowed_values = ["WORD", "PUNCTUATION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
