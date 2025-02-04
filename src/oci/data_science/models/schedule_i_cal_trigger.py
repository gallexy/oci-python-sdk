# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .schedule_trigger import ScheduleTrigger
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleICalTrigger(ScheduleTrigger):
    """
    The iCal schedule trigger.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleICalTrigger object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.ScheduleICalTrigger.trigger_type` attribute
        of this class is ``ICAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param trigger_type:
            The value to assign to the trigger_type property of this ScheduleICalTrigger.
            Allowed values for this property are: "CRON", "INTERVAL", "ICAL"
        :type trigger_type: str

        :param time_start:
            The value to assign to the time_start property of this ScheduleICalTrigger.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this ScheduleICalTrigger.
        :type time_end: datetime

        :param recurrence:
            The value to assign to the recurrence property of this ScheduleICalTrigger.
        :type recurrence: str

        """
        self.swagger_types = {
            'trigger_type': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'recurrence': 'str'
        }

        self.attribute_map = {
            'trigger_type': 'triggerType',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'recurrence': 'recurrence'
        }

        self._trigger_type = None
        self._time_start = None
        self._time_end = None
        self._recurrence = None
        self._trigger_type = 'ICAL'

    @property
    def recurrence(self):
        """
        **[Required]** Gets the recurrence of this ScheduleICalTrigger.
        This recurrence field conforms to RFC-5545 formatting


        :return: The recurrence of this ScheduleICalTrigger.
        :rtype: str
        """
        return self._recurrence

    @recurrence.setter
    def recurrence(self, recurrence):
        """
        Sets the recurrence of this ScheduleICalTrigger.
        This recurrence field conforms to RFC-5545 formatting


        :param recurrence: The recurrence of this ScheduleICalTrigger.
        :type: str
        """
        self._recurrence = recurrence

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
