# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_frequency_details import AbstractFrequencyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HourlyFrequencyDetails(AbstractFrequencyDetails):
    """
    Frequency details model to set hourly frequency
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HourlyFrequencyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.HourlyFrequencyDetails.model_type` attribute
        of this class is ``HOURLY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this HourlyFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY"
        :type model_type: str

        :param frequency:
            The value to assign to the frequency property of this HourlyFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY"
        :type frequency: str

        :param interval:
            The value to assign to the interval property of this HourlyFrequencyDetails.
        :type interval: int

        :param time:
            The value to assign to the time property of this HourlyFrequencyDetails.
        :type time: oci.data_integration.models.Time

        """
        self.swagger_types = {
            'model_type': 'str',
            'frequency': 'str',
            'interval': 'int',
            'time': 'Time'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'frequency': 'frequency',
            'interval': 'interval',
            'time': 'time'
        }

        self._model_type = None
        self._frequency = None
        self._interval = None
        self._time = None
        self._model_type = 'HOURLY'

    @property
    def interval(self):
        """
        Gets the interval of this HourlyFrequencyDetails.
        This hold the repeatability aspect of a schedule. i.e. in a monhtly frequency, a task can be scheduled for every month, once in two months, once in tree months etc.


        :return: The interval of this HourlyFrequencyDetails.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this HourlyFrequencyDetails.
        This hold the repeatability aspect of a schedule. i.e. in a monhtly frequency, a task can be scheduled for every month, once in two months, once in tree months etc.


        :param interval: The interval of this HourlyFrequencyDetails.
        :type: int
        """
        self._interval = interval

    @property
    def time(self):
        """
        Gets the time of this HourlyFrequencyDetails.

        :return: The time of this HourlyFrequencyDetails.
        :rtype: oci.data_integration.models.Time
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this HourlyFrequencyDetails.

        :param time: The time of this HourlyFrequencyDetails.
        :type: oci.data_integration.models.Time
        """
        self._time = time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
