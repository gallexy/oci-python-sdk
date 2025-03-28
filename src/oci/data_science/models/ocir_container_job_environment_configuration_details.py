# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .job_environment_configuration_details import JobEnvironmentConfigurationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OcirContainerJobEnvironmentConfigurationDetails(JobEnvironmentConfigurationDetails):
    """
    Environment configuration based on container image stored in OCI Container Registry.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OcirContainerJobEnvironmentConfigurationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.OcirContainerJobEnvironmentConfigurationDetails.job_environment_type` attribute
        of this class is ``OCIR_CONTAINER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param job_environment_type:
            The value to assign to the job_environment_type property of this OcirContainerJobEnvironmentConfigurationDetails.
            Allowed values for this property are: "OCIR_CONTAINER"
        :type job_environment_type: str

        :param image:
            The value to assign to the image property of this OcirContainerJobEnvironmentConfigurationDetails.
        :type image: str

        :param cmd:
            The value to assign to the cmd property of this OcirContainerJobEnvironmentConfigurationDetails.
        :type cmd: list[str]

        :param entrypoint:
            The value to assign to the entrypoint property of this OcirContainerJobEnvironmentConfigurationDetails.
        :type entrypoint: list[str]

        :param image_digest:
            The value to assign to the image_digest property of this OcirContainerJobEnvironmentConfigurationDetails.
        :type image_digest: str

        :param image_signature_id:
            The value to assign to the image_signature_id property of this OcirContainerJobEnvironmentConfigurationDetails.
        :type image_signature_id: str

        """
        self.swagger_types = {
            'job_environment_type': 'str',
            'image': 'str',
            'cmd': 'list[str]',
            'entrypoint': 'list[str]',
            'image_digest': 'str',
            'image_signature_id': 'str'
        }
        self.attribute_map = {
            'job_environment_type': 'jobEnvironmentType',
            'image': 'image',
            'cmd': 'cmd',
            'entrypoint': 'entrypoint',
            'image_digest': 'imageDigest',
            'image_signature_id': 'imageSignatureId'
        }
        self._job_environment_type = None
        self._image = None
        self._cmd = None
        self._entrypoint = None
        self._image_digest = None
        self._image_signature_id = None
        self._job_environment_type = 'OCIR_CONTAINER'

    @property
    def image(self):
        """
        **[Required]** Gets the image of this OcirContainerJobEnvironmentConfigurationDetails.
        The full path to the Oracle Container Repository (OCIR) registry, image, and tag in a canonical format.
        Acceptable format:
        `<region>.ocir.io/<registry>/<image>:<tag>`
        `<region>.ocir.io/<registry>/<image>:<tag>@digest`


        :return: The image of this OcirContainerJobEnvironmentConfigurationDetails.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this OcirContainerJobEnvironmentConfigurationDetails.
        The full path to the Oracle Container Repository (OCIR) registry, image, and tag in a canonical format.
        Acceptable format:
        `<region>.ocir.io/<registry>/<image>:<tag>`
        `<region>.ocir.io/<registry>/<image>:<tag>@digest`


        :param image: The image of this OcirContainerJobEnvironmentConfigurationDetails.
        :type: str
        """
        self._image = image

    @property
    def cmd(self):
        """
        Gets the cmd of this OcirContainerJobEnvironmentConfigurationDetails.
        The container image run `CMD`__ as a list of strings.
        Use `CMD` as arguments to the `ENTRYPOINT` or the only command to run in the absence of an `ENTRYPOINT`.
        The combined size of `CMD` and `ENTRYPOINT` must be less than 2048 bytes.

        __ https://docs.docker.com/engine/reference/builder/#cmd


        :return: The cmd of this OcirContainerJobEnvironmentConfigurationDetails.
        :rtype: list[str]
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        """
        Sets the cmd of this OcirContainerJobEnvironmentConfigurationDetails.
        The container image run `CMD`__ as a list of strings.
        Use `CMD` as arguments to the `ENTRYPOINT` or the only command to run in the absence of an `ENTRYPOINT`.
        The combined size of `CMD` and `ENTRYPOINT` must be less than 2048 bytes.

        __ https://docs.docker.com/engine/reference/builder/#cmd


        :param cmd: The cmd of this OcirContainerJobEnvironmentConfigurationDetails.
        :type: list[str]
        """
        self._cmd = cmd

    @property
    def entrypoint(self):
        """
        Gets the entrypoint of this OcirContainerJobEnvironmentConfigurationDetails.
        The container image run `ENTRYPOINT`__ as a list of strings.
        Accept the `CMD` as extra arguments.
        The combined size of `CMD` and `ENTRYPOINT` must be less than 2048 bytes.
        More information on how `CMD` and `ENTRYPOINT` interact are `here`__.

        __ https://docs.docker.com/engine/reference/builder/#entrypoint
        __ https://docs.docker.com/engine/reference/builder/#understand-how-cmd-and-entrypoint-interact


        :return: The entrypoint of this OcirContainerJobEnvironmentConfigurationDetails.
        :rtype: list[str]
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """
        Sets the entrypoint of this OcirContainerJobEnvironmentConfigurationDetails.
        The container image run `ENTRYPOINT`__ as a list of strings.
        Accept the `CMD` as extra arguments.
        The combined size of `CMD` and `ENTRYPOINT` must be less than 2048 bytes.
        More information on how `CMD` and `ENTRYPOINT` interact are `here`__.

        __ https://docs.docker.com/engine/reference/builder/#entrypoint
        __ https://docs.docker.com/engine/reference/builder/#understand-how-cmd-and-entrypoint-interact


        :param entrypoint: The entrypoint of this OcirContainerJobEnvironmentConfigurationDetails.
        :type: list[str]
        """
        self._entrypoint = entrypoint

    @property
    def image_digest(self):
        """
        Gets the image_digest of this OcirContainerJobEnvironmentConfigurationDetails.
        The digest of the container image. For example,
        `sha256:881303a6b2738834d795a32b4a98eb0e5e3d1cad590a712d1e04f9b2fa90a030`


        :return: The image_digest of this OcirContainerJobEnvironmentConfigurationDetails.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        """
        Sets the image_digest of this OcirContainerJobEnvironmentConfigurationDetails.
        The digest of the container image. For example,
        `sha256:881303a6b2738834d795a32b4a98eb0e5e3d1cad590a712d1e04f9b2fa90a030`


        :param image_digest: The image_digest of this OcirContainerJobEnvironmentConfigurationDetails.
        :type: str
        """
        self._image_digest = image_digest

    @property
    def image_signature_id(self):
        """
        Gets the image_signature_id of this OcirContainerJobEnvironmentConfigurationDetails.
        OCID of the container image signature


        :return: The image_signature_id of this OcirContainerJobEnvironmentConfigurationDetails.
        :rtype: str
        """
        return self._image_signature_id

    @image_signature_id.setter
    def image_signature_id(self, image_signature_id):
        """
        Sets the image_signature_id of this OcirContainerJobEnvironmentConfigurationDetails.
        OCID of the container image signature


        :param image_signature_id: The image_signature_id of this OcirContainerJobEnvironmentConfigurationDetails.
        :type: str
        """
        self._image_signature_id = image_signature_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
