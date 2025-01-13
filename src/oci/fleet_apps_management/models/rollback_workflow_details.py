# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RollbackWorkflowDetails(object):
    """
    Rollback Workflow details.
    """

    #: A constant which can be used with the scope property of a RollbackWorkflowDetails.
    #: This constant has a value of "ACTION_GROUP"
    SCOPE_ACTION_GROUP = "ACTION_GROUP"

    #: A constant which can be used with the scope property of a RollbackWorkflowDetails.
    #: This constant has a value of "TARGET"
    SCOPE_TARGET = "TARGET"

    def __init__(self, **kwargs):
        """
        Initializes a new RollbackWorkflowDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scope:
            The value to assign to the scope property of this RollbackWorkflowDetails.
            Allowed values for this property are: "ACTION_GROUP", "TARGET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scope: str

        :param workflow:
            The value to assign to the workflow property of this RollbackWorkflowDetails.
        :type workflow: list[oci.fleet_apps_management.models.WorkflowGroup]

        """
        self.swagger_types = {
            'scope': 'str',
            'workflow': 'list[WorkflowGroup]'
        }

        self.attribute_map = {
            'scope': 'scope',
            'workflow': 'workflow'
        }

        self._scope = None
        self._workflow = None

    @property
    def scope(self):
        """
        **[Required]** Gets the scope of this RollbackWorkflowDetails.
        rollback Scope

        Allowed values for this property are: "ACTION_GROUP", "TARGET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The scope of this RollbackWorkflowDetails.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this RollbackWorkflowDetails.
        rollback Scope


        :param scope: The scope of this RollbackWorkflowDetails.
        :type: str
        """
        allowed_values = ["ACTION_GROUP", "TARGET"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            scope = 'UNKNOWN_ENUM_VALUE'
        self._scope = scope

    @property
    def workflow(self):
        """
        **[Required]** Gets the workflow of this RollbackWorkflowDetails.
        Rollback Workflow for the runbook.


        :return: The workflow of this RollbackWorkflowDetails.
        :rtype: list[oci.fleet_apps_management.models.WorkflowGroup]
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """
        Sets the workflow of this RollbackWorkflowDetails.
        Rollback Workflow for the runbook.


        :param workflow: The workflow of this RollbackWorkflowDetails.
        :type: list[oci.fleet_apps_management.models.WorkflowGroup]
        """
        self._workflow = workflow

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
