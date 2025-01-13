# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEndpointDetails(object):
    """
    The data to create an endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateEndpointDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateEndpointDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateEndpointDetails.
        :type compartment_id: str

        :param model_id:
            The value to assign to the model_id property of this CreateEndpointDetails.
        :type model_id: str

        :param dedicated_ai_cluster_id:
            The value to assign to the dedicated_ai_cluster_id property of this CreateEndpointDetails.
        :type dedicated_ai_cluster_id: str

        :param content_moderation_config:
            The value to assign to the content_moderation_config property of this CreateEndpointDetails.
        :type content_moderation_config: oci.generative_ai.models.ContentModerationConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'model_id': 'str',
            'dedicated_ai_cluster_id': 'str',
            'content_moderation_config': 'ContentModerationConfig',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'model_id': 'modelId',
            'dedicated_ai_cluster_id': 'dedicatedAiClusterId',
            'content_moderation_config': 'contentModerationConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._model_id = None
        self._dedicated_ai_cluster_id = None
        self._content_moderation_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateEndpointDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this CreateEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateEndpointDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CreateEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateEndpointDetails.
        An optional description of the endpoint.


        :return: The description of this CreateEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateEndpointDetails.
        An optional description of the endpoint.


        :param description: The description of this CreateEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateEndpointDetails.
        The compartment OCID to create the endpoint in.


        :return: The compartment_id of this CreateEndpointDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateEndpointDetails.
        The compartment OCID to create the endpoint in.


        :param compartment_id: The compartment_id of this CreateEndpointDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def model_id(self):
        """
        **[Required]** Gets the model_id of this CreateEndpointDetails.
        The OCID of the model that's used to create this endpoint.


        :return: The model_id of this CreateEndpointDetails.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """
        Sets the model_id of this CreateEndpointDetails.
        The OCID of the model that's used to create this endpoint.


        :param model_id: The model_id of this CreateEndpointDetails.
        :type: str
        """
        self._model_id = model_id

    @property
    def dedicated_ai_cluster_id(self):
        """
        **[Required]** Gets the dedicated_ai_cluster_id of this CreateEndpointDetails.
        The OCID of the dedicated AI cluster on which a model will be deployed to.


        :return: The dedicated_ai_cluster_id of this CreateEndpointDetails.
        :rtype: str
        """
        return self._dedicated_ai_cluster_id

    @dedicated_ai_cluster_id.setter
    def dedicated_ai_cluster_id(self, dedicated_ai_cluster_id):
        """
        Sets the dedicated_ai_cluster_id of this CreateEndpointDetails.
        The OCID of the dedicated AI cluster on which a model will be deployed to.


        :param dedicated_ai_cluster_id: The dedicated_ai_cluster_id of this CreateEndpointDetails.
        :type: str
        """
        self._dedicated_ai_cluster_id = dedicated_ai_cluster_id

    @property
    def content_moderation_config(self):
        """
        Gets the content_moderation_config of this CreateEndpointDetails.

        :return: The content_moderation_config of this CreateEndpointDetails.
        :rtype: oci.generative_ai.models.ContentModerationConfig
        """
        return self._content_moderation_config

    @content_moderation_config.setter
    def content_moderation_config(self, content_moderation_config):
        """
        Sets the content_moderation_config of this CreateEndpointDetails.

        :param content_moderation_config: The content_moderation_config of this CreateEndpointDetails.
        :type: oci.generative_ai.models.ContentModerationConfig
        """
        self._content_moderation_config = content_moderation_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateEndpointDetails.
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
