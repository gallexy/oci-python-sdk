# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220919


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvailableShapeSummary(object):
    """
    Sumarized information about a shape.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AvailableShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this AvailableShapeSummary.
        :type availability_domain: str

        :param pagination_token:
            The value to assign to the pagination_token property of this AvailableShapeSummary.
        :type pagination_token: str

        :param min_total_baseline_ocpus_required:
            The value to assign to the min_total_baseline_ocpus_required property of this AvailableShapeSummary.
        :type min_total_baseline_ocpus_required: float

        :param shape:
            The value to assign to the shape property of this AvailableShapeSummary.
        :type shape: str

        :param processor_description:
            The value to assign to the processor_description property of this AvailableShapeSummary.
        :type processor_description: str

        :param ocpus:
            The value to assign to the ocpus property of this AvailableShapeSummary.
        :type ocpus: float

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this AvailableShapeSummary.
        :type memory_in_gbs: float

        :param networking_bandwidth_in_gbps:
            The value to assign to the networking_bandwidth_in_gbps property of this AvailableShapeSummary.
        :type networking_bandwidth_in_gbps: float

        :param max_vnic_attachments:
            The value to assign to the max_vnic_attachments property of this AvailableShapeSummary.
        :type max_vnic_attachments: int

        :param gpus:
            The value to assign to the gpus property of this AvailableShapeSummary.
        :type gpus: int

        :param gpu_description:
            The value to assign to the gpu_description property of this AvailableShapeSummary.
        :type gpu_description: str

        :param local_disks:
            The value to assign to the local_disks property of this AvailableShapeSummary.
        :type local_disks: int

        :param local_disks_total_size_in_gbs:
            The value to assign to the local_disks_total_size_in_gbs property of this AvailableShapeSummary.
        :type local_disks_total_size_in_gbs: float

        :param local_disk_description:
            The value to assign to the local_disk_description property of this AvailableShapeSummary.
        :type local_disk_description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AvailableShapeSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AvailableShapeSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AvailableShapeSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'pagination_token': 'str',
            'min_total_baseline_ocpus_required': 'float',
            'shape': 'str',
            'processor_description': 'str',
            'ocpus': 'float',
            'memory_in_gbs': 'float',
            'networking_bandwidth_in_gbps': 'float',
            'max_vnic_attachments': 'int',
            'gpus': 'int',
            'gpu_description': 'str',
            'local_disks': 'int',
            'local_disks_total_size_in_gbs': 'float',
            'local_disk_description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'pagination_token': 'paginationToken',
            'min_total_baseline_ocpus_required': 'minTotalBaselineOcpusRequired',
            'shape': 'shape',
            'processor_description': 'processorDescription',
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs',
            'networking_bandwidth_in_gbps': 'networkingBandwidthInGbps',
            'max_vnic_attachments': 'maxVnicAttachments',
            'gpus': 'gpus',
            'gpu_description': 'gpuDescription',
            'local_disks': 'localDisks',
            'local_disks_total_size_in_gbs': 'localDisksTotalSizeInGBs',
            'local_disk_description': 'localDiskDescription',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._availability_domain = None
        self._pagination_token = None
        self._min_total_baseline_ocpus_required = None
        self._shape = None
        self._processor_description = None
        self._ocpus = None
        self._memory_in_gbs = None
        self._networking_bandwidth_in_gbps = None
        self._max_vnic_attachments = None
        self._gpus = None
        self._gpu_description = None
        self._local_disks = None
        self._local_disks_total_size_in_gbs = None
        self._local_disk_description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this AvailableShapeSummary.
        Availability domain of the shape.


        :return: The availability_domain of this AvailableShapeSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this AvailableShapeSummary.
        Availability domain of the shape.


        :param availability_domain: The availability_domain of this AvailableShapeSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def pagination_token(self):
        """
        **[Required]** Gets the pagination_token of this AvailableShapeSummary.
        Shape name and availability domain.  Used for pagination.


        :return: The pagination_token of this AvailableShapeSummary.
        :rtype: str
        """
        return self._pagination_token

    @pagination_token.setter
    def pagination_token(self, pagination_token):
        """
        Sets the pagination_token of this AvailableShapeSummary.
        Shape name and availability domain.  Used for pagination.


        :param pagination_token: The pagination_token of this AvailableShapeSummary.
        :type: str
        """
        self._pagination_token = pagination_token

    @property
    def min_total_baseline_ocpus_required(self):
        """
        Gets the min_total_baseline_ocpus_required of this AvailableShapeSummary.
        Minimum CPUs required.


        :return: The min_total_baseline_ocpus_required of this AvailableShapeSummary.
        :rtype: float
        """
        return self._min_total_baseline_ocpus_required

    @min_total_baseline_ocpus_required.setter
    def min_total_baseline_ocpus_required(self, min_total_baseline_ocpus_required):
        """
        Sets the min_total_baseline_ocpus_required of this AvailableShapeSummary.
        Minimum CPUs required.


        :param min_total_baseline_ocpus_required: The min_total_baseline_ocpus_required of this AvailableShapeSummary.
        :type: float
        """
        self._min_total_baseline_ocpus_required = min_total_baseline_ocpus_required

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this AvailableShapeSummary.
        Name of the shape.


        :return: The shape of this AvailableShapeSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this AvailableShapeSummary.
        Name of the shape.


        :param shape: The shape of this AvailableShapeSummary.
        :type: str
        """
        self._shape = shape

    @property
    def processor_description(self):
        """
        **[Required]** Gets the processor_description of this AvailableShapeSummary.
        Description of the processor.


        :return: The processor_description of this AvailableShapeSummary.
        :rtype: str
        """
        return self._processor_description

    @processor_description.setter
    def processor_description(self, processor_description):
        """
        Sets the processor_description of this AvailableShapeSummary.
        Description of the processor.


        :param processor_description: The processor_description of this AvailableShapeSummary.
        :type: str
        """
        self._processor_description = processor_description

    @property
    def ocpus(self):
        """
        **[Required]** Gets the ocpus of this AvailableShapeSummary.
        Number of CPUs.


        :return: The ocpus of this AvailableShapeSummary.
        :rtype: float
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this AvailableShapeSummary.
        Number of CPUs.


        :param ocpus: The ocpus of this AvailableShapeSummary.
        :type: float
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        **[Required]** Gets the memory_in_gbs of this AvailableShapeSummary.
        Amount of memory for the shape.


        :return: The memory_in_gbs of this AvailableShapeSummary.
        :rtype: float
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this AvailableShapeSummary.
        Amount of memory for the shape.


        :param memory_in_gbs: The memory_in_gbs of this AvailableShapeSummary.
        :type: float
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def networking_bandwidth_in_gbps(self):
        """
        Gets the networking_bandwidth_in_gbps of this AvailableShapeSummary.
        Shape bandwidth.


        :return: The networking_bandwidth_in_gbps of this AvailableShapeSummary.
        :rtype: float
        """
        return self._networking_bandwidth_in_gbps

    @networking_bandwidth_in_gbps.setter
    def networking_bandwidth_in_gbps(self, networking_bandwidth_in_gbps):
        """
        Sets the networking_bandwidth_in_gbps of this AvailableShapeSummary.
        Shape bandwidth.


        :param networking_bandwidth_in_gbps: The networking_bandwidth_in_gbps of this AvailableShapeSummary.
        :type: float
        """
        self._networking_bandwidth_in_gbps = networking_bandwidth_in_gbps

    @property
    def max_vnic_attachments(self):
        """
        Gets the max_vnic_attachments of this AvailableShapeSummary.
        Maximum number of virtual network interfaces that can be attached.


        :return: The max_vnic_attachments of this AvailableShapeSummary.
        :rtype: int
        """
        return self._max_vnic_attachments

    @max_vnic_attachments.setter
    def max_vnic_attachments(self, max_vnic_attachments):
        """
        Sets the max_vnic_attachments of this AvailableShapeSummary.
        Maximum number of virtual network interfaces that can be attached.


        :param max_vnic_attachments: The max_vnic_attachments of this AvailableShapeSummary.
        :type: int
        """
        self._max_vnic_attachments = max_vnic_attachments

    @property
    def gpus(self):
        """
        Gets the gpus of this AvailableShapeSummary.
        Number of GPUs.


        :return: The gpus of this AvailableShapeSummary.
        :rtype: int
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """
        Sets the gpus of this AvailableShapeSummary.
        Number of GPUs.


        :param gpus: The gpus of this AvailableShapeSummary.
        :type: int
        """
        self._gpus = gpus

    @property
    def gpu_description(self):
        """
        Gets the gpu_description of this AvailableShapeSummary.
        Description of the GPUs.


        :return: The gpu_description of this AvailableShapeSummary.
        :rtype: str
        """
        return self._gpu_description

    @gpu_description.setter
    def gpu_description(self, gpu_description):
        """
        Sets the gpu_description of this AvailableShapeSummary.
        Description of the GPUs.


        :param gpu_description: The gpu_description of this AvailableShapeSummary.
        :type: str
        """
        self._gpu_description = gpu_description

    @property
    def local_disks(self):
        """
        Gets the local_disks of this AvailableShapeSummary.
        Number of local disks.


        :return: The local_disks of this AvailableShapeSummary.
        :rtype: int
        """
        return self._local_disks

    @local_disks.setter
    def local_disks(self, local_disks):
        """
        Sets the local_disks of this AvailableShapeSummary.
        Number of local disks.


        :param local_disks: The local_disks of this AvailableShapeSummary.
        :type: int
        """
        self._local_disks = local_disks

    @property
    def local_disks_total_size_in_gbs(self):
        """
        Gets the local_disks_total_size_in_gbs of this AvailableShapeSummary.
        Total size of local disks for shape.


        :return: The local_disks_total_size_in_gbs of this AvailableShapeSummary.
        :rtype: float
        """
        return self._local_disks_total_size_in_gbs

    @local_disks_total_size_in_gbs.setter
    def local_disks_total_size_in_gbs(self, local_disks_total_size_in_gbs):
        """
        Sets the local_disks_total_size_in_gbs of this AvailableShapeSummary.
        Total size of local disks for shape.


        :param local_disks_total_size_in_gbs: The local_disks_total_size_in_gbs of this AvailableShapeSummary.
        :type: float
        """
        self._local_disks_total_size_in_gbs = local_disks_total_size_in_gbs

    @property
    def local_disk_description(self):
        """
        Gets the local_disk_description of this AvailableShapeSummary.
        Description of local disks.


        :return: The local_disk_description of this AvailableShapeSummary.
        :rtype: str
        """
        return self._local_disk_description

    @local_disk_description.setter
    def local_disk_description(self, local_disk_description):
        """
        Sets the local_disk_description of this AvailableShapeSummary.
        Description of local disks.


        :param local_disk_description: The local_disk_description of this AvailableShapeSummary.
        :type: str
        """
        self._local_disk_description = local_disk_description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AvailableShapeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this AvailableShapeSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AvailableShapeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this AvailableShapeSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AvailableShapeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this AvailableShapeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AvailableShapeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this AvailableShapeSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AvailableShapeSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this AvailableShapeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AvailableShapeSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this AvailableShapeSummary.
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
