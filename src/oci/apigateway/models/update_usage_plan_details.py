# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateUsagePlanDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateUsagePlanDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateUsagePlanDetails.
        :type display_name: str

        :param entitlements:
            The value to assign to the entitlements property of this UpdateUsagePlanDetails.
        :type entitlements: list[oci.apigateway.models.Entitlement]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateUsagePlanDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateUsagePlanDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'entitlements': 'list[Entitlement]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'entitlements': 'entitlements',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._entitlements = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateUsagePlanDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this UpdateUsagePlanDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateUsagePlanDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this UpdateUsagePlanDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def entitlements(self):
        """
        Gets the entitlements of this UpdateUsagePlanDetails.
        A collection of entitlements to update the current usage plan with.


        :return: The entitlements of this UpdateUsagePlanDetails.
        :rtype: list[oci.apigateway.models.Entitlement]
        """
        return self._entitlements

    @entitlements.setter
    def entitlements(self, entitlements):
        """
        Sets the entitlements of this UpdateUsagePlanDetails.
        A collection of entitlements to update the current usage plan with.


        :param entitlements: The entitlements of this UpdateUsagePlanDetails.
        :type: list[oci.apigateway.models.Entitlement]
        """
        self._entitlements = entitlements

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateUsagePlanDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateUsagePlanDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateUsagePlanDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateUsagePlanDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateUsagePlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateUsagePlanDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateUsagePlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateUsagePlanDetails.
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
