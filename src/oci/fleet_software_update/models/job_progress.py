# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobProgress(object):
    """
    Summary of progress for the Exadata Fleet Update Job.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobProgress object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param progress_of_operation:
            The value to assign to the progress_of_operation property of this JobProgress.
        :type progress_of_operation: int

        """
        self.swagger_types = {
            'progress_of_operation': 'int'
        }

        self.attribute_map = {
            'progress_of_operation': 'progressOfOperation'
        }

        self._progress_of_operation = None

    @property
    def progress_of_operation(self):
        """
        Gets the progress_of_operation of this JobProgress.
        Percentage of progress against the total to complete the operation.


        :return: The progress_of_operation of this JobProgress.
        :rtype: int
        """
        return self._progress_of_operation

    @progress_of_operation.setter
    def progress_of_operation(self, progress_of_operation):
        """
        Sets the progress_of_operation of this JobProgress.
        Percentage of progress against the total to complete the operation.


        :param progress_of_operation: The progress_of_operation of this JobProgress.
        :type: int
        """
        self._progress_of_operation = progress_of_operation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
