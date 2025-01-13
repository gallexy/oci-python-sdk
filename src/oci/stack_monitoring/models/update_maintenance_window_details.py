# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMaintenanceWindowDetails(object):
    """
    Infomation to create a new Maintenance Window.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMaintenanceWindowDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateMaintenanceWindowDetails.
        :type description: str

        :param resources:
            The value to assign to the resources property of this UpdateMaintenanceWindowDetails.
        :type resources: list[oci.stack_monitoring.models.CreateMaintenanceWindowResourceDetails]

        :param schedule:
            The value to assign to the schedule property of this UpdateMaintenanceWindowDetails.
        :type schedule: oci.stack_monitoring.models.MaintenanceWindowSchedule

        """
        self.swagger_types = {
            'description': 'str',
            'resources': 'list[CreateMaintenanceWindowResourceDetails]',
            'schedule': 'MaintenanceWindowSchedule'
        }

        self.attribute_map = {
            'description': 'description',
            'resources': 'resources',
            'schedule': 'schedule'
        }

        self._description = None
        self._resources = None
        self._schedule = None

    @property
    def description(self):
        """
        Gets the description of this UpdateMaintenanceWindowDetails.
        Maintenance Window description.


        :return: The description of this UpdateMaintenanceWindowDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateMaintenanceWindowDetails.
        Maintenance Window description.


        :param description: The description of this UpdateMaintenanceWindowDetails.
        :type: str
        """
        self._description = description

    @property
    def resources(self):
        """
        Gets the resources of this UpdateMaintenanceWindowDetails.
        List of resource Ids which are part of the Maintenance Window


        :return: The resources of this UpdateMaintenanceWindowDetails.
        :rtype: list[oci.stack_monitoring.models.CreateMaintenanceWindowResourceDetails]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this UpdateMaintenanceWindowDetails.
        List of resource Ids which are part of the Maintenance Window


        :param resources: The resources of this UpdateMaintenanceWindowDetails.
        :type: list[oci.stack_monitoring.models.CreateMaintenanceWindowResourceDetails]
        """
        self._resources = resources

    @property
    def schedule(self):
        """
        Gets the schedule of this UpdateMaintenanceWindowDetails.

        :return: The schedule of this UpdateMaintenanceWindowDetails.
        :rtype: oci.stack_monitoring.models.MaintenanceWindowSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this UpdateMaintenanceWindowDetails.

        :param schedule: The schedule of this UpdateMaintenanceWindowDetails.
        :type: oci.stack_monitoring.models.MaintenanceWindowSchedule
        """
        self._schedule = schedule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
