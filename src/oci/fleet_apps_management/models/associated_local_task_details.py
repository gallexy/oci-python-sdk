# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .associated_task_details import AssociatedTaskDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociatedLocalTaskDetails(AssociatedTaskDetails):
    """
    The details of the local task.
    The local tasks are specific to a single runbook.
    """

    #: A constant which can be used with the os_type property of a AssociatedLocalTaskDetails.
    #: This constant has a value of "WINDOWS"
    OS_TYPE_WINDOWS = "WINDOWS"

    #: A constant which can be used with the os_type property of a AssociatedLocalTaskDetails.
    #: This constant has a value of "LINUX"
    OS_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the os_type property of a AssociatedLocalTaskDetails.
    #: This constant has a value of "GENERIC"
    OS_TYPE_GENERIC = "GENERIC"

    def __init__(self, **kwargs):
        """
        Initializes a new AssociatedLocalTaskDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.AssociatedLocalTaskDetails.scope` attribute
        of this class is ``LOCAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scope:
            The value to assign to the scope property of this AssociatedLocalTaskDetails.
            Allowed values for this property are: "LOCAL", "SHARED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scope: str

        :param execution_details:
            The value to assign to the execution_details property of this AssociatedLocalTaskDetails.
        :type execution_details: oci.fleet_apps_management.models.ExecutionDetails

        :param description:
            The value to assign to the description property of this AssociatedLocalTaskDetails.
        :type description: str

        :param platform:
            The value to assign to the platform property of this AssociatedLocalTaskDetails.
        :type platform: str

        :param is_copy_to_library_enabled:
            The value to assign to the is_copy_to_library_enabled property of this AssociatedLocalTaskDetails.
        :type is_copy_to_library_enabled: bool

        :param os_type:
            The value to assign to the os_type property of this AssociatedLocalTaskDetails.
            Allowed values for this property are: "WINDOWS", "LINUX", "GENERIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_type: str

        :param properties:
            The value to assign to the properties property of this AssociatedLocalTaskDetails.
        :type properties: oci.fleet_apps_management.models.Properties

        :param is_discovery_output_task:
            The value to assign to the is_discovery_output_task property of this AssociatedLocalTaskDetails.
        :type is_discovery_output_task: bool

        :param is_apply_subject_task:
            The value to assign to the is_apply_subject_task property of this AssociatedLocalTaskDetails.
        :type is_apply_subject_task: bool

        :param name:
            The value to assign to the name property of this AssociatedLocalTaskDetails.
        :type name: str

        """
        self.swagger_types = {
            'scope': 'str',
            'execution_details': 'ExecutionDetails',
            'description': 'str',
            'platform': 'str',
            'is_copy_to_library_enabled': 'bool',
            'os_type': 'str',
            'properties': 'Properties',
            'is_discovery_output_task': 'bool',
            'is_apply_subject_task': 'bool',
            'name': 'str'
        }

        self.attribute_map = {
            'scope': 'scope',
            'execution_details': 'executionDetails',
            'description': 'description',
            'platform': 'platform',
            'is_copy_to_library_enabled': 'isCopyToLibraryEnabled',
            'os_type': 'osType',
            'properties': 'properties',
            'is_discovery_output_task': 'isDiscoveryOutputTask',
            'is_apply_subject_task': 'isApplySubjectTask',
            'name': 'name'
        }

        self._scope = None
        self._execution_details = None
        self._description = None
        self._platform = None
        self._is_copy_to_library_enabled = None
        self._os_type = None
        self._properties = None
        self._is_discovery_output_task = None
        self._is_apply_subject_task = None
        self._name = None
        self._scope = 'LOCAL'

    @property
    def execution_details(self):
        """
        **[Required]** Gets the execution_details of this AssociatedLocalTaskDetails.

        :return: The execution_details of this AssociatedLocalTaskDetails.
        :rtype: oci.fleet_apps_management.models.ExecutionDetails
        """
        return self._execution_details

    @execution_details.setter
    def execution_details(self, execution_details):
        """
        Sets the execution_details of this AssociatedLocalTaskDetails.

        :param execution_details: The execution_details of this AssociatedLocalTaskDetails.
        :type: oci.fleet_apps_management.models.ExecutionDetails
        """
        self._execution_details = execution_details

    @property
    def description(self):
        """
        Gets the description of this AssociatedLocalTaskDetails.
        The description of the task.


        :return: The description of this AssociatedLocalTaskDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AssociatedLocalTaskDetails.
        The description of the task.


        :param description: The description of this AssociatedLocalTaskDetails.
        :type: str
        """
        self._description = description

    @property
    def platform(self):
        """
        Gets the platform of this AssociatedLocalTaskDetails.
        The platform of the runbook.


        :return: The platform of this AssociatedLocalTaskDetails.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this AssociatedLocalTaskDetails.
        The platform of the runbook.


        :param platform: The platform of this AssociatedLocalTaskDetails.
        :type: str
        """
        self._platform = platform

    @property
    def is_copy_to_library_enabled(self):
        """
        Gets the is_copy_to_library_enabled of this AssociatedLocalTaskDetails.
        Make a copy of this task in Library


        :return: The is_copy_to_library_enabled of this AssociatedLocalTaskDetails.
        :rtype: bool
        """
        return self._is_copy_to_library_enabled

    @is_copy_to_library_enabled.setter
    def is_copy_to_library_enabled(self, is_copy_to_library_enabled):
        """
        Sets the is_copy_to_library_enabled of this AssociatedLocalTaskDetails.
        Make a copy of this task in Library


        :param is_copy_to_library_enabled: The is_copy_to_library_enabled of this AssociatedLocalTaskDetails.
        :type: bool
        """
        self._is_copy_to_library_enabled = is_copy_to_library_enabled

    @property
    def os_type(self):
        """
        **[Required]** Gets the os_type of this AssociatedLocalTaskDetails.
        The OS for the task.

        Allowed values for this property are: "WINDOWS", "LINUX", "GENERIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_type of this AssociatedLocalTaskDetails.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """
        Sets the os_type of this AssociatedLocalTaskDetails.
        The OS for the task.


        :param os_type: The os_type of this AssociatedLocalTaskDetails.
        :type: str
        """
        allowed_values = ["WINDOWS", "LINUX", "GENERIC"]
        if not value_allowed_none_or_none_sentinel(os_type, allowed_values):
            os_type = 'UNKNOWN_ENUM_VALUE'
        self._os_type = os_type

    @property
    def properties(self):
        """
        Gets the properties of this AssociatedLocalTaskDetails.

        :return: The properties of this AssociatedLocalTaskDetails.
        :rtype: oci.fleet_apps_management.models.Properties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this AssociatedLocalTaskDetails.

        :param properties: The properties of this AssociatedLocalTaskDetails.
        :type: oci.fleet_apps_management.models.Properties
        """
        self._properties = properties

    @property
    def is_discovery_output_task(self):
        """
        Gets the is_discovery_output_task of this AssociatedLocalTaskDetails.
        Is this a discovery output task?


        :return: The is_discovery_output_task of this AssociatedLocalTaskDetails.
        :rtype: bool
        """
        return self._is_discovery_output_task

    @is_discovery_output_task.setter
    def is_discovery_output_task(self, is_discovery_output_task):
        """
        Sets the is_discovery_output_task of this AssociatedLocalTaskDetails.
        Is this a discovery output task?


        :param is_discovery_output_task: The is_discovery_output_task of this AssociatedLocalTaskDetails.
        :type: bool
        """
        self._is_discovery_output_task = is_discovery_output_task

    @property
    def is_apply_subject_task(self):
        """
        Gets the is_apply_subject_task of this AssociatedLocalTaskDetails.
        Is this an Apply Subject Task? Ex. Patch Execution Task


        :return: The is_apply_subject_task of this AssociatedLocalTaskDetails.
        :rtype: bool
        """
        return self._is_apply_subject_task

    @is_apply_subject_task.setter
    def is_apply_subject_task(self, is_apply_subject_task):
        """
        Sets the is_apply_subject_task of this AssociatedLocalTaskDetails.
        Is this an Apply Subject Task? Ex. Patch Execution Task


        :param is_apply_subject_task: The is_apply_subject_task of this AssociatedLocalTaskDetails.
        :type: bool
        """
        self._is_apply_subject_task = is_apply_subject_task

    @property
    def name(self):
        """
        Gets the name of this AssociatedLocalTaskDetails.
        The name of the task


        :return: The name of this AssociatedLocalTaskDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AssociatedLocalTaskDetails.
        The name of the task


        :param name: The name of this AssociatedLocalTaskDetails.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
