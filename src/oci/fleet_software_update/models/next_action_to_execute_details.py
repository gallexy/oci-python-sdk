# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NextActionToExecuteDetails(object):
    """
    Details of the next Exadata Fleet Update Action to execute in a Maintenance Cycle.
    """

    #: A constant which can be used with the type property of a NextActionToExecuteDetails.
    #: This constant has a value of "STAGE"
    TYPE_STAGE = "STAGE"

    #: A constant which can be used with the type property of a NextActionToExecuteDetails.
    #: This constant has a value of "PRECHECK_STAGE"
    TYPE_PRECHECK_STAGE = "PRECHECK_STAGE"

    #: A constant which can be used with the type property of a NextActionToExecuteDetails.
    #: This constant has a value of "PRECHECK_APPLY"
    TYPE_PRECHECK_APPLY = "PRECHECK_APPLY"

    #: A constant which can be used with the type property of a NextActionToExecuteDetails.
    #: This constant has a value of "APPLY"
    TYPE_APPLY = "APPLY"

    #: A constant which can be used with the type property of a NextActionToExecuteDetails.
    #: This constant has a value of "ROLLBACK_AND_REMOVE_TARGET"
    TYPE_ROLLBACK_AND_REMOVE_TARGET = "ROLLBACK_AND_REMOVE_TARGET"

    #: A constant which can be used with the type property of a NextActionToExecuteDetails.
    #: This constant has a value of "CLEANUP"
    TYPE_CLEANUP = "CLEANUP"

    #: A constant which can be used with the type property of a NextActionToExecuteDetails.
    #: This constant has a value of "ROLLBACK_MAINTENANCE_CYCLE"
    TYPE_ROLLBACK_MAINTENANCE_CYCLE = "ROLLBACK_MAINTENANCE_CYCLE"

    def __init__(self, **kwargs):
        """
        Initializes a new NextActionToExecuteDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this NextActionToExecuteDetails.
            Allowed values for this property are: "STAGE", "PRECHECK_STAGE", "PRECHECK_APPLY", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP", "ROLLBACK_MAINTENANCE_CYCLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param time_to_start:
            The value to assign to the time_to_start property of this NextActionToExecuteDetails.
        :type time_to_start: datetime

        """
        self.swagger_types = {
            'type': 'str',
            'time_to_start': 'datetime'
        }

        self.attribute_map = {
            'type': 'type',
            'time_to_start': 'timeToStart'
        }

        self._type = None
        self._time_to_start = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this NextActionToExecuteDetails.
        Type of Exadata Fleet Update Action

        Allowed values for this property are: "STAGE", "PRECHECK_STAGE", "PRECHECK_APPLY", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP", "ROLLBACK_MAINTENANCE_CYCLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this NextActionToExecuteDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this NextActionToExecuteDetails.
        Type of Exadata Fleet Update Action


        :param type: The type of this NextActionToExecuteDetails.
        :type: str
        """
        allowed_values = ["STAGE", "PRECHECK_STAGE", "PRECHECK_APPLY", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP", "ROLLBACK_MAINTENANCE_CYCLE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def time_to_start(self):
        """
        Gets the time_to_start of this NextActionToExecuteDetails.
        The date and time the Exadata Fleet Update Action is expected to start. Null if no Action has been scheduled.
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_to_start of this NextActionToExecuteDetails.
        :rtype: datetime
        """
        return self._time_to_start

    @time_to_start.setter
    def time_to_start(self, time_to_start):
        """
        Sets the time_to_start of this NextActionToExecuteDetails.
        The date and time the Exadata Fleet Update Action is expected to start. Null if no Action has been scheduled.
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_to_start: The time_to_start of this NextActionToExecuteDetails.
        :type: datetime
        """
        self._time_to_start = time_to_start

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
