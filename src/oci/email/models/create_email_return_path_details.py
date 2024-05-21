# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20170907


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEmailReturnPathDetails(object):
    """
    Properties to create a new email return path.
    The new object will be created in the same compartment as the parent resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEmailReturnPathDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateEmailReturnPathDetails.
        :type name: str

        :param parent_resource_id:
            The value to assign to the parent_resource_id property of this CreateEmailReturnPathDetails.
        :type parent_resource_id: str

        :param description:
            The value to assign to the description property of this CreateEmailReturnPathDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateEmailReturnPathDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateEmailReturnPathDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'parent_resource_id': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'parent_resource_id': 'parentResourceId',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._parent_resource_id = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        Gets the name of this CreateEmailReturnPathDetails.
        The name of the email return path domain in the Internet Domain Name System (DNS).
        The name must be a subdomain of the email domain used to send emails.
        The email return path name must be globally unique for this tenancy.
        If you do not provide the email return path name, we will generate one for you.
        If you do provide the email return path name, we suggest adding a short region indicator to
        allow using the same parent domain in other regions you might be subscribed to.
        Domain names limited to ASCII characters use alphanumeric, dash (\"-\"), and dot (\".\") characters.
        The dash and dot are only allowed between alphanumeric characters.
        Non-ASCII domain names should adopt IDNA2008 normalization (RFC 5891-5892).


        :return: The name of this CreateEmailReturnPathDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateEmailReturnPathDetails.
        The name of the email return path domain in the Internet Domain Name System (DNS).
        The name must be a subdomain of the email domain used to send emails.
        The email return path name must be globally unique for this tenancy.
        If you do not provide the email return path name, we will generate one for you.
        If you do provide the email return path name, we suggest adding a short region indicator to
        allow using the same parent domain in other regions you might be subscribed to.
        Domain names limited to ASCII characters use alphanumeric, dash (\"-\"), and dot (\".\") characters.
        The dash and dot are only allowed between alphanumeric characters.
        Non-ASCII domain names should adopt IDNA2008 normalization (RFC 5891-5892).


        :param name: The name of this CreateEmailReturnPathDetails.
        :type: str
        """
        self._name = name

    @property
    def parent_resource_id(self):
        """
        **[Required]** Gets the parent_resource_id of this CreateEmailReturnPathDetails.
        The `OCID`__ of the EmailDomain for this email return path.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The parent_resource_id of this CreateEmailReturnPathDetails.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """
        Sets the parent_resource_id of this CreateEmailReturnPathDetails.
        The `OCID`__ of the EmailDomain for this email return path.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param parent_resource_id: The parent_resource_id of this CreateEmailReturnPathDetails.
        :type: str
        """
        self._parent_resource_id = parent_resource_id

    @property
    def description(self):
        """
        Gets the description of this CreateEmailReturnPathDetails.
        A string that describes the details about the email return path. It does not have to be unique,
        and you can change it. Avoid entering confidential information.


        :return: The description of this CreateEmailReturnPathDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateEmailReturnPathDetails.
        A string that describes the details about the email return path. It does not have to be unique,
        and you can change it. Avoid entering confidential information.


        :param description: The description of this CreateEmailReturnPathDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateEmailReturnPathDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateEmailReturnPathDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateEmailReturnPathDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateEmailReturnPathDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateEmailReturnPathDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateEmailReturnPathDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateEmailReturnPathDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateEmailReturnPathDetails.
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