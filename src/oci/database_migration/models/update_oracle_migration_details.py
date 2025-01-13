# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .update_migration_details import UpdateMigrationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOracleMigrationDetails(UpdateMigrationDetails):
    """
    Create Migration resource parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOracleMigrationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.UpdateOracleMigrationDetails.database_combination` attribute
        of this class is ``ORACLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateOracleMigrationDetails.
        :type description: str

        :param database_combination:
            The value to assign to the database_combination property of this UpdateOracleMigrationDetails.
            Allowed values for this property are: "MYSQL", "ORACLE"
        :type database_combination: str

        :param type:
            The value to assign to the type property of this UpdateOracleMigrationDetails.
            Allowed values for this property are: "ONLINE", "OFFLINE"
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateOracleMigrationDetails.
        :type display_name: str

        :param source_database_connection_id:
            The value to assign to the source_database_connection_id property of this UpdateOracleMigrationDetails.
        :type source_database_connection_id: str

        :param target_database_connection_id:
            The value to assign to the target_database_connection_id property of this UpdateOracleMigrationDetails.
        :type target_database_connection_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOracleMigrationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOracleMigrationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param data_transfer_medium_details:
            The value to assign to the data_transfer_medium_details property of this UpdateOracleMigrationDetails.
        :type data_transfer_medium_details: oci.database_migration.models.UpdateOracleDataTransferMediumDetails

        :param initial_load_settings:
            The value to assign to the initial_load_settings property of this UpdateOracleMigrationDetails.
        :type initial_load_settings: oci.database_migration.models.UpdateOracleInitialLoadSettings

        :param advisor_settings:
            The value to assign to the advisor_settings property of this UpdateOracleMigrationDetails.
        :type advisor_settings: oci.database_migration.models.UpdateOracleAdvisorSettings

        :param hub_details:
            The value to assign to the hub_details property of this UpdateOracleMigrationDetails.
        :type hub_details: oci.database_migration.models.UpdateGoldenGateHubDetails

        :param ggs_details:
            The value to assign to the ggs_details property of this UpdateOracleMigrationDetails.
        :type ggs_details: oci.database_migration.models.UpdateOracleGgsDeploymentDetails

        :param advanced_parameters:
            The value to assign to the advanced_parameters property of this UpdateOracleMigrationDetails.
        :type advanced_parameters: list[oci.database_migration.models.MigrationParameterDetails]

        :param source_container_database_connection_id:
            The value to assign to the source_container_database_connection_id property of this UpdateOracleMigrationDetails.
        :type source_container_database_connection_id: str

        """
        self.swagger_types = {
            'description': 'str',
            'database_combination': 'str',
            'type': 'str',
            'display_name': 'str',
            'source_database_connection_id': 'str',
            'target_database_connection_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'data_transfer_medium_details': 'UpdateOracleDataTransferMediumDetails',
            'initial_load_settings': 'UpdateOracleInitialLoadSettings',
            'advisor_settings': 'UpdateOracleAdvisorSettings',
            'hub_details': 'UpdateGoldenGateHubDetails',
            'ggs_details': 'UpdateOracleGgsDeploymentDetails',
            'advanced_parameters': 'list[MigrationParameterDetails]',
            'source_container_database_connection_id': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'database_combination': 'databaseCombination',
            'type': 'type',
            'display_name': 'displayName',
            'source_database_connection_id': 'sourceDatabaseConnectionId',
            'target_database_connection_id': 'targetDatabaseConnectionId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'data_transfer_medium_details': 'dataTransferMediumDetails',
            'initial_load_settings': 'initialLoadSettings',
            'advisor_settings': 'advisorSettings',
            'hub_details': 'hubDetails',
            'ggs_details': 'ggsDetails',
            'advanced_parameters': 'advancedParameters',
            'source_container_database_connection_id': 'sourceContainerDatabaseConnectionId'
        }

        self._description = None
        self._database_combination = None
        self._type = None
        self._display_name = None
        self._source_database_connection_id = None
        self._target_database_connection_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._data_transfer_medium_details = None
        self._initial_load_settings = None
        self._advisor_settings = None
        self._hub_details = None
        self._ggs_details = None
        self._advanced_parameters = None
        self._source_container_database_connection_id = None
        self._database_combination = 'ORACLE'

    @property
    def data_transfer_medium_details(self):
        """
        Gets the data_transfer_medium_details of this UpdateOracleMigrationDetails.

        :return: The data_transfer_medium_details of this UpdateOracleMigrationDetails.
        :rtype: oci.database_migration.models.UpdateOracleDataTransferMediumDetails
        """
        return self._data_transfer_medium_details

    @data_transfer_medium_details.setter
    def data_transfer_medium_details(self, data_transfer_medium_details):
        """
        Sets the data_transfer_medium_details of this UpdateOracleMigrationDetails.

        :param data_transfer_medium_details: The data_transfer_medium_details of this UpdateOracleMigrationDetails.
        :type: oci.database_migration.models.UpdateOracleDataTransferMediumDetails
        """
        self._data_transfer_medium_details = data_transfer_medium_details

    @property
    def initial_load_settings(self):
        """
        Gets the initial_load_settings of this UpdateOracleMigrationDetails.

        :return: The initial_load_settings of this UpdateOracleMigrationDetails.
        :rtype: oci.database_migration.models.UpdateOracleInitialLoadSettings
        """
        return self._initial_load_settings

    @initial_load_settings.setter
    def initial_load_settings(self, initial_load_settings):
        """
        Sets the initial_load_settings of this UpdateOracleMigrationDetails.

        :param initial_load_settings: The initial_load_settings of this UpdateOracleMigrationDetails.
        :type: oci.database_migration.models.UpdateOracleInitialLoadSettings
        """
        self._initial_load_settings = initial_load_settings

    @property
    def advisor_settings(self):
        """
        Gets the advisor_settings of this UpdateOracleMigrationDetails.

        :return: The advisor_settings of this UpdateOracleMigrationDetails.
        :rtype: oci.database_migration.models.UpdateOracleAdvisorSettings
        """
        return self._advisor_settings

    @advisor_settings.setter
    def advisor_settings(self, advisor_settings):
        """
        Sets the advisor_settings of this UpdateOracleMigrationDetails.

        :param advisor_settings: The advisor_settings of this UpdateOracleMigrationDetails.
        :type: oci.database_migration.models.UpdateOracleAdvisorSettings
        """
        self._advisor_settings = advisor_settings

    @property
    def hub_details(self):
        """
        Gets the hub_details of this UpdateOracleMigrationDetails.

        :return: The hub_details of this UpdateOracleMigrationDetails.
        :rtype: oci.database_migration.models.UpdateGoldenGateHubDetails
        """
        return self._hub_details

    @hub_details.setter
    def hub_details(self, hub_details):
        """
        Sets the hub_details of this UpdateOracleMigrationDetails.

        :param hub_details: The hub_details of this UpdateOracleMigrationDetails.
        :type: oci.database_migration.models.UpdateGoldenGateHubDetails
        """
        self._hub_details = hub_details

    @property
    def ggs_details(self):
        """
        Gets the ggs_details of this UpdateOracleMigrationDetails.

        :return: The ggs_details of this UpdateOracleMigrationDetails.
        :rtype: oci.database_migration.models.UpdateOracleGgsDeploymentDetails
        """
        return self._ggs_details

    @ggs_details.setter
    def ggs_details(self, ggs_details):
        """
        Sets the ggs_details of this UpdateOracleMigrationDetails.

        :param ggs_details: The ggs_details of this UpdateOracleMigrationDetails.
        :type: oci.database_migration.models.UpdateOracleGgsDeploymentDetails
        """
        self._ggs_details = ggs_details

    @property
    def advanced_parameters(self):
        """
        Gets the advanced_parameters of this UpdateOracleMigrationDetails.
        List of Migration Parameter objects.


        :return: The advanced_parameters of this UpdateOracleMigrationDetails.
        :rtype: list[oci.database_migration.models.MigrationParameterDetails]
        """
        return self._advanced_parameters

    @advanced_parameters.setter
    def advanced_parameters(self, advanced_parameters):
        """
        Sets the advanced_parameters of this UpdateOracleMigrationDetails.
        List of Migration Parameter objects.


        :param advanced_parameters: The advanced_parameters of this UpdateOracleMigrationDetails.
        :type: list[oci.database_migration.models.MigrationParameterDetails]
        """
        self._advanced_parameters = advanced_parameters

    @property
    def source_container_database_connection_id(self):
        """
        Gets the source_container_database_connection_id of this UpdateOracleMigrationDetails.
        The OCID of the resource being referenced.


        :return: The source_container_database_connection_id of this UpdateOracleMigrationDetails.
        :rtype: str
        """
        return self._source_container_database_connection_id

    @source_container_database_connection_id.setter
    def source_container_database_connection_id(self, source_container_database_connection_id):
        """
        Sets the source_container_database_connection_id of this UpdateOracleMigrationDetails.
        The OCID of the resource being referenced.


        :param source_container_database_connection_id: The source_container_database_connection_id of this UpdateOracleMigrationDetails.
        :type: str
        """
        self._source_container_database_connection_id = source_container_database_connection_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
