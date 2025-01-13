# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240815


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityAttributeSummary(object):
    """
    A security attribute definition that belongs to a specific security attribute namespace.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityAttributeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this SecurityAttributeSummary.
        :type compartment_id: str

        :param security_attribute_namespace_id:
            The value to assign to the security_attribute_namespace_id property of this SecurityAttributeSummary.
        :type security_attribute_namespace_id: str

        :param security_attribute_namespace_name:
            The value to assign to the security_attribute_namespace_name property of this SecurityAttributeSummary.
        :type security_attribute_namespace_name: str

        :param id:
            The value to assign to the id property of this SecurityAttributeSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this SecurityAttributeSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this SecurityAttributeSummary.
        :type description: str

        :param type:
            The value to assign to the type property of this SecurityAttributeSummary.
        :type type: str

        :param is_retired:
            The value to assign to the is_retired property of this SecurityAttributeSummary.
        :type is_retired: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SecurityAttributeSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this SecurityAttributeSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'security_attribute_namespace_id': 'str',
            'security_attribute_namespace_name': 'str',
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'type': 'str',
            'is_retired': 'bool',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'security_attribute_namespace_id': 'securityAttributeNamespaceId',
            'security_attribute_namespace_name': 'securityAttributeNamespaceName',
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'is_retired': 'isRetired',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._security_attribute_namespace_id = None
        self._security_attribute_namespace_name = None
        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._is_retired = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this SecurityAttributeSummary.
        The OCID of the compartment that contains the security attribute.


        :return: The compartment_id of this SecurityAttributeSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SecurityAttributeSummary.
        The OCID of the compartment that contains the security attribute.


        :param compartment_id: The compartment_id of this SecurityAttributeSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def security_attribute_namespace_id(self):
        """
        Gets the security_attribute_namespace_id of this SecurityAttributeSummary.
        The OCID of the namespace that contains the security attribute.


        :return: The security_attribute_namespace_id of this SecurityAttributeSummary.
        :rtype: str
        """
        return self._security_attribute_namespace_id

    @security_attribute_namespace_id.setter
    def security_attribute_namespace_id(self, security_attribute_namespace_id):
        """
        Sets the security_attribute_namespace_id of this SecurityAttributeSummary.
        The OCID of the namespace that contains the security attribute.


        :param security_attribute_namespace_id: The security_attribute_namespace_id of this SecurityAttributeSummary.
        :type: str
        """
        self._security_attribute_namespace_id = security_attribute_namespace_id

    @property
    def security_attribute_namespace_name(self):
        """
        Gets the security_attribute_namespace_name of this SecurityAttributeSummary.
        The name of the security attribute namespace that contains the security attribute.


        :return: The security_attribute_namespace_name of this SecurityAttributeSummary.
        :rtype: str
        """
        return self._security_attribute_namespace_name

    @security_attribute_namespace_name.setter
    def security_attribute_namespace_name(self, security_attribute_namespace_name):
        """
        Sets the security_attribute_namespace_name of this SecurityAttributeSummary.
        The name of the security attribute namespace that contains the security attribute.


        :param security_attribute_namespace_name: The security_attribute_namespace_name of this SecurityAttributeSummary.
        :type: str
        """
        self._security_attribute_namespace_name = security_attribute_namespace_name

    @property
    def id(self):
        """
        Gets the id of this SecurityAttributeSummary.
        The OCID of the security attribute.


        :return: The id of this SecurityAttributeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityAttributeSummary.
        The OCID of the security attribute.


        :param id: The id of this SecurityAttributeSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SecurityAttributeSummary.
        The name assigned to the security attribute during creation. This is the security attribute.
        The name must be unique within the security attribute namespace and cannot be changed.


        :return: The name of this SecurityAttributeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SecurityAttributeSummary.
        The name assigned to the security attribute during creation. This is the security attribute.
        The name must be unique within the security attribute namespace and cannot be changed.


        :param name: The name of this SecurityAttributeSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SecurityAttributeSummary.
        The description you assign to the security attribute.


        :return: The description of this SecurityAttributeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SecurityAttributeSummary.
        The description you assign to the security attribute.


        :param description: The description of this SecurityAttributeSummary.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        Gets the type of this SecurityAttributeSummary.
        The data type of the security attribute.


        :return: The type of this SecurityAttributeSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SecurityAttributeSummary.
        The data type of the security attribute.


        :param type: The type of this SecurityAttributeSummary.
        :type: str
        """
        self._type = type

    @property
    def is_retired(self):
        """
        Gets the is_retired of this SecurityAttributeSummary.
        Whether the security attribute is retired.
        See `Managing Security Attributes`__.

        __ https://docs.cloud.oracle.com/Content/zero-trust-packet-routing/managing-security-attributes.htm


        :return: The is_retired of this SecurityAttributeSummary.
        :rtype: bool
        """
        return self._is_retired

    @is_retired.setter
    def is_retired(self, is_retired):
        """
        Sets the is_retired of this SecurityAttributeSummary.
        Whether the security attribute is retired.
        See `Managing Security Attributes`__.

        __ https://docs.cloud.oracle.com/Content/zero-trust-packet-routing/managing-security-attributes.htm


        :param is_retired: The is_retired of this SecurityAttributeSummary.
        :type: bool
        """
        self._is_retired = is_retired

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SecurityAttributeSummary.
        The security attribute's current state. After creating a security attribute, make sure its `lifecycleState` is ACTIVE before using it. After retiring a security attribute, make sure its `lifecycleState` is INACTIVE before using it. If you delete a security attribute, you cannot delete another security attribute until the deleted security attribute's `lifecycleState` changes from DELETING to DELETED.


        :return: The lifecycle_state of this SecurityAttributeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SecurityAttributeSummary.
        The security attribute's current state. After creating a security attribute, make sure its `lifecycleState` is ACTIVE before using it. After retiring a security attribute, make sure its `lifecycleState` is INACTIVE before using it. If you delete a security attribute, you cannot delete another security attribute until the deleted security attribute's `lifecycleState` changes from DELETING to DELETED.


        :param lifecycle_state: The lifecycle_state of this SecurityAttributeSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this SecurityAttributeSummary.
        Date and time the security attribute was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this SecurityAttributeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecurityAttributeSummary.
        Date and time the security attribute was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this SecurityAttributeSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
