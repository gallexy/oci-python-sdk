# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMonitoredResourceTypeDetails(object):
    """
    The information about new monitored resource type. The resource type name should be unique across tenancy.
    A set of resource types are created by the service by default. These resource types are available
    for all tenancies. Service provided resource types can not be duplicated or overwritten in any tenancy.
    """

    #: A constant which can be used with the source_type property of a CreateMonitoredResourceTypeDetails.
    #: This constant has a value of "SM_MGMT_AGENT_MONITORED"
    SOURCE_TYPE_SM_MGMT_AGENT_MONITORED = "SM_MGMT_AGENT_MONITORED"

    #: A constant which can be used with the source_type property of a CreateMonitoredResourceTypeDetails.
    #: This constant has a value of "SM_REPO_ONLY"
    SOURCE_TYPE_SM_REPO_ONLY = "SM_REPO_ONLY"

    #: A constant which can be used with the source_type property of a CreateMonitoredResourceTypeDetails.
    #: This constant has a value of "OCI_NATIVE"
    SOURCE_TYPE_OCI_NATIVE = "OCI_NATIVE"

    #: A constant which can be used with the source_type property of a CreateMonitoredResourceTypeDetails.
    #: This constant has a value of "PROMETHEUS"
    SOURCE_TYPE_PROMETHEUS = "PROMETHEUS"

    #: A constant which can be used with the source_type property of a CreateMonitoredResourceTypeDetails.
    #: This constant has a value of "TELEGRAF"
    SOURCE_TYPE_TELEGRAF = "TELEGRAF"

    #: A constant which can be used with the source_type property of a CreateMonitoredResourceTypeDetails.
    #: This constant has a value of "COLLECTD"
    SOURCE_TYPE_COLLECTD = "COLLECTD"

    #: A constant which can be used with the resource_category property of a CreateMonitoredResourceTypeDetails.
    #: This constant has a value of "APPLICATION"
    RESOURCE_CATEGORY_APPLICATION = "APPLICATION"

    #: A constant which can be used with the resource_category property of a CreateMonitoredResourceTypeDetails.
    #: This constant has a value of "DATABASE"
    RESOURCE_CATEGORY_DATABASE = "DATABASE"

    #: A constant which can be used with the resource_category property of a CreateMonitoredResourceTypeDetails.
    #: This constant has a value of "MIDDLEWARE"
    RESOURCE_CATEGORY_MIDDLEWARE = "MIDDLEWARE"

    #: A constant which can be used with the resource_category property of a CreateMonitoredResourceTypeDetails.
    #: This constant has a value of "INFRASTRUCTURE"
    RESOURCE_CATEGORY_INFRASTRUCTURE = "INFRASTRUCTURE"

    #: A constant which can be used with the resource_category property of a CreateMonitoredResourceTypeDetails.
    #: This constant has a value of "UNKNOWN"
    RESOURCE_CATEGORY_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMonitoredResourceTypeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateMonitoredResourceTypeDetails.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this CreateMonitoredResourceTypeDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateMonitoredResourceTypeDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMonitoredResourceTypeDetails.
        :type compartment_id: str

        :param metric_namespace:
            The value to assign to the metric_namespace property of this CreateMonitoredResourceTypeDetails.
        :type metric_namespace: str

        :param source_type:
            The value to assign to the source_type property of this CreateMonitoredResourceTypeDetails.
            Allowed values for this property are: "SM_MGMT_AGENT_MONITORED", "SM_REPO_ONLY", "OCI_NATIVE", "PROMETHEUS", "TELEGRAF", "COLLECTD"
        :type source_type: str

        :param resource_category:
            The value to assign to the resource_category property of this CreateMonitoredResourceTypeDetails.
            Allowed values for this property are: "APPLICATION", "DATABASE", "MIDDLEWARE", "INFRASTRUCTURE", "UNKNOWN"
        :type resource_category: str

        :param metadata:
            The value to assign to the metadata property of this CreateMonitoredResourceTypeDetails.
        :type metadata: oci.stack_monitoring.models.ResourceTypeMetadataDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMonitoredResourceTypeDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMonitoredResourceTypeDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'metric_namespace': 'str',
            'source_type': 'str',
            'resource_category': 'str',
            'metadata': 'ResourceTypeMetadataDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'metric_namespace': 'metricNamespace',
            'source_type': 'sourceType',
            'resource_category': 'resourceCategory',
            'metadata': 'metadata',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._name = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._metric_namespace = None
        self._source_type = None
        self._resource_category = None
        self._metadata = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateMonitoredResourceTypeDetails.
        A unique monitored resource type name. The name must be unique across tenancy.
        Name can not be changed.


        :return: The name of this CreateMonitoredResourceTypeDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateMonitoredResourceTypeDetails.
        A unique monitored resource type name. The name must be unique across tenancy.
        Name can not be changed.


        :param name: The name of this CreateMonitoredResourceTypeDetails.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateMonitoredResourceTypeDetails.
        Monitored resource type display name.


        :return: The display_name of this CreateMonitoredResourceTypeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMonitoredResourceTypeDetails.
        Monitored resource type display name.


        :param display_name: The display_name of this CreateMonitoredResourceTypeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateMonitoredResourceTypeDetails.
        A friendly description.


        :return: The description of this CreateMonitoredResourceTypeDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateMonitoredResourceTypeDetails.
        A friendly description.


        :param description: The description of this CreateMonitoredResourceTypeDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMonitoredResourceTypeDetails.
        Compartment Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateMonitoredResourceTypeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMonitoredResourceTypeDetails.
        Compartment Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateMonitoredResourceTypeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def metric_namespace(self):
        """
        Gets the metric_namespace of this CreateMonitoredResourceTypeDetails.
        Metric namespace for resource type.


        :return: The metric_namespace of this CreateMonitoredResourceTypeDetails.
        :rtype: str
        """
        return self._metric_namespace

    @metric_namespace.setter
    def metric_namespace(self, metric_namespace):
        """
        Sets the metric_namespace of this CreateMonitoredResourceTypeDetails.
        Metric namespace for resource type.


        :param metric_namespace: The metric_namespace of this CreateMonitoredResourceTypeDetails.
        :type: str
        """
        self._metric_namespace = metric_namespace

    @property
    def source_type(self):
        """
        Gets the source_type of this CreateMonitoredResourceTypeDetails.
        Source type to indicate if the resource is stack monitoring discovered, OCI native resource, etc.

        Allowed values for this property are: "SM_MGMT_AGENT_MONITORED", "SM_REPO_ONLY", "OCI_NATIVE", "PROMETHEUS", "TELEGRAF", "COLLECTD"


        :return: The source_type of this CreateMonitoredResourceTypeDetails.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this CreateMonitoredResourceTypeDetails.
        Source type to indicate if the resource is stack monitoring discovered, OCI native resource, etc.


        :param source_type: The source_type of this CreateMonitoredResourceTypeDetails.
        :type: str
        """
        allowed_values = ["SM_MGMT_AGENT_MONITORED", "SM_REPO_ONLY", "OCI_NATIVE", "PROMETHEUS", "TELEGRAF", "COLLECTD"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            raise ValueError(
                f"Invalid value for `source_type`, must be None or one of {allowed_values}"
            )
        self._source_type = source_type

    @property
    def resource_category(self):
        """
        Gets the resource_category of this CreateMonitoredResourceTypeDetails.
        Resource Category to indicate the kind of resource type.

        Allowed values for this property are: "APPLICATION", "DATABASE", "MIDDLEWARE", "INFRASTRUCTURE", "UNKNOWN"


        :return: The resource_category of this CreateMonitoredResourceTypeDetails.
        :rtype: str
        """
        return self._resource_category

    @resource_category.setter
    def resource_category(self, resource_category):
        """
        Sets the resource_category of this CreateMonitoredResourceTypeDetails.
        Resource Category to indicate the kind of resource type.


        :param resource_category: The resource_category of this CreateMonitoredResourceTypeDetails.
        :type: str
        """
        allowed_values = ["APPLICATION", "DATABASE", "MIDDLEWARE", "INFRASTRUCTURE", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(resource_category, allowed_values):
            raise ValueError(
                f"Invalid value for `resource_category`, must be None or one of {allowed_values}"
            )
        self._resource_category = resource_category

    @property
    def metadata(self):
        """
        Gets the metadata of this CreateMonitoredResourceTypeDetails.

        :return: The metadata of this CreateMonitoredResourceTypeDetails.
        :rtype: oci.stack_monitoring.models.ResourceTypeMetadataDetails
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateMonitoredResourceTypeDetails.

        :param metadata: The metadata of this CreateMonitoredResourceTypeDetails.
        :type: oci.stack_monitoring.models.ResourceTypeMetadataDetails
        """
        self._metadata = metadata

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMonitoredResourceTypeDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateMonitoredResourceTypeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMonitoredResourceTypeDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateMonitoredResourceTypeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMonitoredResourceTypeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateMonitoredResourceTypeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMonitoredResourceTypeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateMonitoredResourceTypeDetails.
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
