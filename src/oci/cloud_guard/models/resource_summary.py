# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceSummary(object):
    """
    Summary of CG Resource
    """

    #: A constant which can be used with the risk_level property of a ResourceSummary.
    #: This constant has a value of "CRITICAL"
    RISK_LEVEL_CRITICAL = "CRITICAL"

    #: A constant which can be used with the risk_level property of a ResourceSummary.
    #: This constant has a value of "HIGH"
    RISK_LEVEL_HIGH = "HIGH"

    #: A constant which can be used with the risk_level property of a ResourceSummary.
    #: This constant has a value of "MEDIUM"
    RISK_LEVEL_MEDIUM = "MEDIUM"

    #: A constant which can be used with the risk_level property of a ResourceSummary.
    #: This constant has a value of "LOW"
    RISK_LEVEL_LOW = "LOW"

    #: A constant which can be used with the risk_level property of a ResourceSummary.
    #: This constant has a value of "MINOR"
    RISK_LEVEL_MINOR = "MINOR"

    #: A constant which can be used with the risk_level property of a ResourceSummary.
    #: This constant has a value of "NONE"
    RISK_LEVEL_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ResourceSummary.
        :type id: str

        :param resource_name:
            The value to assign to the resource_name property of this ResourceSummary.
        :type resource_name: str

        :param resource_type:
            The value to assign to the resource_type property of this ResourceSummary.
        :type resource_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ResourceSummary.
        :type compartment_id: str

        :param target_id:
            The value to assign to the target_id property of this ResourceSummary.
        :type target_id: str

        :param target_name:
            The value to assign to the target_name property of this ResourceSummary.
        :type target_name: str

        :param region:
            The value to assign to the region property of this ResourceSummary.
        :type region: str

        :param risk_level:
            The value to assign to the risk_level property of this ResourceSummary.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type risk_level: str

        :param problem_count:
            The value to assign to the problem_count property of this ResourceSummary.
        :type problem_count: int

        :param vulnerability_count:
            The value to assign to the vulnerability_count property of this ResourceSummary.
        :type vulnerability_count: int

        :param open_ports_count:
            The value to assign to the open_ports_count property of this ResourceSummary.
        :type open_ports_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ResourceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ResourceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ResourceSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'resource_name': 'str',
            'resource_type': 'str',
            'compartment_id': 'str',
            'target_id': 'str',
            'target_name': 'str',
            'region': 'str',
            'risk_level': 'str',
            'problem_count': 'int',
            'vulnerability_count': 'int',
            'open_ports_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'resource_name': 'resourceName',
            'resource_type': 'resourceType',
            'compartment_id': 'compartmentId',
            'target_id': 'targetId',
            'target_name': 'targetName',
            'region': 'region',
            'risk_level': 'riskLevel',
            'problem_count': 'problemCount',
            'vulnerability_count': 'vulnerabilityCount',
            'open_ports_count': 'openPortsCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._resource_name = None
        self._resource_type = None
        self._compartment_id = None
        self._target_id = None
        self._target_name = None
        self._region = None
        self._risk_level = None
        self._problem_count = None
        self._vulnerability_count = None
        self._open_ports_count = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ResourceSummary.
        Ocid for CG resource


        :return: The id of this ResourceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ResourceSummary.
        Ocid for CG resource


        :param id: The id of this ResourceSummary.
        :type: str
        """
        self._id = id

    @property
    def resource_name(self):
        """
        Gets the resource_name of this ResourceSummary.
        name of the CG resource


        :return: The resource_name of this ResourceSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this ResourceSummary.
        name of the CG resource


        :param resource_name: The resource_name of this ResourceSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """
        Gets the resource_type of this ResourceSummary.
        resource type of the CG resource


        :return: The resource_type of this ResourceSummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this ResourceSummary.
        resource type of the CG resource


        :param resource_type: The resource_type of this ResourceSummary.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ResourceSummary.
        CompartmentId of CG Resource


        :return: The compartment_id of this ResourceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ResourceSummary.
        CompartmentId of CG Resource


        :param compartment_id: The compartment_id of this ResourceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_id(self):
        """
        Gets the target_id of this ResourceSummary.
        TargetId of CG Resource


        :return: The target_id of this ResourceSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this ResourceSummary.
        TargetId of CG Resource


        :param target_id: The target_id of this ResourceSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def target_name(self):
        """
        Gets the target_name of this ResourceSummary.
        Target name for the CG Resource


        :return: The target_name of this ResourceSummary.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """
        Sets the target_name of this ResourceSummary.
        Target name for the CG Resource


        :param target_name: The target_name of this ResourceSummary.
        :type: str
        """
        self._target_name = target_name

    @property
    def region(self):
        """
        Gets the region of this ResourceSummary.
        region of CG Resource


        :return: The region of this ResourceSummary.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this ResourceSummary.
        region of CG Resource


        :param region: The region of this ResourceSummary.
        :type: str
        """
        self._region = region

    @property
    def risk_level(self):
        """
        Gets the risk_level of this ResourceSummary.
        The Risk Level

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The risk_level of this ResourceSummary.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this ResourceSummary.
        The Risk Level


        :param risk_level: The risk_level of this ResourceSummary.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", "NONE"]
        if not value_allowed_none_or_none_sentinel(risk_level, allowed_values):
            risk_level = 'UNKNOWN_ENUM_VALUE'
        self._risk_level = risk_level

    @property
    def problem_count(self):
        """
        Gets the problem_count of this ResourceSummary.
        Count of existing problems for a resource


        :return: The problem_count of this ResourceSummary.
        :rtype: int
        """
        return self._problem_count

    @problem_count.setter
    def problem_count(self, problem_count):
        """
        Sets the problem_count of this ResourceSummary.
        Count of existing problems for a resource


        :param problem_count: The problem_count of this ResourceSummary.
        :type: int
        """
        self._problem_count = problem_count

    @property
    def vulnerability_count(self):
        """
        Gets the vulnerability_count of this ResourceSummary.
        Count of existing number of vulnerabilities in the resource


        :return: The vulnerability_count of this ResourceSummary.
        :rtype: int
        """
        return self._vulnerability_count

    @vulnerability_count.setter
    def vulnerability_count(self, vulnerability_count):
        """
        Sets the vulnerability_count of this ResourceSummary.
        Count of existing number of vulnerabilities in the resource


        :param vulnerability_count: The vulnerability_count of this ResourceSummary.
        :type: int
        """
        self._vulnerability_count = vulnerability_count

    @property
    def open_ports_count(self):
        """
        Gets the open_ports_count of this ResourceSummary.
        Number of open ports in a resource


        :return: The open_ports_count of this ResourceSummary.
        :rtype: int
        """
        return self._open_ports_count

    @open_ports_count.setter
    def open_ports_count(self, open_ports_count):
        """
        Sets the open_ports_count of this ResourceSummary.
        Number of open ports in a resource


        :param open_ports_count: The open_ports_count of this ResourceSummary.
        :type: int
        """
        self._open_ports_count = open_ports_count

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ResourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this ResourceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ResourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this ResourceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ResourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ResourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ResourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ResourceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ResourceSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ResourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ResourceSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ResourceSummary.
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