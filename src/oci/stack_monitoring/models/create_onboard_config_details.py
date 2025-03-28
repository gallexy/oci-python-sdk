# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330

from .create_config_details import CreateConfigDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOnboardConfigDetails(CreateConfigDetails):
    """
    A configuration of the ONBOARD type, contains fields describing Onboarding customization: policies,
    dynamic groups, user groups.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOnboardConfigDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.stack_monitoring.models.CreateOnboardConfigDetails.config_type` attribute
        of this class is ``ONBOARD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateOnboardConfigDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOnboardConfigDetails.
        :type compartment_id: str

        :param config_type:
            The value to assign to the config_type property of this CreateOnboardConfigDetails.
        :type config_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOnboardConfigDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOnboardConfigDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param version:
            The value to assign to the version property of this CreateOnboardConfigDetails.
        :type version: str

        :param is_manually_onboarded:
            The value to assign to the is_manually_onboarded property of this CreateOnboardConfigDetails.
        :type is_manually_onboarded: bool

        :param policy_names:
            The value to assign to the policy_names property of this CreateOnboardConfigDetails.
        :type policy_names: list[str]

        :param dynamic_groups:
            The value to assign to the dynamic_groups property of this CreateOnboardConfigDetails.
        :type dynamic_groups: list[oci.stack_monitoring.models.DynamicGroupDetails]

        :param user_groups:
            The value to assign to the user_groups property of this CreateOnboardConfigDetails.
        :type user_groups: list[oci.stack_monitoring.models.GroupDetails]

        :param additional_configurations:
            The value to assign to the additional_configurations property of this CreateOnboardConfigDetails.
        :type additional_configurations: oci.stack_monitoring.models.AdditionalConfigurationDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'config_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'version': 'str',
            'is_manually_onboarded': 'bool',
            'policy_names': 'list[str]',
            'dynamic_groups': 'list[DynamicGroupDetails]',
            'user_groups': 'list[GroupDetails]',
            'additional_configurations': 'AdditionalConfigurationDetails'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'config_type': 'configType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'version': 'version',
            'is_manually_onboarded': 'isManuallyOnboarded',
            'policy_names': 'policyNames',
            'dynamic_groups': 'dynamicGroups',
            'user_groups': 'userGroups',
            'additional_configurations': 'additionalConfigurations'
        }
        self._display_name = None
        self._compartment_id = None
        self._config_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._version = None
        self._is_manually_onboarded = None
        self._policy_names = None
        self._dynamic_groups = None
        self._user_groups = None
        self._additional_configurations = None
        self._config_type = 'ONBOARD'

    @property
    def version(self):
        """
        Gets the version of this CreateOnboardConfigDetails.
        Assigned version to given onboard configuration.


        :return: The version of this CreateOnboardConfigDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CreateOnboardConfigDetails.
        Assigned version to given onboard configuration.


        :param version: The version of this CreateOnboardConfigDetails.
        :type: str
        """
        self._version = version

    @property
    def is_manually_onboarded(self):
        """
        **[Required]** Gets the is_manually_onboarded of this CreateOnboardConfigDetails.
        True if customer decides marks configuration as manually configured.


        :return: The is_manually_onboarded of this CreateOnboardConfigDetails.
        :rtype: bool
        """
        return self._is_manually_onboarded

    @is_manually_onboarded.setter
    def is_manually_onboarded(self, is_manually_onboarded):
        """
        Sets the is_manually_onboarded of this CreateOnboardConfigDetails.
        True if customer decides marks configuration as manually configured.


        :param is_manually_onboarded: The is_manually_onboarded of this CreateOnboardConfigDetails.
        :type: bool
        """
        self._is_manually_onboarded = is_manually_onboarded

    @property
    def policy_names(self):
        """
        Gets the policy_names of this CreateOnboardConfigDetails.
        List of policy names assigned for onboarding


        :return: The policy_names of this CreateOnboardConfigDetails.
        :rtype: list[str]
        """
        return self._policy_names

    @policy_names.setter
    def policy_names(self, policy_names):
        """
        Sets the policy_names of this CreateOnboardConfigDetails.
        List of policy names assigned for onboarding


        :param policy_names: The policy_names of this CreateOnboardConfigDetails.
        :type: list[str]
        """
        self._policy_names = policy_names

    @property
    def dynamic_groups(self):
        """
        Gets the dynamic_groups of this CreateOnboardConfigDetails.
        List of dynamic groups dedicated for Stack Monitoring.


        :return: The dynamic_groups of this CreateOnboardConfigDetails.
        :rtype: list[oci.stack_monitoring.models.DynamicGroupDetails]
        """
        return self._dynamic_groups

    @dynamic_groups.setter
    def dynamic_groups(self, dynamic_groups):
        """
        Sets the dynamic_groups of this CreateOnboardConfigDetails.
        List of dynamic groups dedicated for Stack Monitoring.


        :param dynamic_groups: The dynamic_groups of this CreateOnboardConfigDetails.
        :type: list[oci.stack_monitoring.models.DynamicGroupDetails]
        """
        self._dynamic_groups = dynamic_groups

    @property
    def user_groups(self):
        """
        Gets the user_groups of this CreateOnboardConfigDetails.
        List of user groups dedicated for Stack Monitoring.


        :return: The user_groups of this CreateOnboardConfigDetails.
        :rtype: list[oci.stack_monitoring.models.GroupDetails]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """
        Sets the user_groups of this CreateOnboardConfigDetails.
        List of user groups dedicated for Stack Monitoring.


        :param user_groups: The user_groups of this CreateOnboardConfigDetails.
        :type: list[oci.stack_monitoring.models.GroupDetails]
        """
        self._user_groups = user_groups

    @property
    def additional_configurations(self):
        """
        Gets the additional_configurations of this CreateOnboardConfigDetails.

        :return: The additional_configurations of this CreateOnboardConfigDetails.
        :rtype: oci.stack_monitoring.models.AdditionalConfigurationDetails
        """
        return self._additional_configurations

    @additional_configurations.setter
    def additional_configurations(self, additional_configurations):
        """
        Sets the additional_configurations of this CreateOnboardConfigDetails.

        :param additional_configurations: The additional_configurations of this CreateOnboardConfigDetails.
        :type: oci.stack_monitoring.models.AdditionalConfigurationDetails
        """
        self._additional_configurations = additional_configurations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
