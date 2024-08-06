# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .software_source import SoftwareSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomSoftwareSource(SoftwareSource):
    """
    The object that defines a custom software source. A software source contains a collection of packages. For more information, see `Managing Software Sources`__.

    __ https://docs.cloud.oracle.com/iaas/osmh/doc/software-sources.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomSoftwareSource object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.CustomSoftwareSource.software_source_type` attribute
        of this class is ``CUSTOM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CustomSoftwareSource.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CustomSoftwareSource.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CustomSoftwareSource.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this CustomSoftwareSource.
        :type time_created: datetime

        :param description:
            The value to assign to the description property of this CustomSoftwareSource.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this CustomSoftwareSource.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED"
        :type software_source_type: str

        :param availability:
            The value to assign to the availability property of this CustomSoftwareSource.
            Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"
        :type availability: str

        :param availability_at_oci:
            The value to assign to the availability_at_oci property of this CustomSoftwareSource.
            Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"
        :type availability_at_oci: str

        :param repo_id:
            The value to assign to the repo_id property of this CustomSoftwareSource.
        :type repo_id: str

        :param os_family:
            The value to assign to the os_family property of this CustomSoftwareSource.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this CustomSoftwareSource.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"
        :type arch_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CustomSoftwareSource.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param package_count:
            The value to assign to the package_count property of this CustomSoftwareSource.
        :type package_count: int

        :param url:
            The value to assign to the url property of this CustomSoftwareSource.
        :type url: str

        :param checksum_type:
            The value to assign to the checksum_type property of this CustomSoftwareSource.
            Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512"
        :type checksum_type: str

        :param gpg_key_url:
            The value to assign to the gpg_key_url property of this CustomSoftwareSource.
        :type gpg_key_url: str

        :param gpg_key_id:
            The value to assign to the gpg_key_id property of this CustomSoftwareSource.
        :type gpg_key_id: str

        :param gpg_key_fingerprint:
            The value to assign to the gpg_key_fingerprint property of this CustomSoftwareSource.
        :type gpg_key_fingerprint: str

        :param size:
            The value to assign to the size property of this CustomSoftwareSource.
        :type size: float

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CustomSoftwareSource.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CustomSoftwareSource.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CustomSoftwareSource.
        :type system_tags: dict(str, dict(str, object))

        :param vendor_software_sources:
            The value to assign to the vendor_software_sources property of this CustomSoftwareSource.
        :type vendor_software_sources: list[oci.os_management_hub.models.Id]

        :param custom_software_source_filter:
            The value to assign to the custom_software_source_filter property of this CustomSoftwareSource.
        :type custom_software_source_filter: oci.os_management_hub.models.CustomSoftwareSourceFilter

        :param is_automatically_updated:
            The value to assign to the is_automatically_updated property of this CustomSoftwareSource.
        :type is_automatically_updated: bool

        :param is_auto_resolve_dependencies:
            The value to assign to the is_auto_resolve_dependencies property of this CustomSoftwareSource.
        :type is_auto_resolve_dependencies: bool

        :param is_created_from_package_list:
            The value to assign to the is_created_from_package_list property of this CustomSoftwareSource.
        :type is_created_from_package_list: bool

        :param is_latest_content_only:
            The value to assign to the is_latest_content_only property of this CustomSoftwareSource.
        :type is_latest_content_only: bool

        :param packages:
            The value to assign to the packages property of this CustomSoftwareSource.
        :type packages: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'description': 'str',
            'software_source_type': 'str',
            'availability': 'str',
            'availability_at_oci': 'str',
            'repo_id': 'str',
            'os_family': 'str',
            'arch_type': 'str',
            'lifecycle_state': 'str',
            'package_count': 'int',
            'url': 'str',
            'checksum_type': 'str',
            'gpg_key_url': 'str',
            'gpg_key_id': 'str',
            'gpg_key_fingerprint': 'str',
            'size': 'float',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'vendor_software_sources': 'list[Id]',
            'custom_software_source_filter': 'CustomSoftwareSourceFilter',
            'is_automatically_updated': 'bool',
            'is_auto_resolve_dependencies': 'bool',
            'is_created_from_package_list': 'bool',
            'is_latest_content_only': 'bool',
            'packages': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'description': 'description',
            'software_source_type': 'softwareSourceType',
            'availability': 'availability',
            'availability_at_oci': 'availabilityAtOci',
            'repo_id': 'repoId',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'lifecycle_state': 'lifecycleState',
            'package_count': 'packageCount',
            'url': 'url',
            'checksum_type': 'checksumType',
            'gpg_key_url': 'gpgKeyUrl',
            'gpg_key_id': 'gpgKeyId',
            'gpg_key_fingerprint': 'gpgKeyFingerprint',
            'size': 'size',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'vendor_software_sources': 'vendorSoftwareSources',
            'custom_software_source_filter': 'customSoftwareSourceFilter',
            'is_automatically_updated': 'isAutomaticallyUpdated',
            'is_auto_resolve_dependencies': 'isAutoResolveDependencies',
            'is_created_from_package_list': 'isCreatedFromPackageList',
            'is_latest_content_only': 'isLatestContentOnly',
            'packages': 'packages'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._description = None
        self._software_source_type = None
        self._availability = None
        self._availability_at_oci = None
        self._repo_id = None
        self._os_family = None
        self._arch_type = None
        self._lifecycle_state = None
        self._package_count = None
        self._url = None
        self._checksum_type = None
        self._gpg_key_url = None
        self._gpg_key_id = None
        self._gpg_key_fingerprint = None
        self._size = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._vendor_software_sources = None
        self._custom_software_source_filter = None
        self._is_automatically_updated = None
        self._is_auto_resolve_dependencies = None
        self._is_created_from_package_list = None
        self._is_latest_content_only = None
        self._packages = None
        self._software_source_type = 'CUSTOM'

    @property
    def vendor_software_sources(self):
        """
        **[Required]** Gets the vendor_software_sources of this CustomSoftwareSource.
        List of vendor software sources that are used for the basis of the custom software source.


        :return: The vendor_software_sources of this CustomSoftwareSource.
        :rtype: list[oci.os_management_hub.models.Id]
        """
        return self._vendor_software_sources

    @vendor_software_sources.setter
    def vendor_software_sources(self, vendor_software_sources):
        """
        Sets the vendor_software_sources of this CustomSoftwareSource.
        List of vendor software sources that are used for the basis of the custom software source.


        :param vendor_software_sources: The vendor_software_sources of this CustomSoftwareSource.
        :type: list[oci.os_management_hub.models.Id]
        """
        self._vendor_software_sources = vendor_software_sources

    @property
    def custom_software_source_filter(self):
        """
        Gets the custom_software_source_filter of this CustomSoftwareSource.

        :return: The custom_software_source_filter of this CustomSoftwareSource.
        :rtype: oci.os_management_hub.models.CustomSoftwareSourceFilter
        """
        return self._custom_software_source_filter

    @custom_software_source_filter.setter
    def custom_software_source_filter(self, custom_software_source_filter):
        """
        Sets the custom_software_source_filter of this CustomSoftwareSource.

        :param custom_software_source_filter: The custom_software_source_filter of this CustomSoftwareSource.
        :type: oci.os_management_hub.models.CustomSoftwareSourceFilter
        """
        self._custom_software_source_filter = custom_software_source_filter

    @property
    def is_automatically_updated(self):
        """
        Gets the is_automatically_updated of this CustomSoftwareSource.
        Indicates whether the service should automatically update the custom software source to use the latest package versions available. The service reviews packages levels once a day.


        :return: The is_automatically_updated of this CustomSoftwareSource.
        :rtype: bool
        """
        return self._is_automatically_updated

    @is_automatically_updated.setter
    def is_automatically_updated(self, is_automatically_updated):
        """
        Sets the is_automatically_updated of this CustomSoftwareSource.
        Indicates whether the service should automatically update the custom software source to use the latest package versions available. The service reviews packages levels once a day.


        :param is_automatically_updated: The is_automatically_updated of this CustomSoftwareSource.
        :type: bool
        """
        self._is_automatically_updated = is_automatically_updated

    @property
    def is_auto_resolve_dependencies(self):
        """
        Gets the is_auto_resolve_dependencies of this CustomSoftwareSource.
        Indicates whether the service should automatically resolve package dependencies when including specific packages in the software source.


        :return: The is_auto_resolve_dependencies of this CustomSoftwareSource.
        :rtype: bool
        """
        return self._is_auto_resolve_dependencies

    @is_auto_resolve_dependencies.setter
    def is_auto_resolve_dependencies(self, is_auto_resolve_dependencies):
        """
        Sets the is_auto_resolve_dependencies of this CustomSoftwareSource.
        Indicates whether the service should automatically resolve package dependencies when including specific packages in the software source.


        :param is_auto_resolve_dependencies: The is_auto_resolve_dependencies of this CustomSoftwareSource.
        :type: bool
        """
        self._is_auto_resolve_dependencies = is_auto_resolve_dependencies

    @property
    def is_created_from_package_list(self):
        """
        Gets the is_created_from_package_list of this CustomSoftwareSource.
        Indicates whether the service should create the software source from a list of packages provided by the user.


        :return: The is_created_from_package_list of this CustomSoftwareSource.
        :rtype: bool
        """
        return self._is_created_from_package_list

    @is_created_from_package_list.setter
    def is_created_from_package_list(self, is_created_from_package_list):
        """
        Sets the is_created_from_package_list of this CustomSoftwareSource.
        Indicates whether the service should create the software source from a list of packages provided by the user.


        :param is_created_from_package_list: The is_created_from_package_list of this CustomSoftwareSource.
        :type: bool
        """
        self._is_created_from_package_list = is_created_from_package_list

    @property
    def is_latest_content_only(self):
        """
        Gets the is_latest_content_only of this CustomSoftwareSource.
        Indicates whether the software source will include only the latest versions of content from vendor software sources, while accounting for other constraints set in the custom or versioned custom software source (such as a package list or filters).
        * For a module filter that does not specify a stream, this will include all available streams, and within each stream only the latest version of packages.
        * For a module filter that does specify a stream, this will include only the latest version of packages for the specified stream.
        * For a package filter that does not specify a version, this will include only the latest available version of the package.
        * For a package filter that does specify a version, this will include only the specified version of the package (the isLatestContentOnly attribute is ignored).
        * For a package list, this will include only the specified version of packages and modules in the list (the isLatestContentOnly attribute is ignored).


        :return: The is_latest_content_only of this CustomSoftwareSource.
        :rtype: bool
        """
        return self._is_latest_content_only

    @is_latest_content_only.setter
    def is_latest_content_only(self, is_latest_content_only):
        """
        Sets the is_latest_content_only of this CustomSoftwareSource.
        Indicates whether the software source will include only the latest versions of content from vendor software sources, while accounting for other constraints set in the custom or versioned custom software source (such as a package list or filters).
        * For a module filter that does not specify a stream, this will include all available streams, and within each stream only the latest version of packages.
        * For a module filter that does specify a stream, this will include only the latest version of packages for the specified stream.
        * For a package filter that does not specify a version, this will include only the latest available version of the package.
        * For a package filter that does specify a version, this will include only the specified version of the package (the isLatestContentOnly attribute is ignored).
        * For a package list, this will include only the specified version of packages and modules in the list (the isLatestContentOnly attribute is ignored).


        :param is_latest_content_only: The is_latest_content_only of this CustomSoftwareSource.
        :type: bool
        """
        self._is_latest_content_only = is_latest_content_only

    @property
    def packages(self):
        """
        Gets the packages of this CustomSoftwareSource.
        The packages in the software source.


        :return: The packages of this CustomSoftwareSource.
        :rtype: list[str]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """
        Sets the packages of this CustomSoftwareSource.
        The packages in the software source.


        :param packages: The packages of this CustomSoftwareSource.
        :type: list[str]
        """
        self._packages = packages

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
