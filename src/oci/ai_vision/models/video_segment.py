# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VideoSegment(object):
    """
    A sequence of frames that was (or appears to be) continuously captured for a label/object/text?.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VideoSegment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param start_time_offset_ms:
            The value to assign to the start_time_offset_ms property of this VideoSegment.
        :type start_time_offset_ms: int

        :param end_time_offset_ms:
            The value to assign to the end_time_offset_ms property of this VideoSegment.
        :type end_time_offset_ms: int

        """
        self.swagger_types = {
            'start_time_offset_ms': 'int',
            'end_time_offset_ms': 'int'
        }

        self.attribute_map = {
            'start_time_offset_ms': 'startTimeOffsetMs',
            'end_time_offset_ms': 'endTimeOffsetMs'
        }

        self._start_time_offset_ms = None
        self._end_time_offset_ms = None

    @property
    def start_time_offset_ms(self):
        """
        **[Required]** Gets the start_time_offset_ms of this VideoSegment.
        Video start time offset(Milliseconds).


        :return: The start_time_offset_ms of this VideoSegment.
        :rtype: int
        """
        return self._start_time_offset_ms

    @start_time_offset_ms.setter
    def start_time_offset_ms(self, start_time_offset_ms):
        """
        Sets the start_time_offset_ms of this VideoSegment.
        Video start time offset(Milliseconds).


        :param start_time_offset_ms: The start_time_offset_ms of this VideoSegment.
        :type: int
        """
        self._start_time_offset_ms = start_time_offset_ms

    @property
    def end_time_offset_ms(self):
        """
        **[Required]** Gets the end_time_offset_ms of this VideoSegment.
        Video end time offset(Milliseconds).


        :return: The end_time_offset_ms of this VideoSegment.
        :rtype: int
        """
        return self._end_time_offset_ms

    @end_time_offset_ms.setter
    def end_time_offset_ms(self, end_time_offset_ms):
        """
        Sets the end_time_offset_ms of this VideoSegment.
        Video end time offset(Milliseconds).


        :param end_time_offset_ms: The end_time_offset_ms of this VideoSegment.
        :type: int
        """
        self._end_time_offset_ms = end_time_offset_ms

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
