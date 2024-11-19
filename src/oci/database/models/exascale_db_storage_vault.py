# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExascaleDbStorageVault(object):
    """
    Details of the Exadata Database Storage Vault.
    """

    #: A constant which can be used with the lifecycle_state property of a ExascaleDbStorageVault.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a ExascaleDbStorageVault.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a ExascaleDbStorageVault.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExascaleDbStorageVault.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a ExascaleDbStorageVault.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a ExascaleDbStorageVault.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ExascaleDbStorageVault object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExascaleDbStorageVault.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExascaleDbStorageVault.
        :type compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this ExascaleDbStorageVault.
        :type availability_domain: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExascaleDbStorageVault.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this ExascaleDbStorageVault.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ExascaleDbStorageVault.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this ExascaleDbStorageVault.
        :type time_created: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExascaleDbStorageVault.
        :type lifecycle_details: str

        :param time_zone:
            The value to assign to the time_zone property of this ExascaleDbStorageVault.
        :type time_zone: str

        :param vm_cluster_ids:
            The value to assign to the vm_cluster_ids property of this ExascaleDbStorageVault.
        :type vm_cluster_ids: list[str]

        :param vm_cluster_count:
            The value to assign to the vm_cluster_count property of this ExascaleDbStorageVault.
        :type vm_cluster_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExascaleDbStorageVault.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ExascaleDbStorageVault.
        :type defined_tags: dict(str, dict(str, object))

        :param exadata_infrastructure_id:
            The value to assign to the exadata_infrastructure_id property of this ExascaleDbStorageVault.
        :type exadata_infrastructure_id: str

        :param system_tags:
            The value to assign to the system_tags property of this ExascaleDbStorageVault.
        :type system_tags: dict(str, dict(str, object))

        :param high_capacity_database_storage:
            The value to assign to the high_capacity_database_storage property of this ExascaleDbStorageVault.
        :type high_capacity_database_storage: oci.database.models.ExascaleDbStorageDetails

        :param additional_flash_cache_in_percent:
            The value to assign to the additional_flash_cache_in_percent property of this ExascaleDbStorageVault.
        :type additional_flash_cache_in_percent: int

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'availability_domain': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_details': 'str',
            'time_zone': 'str',
            'vm_cluster_ids': 'list[str]',
            'vm_cluster_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'exadata_infrastructure_id': 'str',
            'system_tags': 'dict(str, dict(str, object))',
            'high_capacity_database_storage': 'ExascaleDbStorageDetails',
            'additional_flash_cache_in_percent': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'availability_domain': 'availabilityDomain',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_details': 'lifecycleDetails',
            'time_zone': 'timeZone',
            'vm_cluster_ids': 'vmClusterIds',
            'vm_cluster_count': 'vmClusterCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'exadata_infrastructure_id': 'exadataInfrastructureId',
            'system_tags': 'systemTags',
            'high_capacity_database_storage': 'highCapacityDatabaseStorage',
            'additional_flash_cache_in_percent': 'additionalFlashCacheInPercent'
        }

        self._id = None
        self._compartment_id = None
        self._availability_domain = None
        self._lifecycle_state = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._lifecycle_details = None
        self._time_zone = None
        self._vm_cluster_ids = None
        self._vm_cluster_count = None
        self._freeform_tags = None
        self._defined_tags = None
        self._exadata_infrastructure_id = None
        self._system_tags = None
        self._high_capacity_database_storage = None
        self._additional_flash_cache_in_percent = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExascaleDbStorageVault.
        The `OCID`__ of the Exadata Database Storage Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExascaleDbStorageVault.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExascaleDbStorageVault.
        The `OCID`__ of the Exadata Database Storage Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExascaleDbStorageVault.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExascaleDbStorageVault.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExascaleDbStorageVault.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExascaleDbStorageVault.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExascaleDbStorageVault.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ExascaleDbStorageVault.
        The name of the availability domain in which the Exadata Database Storage Vault is located.


        :return: The availability_domain of this ExascaleDbStorageVault.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ExascaleDbStorageVault.
        The name of the availability domain in which the Exadata Database Storage Vault is located.


        :param availability_domain: The availability_domain of this ExascaleDbStorageVault.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExascaleDbStorageVault.
        The current state of the Exadata Database Storage Vault.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExascaleDbStorageVault.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExascaleDbStorageVault.
        The current state of the Exadata Database Storage Vault.


        :param lifecycle_state: The lifecycle_state of this ExascaleDbStorageVault.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExascaleDbStorageVault.
        The user-friendly name for the Exadata Database Storage Vault. The name does not need to be unique.


        :return: The display_name of this ExascaleDbStorageVault.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExascaleDbStorageVault.
        The user-friendly name for the Exadata Database Storage Vault. The name does not need to be unique.


        :param display_name: The display_name of this ExascaleDbStorageVault.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ExascaleDbStorageVault.
        Exadata Database Storage Vault description.


        :return: The description of this ExascaleDbStorageVault.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExascaleDbStorageVault.
        Exadata Database Storage Vault description.


        :param description: The description of this ExascaleDbStorageVault.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this ExascaleDbStorageVault.
        The date and time that the Exadata Database Storage Vault was created.


        :return: The time_created of this ExascaleDbStorageVault.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExascaleDbStorageVault.
        The date and time that the Exadata Database Storage Vault was created.


        :param time_created: The time_created of this ExascaleDbStorageVault.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExascaleDbStorageVault.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExascaleDbStorageVault.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExascaleDbStorageVault.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExascaleDbStorageVault.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_zone(self):
        """
        Gets the time_zone of this ExascaleDbStorageVault.
        The time zone that you want to use for the Exadata Database Storage Vault. For details, see `Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this ExascaleDbStorageVault.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this ExascaleDbStorageVault.
        The time zone that you want to use for the Exadata Database Storage Vault. For details, see `Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this ExascaleDbStorageVault.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def vm_cluster_ids(self):
        """
        Gets the vm_cluster_ids of this ExascaleDbStorageVault.
        The List of Exadata VM cluster on Exascale Infrastructure `OCIDs`__
        **Note:** If Exadata Database Storage Vault is not used for any Exadata VM cluster on Exascale Infrastructure, this list is empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vm_cluster_ids of this ExascaleDbStorageVault.
        :rtype: list[str]
        """
        return self._vm_cluster_ids

    @vm_cluster_ids.setter
    def vm_cluster_ids(self, vm_cluster_ids):
        """
        Sets the vm_cluster_ids of this ExascaleDbStorageVault.
        The List of Exadata VM cluster on Exascale Infrastructure `OCIDs`__
        **Note:** If Exadata Database Storage Vault is not used for any Exadata VM cluster on Exascale Infrastructure, this list is empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vm_cluster_ids: The vm_cluster_ids of this ExascaleDbStorageVault.
        :type: list[str]
        """
        self._vm_cluster_ids = vm_cluster_ids

    @property
    def vm_cluster_count(self):
        """
        Gets the vm_cluster_count of this ExascaleDbStorageVault.
        The number of Exadata VM clusters used the Exadata Database Storage Vault.


        :return: The vm_cluster_count of this ExascaleDbStorageVault.
        :rtype: int
        """
        return self._vm_cluster_count

    @vm_cluster_count.setter
    def vm_cluster_count(self, vm_cluster_count):
        """
        Sets the vm_cluster_count of this ExascaleDbStorageVault.
        The number of Exadata VM clusters used the Exadata Database Storage Vault.


        :param vm_cluster_count: The vm_cluster_count of this ExascaleDbStorageVault.
        :type: int
        """
        self._vm_cluster_count = vm_cluster_count

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ExascaleDbStorageVault.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ExascaleDbStorageVault.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExascaleDbStorageVault.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ExascaleDbStorageVault.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ExascaleDbStorageVault.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ExascaleDbStorageVault.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExascaleDbStorageVault.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ExascaleDbStorageVault.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def exadata_infrastructure_id(self):
        """
        Gets the exadata_infrastructure_id of this ExascaleDbStorageVault.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The exadata_infrastructure_id of this ExascaleDbStorageVault.
        :rtype: str
        """
        return self._exadata_infrastructure_id

    @exadata_infrastructure_id.setter
    def exadata_infrastructure_id(self, exadata_infrastructure_id):
        """
        Sets the exadata_infrastructure_id of this ExascaleDbStorageVault.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param exadata_infrastructure_id: The exadata_infrastructure_id of this ExascaleDbStorageVault.
        :type: str
        """
        self._exadata_infrastructure_id = exadata_infrastructure_id

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ExascaleDbStorageVault.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ExascaleDbStorageVault.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ExascaleDbStorageVault.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ExascaleDbStorageVault.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def high_capacity_database_storage(self):
        """
        **[Required]** Gets the high_capacity_database_storage of this ExascaleDbStorageVault.

        :return: The high_capacity_database_storage of this ExascaleDbStorageVault.
        :rtype: oci.database.models.ExascaleDbStorageDetails
        """
        return self._high_capacity_database_storage

    @high_capacity_database_storage.setter
    def high_capacity_database_storage(self, high_capacity_database_storage):
        """
        Sets the high_capacity_database_storage of this ExascaleDbStorageVault.

        :param high_capacity_database_storage: The high_capacity_database_storage of this ExascaleDbStorageVault.
        :type: oci.database.models.ExascaleDbStorageDetails
        """
        self._high_capacity_database_storage = high_capacity_database_storage

    @property
    def additional_flash_cache_in_percent(self):
        """
        Gets the additional_flash_cache_in_percent of this ExascaleDbStorageVault.
        The size of additional Flash Cache in percentage of High Capacity database storage.


        :return: The additional_flash_cache_in_percent of this ExascaleDbStorageVault.
        :rtype: int
        """
        return self._additional_flash_cache_in_percent

    @additional_flash_cache_in_percent.setter
    def additional_flash_cache_in_percent(self, additional_flash_cache_in_percent):
        """
        Sets the additional_flash_cache_in_percent of this ExascaleDbStorageVault.
        The size of additional Flash Cache in percentage of High Capacity database storage.


        :param additional_flash_cache_in_percent: The additional_flash_cache_in_percent of this ExascaleDbStorageVault.
        :type: int
        """
        self._additional_flash_cache_in_percent = additional_flash_cache_in_percent

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
