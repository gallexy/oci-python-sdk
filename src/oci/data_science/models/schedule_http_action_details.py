# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleHttpActionDetails(object):
    """
    Schedule Http action details
    """

    #: A constant which can be used with the http_action_type property of a ScheduleHttpActionDetails.
    #: This constant has a value of "CREATE_JOB_RUN"
    HTTP_ACTION_TYPE_CREATE_JOB_RUN = "CREATE_JOB_RUN"

    #: A constant which can be used with the http_action_type property of a ScheduleHttpActionDetails.
    #: This constant has a value of "CREATE_PIPELINE_RUN"
    HTTP_ACTION_TYPE_CREATE_PIPELINE_RUN = "CREATE_PIPELINE_RUN"

    #: A constant which can be used with the http_action_type property of a ScheduleHttpActionDetails.
    #: This constant has a value of "INVOKE_ML_APPLICATION_PROVIDER_TRIGGER"
    HTTP_ACTION_TYPE_INVOKE_ML_APPLICATION_PROVIDER_TRIGGER = "INVOKE_ML_APPLICATION_PROVIDER_TRIGGER"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleHttpActionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_science.models.CreateJobRunScheduleActionDetails`
        * :class:`~oci.data_science.models.InvokeMlApplicationProviderTriggerScheduleActionDetails`
        * :class:`~oci.data_science.models.CreatePipelineRunScheduleActionDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param http_action_type:
            The value to assign to the http_action_type property of this ScheduleHttpActionDetails.
            Allowed values for this property are: "CREATE_JOB_RUN", "CREATE_PIPELINE_RUN", "INVOKE_ML_APPLICATION_PROVIDER_TRIGGER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type http_action_type: str

        """
        self.swagger_types = {
            'http_action_type': 'str'
        }

        self.attribute_map = {
            'http_action_type': 'httpActionType'
        }

        self._http_action_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['httpActionType']

        if type == 'CREATE_JOB_RUN':
            return 'CreateJobRunScheduleActionDetails'

        if type == 'INVOKE_ML_APPLICATION_PROVIDER_TRIGGER':
            return 'InvokeMlApplicationProviderTriggerScheduleActionDetails'

        if type == 'CREATE_PIPELINE_RUN':
            return 'CreatePipelineRunScheduleActionDetails'
        else:
            return 'ScheduleHttpActionDetails'

    @property
    def http_action_type(self):
        """
        **[Required]** Gets the http_action_type of this ScheduleHttpActionDetails.
        The type of http action to trigger.

        Allowed values for this property are: "CREATE_JOB_RUN", "CREATE_PIPELINE_RUN", "INVOKE_ML_APPLICATION_PROVIDER_TRIGGER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The http_action_type of this ScheduleHttpActionDetails.
        :rtype: str
        """
        return self._http_action_type

    @http_action_type.setter
    def http_action_type(self, http_action_type):
        """
        Sets the http_action_type of this ScheduleHttpActionDetails.
        The type of http action to trigger.


        :param http_action_type: The http_action_type of this ScheduleHttpActionDetails.
        :type: str
        """
        allowed_values = ["CREATE_JOB_RUN", "CREATE_PIPELINE_RUN", "INVOKE_ML_APPLICATION_PROVIDER_TRIGGER"]
        if not value_allowed_none_or_none_sentinel(http_action_type, allowed_values):
            http_action_type = 'UNKNOWN_ENUM_VALUE'
        self._http_action_type = http_action_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
