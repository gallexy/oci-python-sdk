# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Desktop(object):
    """
    Provides information about a desktop including name, state, id, configuration, owner, and time created.
    """

    #: A constant which can be used with the lifecycle_state property of a Desktop.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Desktop.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Desktop.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Desktop.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Desktop.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Desktop.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Desktop.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Desktop object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Desktop.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Desktop.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Desktop.
        :type time_created: datetime

        :param display_name:
            The value to assign to the display_name property of this Desktop.
        :type display_name: str

        :param device_policy:
            The value to assign to the device_policy property of this Desktop.
        :type device_policy: oci.desktops.models.DesktopDevicePolicy

        :param hosting_options:
            The value to assign to the hosting_options property of this Desktop.
        :type hosting_options: oci.desktops.models.HostingOptions

        :param user_name:
            The value to assign to the user_name property of this Desktop.
        :type user_name: str

        :param pool_id:
            The value to assign to the pool_id property of this Desktop.
        :type pool_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Desktop.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Desktop.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'display_name': 'str',
            'device_policy': 'DesktopDevicePolicy',
            'hosting_options': 'HostingOptions',
            'user_name': 'str',
            'pool_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'display_name': 'displayName',
            'device_policy': 'devicePolicy',
            'hosting_options': 'hostingOptions',
            'user_name': 'userName',
            'pool_id': 'poolId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._display_name = None
        self._device_policy = None
        self._hosting_options = None
        self._user_name = None
        self._pool_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Desktop.
        The OCID of the desktop.


        :return: The id of this Desktop.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Desktop.
        The OCID of the desktop.


        :param id: The id of this Desktop.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Desktop.
        The state of the desktop.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Desktop.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Desktop.
        The state of the desktop.


        :param lifecycle_state: The lifecycle_state of this Desktop.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Desktop.
        The date and time the resource was created.


        :return: The time_created of this Desktop.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Desktop.
        The date and time the resource was created.


        :param time_created: The time_created of this Desktop.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Desktop.
        A user friendly display name. Avoid entering confidential information.


        :return: The display_name of this Desktop.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Desktop.
        A user friendly display name. Avoid entering confidential information.


        :param display_name: The display_name of this Desktop.
        :type: str
        """
        self._display_name = display_name

    @property
    def device_policy(self):
        """
        **[Required]** Gets the device_policy of this Desktop.

        :return: The device_policy of this Desktop.
        :rtype: oci.desktops.models.DesktopDevicePolicy
        """
        return self._device_policy

    @device_policy.setter
    def device_policy(self, device_policy):
        """
        Sets the device_policy of this Desktop.

        :param device_policy: The device_policy of this Desktop.
        :type: oci.desktops.models.DesktopDevicePolicy
        """
        self._device_policy = device_policy

    @property
    def hosting_options(self):
        """
        **[Required]** Gets the hosting_options of this Desktop.

        :return: The hosting_options of this Desktop.
        :rtype: oci.desktops.models.HostingOptions
        """
        return self._hosting_options

    @hosting_options.setter
    def hosting_options(self, hosting_options):
        """
        Sets the hosting_options of this Desktop.

        :param hosting_options: The hosting_options of this Desktop.
        :type: oci.desktops.models.HostingOptions
        """
        self._hosting_options = hosting_options

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this Desktop.
        The owner of the desktop.


        :return: The user_name of this Desktop.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this Desktop.
        The owner of the desktop.


        :param user_name: The user_name of this Desktop.
        :type: str
        """
        self._user_name = user_name

    @property
    def pool_id(self):
        """
        **[Required]** Gets the pool_id of this Desktop.
        The OCID of the desktop pool the desktop is a member of.


        :return: The pool_id of this Desktop.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """
        Sets the pool_id of this Desktop.
        The OCID of the desktop pool the desktop is a member of.


        :param pool_id: The pool_id of this Desktop.
        :type: str
        """
        self._pool_id = pool_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Desktop.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Desktop.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Desktop.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Desktop.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Desktop.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Desktop.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Desktop.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Desktop.
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
