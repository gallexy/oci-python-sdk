# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .record_metadata import RecordMetadata
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentMetadata(RecordMetadata):
    """
    Collection of metadata related to document record.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentMetadata object with values from keyword arguments. The default value of the :py:attr:`~oci.data_labeling_service_dataplane.models.DocumentMetadata.record_type` attribute
        of this class is ``DOCUMENT_METADATA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param record_type:
            The value to assign to the record_type property of this DocumentMetadata.
            Allowed values for this property are: "IMAGE_METADATA", "TEXT_METADATA", "DOCUMENT_METADATA"
        :type record_type: str

        :param job_id:
            The value to assign to the job_id property of this DocumentMetadata.
        :type job_id: str

        """
        self.swagger_types = {
            'record_type': 'str',
            'job_id': 'str'
        }

        self.attribute_map = {
            'record_type': 'recordType',
            'job_id': 'jobId'
        }

        self._record_type = None
        self._job_id = None
        self._record_type = 'DOCUMENT_METADATA'

    @property
    def job_id(self):
        """
        Gets the job_id of this DocumentMetadata.
        Job id ocid of OCR batch call.


        :return: The job_id of this DocumentMetadata.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this DocumentMetadata.
        Job id ocid of OCR batch call.


        :param job_id: The job_id of this DocumentMetadata.
        :type: str
        """
        self._job_id = job_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
