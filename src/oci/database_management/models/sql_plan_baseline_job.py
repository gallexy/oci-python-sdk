# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlPlanBaselineJob(object):
    """
    The details of the database job used for loading and evolving SQL plan baselines.
    """

    #: A constant which can be used with the type property of a SqlPlanBaselineJob.
    #: This constant has a value of "LOAD"
    TYPE_LOAD = "LOAD"

    #: A constant which can be used with the status property of a SqlPlanBaselineJob.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a SqlPlanBaselineJob.
    #: This constant has a value of "SCHEDULED"
    STATUS_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the status property of a SqlPlanBaselineJob.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlPlanBaselineJob object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SqlPlanBaselineJob.
        :type name: str

        :param type:
            The value to assign to the type property of this SqlPlanBaselineJob.
            Allowed values for this property are: "LOAD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param status:
            The value to assign to the status property of this SqlPlanBaselineJob.
            Allowed values for this property are: "SUCCEEDED", "SCHEDULED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this SqlPlanBaselineJob.
        :type time_created: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'status': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'status': 'status',
            'time_created': 'timeCreated'
        }

        self._name = None
        self._type = None
        self._status = None
        self._time_created = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SqlPlanBaselineJob.
        The job name.


        :return: The name of this SqlPlanBaselineJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SqlPlanBaselineJob.
        The job name.


        :param name: The name of this SqlPlanBaselineJob.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this SqlPlanBaselineJob.
        The job type.

        Allowed values for this property are: "LOAD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this SqlPlanBaselineJob.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SqlPlanBaselineJob.
        The job type.


        :param type: The type of this SqlPlanBaselineJob.
        :type: str
        """
        allowed_values = ["LOAD"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this SqlPlanBaselineJob.
        The job status.

        Allowed values for this property are: "SUCCEEDED", "SCHEDULED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this SqlPlanBaselineJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SqlPlanBaselineJob.
        The job status.


        :param status: The status of this SqlPlanBaselineJob.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "SCHEDULED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_created(self):
        """
        Gets the time_created of this SqlPlanBaselineJob.
        The date and time the job was created.


        :return: The time_created of this SqlPlanBaselineJob.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SqlPlanBaselineJob.
        The date and time the job was created.


        :param time_created: The time_created of this SqlPlanBaselineJob.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
