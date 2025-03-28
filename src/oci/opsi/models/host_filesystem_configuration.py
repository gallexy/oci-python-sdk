# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .host_configuration_metric_group import HostConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostFilesystemConfiguration(HostConfigurationMetricGroup):
    """
    Filesystem Configuration metric for the host.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostFilesystemConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostFilesystemConfiguration.metric_name` attribute
        of this class is ``HOST_FILESYSTEM_CONFIGURATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostFilesystemConfiguration.
            Allowed values for this property are: "HOST_PRODUCT", "HOST_RESOURCE_ALLOCATION", "HOST_MEMORY_CONFIGURATION", "HOST_HARDWARE_CONFIGURATION", "HOST_CPU_HARDWARE_CONFIGURATION", "HOST_NETWORK_CONFIGURATION", "HOST_ENTITES", "HOST_FILESYSTEM_CONFIGURATION", "HOST_GPU_CONFIGURATION", "HOST_CONTAINERS"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostFilesystemConfiguration.
        :type time_collected: datetime

        :param file_system_name:
            The value to assign to the file_system_name property of this HostFilesystemConfiguration.
        :type file_system_name: str

        :param mount_point:
            The value to assign to the mount_point property of this HostFilesystemConfiguration.
        :type mount_point: str

        :param file_system_size_in_gb:
            The value to assign to the file_system_size_in_gb property of this HostFilesystemConfiguration.
        :type file_system_size_in_gb: float

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'file_system_name': 'str',
            'mount_point': 'str',
            'file_system_size_in_gb': 'float'
        }
        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'file_system_name': 'fileSystemName',
            'mount_point': 'mountPoint',
            'file_system_size_in_gb': 'fileSystemSizeInGB'
        }
        self._metric_name = None
        self._time_collected = None
        self._file_system_name = None
        self._mount_point = None
        self._file_system_size_in_gb = None
        self._metric_name = 'HOST_FILESYSTEM_CONFIGURATION'

    @property
    def file_system_name(self):
        """
        **[Required]** Gets the file_system_name of this HostFilesystemConfiguration.
        Name of filesystem


        :return: The file_system_name of this HostFilesystemConfiguration.
        :rtype: str
        """
        return self._file_system_name

    @file_system_name.setter
    def file_system_name(self, file_system_name):
        """
        Sets the file_system_name of this HostFilesystemConfiguration.
        Name of filesystem


        :param file_system_name: The file_system_name of this HostFilesystemConfiguration.
        :type: str
        """
        self._file_system_name = file_system_name

    @property
    def mount_point(self):
        """
        **[Required]** Gets the mount_point of this HostFilesystemConfiguration.
        Mount points are specialized NTFS filesystem objects


        :return: The mount_point of this HostFilesystemConfiguration.
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """
        Sets the mount_point of this HostFilesystemConfiguration.
        Mount points are specialized NTFS filesystem objects


        :param mount_point: The mount_point of this HostFilesystemConfiguration.
        :type: str
        """
        self._mount_point = mount_point

    @property
    def file_system_size_in_gb(self):
        """
        **[Required]** Gets the file_system_size_in_gb of this HostFilesystemConfiguration.
        Size of filesystem


        :return: The file_system_size_in_gb of this HostFilesystemConfiguration.
        :rtype: float
        """
        return self._file_system_size_in_gb

    @file_system_size_in_gb.setter
    def file_system_size_in_gb(self, file_system_size_in_gb):
        """
        Sets the file_system_size_in_gb of this HostFilesystemConfiguration.
        Size of filesystem


        :param file_system_size_in_gb: The file_system_size_in_gb of this HostFilesystemConfiguration.
        :type: float
        """
        self._file_system_size_in_gb = file_system_size_in_gb

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
