# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiagnosticsCollectionDetails(object):
    """
    Details to configure diagnostics collection for targets affected by this Exadata Fleet Update Maintenance Cycle.
    """

    #: A constant which can be used with the log_collection_mode property of a DiagnosticsCollectionDetails.
    #: This constant has a value of "ENABLE"
    LOG_COLLECTION_MODE_ENABLE = "ENABLE"

    #: A constant which can be used with the log_collection_mode property of a DiagnosticsCollectionDetails.
    #: This constant has a value of "ENABLE_AND_RESTORE"
    LOG_COLLECTION_MODE_ENABLE_AND_RESTORE = "ENABLE_AND_RESTORE"

    #: A constant which can be used with the log_collection_mode property of a DiagnosticsCollectionDetails.
    #: This constant has a value of "NO_CHANGE"
    LOG_COLLECTION_MODE_NO_CHANGE = "NO_CHANGE"

    def __init__(self, **kwargs):
        """
        Initializes a new DiagnosticsCollectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param log_collection_mode:
            The value to assign to the log_collection_mode property of this DiagnosticsCollectionDetails.
            Allowed values for this property are: "ENABLE", "ENABLE_AND_RESTORE", "NO_CHANGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type log_collection_mode: str

        """
        self.swagger_types = {
            'log_collection_mode': 'str'
        }

        self.attribute_map = {
            'log_collection_mode': 'logCollectionMode'
        }

        self._log_collection_mode = None

    @property
    def log_collection_mode(self):
        """
        Gets the log_collection_mode of this DiagnosticsCollectionDetails.
        Enable incident logs and trace collection.
        Allow Oracle to collect incident logs and traces to enable fault diagnosis and issue resolution according to the selected mode.

        Allowed values for this property are: "ENABLE", "ENABLE_AND_RESTORE", "NO_CHANGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The log_collection_mode of this DiagnosticsCollectionDetails.
        :rtype: str
        """
        return self._log_collection_mode

    @log_collection_mode.setter
    def log_collection_mode(self, log_collection_mode):
        """
        Sets the log_collection_mode of this DiagnosticsCollectionDetails.
        Enable incident logs and trace collection.
        Allow Oracle to collect incident logs and traces to enable fault diagnosis and issue resolution according to the selected mode.


        :param log_collection_mode: The log_collection_mode of this DiagnosticsCollectionDetails.
        :type: str
        """
        allowed_values = ["ENABLE", "ENABLE_AND_RESTORE", "NO_CHANGE"]
        if not value_allowed_none_or_none_sentinel(log_collection_mode, allowed_values):
            log_collection_mode = 'UNKNOWN_ENUM_VALUE'
        self._log_collection_mode = log_collection_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
