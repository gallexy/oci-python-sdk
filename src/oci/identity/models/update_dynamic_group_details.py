# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDynamicGroupDetails(object):
    """
    Properties for updating a dynamic group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDynamicGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateDynamicGroupDetails.
        :type description: str

        :param matching_rule:
            The value to assign to the matching_rule property of this UpdateDynamicGroupDetails.
        :type matching_rule: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDynamicGroupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDynamicGroupDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'matching_rule': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'description': 'description',
            'matching_rule': 'matchingRule',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._description = None
        self._matching_rule = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateDynamicGroupDetails.
        The description you assign to the dynamic group. Does not have to be unique, and it's changeable.

        (For tenancies that support identity domains) You can have an empty description.


        :return: The description of this UpdateDynamicGroupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDynamicGroupDetails.
        The description you assign to the dynamic group. Does not have to be unique, and it's changeable.

        (For tenancies that support identity domains) You can have an empty description.


        :param description: The description of this UpdateDynamicGroupDetails.
        :type: str
        """
        self._description = description

    @property
    def matching_rule(self):
        """
        Gets the matching_rule of this UpdateDynamicGroupDetails.
        The matching rule to dynamically match an instance certificate to this dynamic group.
        For rule syntax, see `Managing Dynamic Groups`__.

        __ https://docs.cloud.oracle.com/Content/Identity/dynamicgroups/managingdynamicgroups.htm


        :return: The matching_rule of this UpdateDynamicGroupDetails.
        :rtype: str
        """
        return self._matching_rule

    @matching_rule.setter
    def matching_rule(self, matching_rule):
        """
        Sets the matching_rule of this UpdateDynamicGroupDetails.
        The matching rule to dynamically match an instance certificate to this dynamic group.
        For rule syntax, see `Managing Dynamic Groups`__.

        __ https://docs.cloud.oracle.com/Content/Identity/dynamicgroups/managingdynamicgroups.htm


        :param matching_rule: The matching_rule of this UpdateDynamicGroupDetails.
        :type: str
        """
        self._matching_rule = matching_rule

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDynamicGroupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateDynamicGroupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDynamicGroupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateDynamicGroupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDynamicGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateDynamicGroupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDynamicGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateDynamicGroupDetails.
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
