# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrPlanGroupDetails(object):
    """
    The details for updating a group in a DR plan.
    """

    #: A constant which can be used with the type property of a UpdateDrPlanGroupDetails.
    #: This constant has a value of "USER_DEFINED"
    TYPE_USER_DEFINED = "USER_DEFINED"

    #: A constant which can be used with the type property of a UpdateDrPlanGroupDetails.
    #: This constant has a value of "BUILT_IN"
    TYPE_BUILT_IN = "BUILT_IN"

    #: A constant which can be used with the type property of a UpdateDrPlanGroupDetails.
    #: This constant has a value of "BUILT_IN_PRECHECK"
    TYPE_BUILT_IN_PRECHECK = "BUILT_IN_PRECHECK"

    #: A constant which can be used with the type property of a UpdateDrPlanGroupDetails.
    #: This constant has a value of "USER_DEFINED_PAUSE"
    TYPE_USER_DEFINED_PAUSE = "USER_DEFINED_PAUSE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrPlanGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this UpdateDrPlanGroupDetails.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this UpdateDrPlanGroupDetails.
        :type display_name: str

        :param type:
            The value to assign to the type property of this UpdateDrPlanGroupDetails.
            Allowed values for this property are: "USER_DEFINED", "BUILT_IN", "BUILT_IN_PRECHECK", "USER_DEFINED_PAUSE"
        :type type: str

        :param is_pause_enabled:
            The value to assign to the is_pause_enabled property of this UpdateDrPlanGroupDetails.
        :type is_pause_enabled: bool

        :param steps:
            The value to assign to the steps property of this UpdateDrPlanGroupDetails.
        :type steps: list[oci.disaster_recovery.models.UpdateDrPlanStepDetails]

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'type': 'str',
            'is_pause_enabled': 'bool',
            'steps': 'list[UpdateDrPlanStepDetails]'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'type': 'type',
            'is_pause_enabled': 'isPauseEnabled',
            'steps': 'steps'
        }
        self._id = None
        self._display_name = None
        self._type = None
        self._is_pause_enabled = None
        self._steps = None

    @property
    def id(self):
        """
        Gets the id of this UpdateDrPlanGroupDetails.
        The unique id of the group. Must not be modified by user.

        Example: `sgid1.group..uniqueID`


        :return: The id of this UpdateDrPlanGroupDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateDrPlanGroupDetails.
        The unique id of the group. Must not be modified by user.

        Example: `sgid1.group..uniqueID`


        :param id: The id of this UpdateDrPlanGroupDetails.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDrPlanGroupDetails.
        The display name of the group.

        Example: `My_GROUP_3 - EBS Start`


        :return: The display_name of this UpdateDrPlanGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDrPlanGroupDetails.
        The display name of the group.

        Example: `My_GROUP_3 - EBS Start`


        :param display_name: The display_name of this UpdateDrPlanGroupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        Gets the type of this UpdateDrPlanGroupDetails.
        The group type.

        Example: `BUILT_IN`

        Allowed values for this property are: "USER_DEFINED", "BUILT_IN", "BUILT_IN_PRECHECK", "USER_DEFINED_PAUSE"


        :return: The type of this UpdateDrPlanGroupDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateDrPlanGroupDetails.
        The group type.

        Example: `BUILT_IN`


        :param type: The type of this UpdateDrPlanGroupDetails.
        :type: str
        """
        allowed_values = ["USER_DEFINED", "BUILT_IN", "BUILT_IN_PRECHECK", "USER_DEFINED_PAUSE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    @property
    def is_pause_enabled(self):
        """
        Gets the is_pause_enabled of this UpdateDrPlanGroupDetails.
        A flag indicating whether this group should be enabled for execution.
        This flag is only applicable to the `USER_DEFINED_PAUSE` group. The flag should be null for the remaining group types.

        Example: `true`


        :return: The is_pause_enabled of this UpdateDrPlanGroupDetails.
        :rtype: bool
        """
        return self._is_pause_enabled

    @is_pause_enabled.setter
    def is_pause_enabled(self, is_pause_enabled):
        """
        Sets the is_pause_enabled of this UpdateDrPlanGroupDetails.
        A flag indicating whether this group should be enabled for execution.
        This flag is only applicable to the `USER_DEFINED_PAUSE` group. The flag should be null for the remaining group types.

        Example: `true`


        :param is_pause_enabled: The is_pause_enabled of this UpdateDrPlanGroupDetails.
        :type: bool
        """
        self._is_pause_enabled = is_pause_enabled

    @property
    def steps(self):
        """
        Gets the steps of this UpdateDrPlanGroupDetails.
        The list of steps in this group.


        :return: The steps of this UpdateDrPlanGroupDetails.
        :rtype: list[oci.disaster_recovery.models.UpdateDrPlanStepDetails]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """
        Sets the steps of this UpdateDrPlanGroupDetails.
        The list of steps in this group.


        :param steps: The steps of this UpdateDrPlanGroupDetails.
        :type: list[oci.disaster_recovery.models.UpdateDrPlanStepDetails]
        """
        self._steps = steps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
