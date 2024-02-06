# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .rollback_details import RollbackDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListOfTargetsRollbackDetails(RollbackDetails):
    """
    LIST_OF_TARGETS strategy rollback details.
    The specified list would only act-upon targets that had a failed job during patching.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ListOfTargetsRollbackDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.ListOfTargetsRollbackDetails.strategy` attribute
        of this class is ``LIST_OF_TARGETS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param strategy:
            The value to assign to the strategy property of this ListOfTargetsRollbackDetails.
            Allowed values for this property are: "FAILED_JOBS", "LIST_OF_TARGETS"
        :type strategy: str

        :param targets:
            The value to assign to the targets property of this ListOfTargetsRollbackDetails.
        :type targets: list[str]

        """
        self.swagger_types = {
            'strategy': 'str',
            'targets': 'list[str]'
        }

        self.attribute_map = {
            'strategy': 'strategy',
            'targets': 'targets'
        }

        self._strategy = None
        self._targets = None
        self._strategy = 'LIST_OF_TARGETS'

    @property
    def targets(self):
        """
        **[Required]** Gets the targets of this ListOfTargetsRollbackDetails.
        OCIDs of targets to rollback.


        :return: The targets of this ListOfTargetsRollbackDetails.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this ListOfTargetsRollbackDetails.
        OCIDs of targets to rollback.


        :param targets: The targets of this ListOfTargetsRollbackDetails.
        :type: list[str]
        """
        self._targets = targets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other