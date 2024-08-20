# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFleetDetails(object):
    """
    The information about new Fleet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFleetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateFleetDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateFleetDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateFleetDetails.
        :type compartment_id: str

        :param fleet_type:
            The value to assign to the fleet_type property of this CreateFleetDetails.
        :type fleet_type: str

        :param products:
            The value to assign to the products property of this CreateFleetDetails.
        :type products: list[str]

        :param application_type:
            The value to assign to the application_type property of this CreateFleetDetails.
        :type application_type: str

        :param environment_type:
            The value to assign to the environment_type property of this CreateFleetDetails.
        :type environment_type: str

        :param group_type:
            The value to assign to the group_type property of this CreateFleetDetails.
        :type group_type: str

        :param resource_selection_type:
            The value to assign to the resource_selection_type property of this CreateFleetDetails.
        :type resource_selection_type: str

        :param rule_selection_criteria:
            The value to assign to the rule_selection_criteria property of this CreateFleetDetails.
        :type rule_selection_criteria: oci.fleet_apps_management.models.SelectionCriteria

        :param notification_preferences:
            The value to assign to the notification_preferences property of this CreateFleetDetails.
        :type notification_preferences: oci.fleet_apps_management.models.NotificationPreferences

        :param resources:
            The value to assign to the resources property of this CreateFleetDetails.
        :type resources: list[oci.fleet_apps_management.models.AssociatedFleetResourceDetails]

        :param is_target_auto_confirm:
            The value to assign to the is_target_auto_confirm property of this CreateFleetDetails.
        :type is_target_auto_confirm: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateFleetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateFleetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'fleet_type': 'str',
            'products': 'list[str]',
            'application_type': 'str',
            'environment_type': 'str',
            'group_type': 'str',
            'resource_selection_type': 'str',
            'rule_selection_criteria': 'SelectionCriteria',
            'notification_preferences': 'NotificationPreferences',
            'resources': 'list[AssociatedFleetResourceDetails]',
            'is_target_auto_confirm': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'fleet_type': 'fleetType',
            'products': 'products',
            'application_type': 'applicationType',
            'environment_type': 'environmentType',
            'group_type': 'groupType',
            'resource_selection_type': 'resourceSelectionType',
            'rule_selection_criteria': 'ruleSelectionCriteria',
            'notification_preferences': 'notificationPreferences',
            'resources': 'resources',
            'is_target_auto_confirm': 'isTargetAutoConfirm',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._fleet_type = None
        self._products = None
        self._application_type = None
        self._environment_type = None
        self._group_type = None
        self._resource_selection_type = None
        self._rule_selection_criteria = None
        self._notification_preferences = None
        self._resources = None
        self._is_target_auto_confirm = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateFleetDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this CreateFleetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateFleetDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this CreateFleetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateFleetDetails.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :return: The description of this CreateFleetDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateFleetDetails.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :param description: The description of this CreateFleetDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateFleetDetails.
        Tenancy OCID


        :return: The compartment_id of this CreateFleetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateFleetDetails.
        Tenancy OCID


        :param compartment_id: The compartment_id of this CreateFleetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def fleet_type(self):
        """
        **[Required]** Gets the fleet_type of this CreateFleetDetails.
        Type of the Fleet


        :return: The fleet_type of this CreateFleetDetails.
        :rtype: str
        """
        return self._fleet_type

    @fleet_type.setter
    def fleet_type(self, fleet_type):
        """
        Sets the fleet_type of this CreateFleetDetails.
        Type of the Fleet


        :param fleet_type: The fleet_type of this CreateFleetDetails.
        :type: str
        """
        self._fleet_type = fleet_type

    @property
    def products(self):
        """
        Gets the products of this CreateFleetDetails.
        Products associated with the Fleet


        :return: The products of this CreateFleetDetails.
        :rtype: list[str]
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this CreateFleetDetails.
        Products associated with the Fleet


        :param products: The products of this CreateFleetDetails.
        :type: list[str]
        """
        self._products = products

    @property
    def application_type(self):
        """
        Gets the application_type of this CreateFleetDetails.
        Application Type associated with the Fleet.Applicable for Environment fleet types.


        :return: The application_type of this CreateFleetDetails.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """
        Sets the application_type of this CreateFleetDetails.
        Application Type associated with the Fleet.Applicable for Environment fleet types.


        :param application_type: The application_type of this CreateFleetDetails.
        :type: str
        """
        self._application_type = application_type

    @property
    def environment_type(self):
        """
        Gets the environment_type of this CreateFleetDetails.
        Environment Type associated with the Fleet.Applicable for Environment fleet types.


        :return: The environment_type of this CreateFleetDetails.
        :rtype: str
        """
        return self._environment_type

    @environment_type.setter
    def environment_type(self, environment_type):
        """
        Sets the environment_type of this CreateFleetDetails.
        Environment Type associated with the Fleet.Applicable for Environment fleet types.


        :param environment_type: The environment_type of this CreateFleetDetails.
        :type: str
        """
        self._environment_type = environment_type

    @property
    def group_type(self):
        """
        Gets the group_type of this CreateFleetDetails.
        Group Type associated with Group Fleet.Applicable for Group fleet types.


        :return: The group_type of this CreateFleetDetails.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """
        Sets the group_type of this CreateFleetDetails.
        Group Type associated with Group Fleet.Applicable for Group fleet types.


        :param group_type: The group_type of this CreateFleetDetails.
        :type: str
        """
        self._group_type = group_type

    @property
    def resource_selection_type(self):
        """
        Gets the resource_selection_type of this CreateFleetDetails.
        Type of resource selection in a fleet


        :return: The resource_selection_type of this CreateFleetDetails.
        :rtype: str
        """
        return self._resource_selection_type

    @resource_selection_type.setter
    def resource_selection_type(self, resource_selection_type):
        """
        Sets the resource_selection_type of this CreateFleetDetails.
        Type of resource selection in a fleet


        :param resource_selection_type: The resource_selection_type of this CreateFleetDetails.
        :type: str
        """
        self._resource_selection_type = resource_selection_type

    @property
    def rule_selection_criteria(self):
        """
        Gets the rule_selection_criteria of this CreateFleetDetails.

        :return: The rule_selection_criteria of this CreateFleetDetails.
        :rtype: oci.fleet_apps_management.models.SelectionCriteria
        """
        return self._rule_selection_criteria

    @rule_selection_criteria.setter
    def rule_selection_criteria(self, rule_selection_criteria):
        """
        Sets the rule_selection_criteria of this CreateFleetDetails.

        :param rule_selection_criteria: The rule_selection_criteria of this CreateFleetDetails.
        :type: oci.fleet_apps_management.models.SelectionCriteria
        """
        self._rule_selection_criteria = rule_selection_criteria

    @property
    def notification_preferences(self):
        """
        Gets the notification_preferences of this CreateFleetDetails.

        :return: The notification_preferences of this CreateFleetDetails.
        :rtype: oci.fleet_apps_management.models.NotificationPreferences
        """
        return self._notification_preferences

    @notification_preferences.setter
    def notification_preferences(self, notification_preferences):
        """
        Sets the notification_preferences of this CreateFleetDetails.

        :param notification_preferences: The notification_preferences of this CreateFleetDetails.
        :type: oci.fleet_apps_management.models.NotificationPreferences
        """
        self._notification_preferences = notification_preferences

    @property
    def resources(self):
        """
        Gets the resources of this CreateFleetDetails.
        Resources to be added during fleet creation when Resource selection type is Manual.


        :return: The resources of this CreateFleetDetails.
        :rtype: list[oci.fleet_apps_management.models.AssociatedFleetResourceDetails]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this CreateFleetDetails.
        Resources to be added during fleet creation when Resource selection type is Manual.


        :param resources: The resources of this CreateFleetDetails.
        :type: list[oci.fleet_apps_management.models.AssociatedFleetResourceDetails]
        """
        self._resources = resources

    @property
    def is_target_auto_confirm(self):
        """
        Gets the is_target_auto_confirm of this CreateFleetDetails.
        A value which represents if auto confirming of the targets can be enabled


        :return: The is_target_auto_confirm of this CreateFleetDetails.
        :rtype: bool
        """
        return self._is_target_auto_confirm

    @is_target_auto_confirm.setter
    def is_target_auto_confirm(self, is_target_auto_confirm):
        """
        Sets the is_target_auto_confirm of this CreateFleetDetails.
        A value which represents if auto confirming of the targets can be enabled


        :param is_target_auto_confirm: The is_target_auto_confirm of this CreateFleetDetails.
        :type: bool
        """
        self._is_target_auto_confirm = is_target_auto_confirm

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateFleetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateFleetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateFleetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateFleetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateFleetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateFleetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateFleetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateFleetDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
