# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateManagedInstanceDetails(object):
    """
    Provides the information used to update a managed instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateManagedInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateManagedInstanceDetails.
        :type description: str

        :param primary_management_station_id:
            The value to assign to the primary_management_station_id property of this UpdateManagedInstanceDetails.
        :type primary_management_station_id: str

        :param secondary_management_station_id:
            The value to assign to the secondary_management_station_id property of this UpdateManagedInstanceDetails.
        :type secondary_management_station_id: str

        :param notification_topic_id:
            The value to assign to the notification_topic_id property of this UpdateManagedInstanceDetails.
        :type notification_topic_id: str

        :param autonomous_settings:
            The value to assign to the autonomous_settings property of this UpdateManagedInstanceDetails.
        :type autonomous_settings: oci.os_management_hub.models.UpdatableAutonomousSettings

        """
        self.swagger_types = {
            'description': 'str',
            'primary_management_station_id': 'str',
            'secondary_management_station_id': 'str',
            'notification_topic_id': 'str',
            'autonomous_settings': 'UpdatableAutonomousSettings'
        }

        self.attribute_map = {
            'description': 'description',
            'primary_management_station_id': 'primaryManagementStationId',
            'secondary_management_station_id': 'secondaryManagementStationId',
            'notification_topic_id': 'notificationTopicId',
            'autonomous_settings': 'autonomousSettings'
        }

        self._description = None
        self._primary_management_station_id = None
        self._secondary_management_station_id = None
        self._notification_topic_id = None
        self._autonomous_settings = None

    @property
    def description(self):
        """
        Gets the description of this UpdateManagedInstanceDetails.
        User-specified description of the managed instance. Avoid entering confidential information.


        :return: The description of this UpdateManagedInstanceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateManagedInstanceDetails.
        User-specified description of the managed instance. Avoid entering confidential information.


        :param description: The description of this UpdateManagedInstanceDetails.
        :type: str
        """
        self._description = description

    @property
    def primary_management_station_id(self):
        """
        Gets the primary_management_station_id of this UpdateManagedInstanceDetails.
        The `OCID`__ of the management station for the instance to use as primary management station.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The primary_management_station_id of this UpdateManagedInstanceDetails.
        :rtype: str
        """
        return self._primary_management_station_id

    @primary_management_station_id.setter
    def primary_management_station_id(self, primary_management_station_id):
        """
        Sets the primary_management_station_id of this UpdateManagedInstanceDetails.
        The `OCID`__ of the management station for the instance to use as primary management station.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param primary_management_station_id: The primary_management_station_id of this UpdateManagedInstanceDetails.
        :type: str
        """
        self._primary_management_station_id = primary_management_station_id

    @property
    def secondary_management_station_id(self):
        """
        Gets the secondary_management_station_id of this UpdateManagedInstanceDetails.
        The `OCID`__ of the management station for the instance to use as secondary management station.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The secondary_management_station_id of this UpdateManagedInstanceDetails.
        :rtype: str
        """
        return self._secondary_management_station_id

    @secondary_management_station_id.setter
    def secondary_management_station_id(self, secondary_management_station_id):
        """
        Sets the secondary_management_station_id of this UpdateManagedInstanceDetails.
        The `OCID`__ of the management station for the instance to use as secondary management station.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param secondary_management_station_id: The secondary_management_station_id of this UpdateManagedInstanceDetails.
        :type: str
        """
        self._secondary_management_station_id = secondary_management_station_id

    @property
    def notification_topic_id(self):
        """
        Gets the notification_topic_id of this UpdateManagedInstanceDetails.
        The `OCID`__ for the Oracle Notifications service (ONS) topic. ONS is the channel used to send notifications to the customer.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The notification_topic_id of this UpdateManagedInstanceDetails.
        :rtype: str
        """
        return self._notification_topic_id

    @notification_topic_id.setter
    def notification_topic_id(self, notification_topic_id):
        """
        Sets the notification_topic_id of this UpdateManagedInstanceDetails.
        The `OCID`__ for the Oracle Notifications service (ONS) topic. ONS is the channel used to send notifications to the customer.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param notification_topic_id: The notification_topic_id of this UpdateManagedInstanceDetails.
        :type: str
        """
        self._notification_topic_id = notification_topic_id

    @property
    def autonomous_settings(self):
        """
        Gets the autonomous_settings of this UpdateManagedInstanceDetails.

        :return: The autonomous_settings of this UpdateManagedInstanceDetails.
        :rtype: oci.os_management_hub.models.UpdatableAutonomousSettings
        """
        return self._autonomous_settings

    @autonomous_settings.setter
    def autonomous_settings(self, autonomous_settings):
        """
        Sets the autonomous_settings of this UpdateManagedInstanceDetails.

        :param autonomous_settings: The autonomous_settings of this UpdateManagedInstanceDetails.
        :type: oci.os_management_hub.models.UpdatableAutonomousSettings
        """
        self._autonomous_settings = autonomous_settings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
