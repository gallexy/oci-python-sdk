# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GrantEntitlement(object):
    """
    The entitlement or privilege that is being granted

    **SCIM++ Properties:**
    - idcsCsvAttributeNameMappings: [[columnHeaderName:Entitlement Value, csvColumnForResolvingResourceType:Entitlement Name, mapsTo:entitlement.attributeValue, referencedResourceTypeUniqueAttributeNameMappings:[[mapsFromColumnName:Entitlement Value, resourceTypeAttributeName:displayName], [mapsFromColumnName:App Name, resourceTypeAttributeName:app.display]], resolveValueUsingResourceType:[[resolveBy:AppRole, valueToBeResolved:appRoles]]], [columnHeaderName:Entitlement Name, defaultValue:appRoles, mapsTo:entitlement.attributeName]]
    - idcsSearchable: true
    - multiValued: false
    - mutability: immutable
    - required: false
    - returned: default
    - type: complex
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GrantEntitlement object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_name:
            The value to assign to the attribute_name property of this GrantEntitlement.
        :type attribute_name: str

        :param attribute_value:
            The value to assign to the attribute_value property of this GrantEntitlement.
        :type attribute_value: str

        """
        self.swagger_types = {
            'attribute_name': 'str',
            'attribute_value': 'str'
        }

        self.attribute_map = {
            'attribute_name': 'attributeName',
            'attribute_value': 'attributeValue'
        }

        self._attribute_name = None
        self._attribute_value = None

    @property
    def attribute_name(self):
        """
        **[Required]** Gets the attribute_name of this GrantEntitlement.
        The name of the attribute whose value (specified by attributeValue) confers privilege within the service-instance (specified by app).

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The attribute_name of this GrantEntitlement.
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """
        Sets the attribute_name of this GrantEntitlement.
        The name of the attribute whose value (specified by attributeValue) confers privilege within the service-instance (specified by app).

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param attribute_name: The attribute_name of this GrantEntitlement.
        :type: str
        """
        self._attribute_name = attribute_name

    @property
    def attribute_value(self):
        """
        **[Required]** Gets the attribute_value of this GrantEntitlement.
        The value of the attribute (specified by attributeName) that confers privilege within the service-instance (specified by app).  If attributeName is 'appRoles', then attributeValue is the ID of the AppRole.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsCsvAttributeName: Display Name
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The attribute_value of this GrantEntitlement.
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """
        Sets the attribute_value of this GrantEntitlement.
        The value of the attribute (specified by attributeName) that confers privilege within the service-instance (specified by app).  If attributeName is 'appRoles', then attributeValue is the ID of the AppRole.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsCsvAttributeName: Display Name
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param attribute_value: The attribute_value of this GrantEntitlement.
        :type: str
        """
        self._attribute_value = attribute_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
