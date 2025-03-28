# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .update_software_source_details import UpdateSoftwareSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePrivateSoftwareSourceDetails(UpdateSoftwareSourceDetails):
    """
    Provides the information used to update a private software source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePrivateSoftwareSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.UpdatePrivateSoftwareSourceDetails.software_source_type` attribute
        of this class is ``PRIVATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this UpdatePrivateSoftwareSourceDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this UpdatePrivateSoftwareSourceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdatePrivateSoftwareSourceDetails.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this UpdatePrivateSoftwareSourceDetails.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED", "PRIVATE", "THIRD_PARTY"
        :type software_source_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdatePrivateSoftwareSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdatePrivateSoftwareSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param url:
            The value to assign to the url property of this UpdatePrivateSoftwareSourceDetails.
        :type url: str

        :param gpg_key_url:
            The value to assign to the gpg_key_url property of this UpdatePrivateSoftwareSourceDetails.
        :type gpg_key_url: str

        :param is_gpg_check_enabled:
            The value to assign to the is_gpg_check_enabled property of this UpdatePrivateSoftwareSourceDetails.
        :type is_gpg_check_enabled: bool

        :param is_ssl_verify_enabled:
            The value to assign to the is_ssl_verify_enabled property of this UpdatePrivateSoftwareSourceDetails.
        :type is_ssl_verify_enabled: bool

        :param advanced_repo_options:
            The value to assign to the advanced_repo_options property of this UpdatePrivateSoftwareSourceDetails.
        :type advanced_repo_options: str

        :param is_mirror_sync_allowed:
            The value to assign to the is_mirror_sync_allowed property of this UpdatePrivateSoftwareSourceDetails.
        :type is_mirror_sync_allowed: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'software_source_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'url': 'str',
            'gpg_key_url': 'str',
            'is_gpg_check_enabled': 'bool',
            'is_ssl_verify_enabled': 'bool',
            'advanced_repo_options': 'str',
            'is_mirror_sync_allowed': 'bool'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'software_source_type': 'softwareSourceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'url': 'url',
            'gpg_key_url': 'gpgKeyUrl',
            'is_gpg_check_enabled': 'isGpgCheckEnabled',
            'is_ssl_verify_enabled': 'isSslVerifyEnabled',
            'advanced_repo_options': 'advancedRepoOptions',
            'is_mirror_sync_allowed': 'isMirrorSyncAllowed'
        }
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._software_source_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._url = None
        self._gpg_key_url = None
        self._is_gpg_check_enabled = None
        self._is_ssl_verify_enabled = None
        self._advanced_repo_options = None
        self._is_mirror_sync_allowed = None
        self._software_source_type = 'PRIVATE'

    @property
    def url(self):
        """
        Gets the url of this UpdatePrivateSoftwareSourceDetails.
        URL for the private software source.


        :return: The url of this UpdatePrivateSoftwareSourceDetails.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this UpdatePrivateSoftwareSourceDetails.
        URL for the private software source.


        :param url: The url of this UpdatePrivateSoftwareSourceDetails.
        :type: str
        """
        self._url = url

    @property
    def gpg_key_url(self):
        """
        Gets the gpg_key_url of this UpdatePrivateSoftwareSourceDetails.
        URI of the GPG key for this software source.


        :return: The gpg_key_url of this UpdatePrivateSoftwareSourceDetails.
        :rtype: str
        """
        return self._gpg_key_url

    @gpg_key_url.setter
    def gpg_key_url(self, gpg_key_url):
        """
        Sets the gpg_key_url of this UpdatePrivateSoftwareSourceDetails.
        URI of the GPG key for this software source.


        :param gpg_key_url: The gpg_key_url of this UpdatePrivateSoftwareSourceDetails.
        :type: str
        """
        self._gpg_key_url = gpg_key_url

    @property
    def is_gpg_check_enabled(self):
        """
        Gets the is_gpg_check_enabled of this UpdatePrivateSoftwareSourceDetails.
        Whether signature verification should be done for the software source.


        :return: The is_gpg_check_enabled of this UpdatePrivateSoftwareSourceDetails.
        :rtype: bool
        """
        return self._is_gpg_check_enabled

    @is_gpg_check_enabled.setter
    def is_gpg_check_enabled(self, is_gpg_check_enabled):
        """
        Sets the is_gpg_check_enabled of this UpdatePrivateSoftwareSourceDetails.
        Whether signature verification should be done for the software source.


        :param is_gpg_check_enabled: The is_gpg_check_enabled of this UpdatePrivateSoftwareSourceDetails.
        :type: bool
        """
        self._is_gpg_check_enabled = is_gpg_check_enabled

    @property
    def is_ssl_verify_enabled(self):
        """
        Gets the is_ssl_verify_enabled of this UpdatePrivateSoftwareSourceDetails.
        Whether SSL validation needs to be turned on


        :return: The is_ssl_verify_enabled of this UpdatePrivateSoftwareSourceDetails.
        :rtype: bool
        """
        return self._is_ssl_verify_enabled

    @is_ssl_verify_enabled.setter
    def is_ssl_verify_enabled(self, is_ssl_verify_enabled):
        """
        Sets the is_ssl_verify_enabled of this UpdatePrivateSoftwareSourceDetails.
        Whether SSL validation needs to be turned on


        :param is_ssl_verify_enabled: The is_ssl_verify_enabled of this UpdatePrivateSoftwareSourceDetails.
        :type: bool
        """
        self._is_ssl_verify_enabled = is_ssl_verify_enabled

    @property
    def advanced_repo_options(self):
        """
        Gets the advanced_repo_options of this UpdatePrivateSoftwareSourceDetails.
        Advanced repository options for the software source


        :return: The advanced_repo_options of this UpdatePrivateSoftwareSourceDetails.
        :rtype: str
        """
        return self._advanced_repo_options

    @advanced_repo_options.setter
    def advanced_repo_options(self, advanced_repo_options):
        """
        Sets the advanced_repo_options of this UpdatePrivateSoftwareSourceDetails.
        Advanced repository options for the software source


        :param advanced_repo_options: The advanced_repo_options of this UpdatePrivateSoftwareSourceDetails.
        :type: str
        """
        self._advanced_repo_options = advanced_repo_options

    @property
    def is_mirror_sync_allowed(self):
        """
        Gets the is_mirror_sync_allowed of this UpdatePrivateSoftwareSourceDetails.
        Whether this software source can be synced to a management station


        :return: The is_mirror_sync_allowed of this UpdatePrivateSoftwareSourceDetails.
        :rtype: bool
        """
        return self._is_mirror_sync_allowed

    @is_mirror_sync_allowed.setter
    def is_mirror_sync_allowed(self, is_mirror_sync_allowed):
        """
        Sets the is_mirror_sync_allowed of this UpdatePrivateSoftwareSourceDetails.
        Whether this software source can be synced to a management station


        :param is_mirror_sync_allowed: The is_mirror_sync_allowed of this UpdatePrivateSoftwareSourceDetails.
        :type: bool
        """
        self._is_mirror_sync_allowed = is_mirror_sync_allowed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
