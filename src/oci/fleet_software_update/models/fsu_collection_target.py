# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FsuCollectionTarget(object):
    """
    Details of a target member of a Exadata Fleet Update Collection.
    """

    #: A constant which can be used with the status property of a FsuCollectionTarget.
    #: This constant has a value of "IDLE"
    STATUS_IDLE = "IDLE"

    #: A constant which can be used with the status property of a FsuCollectionTarget.
    #: This constant has a value of "EXECUTING_JOB"
    STATUS_EXECUTING_JOB = "EXECUTING_JOB"

    #: A constant which can be used with the status property of a FsuCollectionTarget.
    #: This constant has a value of "JOB_FAILED"
    STATUS_JOB_FAILED = "JOB_FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new FsuCollectionTarget object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target:
            The value to assign to the target property of this FsuCollectionTarget.
        :type target: oci.fleet_software_update.models.TargetDetails

        :param current_version:
            The value to assign to the current_version property of this FsuCollectionTarget.
        :type current_version: str

        :param status:
            The value to assign to the status property of this FsuCollectionTarget.
            Allowed values for this property are: "IDLE", "EXECUTING_JOB", "JOB_FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param executing_fsu_job_id:
            The value to assign to the executing_fsu_job_id property of this FsuCollectionTarget.
        :type executing_fsu_job_id: str

        :param active_fsu_cycle_id:
            The value to assign to the active_fsu_cycle_id property of this FsuCollectionTarget.
        :type active_fsu_cycle_id: str

        :param progress:
            The value to assign to the progress property of this FsuCollectionTarget.
        :type progress: oci.fleet_software_update.models.TargetProgressSummary

        """
        self.swagger_types = {
            'target': 'TargetDetails',
            'current_version': 'str',
            'status': 'str',
            'executing_fsu_job_id': 'str',
            'active_fsu_cycle_id': 'str',
            'progress': 'TargetProgressSummary'
        }

        self.attribute_map = {
            'target': 'target',
            'current_version': 'currentVersion',
            'status': 'status',
            'executing_fsu_job_id': 'executingFsuJobId',
            'active_fsu_cycle_id': 'activeFsuCycleId',
            'progress': 'progress'
        }

        self._target = None
        self._current_version = None
        self._status = None
        self._executing_fsu_job_id = None
        self._active_fsu_cycle_id = None
        self._progress = None

    @property
    def target(self):
        """
        **[Required]** Gets the target of this FsuCollectionTarget.

        :return: The target of this FsuCollectionTarget.
        :rtype: oci.fleet_software_update.models.TargetDetails
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this FsuCollectionTarget.

        :param target: The target of this FsuCollectionTarget.
        :type: oci.fleet_software_update.models.TargetDetails
        """
        self._target = target

    @property
    def current_version(self):
        """
        Gets the current_version of this FsuCollectionTarget.
        Current version of the target.


        :return: The current_version of this FsuCollectionTarget.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """
        Sets the current_version of this FsuCollectionTarget.
        Current version of the target.


        :param current_version: The current_version of this FsuCollectionTarget.
        :type: str
        """
        self._current_version = current_version

    @property
    def status(self):
        """
        Gets the status of this FsuCollectionTarget.
        Status of the target in the Exadata Fleet Update Collection.

        Allowed values for this property are: "IDLE", "EXECUTING_JOB", "JOB_FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this FsuCollectionTarget.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this FsuCollectionTarget.
        Status of the target in the Exadata Fleet Update Collection.


        :param status: The status of this FsuCollectionTarget.
        :type: str
        """
        allowed_values = ["IDLE", "EXECUTING_JOB", "JOB_FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def executing_fsu_job_id(self):
        """
        Gets the executing_fsu_job_id of this FsuCollectionTarget.
        Exadata Fleet Update Job OCID executing an action in the target. Null if no job is being executed.


        :return: The executing_fsu_job_id of this FsuCollectionTarget.
        :rtype: str
        """
        return self._executing_fsu_job_id

    @executing_fsu_job_id.setter
    def executing_fsu_job_id(self, executing_fsu_job_id):
        """
        Sets the executing_fsu_job_id of this FsuCollectionTarget.
        Exadata Fleet Update Job OCID executing an action in the target. Null if no job is being executed.


        :param executing_fsu_job_id: The executing_fsu_job_id of this FsuCollectionTarget.
        :type: str
        """
        self._executing_fsu_job_id = executing_fsu_job_id

    @property
    def active_fsu_cycle_id(self):
        """
        Gets the active_fsu_cycle_id of this FsuCollectionTarget.
        Active Exadata Fleet Update Cycle OCID. Null if no Cycle is active that has this target as member.


        :return: The active_fsu_cycle_id of this FsuCollectionTarget.
        :rtype: str
        """
        return self._active_fsu_cycle_id

    @active_fsu_cycle_id.setter
    def active_fsu_cycle_id(self, active_fsu_cycle_id):
        """
        Sets the active_fsu_cycle_id of this FsuCollectionTarget.
        Active Exadata Fleet Update Cycle OCID. Null if no Cycle is active that has this target as member.


        :param active_fsu_cycle_id: The active_fsu_cycle_id of this FsuCollectionTarget.
        :type: str
        """
        self._active_fsu_cycle_id = active_fsu_cycle_id

    @property
    def progress(self):
        """
        Gets the progress of this FsuCollectionTarget.

        :return: The progress of this FsuCollectionTarget.
        :rtype: oci.fleet_software_update.models.TargetProgressSummary
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this FsuCollectionTarget.

        :param progress: The progress of this FsuCollectionTarget.
        :type: oci.fleet_software_update.models.TargetProgressSummary
        """
        self._progress = progress

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
