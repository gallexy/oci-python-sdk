# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240815


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityAttributeNamespace(object):
    """
    A managed container for security attributes. A security attribute namespace is unique in a tenancy. For more information,
    see `Managing Security Attributes Namespaces`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values
    using the API.

    __ https://docs.cloud.oracle.com/Content/zero-trust-packet-routing/managing-security-attribute-namespaces.htm
    """

    #: A constant which can be used with the lifecycle_state property of a SecurityAttributeNamespace.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SecurityAttributeNamespace.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SecurityAttributeNamespace.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SecurityAttributeNamespace.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityAttributeNamespace object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SecurityAttributeNamespace.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SecurityAttributeNamespace.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this SecurityAttributeNamespace.
        :type name: str

        :param description:
            The value to assign to the description property of this SecurityAttributeNamespace.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SecurityAttributeNamespace.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SecurityAttributeNamespace.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SecurityAttributeNamespace.
        :type system_tags: dict(str, dict(str, object))

        :param is_retired:
            The value to assign to the is_retired property of this SecurityAttributeNamespace.
        :type is_retired: bool

        :param mode:
            The value to assign to the mode property of this SecurityAttributeNamespace.
        :type mode: list[str]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SecurityAttributeNamespace.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this SecurityAttributeNamespace.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'is_retired': 'bool',
            'mode': 'list[str]',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'is_retired': 'isRetired',
            'mode': 'mode',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._is_retired = None
        self._mode = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SecurityAttributeNamespace.
        The OCID of the security attribute namespace.


        :return: The id of this SecurityAttributeNamespace.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityAttributeNamespace.
        The OCID of the security attribute namespace.


        :param id: The id of this SecurityAttributeNamespace.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SecurityAttributeNamespace.
        The OCID of the compartment that contains the namespace.


        :return: The compartment_id of this SecurityAttributeNamespace.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SecurityAttributeNamespace.
        The OCID of the compartment that contains the namespace.


        :param compartment_id: The compartment_id of this SecurityAttributeNamespace.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SecurityAttributeNamespace.
        The name of the namespace. It must be unique across all namespaces in the tenancy and cannot be changed.


        :return: The name of this SecurityAttributeNamespace.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SecurityAttributeNamespace.
        The name of the namespace. It must be unique across all namespaces in the tenancy and cannot be changed.


        :param name: The name of this SecurityAttributeNamespace.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this SecurityAttributeNamespace.
        The description you assign to the security attribute namespace.


        :return: The description of this SecurityAttributeNamespace.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SecurityAttributeNamespace.
        The description you assign to the security attribute namespace.


        :param description: The description of this SecurityAttributeNamespace.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SecurityAttributeNamespace.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SecurityAttributeNamespace.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SecurityAttributeNamespace.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SecurityAttributeNamespace.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SecurityAttributeNamespace.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SecurityAttributeNamespace.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SecurityAttributeNamespace.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SecurityAttributeNamespace.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SecurityAttributeNamespace.
        System tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this SecurityAttributeNamespace.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SecurityAttributeNamespace.
        System tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this SecurityAttributeNamespace.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def is_retired(self):
        """
        **[Required]** Gets the is_retired of this SecurityAttributeNamespace.
        Indicates whether the security attribute namespace is retired.
        See `Managing Security Attribute Namespaces`__.

        __ https://docs.cloud.oracle.com/Content/zero-trust-packet-routing/managing-security-attribute-namespaces.htm


        :return: The is_retired of this SecurityAttributeNamespace.
        :rtype: bool
        """
        return self._is_retired

    @is_retired.setter
    def is_retired(self, is_retired):
        """
        Sets the is_retired of this SecurityAttributeNamespace.
        Indicates whether the security attribute namespace is retired.
        See `Managing Security Attribute Namespaces`__.

        __ https://docs.cloud.oracle.com/Content/zero-trust-packet-routing/managing-security-attribute-namespaces.htm


        :param is_retired: The is_retired of this SecurityAttributeNamespace.
        :type: bool
        """
        self._is_retired = is_retired

    @property
    def mode(self):
        """
        Gets the mode of this SecurityAttributeNamespace.
        Indicates possible modes the security attributes in this namespace can be set to.
        This is not accepted from the user. Currently the supported values are enforce and audit.


        :return: The mode of this SecurityAttributeNamespace.
        :rtype: list[str]
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this SecurityAttributeNamespace.
        Indicates possible modes the security attributes in this namespace can be set to.
        This is not accepted from the user. Currently the supported values are enforce and audit.


        :param mode: The mode of this SecurityAttributeNamespace.
        :type: list[str]
        """
        self._mode = mode

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SecurityAttributeNamespace.
        The security attribute namespace's current state. After creating a security attribute namespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a security attribute namespace, make sure its `lifecycleState` is INACTIVE.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SecurityAttributeNamespace.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SecurityAttributeNamespace.
        The security attribute namespace's current state. After creating a security attribute namespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a security attribute namespace, make sure its `lifecycleState` is INACTIVE.


        :param lifecycle_state: The lifecycle_state of this SecurityAttributeNamespace.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SecurityAttributeNamespace.
        Date and time the security attribute namespace was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this SecurityAttributeNamespace.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecurityAttributeNamespace.
        Date and time the security attribute namespace was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this SecurityAttributeNamespace.
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
