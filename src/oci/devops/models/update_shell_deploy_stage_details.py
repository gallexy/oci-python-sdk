# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .update_deploy_stage_details import UpdateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateShellDeployStageDetails(UpdateDeployStageDetails):
    """
    Specifies the shell stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateShellDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.UpdateShellDeployStageDetails.deploy_stage_type` attribute
        of this class is ``SHELL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateShellDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateShellDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this UpdateShellDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this UpdateShellDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateShellDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateShellDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param container_config:
            The value to assign to the container_config property of this UpdateShellDeployStageDetails.
        :type container_config: oci.devops.models.ContainerConfig

        :param command_spec_deploy_artifact_id:
            The value to assign to the command_spec_deploy_artifact_id property of this UpdateShellDeployStageDetails.
        :type command_spec_deploy_artifact_id: str

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this UpdateShellDeployStageDetails.
        :type timeout_in_seconds: int

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'container_config': 'ContainerConfig',
            'command_spec_deploy_artifact_id': 'str',
            'timeout_in_seconds': 'int'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'container_config': 'containerConfig',
            'command_spec_deploy_artifact_id': 'commandSpecDeployArtifactId',
            'timeout_in_seconds': 'timeoutInSeconds'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._container_config = None
        self._command_spec_deploy_artifact_id = None
        self._timeout_in_seconds = None
        self._deploy_stage_type = 'SHELL'

    @property
    def container_config(self):
        """
        Gets the container_config of this UpdateShellDeployStageDetails.

        :return: The container_config of this UpdateShellDeployStageDetails.
        :rtype: oci.devops.models.ContainerConfig
        """
        return self._container_config

    @container_config.setter
    def container_config(self, container_config):
        """
        Sets the container_config of this UpdateShellDeployStageDetails.

        :param container_config: The container_config of this UpdateShellDeployStageDetails.
        :type: oci.devops.models.ContainerConfig
        """
        self._container_config = container_config

    @property
    def command_spec_deploy_artifact_id(self):
        """
        Gets the command_spec_deploy_artifact_id of this UpdateShellDeployStageDetails.
        The OCID of the artifact that contains the command specification.


        :return: The command_spec_deploy_artifact_id of this UpdateShellDeployStageDetails.
        :rtype: str
        """
        return self._command_spec_deploy_artifact_id

    @command_spec_deploy_artifact_id.setter
    def command_spec_deploy_artifact_id(self, command_spec_deploy_artifact_id):
        """
        Sets the command_spec_deploy_artifact_id of this UpdateShellDeployStageDetails.
        The OCID of the artifact that contains the command specification.


        :param command_spec_deploy_artifact_id: The command_spec_deploy_artifact_id of this UpdateShellDeployStageDetails.
        :type: str
        """
        self._command_spec_deploy_artifact_id = command_spec_deploy_artifact_id

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this UpdateShellDeployStageDetails.
        Time to wait for execution of a shell stage. Defaults to 36000 seconds.


        :return: The timeout_in_seconds of this UpdateShellDeployStageDetails.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this UpdateShellDeployStageDetails.
        Time to wait for execution of a shell stage. Defaults to 36000 seconds.


        :param timeout_in_seconds: The timeout_in_seconds of this UpdateShellDeployStageDetails.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other