# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180222


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkloadMapping(object):
    """
    The properties that define an workloadMapping.
    """

    #: A constant which can be used with the lifecycle_state property of a WorkloadMapping.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a WorkloadMapping.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a WorkloadMapping.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a WorkloadMapping.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a WorkloadMapping.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a WorkloadMapping.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkloadMapping object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkloadMapping.
        :type id: str

        :param cluster_id:
            The value to assign to the cluster_id property of this WorkloadMapping.
        :type cluster_id: str

        :param namespace:
            The value to assign to the namespace property of this WorkloadMapping.
        :type namespace: str

        :param mapped_tenancy_id:
            The value to assign to the mapped_tenancy_id property of this WorkloadMapping.
        :type mapped_tenancy_id: str

        :param mapped_compartment_id:
            The value to assign to the mapped_compartment_id property of this WorkloadMapping.
        :type mapped_compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this WorkloadMapping.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this WorkloadMapping.
            Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this WorkloadMapping.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this WorkloadMapping.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'cluster_id': 'str',
            'namespace': 'str',
            'mapped_tenancy_id': 'str',
            'mapped_compartment_id': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'cluster_id': 'clusterId',
            'namespace': 'namespace',
            'mapped_tenancy_id': 'mappedTenancyId',
            'mapped_compartment_id': 'mappedCompartmentId',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._cluster_id = None
        self._namespace = None
        self._mapped_tenancy_id = None
        self._mapped_compartment_id = None
        self._time_created = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkloadMapping.
        The ocid of the workloadMapping.


        :return: The id of this WorkloadMapping.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkloadMapping.
        The ocid of the workloadMapping.


        :param id: The id of this WorkloadMapping.
        :type: str
        """
        self._id = id

    @property
    def cluster_id(self):
        """
        **[Required]** Gets the cluster_id of this WorkloadMapping.
        The OCID of the cluster.


        :return: The cluster_id of this WorkloadMapping.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this WorkloadMapping.
        The OCID of the cluster.


        :param cluster_id: The cluster_id of this WorkloadMapping.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this WorkloadMapping.
        The namespace of the workloadMapping.


        :return: The namespace of this WorkloadMapping.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this WorkloadMapping.
        The namespace of the workloadMapping.


        :param namespace: The namespace of this WorkloadMapping.
        :type: str
        """
        self._namespace = namespace

    @property
    def mapped_tenancy_id(self):
        """
        **[Required]** Gets the mapped_tenancy_id of this WorkloadMapping.
        The OCID of the mapped customer tenancy.


        :return: The mapped_tenancy_id of this WorkloadMapping.
        :rtype: str
        """
        return self._mapped_tenancy_id

    @mapped_tenancy_id.setter
    def mapped_tenancy_id(self, mapped_tenancy_id):
        """
        Sets the mapped_tenancy_id of this WorkloadMapping.
        The OCID of the mapped customer tenancy.


        :param mapped_tenancy_id: The mapped_tenancy_id of this WorkloadMapping.
        :type: str
        """
        self._mapped_tenancy_id = mapped_tenancy_id

    @property
    def mapped_compartment_id(self):
        """
        **[Required]** Gets the mapped_compartment_id of this WorkloadMapping.
        The OCID of the mapped customer compartment.


        :return: The mapped_compartment_id of this WorkloadMapping.
        :rtype: str
        """
        return self._mapped_compartment_id

    @mapped_compartment_id.setter
    def mapped_compartment_id(self, mapped_compartment_id):
        """
        Sets the mapped_compartment_id of this WorkloadMapping.
        The OCID of the mapped customer compartment.


        :param mapped_compartment_id: The mapped_compartment_id of this WorkloadMapping.
        :type: str
        """
        self._mapped_compartment_id = mapped_compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this WorkloadMapping.
        The time the cluster was created.


        :return: The time_created of this WorkloadMapping.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this WorkloadMapping.
        The time the cluster was created.


        :param time_created: The time_created of this WorkloadMapping.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this WorkloadMapping.
        The state of the workloadMapping.

        Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this WorkloadMapping.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this WorkloadMapping.
        The state of the workloadMapping.


        :param lifecycle_state: The lifecycle_state of this WorkloadMapping.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this WorkloadMapping.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this WorkloadMapping.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this WorkloadMapping.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this WorkloadMapping.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this WorkloadMapping.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this WorkloadMapping.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this WorkloadMapping.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this WorkloadMapping.
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