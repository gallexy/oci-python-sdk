# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .create_deploy_environment_details import CreateDeployEnvironmentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFunctionDeployEnvironmentDetails(CreateDeployEnvironmentDetails):
    """
    Specifies the Function environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFunctionDeployEnvironmentDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateFunctionDeployEnvironmentDetails.deploy_environment_type` attribute
        of this class is ``FUNCTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateFunctionDeployEnvironmentDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateFunctionDeployEnvironmentDetails.
        :type display_name: str

        :param deploy_environment_type:
            The value to assign to the deploy_environment_type property of this CreateFunctionDeployEnvironmentDetails.
        :type deploy_environment_type: str

        :param project_id:
            The value to assign to the project_id property of this CreateFunctionDeployEnvironmentDetails.
        :type project_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateFunctionDeployEnvironmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateFunctionDeployEnvironmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param function_id:
            The value to assign to the function_id property of this CreateFunctionDeployEnvironmentDetails.
        :type function_id: str

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_environment_type': 'str',
            'project_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'function_id': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_environment_type': 'deployEnvironmentType',
            'project_id': 'projectId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'function_id': 'functionId'
        }

        self._description = None
        self._display_name = None
        self._deploy_environment_type = None
        self._project_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._function_id = None
        self._deploy_environment_type = 'FUNCTION'

    @property
    def function_id(self):
        """
        **[Required]** Gets the function_id of this CreateFunctionDeployEnvironmentDetails.
        The OCID of the Function.


        :return: The function_id of this CreateFunctionDeployEnvironmentDetails.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this CreateFunctionDeployEnvironmentDetails.
        The OCID of the Function.


        :param function_id: The function_id of this CreateFunctionDeployEnvironmentDetails.
        :type: str
        """
        self._function_id = function_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
