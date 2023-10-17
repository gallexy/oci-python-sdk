# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateArtifactDetails(object):
    """
    Common Details to create Marketplace Publisher artifact.
    """

    #: A constant which can be used with the artifact_type property of a CreateArtifactDetails.
    #: This constant has a value of "CONTAINER_IMAGE"
    ARTIFACT_TYPE_CONTAINER_IMAGE = "CONTAINER_IMAGE"

    #: A constant which can be used with the artifact_type property of a CreateArtifactDetails.
    #: This constant has a value of "HELM_CHART"
    ARTIFACT_TYPE_HELM_CHART = "HELM_CHART"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateArtifactDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.marketplace_publisher.models.CreateKubernetesImageArtifactDetails`
        * :class:`~oci.marketplace_publisher.models.CreateContainerImageArtifactDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateArtifactDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateArtifactDetails.
        :type display_name: str

        :param artifact_type:
            The value to assign to the artifact_type property of this CreateArtifactDetails.
            Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART"
        :type artifact_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateArtifactDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateArtifactDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'artifact_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'artifact_type': 'artifactType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._artifact_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['artifactType']

        if type == 'HELM_CHART':
            return 'CreateKubernetesImageArtifactDetails'

        if type == 'CONTAINER_IMAGE':
            return 'CreateContainerImageArtifactDetails'
        else:
            return 'CreateArtifactDetails'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateArtifactDetails.
        The unique identifier for the compartment.


        :return: The compartment_id of this CreateArtifactDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateArtifactDetails.
        The unique identifier for the compartment.


        :param compartment_id: The compartment_id of this CreateArtifactDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateArtifactDetails.
        The display name for the artifact.


        :return: The display_name of this CreateArtifactDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateArtifactDetails.
        The display name for the artifact.


        :param display_name: The display_name of this CreateArtifactDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def artifact_type(self):
        """
        **[Required]** Gets the artifact_type of this CreateArtifactDetails.
        Artifact Type for the artifact.

        Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART"


        :return: The artifact_type of this CreateArtifactDetails.
        :rtype: str
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        """
        Sets the artifact_type of this CreateArtifactDetails.
        Artifact Type for the artifact.


        :param artifact_type: The artifact_type of this CreateArtifactDetails.
        :type: str
        """
        allowed_values = ["CONTAINER_IMAGE", "HELM_CHART"]
        if not value_allowed_none_or_none_sentinel(artifact_type, allowed_values):
            raise ValueError(
                f"Invalid value for `artifact_type`, must be None or one of {allowed_values}"
            )
        self._artifact_type = artifact_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateArtifactDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateArtifactDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateArtifactDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateArtifactDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateArtifactDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateArtifactDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateArtifactDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateArtifactDetails.
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
