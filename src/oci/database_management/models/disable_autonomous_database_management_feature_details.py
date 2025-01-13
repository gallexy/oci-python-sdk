# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DisableAutonomousDatabaseManagementFeatureDetails(object):
    """
    The details required to disable a Database Management feature for an Autonomous Database.
    """

    #: A constant which can be used with the feature property of a DisableAutonomousDatabaseManagementFeatureDetails.
    #: This constant has a value of "DIAGNOSTICS_AND_MANAGEMENT"
    FEATURE_DIAGNOSTICS_AND_MANAGEMENT = "DIAGNOSTICS_AND_MANAGEMENT"

    #: A constant which can be used with the feature property of a DisableAutonomousDatabaseManagementFeatureDetails.
    #: This constant has a value of "DB_LIFECYCLE_MANAGEMENT"
    FEATURE_DB_LIFECYCLE_MANAGEMENT = "DB_LIFECYCLE_MANAGEMENT"

    #: A constant which can be used with the feature property of a DisableAutonomousDatabaseManagementFeatureDetails.
    #: This constant has a value of "SQLWATCH"
    FEATURE_SQLWATCH = "SQLWATCH"

    def __init__(self, **kwargs):
        """
        Initializes a new DisableAutonomousDatabaseManagementFeatureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature:
            The value to assign to the feature property of this DisableAutonomousDatabaseManagementFeatureDetails.
            Allowed values for this property are: "DIAGNOSTICS_AND_MANAGEMENT", "DB_LIFECYCLE_MANAGEMENT", "SQLWATCH"
        :type feature: str

        """
        self.swagger_types = {
            'feature': 'str'
        }

        self.attribute_map = {
            'feature': 'feature'
        }

        self._feature = None

    @property
    def feature(self):
        """
        **[Required]** Gets the feature of this DisableAutonomousDatabaseManagementFeatureDetails.
        The name of the Database Management feature.

        Allowed values for this property are: "DIAGNOSTICS_AND_MANAGEMENT", "DB_LIFECYCLE_MANAGEMENT", "SQLWATCH"


        :return: The feature of this DisableAutonomousDatabaseManagementFeatureDetails.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """
        Sets the feature of this DisableAutonomousDatabaseManagementFeatureDetails.
        The name of the Database Management feature.


        :param feature: The feature of this DisableAutonomousDatabaseManagementFeatureDetails.
        :type: str
        """
        allowed_values = ["DIAGNOSTICS_AND_MANAGEMENT", "DB_LIFECYCLE_MANAGEMENT", "SQLWATCH"]
        if not value_allowed_none_or_none_sentinel(feature, allowed_values):
            raise ValueError(
                f"Invalid value for `feature`, must be None or one of {allowed_values}"
            )
        self._feature = feature

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
