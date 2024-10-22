# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseEncryptionKeyHistoryEntry(object):
    """
    The Autonomous Database encryption key history entry.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseEncryptionKeyHistoryEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param encryption_key:
            The value to assign to the encryption_key property of this AutonomousDatabaseEncryptionKeyHistoryEntry.
        :type encryption_key: oci.database.models.AutonomousDatabaseEncryptionKeyDetails

        :param time_activated:
            The value to assign to the time_activated property of this AutonomousDatabaseEncryptionKeyHistoryEntry.
        :type time_activated: datetime

        """
        self.swagger_types = {
            'encryption_key': 'AutonomousDatabaseEncryptionKeyDetails',
            'time_activated': 'datetime'
        }

        self.attribute_map = {
            'encryption_key': 'encryptionKey',
            'time_activated': 'timeActivated'
        }

        self._encryption_key = None
        self._time_activated = None

    @property
    def encryption_key(self):
        """
        Gets the encryption_key of this AutonomousDatabaseEncryptionKeyHistoryEntry.

        :return: The encryption_key of this AutonomousDatabaseEncryptionKeyHistoryEntry.
        :rtype: oci.database.models.AutonomousDatabaseEncryptionKeyDetails
        """
        return self._encryption_key

    @encryption_key.setter
    def encryption_key(self, encryption_key):
        """
        Sets the encryption_key of this AutonomousDatabaseEncryptionKeyHistoryEntry.

        :param encryption_key: The encryption_key of this AutonomousDatabaseEncryptionKeyHistoryEntry.
        :type: oci.database.models.AutonomousDatabaseEncryptionKeyDetails
        """
        self._encryption_key = encryption_key

    @property
    def time_activated(self):
        """
        Gets the time_activated of this AutonomousDatabaseEncryptionKeyHistoryEntry.
        The date and time the encryption key was activated.


        :return: The time_activated of this AutonomousDatabaseEncryptionKeyHistoryEntry.
        :rtype: datetime
        """
        return self._time_activated

    @time_activated.setter
    def time_activated(self, time_activated):
        """
        Sets the time_activated of this AutonomousDatabaseEncryptionKeyHistoryEntry.
        The date and time the encryption key was activated.


        :param time_activated: The time_activated of this AutonomousDatabaseEncryptionKeyHistoryEntry.
        :type: datetime
        """
        self._time_activated = time_activated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
