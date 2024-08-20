# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalPluggableDatabaseFeatureDetails(object):
    """
    The details required to enable the specified Database Management feature.
    """

    #: A constant which can be used with the feature property of a ExternalPluggableDatabaseFeatureDetails.
    #: This constant has a value of "DIAGNOSTICS_AND_MANAGEMENT"
    FEATURE_DIAGNOSTICS_AND_MANAGEMENT = "DIAGNOSTICS_AND_MANAGEMENT"

    #: A constant which can be used with the feature property of a ExternalPluggableDatabaseFeatureDetails.
    #: This constant has a value of "DB_LIFECYCLE_MANAGEMENT"
    FEATURE_DB_LIFECYCLE_MANAGEMENT = "DB_LIFECYCLE_MANAGEMENT"

    #: A constant which can be used with the feature property of a ExternalPluggableDatabaseFeatureDetails.
    #: This constant has a value of "SQLWATCH"
    FEATURE_SQLWATCH = "SQLWATCH"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalPluggableDatabaseFeatureDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.ExternalPluggableDatabaseDiagnosticsAndManagementFeatureDetails`
        * :class:`~oci.database_management.models.ExternalPluggableDatabaseLifecycleManagementFeatureDetails`
        * :class:`~oci.database_management.models.ExternalPluggableDatabaseSqlWatchFeatureDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature:
            The value to assign to the feature property of this ExternalPluggableDatabaseFeatureDetails.
            Allowed values for this property are: "DIAGNOSTICS_AND_MANAGEMENT", "DB_LIFECYCLE_MANAGEMENT", "SQLWATCH"
        :type feature: str

        :param connector_details:
            The value to assign to the connector_details property of this ExternalPluggableDatabaseFeatureDetails.
        :type connector_details: oci.database_management.models.ConnectorDetails

        """
        self.swagger_types = {
            'feature': 'str',
            'connector_details': 'ConnectorDetails'
        }

        self.attribute_map = {
            'feature': 'feature',
            'connector_details': 'connectorDetails'
        }

        self._feature = None
        self._connector_details = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['feature']

        if type == 'DIAGNOSTICS_AND_MANAGEMENT':
            return 'ExternalPluggableDatabaseDiagnosticsAndManagementFeatureDetails'

        if type == 'DB_LIFECYCLE_MANAGEMENT':
            return 'ExternalPluggableDatabaseLifecycleManagementFeatureDetails'

        if type == 'SQLWATCH':
            return 'ExternalPluggableDatabaseSqlWatchFeatureDetails'
        else:
            return 'ExternalPluggableDatabaseFeatureDetails'

    @property
    def feature(self):
        """
        **[Required]** Gets the feature of this ExternalPluggableDatabaseFeatureDetails.
        The name of the Database Management feature.

        Allowed values for this property are: "DIAGNOSTICS_AND_MANAGEMENT", "DB_LIFECYCLE_MANAGEMENT", "SQLWATCH"


        :return: The feature of this ExternalPluggableDatabaseFeatureDetails.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """
        Sets the feature of this ExternalPluggableDatabaseFeatureDetails.
        The name of the Database Management feature.


        :param feature: The feature of this ExternalPluggableDatabaseFeatureDetails.
        :type: str
        """
        allowed_values = ["DIAGNOSTICS_AND_MANAGEMENT", "DB_LIFECYCLE_MANAGEMENT", "SQLWATCH"]
        if not value_allowed_none_or_none_sentinel(feature, allowed_values):
            raise ValueError(
                f"Invalid value for `feature`, must be None or one of {allowed_values}"
            )
        self._feature = feature

    @property
    def connector_details(self):
        """
        **[Required]** Gets the connector_details of this ExternalPluggableDatabaseFeatureDetails.

        :return: The connector_details of this ExternalPluggableDatabaseFeatureDetails.
        :rtype: oci.database_management.models.ConnectorDetails
        """
        return self._connector_details

    @connector_details.setter
    def connector_details(self, connector_details):
        """
        Sets the connector_details of this ExternalPluggableDatabaseFeatureDetails.

        :param connector_details: The connector_details of this ExternalPluggableDatabaseFeatureDetails.
        :type: oci.database_management.models.ConnectorDetails
        """
        self._connector_details = connector_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
