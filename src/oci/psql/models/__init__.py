# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915

from __future__ import absolute_import

from .backup import Backup
from .backup_collection import BackupCollection
from .backup_policy import BackupPolicy
from .backup_source_details import BackupSourceDetails
from .backup_summary import BackupSummary
from .change_backup_compartment_details import ChangeBackupCompartmentDetails
from .change_configuration_compartment_details import ChangeConfigurationCompartmentDetails
from .change_db_system_compartment_details import ChangeDbSystemCompartmentDetails
from .config_overrides import ConfigOverrides
from .config_params import ConfigParams
from .configuration import Configuration
from .configuration_collection import ConfigurationCollection
from .configuration_details import ConfigurationDetails
from .configuration_summary import ConfigurationSummary
from .connection_details import ConnectionDetails
from .create_backup_details import CreateBackupDetails
from .create_configuration_details import CreateConfigurationDetails
from .create_db_instance_details import CreateDbInstanceDetails
from .create_db_system_details import CreateDbSystemDetails
from .credentials import Credentials
from .daily_backup_policy import DailyBackupPolicy
from .db_configuration_override_collection import DbConfigurationOverrideCollection
from .db_instance import DbInstance
from .db_instance_endpoint import DbInstanceEndpoint
from .db_system import DbSystem
from .db_system_collection import DbSystemCollection
from .db_system_details import DbSystemDetails
from .db_system_summary import DbSystemSummary
from .default_config_params import DefaultConfigParams
from .default_configuration import DefaultConfiguration
from .default_configuration_collection import DefaultConfigurationCollection
from .default_configuration_details import DefaultConfigurationDetails
from .default_configuration_summary import DefaultConfigurationSummary
from .endpoint import Endpoint
from .failover_db_system_details import FailoverDbSystemDetails
from .management_policy import ManagementPolicy
from .management_policy_details import ManagementPolicyDetails
from .monthly_backup_policy import MonthlyBackupPolicy
from .network_details import NetworkDetails
from .none_backup_policy import NoneBackupPolicy
from .none_source_details import NoneSourceDetails
from .oci_optimized_storage_details import OciOptimizedStorageDetails
from .password_details import PasswordDetails
from .patch_db_system_details import PatchDbSystemDetails
from .patch_insert_instruction import PatchInsertInstruction
from .patch_instruction import PatchInstruction
from .patch_merge_instruction import PatchMergeInstruction
from .patch_move_instruction import PatchMoveInstruction
from .patch_prohibit_instruction import PatchProhibitInstruction
from .patch_remove_instruction import PatchRemoveInstruction
from .patch_replace_instruction import PatchReplaceInstruction
from .patch_require_instruction import PatchRequireInstruction
from .plain_text_password_details import PlainTextPasswordDetails
from .primary_db_instance_details import PrimaryDbInstanceDetails
from .reset_master_user_password_details import ResetMasterUserPasswordDetails
from .restart_db_instance_in_db_system_details import RestartDbInstanceInDbSystemDetails
from .restore_db_system_details import RestoreDbSystemDetails
from .shape_collection import ShapeCollection
from .shape_memory_options import ShapeMemoryOptions
from .shape_ocpu_options import ShapeOcpuOptions
from .shape_summary import ShapeSummary
from .source_details import SourceDetails
from .storage_details import StorageDetails
from .update_backup_details import UpdateBackupDetails
from .update_configuration_details import UpdateConfigurationDetails
from .update_db_config_params import UpdateDbConfigParams
from .update_db_system_db_instance_details import UpdateDbSystemDbInstanceDetails
from .update_db_system_details import UpdateDbSystemDetails
from .update_network_details import UpdateNetworkDetails
from .update_storage_details_params import UpdateStorageDetailsParams
from .vault_secret_password_details import VaultSecretPasswordDetails
from .weekly_backup_policy import WeeklyBackupPolicy
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for psql services.
psql_type_mapping = {
    "Backup": Backup,
    "BackupCollection": BackupCollection,
    "BackupPolicy": BackupPolicy,
    "BackupSourceDetails": BackupSourceDetails,
    "BackupSummary": BackupSummary,
    "ChangeBackupCompartmentDetails": ChangeBackupCompartmentDetails,
    "ChangeConfigurationCompartmentDetails": ChangeConfigurationCompartmentDetails,
    "ChangeDbSystemCompartmentDetails": ChangeDbSystemCompartmentDetails,
    "ConfigOverrides": ConfigOverrides,
    "ConfigParams": ConfigParams,
    "Configuration": Configuration,
    "ConfigurationCollection": ConfigurationCollection,
    "ConfigurationDetails": ConfigurationDetails,
    "ConfigurationSummary": ConfigurationSummary,
    "ConnectionDetails": ConnectionDetails,
    "CreateBackupDetails": CreateBackupDetails,
    "CreateConfigurationDetails": CreateConfigurationDetails,
    "CreateDbInstanceDetails": CreateDbInstanceDetails,
    "CreateDbSystemDetails": CreateDbSystemDetails,
    "Credentials": Credentials,
    "DailyBackupPolicy": DailyBackupPolicy,
    "DbConfigurationOverrideCollection": DbConfigurationOverrideCollection,
    "DbInstance": DbInstance,
    "DbInstanceEndpoint": DbInstanceEndpoint,
    "DbSystem": DbSystem,
    "DbSystemCollection": DbSystemCollection,
    "DbSystemDetails": DbSystemDetails,
    "DbSystemSummary": DbSystemSummary,
    "DefaultConfigParams": DefaultConfigParams,
    "DefaultConfiguration": DefaultConfiguration,
    "DefaultConfigurationCollection": DefaultConfigurationCollection,
    "DefaultConfigurationDetails": DefaultConfigurationDetails,
    "DefaultConfigurationSummary": DefaultConfigurationSummary,
    "Endpoint": Endpoint,
    "FailoverDbSystemDetails": FailoverDbSystemDetails,
    "ManagementPolicy": ManagementPolicy,
    "ManagementPolicyDetails": ManagementPolicyDetails,
    "MonthlyBackupPolicy": MonthlyBackupPolicy,
    "NetworkDetails": NetworkDetails,
    "NoneBackupPolicy": NoneBackupPolicy,
    "NoneSourceDetails": NoneSourceDetails,
    "OciOptimizedStorageDetails": OciOptimizedStorageDetails,
    "PasswordDetails": PasswordDetails,
    "PatchDbSystemDetails": PatchDbSystemDetails,
    "PatchInsertInstruction": PatchInsertInstruction,
    "PatchInstruction": PatchInstruction,
    "PatchMergeInstruction": PatchMergeInstruction,
    "PatchMoveInstruction": PatchMoveInstruction,
    "PatchProhibitInstruction": PatchProhibitInstruction,
    "PatchRemoveInstruction": PatchRemoveInstruction,
    "PatchReplaceInstruction": PatchReplaceInstruction,
    "PatchRequireInstruction": PatchRequireInstruction,
    "PlainTextPasswordDetails": PlainTextPasswordDetails,
    "PrimaryDbInstanceDetails": PrimaryDbInstanceDetails,
    "ResetMasterUserPasswordDetails": ResetMasterUserPasswordDetails,
    "RestartDbInstanceInDbSystemDetails": RestartDbInstanceInDbSystemDetails,
    "RestoreDbSystemDetails": RestoreDbSystemDetails,
    "ShapeCollection": ShapeCollection,
    "ShapeMemoryOptions": ShapeMemoryOptions,
    "ShapeOcpuOptions": ShapeOcpuOptions,
    "ShapeSummary": ShapeSummary,
    "SourceDetails": SourceDetails,
    "StorageDetails": StorageDetails,
    "UpdateBackupDetails": UpdateBackupDetails,
    "UpdateConfigurationDetails": UpdateConfigurationDetails,
    "UpdateDbConfigParams": UpdateDbConfigParams,
    "UpdateDbSystemDbInstanceDetails": UpdateDbSystemDbInstanceDetails,
    "UpdateDbSystemDetails": UpdateDbSystemDetails,
    "UpdateNetworkDetails": UpdateNetworkDetails,
    "UpdateStorageDetailsParams": UpdateStorageDetailsParams,
    "VaultSecretPasswordDetails": VaultSecretPasswordDetails,
    "WeeklyBackupPolicy": WeeklyBackupPolicy,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
