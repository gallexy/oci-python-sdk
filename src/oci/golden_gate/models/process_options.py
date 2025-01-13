# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProcessOptions(object):
    """
    Required pipeline options to configure the replication process (Extract or Replicat).
    """

    #: A constant which can be used with the should_restart_on_failure property of a ProcessOptions.
    #: This constant has a value of "ENABLED"
    SHOULD_RESTART_ON_FAILURE_ENABLED = "ENABLED"

    #: A constant which can be used with the should_restart_on_failure property of a ProcessOptions.
    #: This constant has a value of "DISABLED"
    SHOULD_RESTART_ON_FAILURE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new ProcessOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param initial_data_load:
            The value to assign to the initial_data_load property of this ProcessOptions.
        :type initial_data_load: oci.golden_gate.models.InitialDataLoad

        :param replicate_schema_change:
            The value to assign to the replicate_schema_change property of this ProcessOptions.
        :type replicate_schema_change: oci.golden_gate.models.ReplicateSchemaChange

        :param should_restart_on_failure:
            The value to assign to the should_restart_on_failure property of this ProcessOptions.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type should_restart_on_failure: str

        """
        self.swagger_types = {
            'initial_data_load': 'InitialDataLoad',
            'replicate_schema_change': 'ReplicateSchemaChange',
            'should_restart_on_failure': 'str'
        }

        self.attribute_map = {
            'initial_data_load': 'initialDataLoad',
            'replicate_schema_change': 'replicateSchemaChange',
            'should_restart_on_failure': 'shouldRestartOnFailure'
        }

        self._initial_data_load = None
        self._replicate_schema_change = None
        self._should_restart_on_failure = None

    @property
    def initial_data_load(self):
        """
        **[Required]** Gets the initial_data_load of this ProcessOptions.

        :return: The initial_data_load of this ProcessOptions.
        :rtype: oci.golden_gate.models.InitialDataLoad
        """
        return self._initial_data_load

    @initial_data_load.setter
    def initial_data_load(self, initial_data_load):
        """
        Sets the initial_data_load of this ProcessOptions.

        :param initial_data_load: The initial_data_load of this ProcessOptions.
        :type: oci.golden_gate.models.InitialDataLoad
        """
        self._initial_data_load = initial_data_load

    @property
    def replicate_schema_change(self):
        """
        **[Required]** Gets the replicate_schema_change of this ProcessOptions.

        :return: The replicate_schema_change of this ProcessOptions.
        :rtype: oci.golden_gate.models.ReplicateSchemaChange
        """
        return self._replicate_schema_change

    @replicate_schema_change.setter
    def replicate_schema_change(self, replicate_schema_change):
        """
        Sets the replicate_schema_change of this ProcessOptions.

        :param replicate_schema_change: The replicate_schema_change of this ProcessOptions.
        :type: oci.golden_gate.models.ReplicateSchemaChange
        """
        self._replicate_schema_change = replicate_schema_change

    @property
    def should_restart_on_failure(self):
        """
        **[Required]** Gets the should_restart_on_failure of this ProcessOptions.
        If ENABLED, then the replication process restarts itself upon failure. This option applies when creating or updating a pipeline.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The should_restart_on_failure of this ProcessOptions.
        :rtype: str
        """
        return self._should_restart_on_failure

    @should_restart_on_failure.setter
    def should_restart_on_failure(self, should_restart_on_failure):
        """
        Sets the should_restart_on_failure of this ProcessOptions.
        If ENABLED, then the replication process restarts itself upon failure. This option applies when creating or updating a pipeline.


        :param should_restart_on_failure: The should_restart_on_failure of this ProcessOptions.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(should_restart_on_failure, allowed_values):
            should_restart_on_failure = 'UNKNOWN_ENUM_VALUE'
        self._should_restart_on_failure = should_restart_on_failure

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
