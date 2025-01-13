# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221208


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CccScheduleEvent(object):
    """
    A period where upgrades may be applied to Compute Cloud@Customer infrastructures
    associated with the schedule. All upgrade windows may not be used.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CccScheduleEvent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CccScheduleEvent.
        :type name: str

        :param description:
            The value to assign to the description property of this CccScheduleEvent.
        :type description: str

        :param time_start:
            The value to assign to the time_start property of this CccScheduleEvent.
        :type time_start: datetime

        :param schedule_event_duration:
            The value to assign to the schedule_event_duration property of this CccScheduleEvent.
        :type schedule_event_duration: str

        :param schedule_event_recurrences:
            The value to assign to the schedule_event_recurrences property of this CccScheduleEvent.
        :type schedule_event_recurrences: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'time_start': 'datetime',
            'schedule_event_duration': 'str',
            'schedule_event_recurrences': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'time_start': 'timeStart',
            'schedule_event_duration': 'scheduleEventDuration',
            'schedule_event_recurrences': 'scheduleEventRecurrences'
        }

        self._name = None
        self._description = None
        self._time_start = None
        self._schedule_event_duration = None
        self._schedule_event_recurrences = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CccScheduleEvent.
        Generated name associated with the event.


        :return: The name of this CccScheduleEvent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CccScheduleEvent.
        Generated name associated with the event.


        :param name: The name of this CccScheduleEvent.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CccScheduleEvent.
        A description of the Compute Cloud@Customer upgrade schedule time block.


        :return: The description of this CccScheduleEvent.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CccScheduleEvent.
        A description of the Compute Cloud@Customer upgrade schedule time block.


        :param description: The description of this CccScheduleEvent.
        :type: str
        """
        self._description = description

    @property
    def time_start(self):
        """
        **[Required]** Gets the time_start of this CccScheduleEvent.
        The date and time when the Compute Cloud@Customer upgrade schedule event starts,
        inclusive. An RFC3339 formatted UTC datetime string. For an event with recurrences,
        this is the date that a recurrence can start being applied.


        :return: The time_start of this CccScheduleEvent.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this CccScheduleEvent.
        The date and time when the Compute Cloud@Customer upgrade schedule event starts,
        inclusive. An RFC3339 formatted UTC datetime string. For an event with recurrences,
        this is the date that a recurrence can start being applied.


        :param time_start: The time_start of this CccScheduleEvent.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def schedule_event_duration(self):
        """
        **[Required]** Gets the schedule_event_duration of this CccScheduleEvent.
        The duration of this block of time. The duration must be specified and be of the
        ISO-8601 format for durations.


        :return: The schedule_event_duration of this CccScheduleEvent.
        :rtype: str
        """
        return self._schedule_event_duration

    @schedule_event_duration.setter
    def schedule_event_duration(self, schedule_event_duration):
        """
        Sets the schedule_event_duration of this CccScheduleEvent.
        The duration of this block of time. The duration must be specified and be of the
        ISO-8601 format for durations.


        :param schedule_event_duration: The schedule_event_duration of this CccScheduleEvent.
        :type: str
        """
        self._schedule_event_duration = schedule_event_duration

    @property
    def schedule_event_recurrences(self):
        """
        Gets the schedule_event_recurrences of this CccScheduleEvent.
        Frequency of recurrence of schedule block. When this field is not included, the event
        is assumed to be a one time occurrence. The frequency field is strictly parsed and must
        conform to RFC-5545 formatting for recurrences.


        :return: The schedule_event_recurrences of this CccScheduleEvent.
        :rtype: str
        """
        return self._schedule_event_recurrences

    @schedule_event_recurrences.setter
    def schedule_event_recurrences(self, schedule_event_recurrences):
        """
        Sets the schedule_event_recurrences of this CccScheduleEvent.
        Frequency of recurrence of schedule block. When this field is not included, the event
        is assumed to be a one time occurrence. The frequency field is strictly parsed and must
        conform to RFC-5545 formatting for recurrences.


        :param schedule_event_recurrences: The schedule_event_recurrences of this CccScheduleEvent.
        :type: str
        """
        self._schedule_event_recurrences = schedule_event_recurrences

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
