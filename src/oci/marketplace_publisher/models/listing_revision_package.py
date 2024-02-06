# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListingRevisionPackage(object):
    """
    A base object for all types of listing revision packages.
    """

    #: A constant which can be used with the package_type property of a ListingRevisionPackage.
    #: This constant has a value of "CONTAINER_IMAGE"
    PACKAGE_TYPE_CONTAINER_IMAGE = "CONTAINER_IMAGE"

    #: A constant which can be used with the package_type property of a ListingRevisionPackage.
    #: This constant has a value of "HELM_CHART"
    PACKAGE_TYPE_HELM_CHART = "HELM_CHART"

    #: A constant which can be used with the lifecycle_state property of a ListingRevisionPackage.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ListingRevisionPackage.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ListingRevisionPackage.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ListingRevisionPackage.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ListingRevisionPackage.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ListingRevisionPackage.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ListingRevisionPackage.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the status property of a ListingRevisionPackage.
    #: This constant has a value of "NEW"
    STATUS_NEW = "NEW"

    #: A constant which can be used with the status property of a ListingRevisionPackage.
    #: This constant has a value of "PUBLISH_IN_PROGRESS"
    STATUS_PUBLISH_IN_PROGRESS = "PUBLISH_IN_PROGRESS"

    #: A constant which can be used with the status property of a ListingRevisionPackage.
    #: This constant has a value of "UNPUBLISH_IN_PROGRESS"
    STATUS_UNPUBLISH_IN_PROGRESS = "UNPUBLISH_IN_PROGRESS"

    #: A constant which can be used with the status property of a ListingRevisionPackage.
    #: This constant has a value of "PUBLISH_FAILED"
    STATUS_PUBLISH_FAILED = "PUBLISH_FAILED"

    #: A constant which can be used with the status property of a ListingRevisionPackage.
    #: This constant has a value of "PUBLISHED"
    STATUS_PUBLISHED = "PUBLISHED"

    #: A constant which can be used with the status property of a ListingRevisionPackage.
    #: This constant has a value of "PUBLISHED_AS_PRIVATE"
    STATUS_PUBLISHED_AS_PRIVATE = "PUBLISHED_AS_PRIVATE"

    #: A constant which can be used with the status property of a ListingRevisionPackage.
    #: This constant has a value of "UNPUBLISHED"
    STATUS_UNPUBLISHED = "UNPUBLISHED"

    def __init__(self, **kwargs):
        """
        Initializes a new ListingRevisionPackage object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.marketplace_publisher.models.HelmChartPackage`
        * :class:`~oci.marketplace_publisher.models.ContainerPackage`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ListingRevisionPackage.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ListingRevisionPackage.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ListingRevisionPackage.
        :type description: str

        :param listing_revision_id:
            The value to assign to the listing_revision_id property of this ListingRevisionPackage.
        :type listing_revision_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ListingRevisionPackage.
        :type compartment_id: str

        :param artifact_id:
            The value to assign to the artifact_id property of this ListingRevisionPackage.
        :type artifact_id: str

        :param term_id:
            The value to assign to the term_id property of this ListingRevisionPackage.
        :type term_id: str

        :param package_version:
            The value to assign to the package_version property of this ListingRevisionPackage.
        :type package_version: str

        :param package_type:
            The value to assign to the package_type property of this ListingRevisionPackage.
            Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ListingRevisionPackage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param status:
            The value to assign to the status property of this ListingRevisionPackage.
            Allowed values for this property are: "NEW", "PUBLISH_IN_PROGRESS", "UNPUBLISH_IN_PROGRESS", "PUBLISH_FAILED", "PUBLISHED", "PUBLISHED_AS_PRIVATE", "UNPUBLISHED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param are_security_upgrades_provided:
            The value to assign to the are_security_upgrades_provided property of this ListingRevisionPackage.
        :type are_security_upgrades_provided: bool

        :param is_default:
            The value to assign to the is_default property of this ListingRevisionPackage.
        :type is_default: bool

        :param time_created:
            The value to assign to the time_created property of this ListingRevisionPackage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ListingRevisionPackage.
        :type time_updated: datetime

        :param extended_metadata:
            The value to assign to the extended_metadata property of this ListingRevisionPackage.
        :type extended_metadata: dict(str, str)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ListingRevisionPackage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ListingRevisionPackage.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ListingRevisionPackage.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'listing_revision_id': 'str',
            'compartment_id': 'str',
            'artifact_id': 'str',
            'term_id': 'str',
            'package_version': 'str',
            'package_type': 'str',
            'lifecycle_state': 'str',
            'status': 'str',
            'are_security_upgrades_provided': 'bool',
            'is_default': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'extended_metadata': 'dict(str, str)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'listing_revision_id': 'listingRevisionId',
            'compartment_id': 'compartmentId',
            'artifact_id': 'artifactId',
            'term_id': 'termId',
            'package_version': 'packageVersion',
            'package_type': 'packageType',
            'lifecycle_state': 'lifecycleState',
            'status': 'status',
            'are_security_upgrades_provided': 'areSecurityUpgradesProvided',
            'is_default': 'isDefault',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'extended_metadata': 'extendedMetadata',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._listing_revision_id = None
        self._compartment_id = None
        self._artifact_id = None
        self._term_id = None
        self._package_version = None
        self._package_type = None
        self._lifecycle_state = None
        self._status = None
        self._are_security_upgrades_provided = None
        self._is_default = None
        self._time_created = None
        self._time_updated = None
        self._extended_metadata = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['packageType']

        if type == 'HELM_CHART':
            return 'HelmChartPackage'

        if type == 'CONTAINER_IMAGE':
            return 'ContainerPackage'
        else:
            return 'ListingRevisionPackage'

    @property
    def id(self):
        """
        Gets the id of this ListingRevisionPackage.
        The OCID for the listing revision package in Marketplace Publisher.


        :return: The id of this ListingRevisionPackage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ListingRevisionPackage.
        The OCID for the listing revision package in Marketplace Publisher.


        :param id: The id of this ListingRevisionPackage.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ListingRevisionPackage.
        The name of the listing revision package.


        :return: The display_name of this ListingRevisionPackage.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ListingRevisionPackage.
        The name of the listing revision package.


        :param display_name: The display_name of this ListingRevisionPackage.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ListingRevisionPackage.
        The description of this package.


        :return: The description of this ListingRevisionPackage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ListingRevisionPackage.
        The description of this package.


        :param description: The description of this ListingRevisionPackage.
        :type: str
        """
        self._description = description

    @property
    def listing_revision_id(self):
        """
        **[Required]** Gets the listing_revision_id of this ListingRevisionPackage.
        The unique identifier for the listing revision.


        :return: The listing_revision_id of this ListingRevisionPackage.
        :rtype: str
        """
        return self._listing_revision_id

    @listing_revision_id.setter
    def listing_revision_id(self, listing_revision_id):
        """
        Sets the listing_revision_id of this ListingRevisionPackage.
        The unique identifier for the listing revision.


        :param listing_revision_id: The listing_revision_id of this ListingRevisionPackage.
        :type: str
        """
        self._listing_revision_id = listing_revision_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ListingRevisionPackage.
        The unique identifier for the compartment.


        :return: The compartment_id of this ListingRevisionPackage.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ListingRevisionPackage.
        The unique identifier for the compartment.


        :param compartment_id: The compartment_id of this ListingRevisionPackage.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def artifact_id(self):
        """
        **[Required]** Gets the artifact_id of this ListingRevisionPackage.
        The unique identifier for the artifact.


        :return: The artifact_id of this ListingRevisionPackage.
        :rtype: str
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """
        Sets the artifact_id of this ListingRevisionPackage.
        The unique identifier for the artifact.


        :param artifact_id: The artifact_id of this ListingRevisionPackage.
        :type: str
        """
        self._artifact_id = artifact_id

    @property
    def term_id(self):
        """
        **[Required]** Gets the term_id of this ListingRevisionPackage.
        The unique identifier for the term.


        :return: The term_id of this ListingRevisionPackage.
        :rtype: str
        """
        return self._term_id

    @term_id.setter
    def term_id(self, term_id):
        """
        Sets the term_id of this ListingRevisionPackage.
        The unique identifier for the term.


        :param term_id: The term_id of this ListingRevisionPackage.
        :type: str
        """
        self._term_id = term_id

    @property
    def package_version(self):
        """
        **[Required]** Gets the package_version of this ListingRevisionPackage.
        The version for the package.


        :return: The package_version of this ListingRevisionPackage.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this ListingRevisionPackage.
        The version for the package.


        :param package_version: The package_version of this ListingRevisionPackage.
        :type: str
        """
        self._package_version = package_version

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this ListingRevisionPackage.
        The package type for the listing.

        Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this ListingRevisionPackage.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this ListingRevisionPackage.
        The package type for the listing.


        :param package_type: The package_type of this ListingRevisionPackage.
        :type: str
        """
        allowed_values = ["CONTAINER_IMAGE", "HELM_CHART"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ListingRevisionPackage.
        The current state for the listing revision package.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ListingRevisionPackage.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ListingRevisionPackage.
        The current state for the listing revision package.


        :param lifecycle_state: The lifecycle_state of this ListingRevisionPackage.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ListingRevisionPackage.
        The current status for the listing revision package.

        Allowed values for this property are: "NEW", "PUBLISH_IN_PROGRESS", "UNPUBLISH_IN_PROGRESS", "PUBLISH_FAILED", "PUBLISHED", "PUBLISHED_AS_PRIVATE", "UNPUBLISHED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ListingRevisionPackage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ListingRevisionPackage.
        The current status for the listing revision package.


        :param status: The status of this ListingRevisionPackage.
        :type: str
        """
        allowed_values = ["NEW", "PUBLISH_IN_PROGRESS", "UNPUBLISH_IN_PROGRESS", "PUBLISH_FAILED", "PUBLISHED", "PUBLISHED_AS_PRIVATE", "UNPUBLISHED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def are_security_upgrades_provided(self):
        """
        **[Required]** Gets the are_security_upgrades_provided of this ListingRevisionPackage.
        Identifies whether security upgrades will be provided for this package.


        :return: The are_security_upgrades_provided of this ListingRevisionPackage.
        :rtype: bool
        """
        return self._are_security_upgrades_provided

    @are_security_upgrades_provided.setter
    def are_security_upgrades_provided(self, are_security_upgrades_provided):
        """
        Sets the are_security_upgrades_provided of this ListingRevisionPackage.
        Identifies whether security upgrades will be provided for this package.


        :param are_security_upgrades_provided: The are_security_upgrades_provided of this ListingRevisionPackage.
        :type: bool
        """
        self._are_security_upgrades_provided = are_security_upgrades_provided

    @property
    def is_default(self):
        """
        **[Required]** Gets the is_default of this ListingRevisionPackage.
        Identifies that this will be default package for the listing revision.


        :return: The is_default of this ListingRevisionPackage.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this ListingRevisionPackage.
        Identifies that this will be default package for the listing revision.


        :param is_default: The is_default of this ListingRevisionPackage.
        :type: bool
        """
        self._is_default = is_default

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ListingRevisionPackage.
        The date and time this listing revision package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ListingRevisionPackage.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ListingRevisionPackage.
        The date and time this listing revision package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ListingRevisionPackage.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ListingRevisionPackage.
        The date and time this listing revision package was updated, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ListingRevisionPackage.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ListingRevisionPackage.
        The date and time this listing revision package was updated, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ListingRevisionPackage.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def extended_metadata(self):
        """
        Gets the extended_metadata of this ListingRevisionPackage.
        Additional metadata key/value pairs for the listing revision package summary.

        For example:

        `{\"partnerListingRevisionPackageStatus\": \"Published\",\"parentListingRevisionPackageId\": \"1\" }`


        :return: The extended_metadata of this ListingRevisionPackage.
        :rtype: dict(str, str)
        """
        return self._extended_metadata

    @extended_metadata.setter
    def extended_metadata(self, extended_metadata):
        """
        Sets the extended_metadata of this ListingRevisionPackage.
        Additional metadata key/value pairs for the listing revision package summary.

        For example:

        `{\"partnerListingRevisionPackageStatus\": \"Published\",\"parentListingRevisionPackageId\": \"1\" }`


        :param extended_metadata: The extended_metadata of this ListingRevisionPackage.
        :type: dict(str, str)
        """
        self._extended_metadata = extended_metadata

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ListingRevisionPackage.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ListingRevisionPackage.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ListingRevisionPackage.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ListingRevisionPackage.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ListingRevisionPackage.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ListingRevisionPackage.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ListingRevisionPackage.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ListingRevisionPackage.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ListingRevisionPackage.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ListingRevisionPackage.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ListingRevisionPackage.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ListingRevisionPackage.
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