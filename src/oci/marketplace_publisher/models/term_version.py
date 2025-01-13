# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TermVersion(object):
    """
    Model object for the term version details.
    """

    #: A constant which can be used with the status property of a TermVersion.
    #: This constant has a value of "AVAILABLE"
    STATUS_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the status property of a TermVersion.
    #: This constant has a value of "NOT_AVAILABLE"
    STATUS_NOT_AVAILABLE = "NOT_AVAILABLE"

    #: A constant which can be used with the status property of a TermVersion.
    #: This constant has a value of "DELETED"
    STATUS_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TermVersion.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TermVersion.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new TermVersion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TermVersion.
        :type id: str

        :param term_id:
            The value to assign to the term_id property of this TermVersion.
        :type term_id: str

        :param term_author:
            The value to assign to the term_author property of this TermVersion.
        :type term_author: str

        :param display_name:
            The value to assign to the display_name property of this TermVersion.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TermVersion.
        :type compartment_id: str

        :param attachment:
            The value to assign to the attachment property of this TermVersion.
        :type attachment: oci.marketplace_publisher.models.TermVersionAttachment

        :param status:
            The value to assign to the status property of this TermVersion.
            Allowed values for this property are: "AVAILABLE", "NOT_AVAILABLE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param author:
            The value to assign to the author property of this TermVersion.
        :type author: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TermVersion.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this TermVersion.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TermVersion.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TermVersion.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TermVersion.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this TermVersion.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'term_id': 'str',
            'term_author': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'attachment': 'TermVersionAttachment',
            'status': 'str',
            'author': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'term_id': 'termId',
            'term_author': 'termAuthor',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'attachment': 'attachment',
            'status': 'status',
            'author': 'author',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._term_id = None
        self._term_author = None
        self._display_name = None
        self._compartment_id = None
        self._attachment = None
        self._status = None
        self._author = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        Gets the id of this TermVersion.
        Unique OCID identifier for the term version.


        :return: The id of this TermVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TermVersion.
        Unique OCID identifier for the term version.


        :param id: The id of this TermVersion.
        :type: str
        """
        self._id = id

    @property
    def term_id(self):
        """
        **[Required]** Gets the term_id of this TermVersion.
        The unique identifier for the term.


        :return: The term_id of this TermVersion.
        :rtype: str
        """
        return self._term_id

    @term_id.setter
    def term_id(self, term_id):
        """
        Sets the term_id of this TermVersion.
        The unique identifier for the term.


        :param term_id: The term_id of this TermVersion.
        :type: str
        """
        self._term_id = term_id

    @property
    def term_author(self):
        """
        **[Required]** Gets the term_author of this TermVersion.
        Who authored the term. Publisher terms will be defaulted to 'PARTNER'.


        :return: The term_author of this TermVersion.
        :rtype: str
        """
        return self._term_author

    @term_author.setter
    def term_author(self, term_author):
        """
        Sets the term_author of this TermVersion.
        Who authored the term. Publisher terms will be defaulted to 'PARTNER'.


        :param term_author: The term_author of this TermVersion.
        :type: str
        """
        self._term_author = term_author

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this TermVersion.
        The name for the term version.


        :return: The display_name of this TermVersion.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TermVersion.
        The name for the term version.


        :param display_name: The display_name of this TermVersion.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this TermVersion.
        The unique identifier for the compartment.


        :return: The compartment_id of this TermVersion.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TermVersion.
        The unique identifier for the compartment.


        :param compartment_id: The compartment_id of this TermVersion.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def attachment(self):
        """
        **[Required]** Gets the attachment of this TermVersion.

        :return: The attachment of this TermVersion.
        :rtype: oci.marketplace_publisher.models.TermVersionAttachment
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """
        Sets the attachment of this TermVersion.

        :param attachment: The attachment of this TermVersion.
        :type: oci.marketplace_publisher.models.TermVersionAttachment
        """
        self._attachment = attachment

    @property
    def status(self):
        """
        **[Required]** Gets the status of this TermVersion.
        The current status for the term version.

        Allowed values for this property are: "AVAILABLE", "NOT_AVAILABLE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this TermVersion.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TermVersion.
        The current status for the term version.


        :param status: The status of this TermVersion.
        :type: str
        """
        allowed_values = ["AVAILABLE", "NOT_AVAILABLE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def author(self):
        """
        Gets the author of this TermVersion.
        Who authored the term. Publisher terms will be defaulted to 'PARTNER'.


        :return: The author of this TermVersion.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this TermVersion.
        Who authored the term. Publisher terms will be defaulted to 'PARTNER'.


        :param author: The author of this TermVersion.
        :type: str
        """
        self._author = author

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this TermVersion.
        The current state for the term version.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TermVersion.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TermVersion.
        The current state for the term version.


        :param lifecycle_state: The lifecycle_state of this TermVersion.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this TermVersion.
        The date and time the term version was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this TermVersion.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TermVersion.
        The date and time the term version was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this TermVersion.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this TermVersion.
        The date and time the term version was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this TermVersion.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TermVersion.
        The date and time the term version was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this TermVersion.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TermVersion.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this TermVersion.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TermVersion.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this TermVersion.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TermVersion.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this TermVersion.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TermVersion.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this TermVersion.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this TermVersion.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this TermVersion.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this TermVersion.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this TermVersion.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
