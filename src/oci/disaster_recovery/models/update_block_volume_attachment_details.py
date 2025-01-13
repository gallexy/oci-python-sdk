# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBlockVolumeAttachmentDetails(object):
    """
    The details for attaching or detaching a block volume.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBlockVolumeAttachmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param volume_attachment_reference_instance_id:
            The value to assign to the volume_attachment_reference_instance_id property of this UpdateBlockVolumeAttachmentDetails.
        :type volume_attachment_reference_instance_id: str

        """
        self.swagger_types = {
            'volume_attachment_reference_instance_id': 'str'
        }

        self.attribute_map = {
            'volume_attachment_reference_instance_id': 'volumeAttachmentReferenceInstanceId'
        }

        self._volume_attachment_reference_instance_id = None

    @property
    def volume_attachment_reference_instance_id(self):
        """
        Gets the volume_attachment_reference_instance_id of this UpdateBlockVolumeAttachmentDetails.
        The OCID of the reference compute instance from which to obtain the attachment details for the volume.
        This reference compute instance is from the peer DR protection group.

        Example: `ocid1.instance.oc1..uniqueID`


        :return: The volume_attachment_reference_instance_id of this UpdateBlockVolumeAttachmentDetails.
        :rtype: str
        """
        return self._volume_attachment_reference_instance_id

    @volume_attachment_reference_instance_id.setter
    def volume_attachment_reference_instance_id(self, volume_attachment_reference_instance_id):
        """
        Sets the volume_attachment_reference_instance_id of this UpdateBlockVolumeAttachmentDetails.
        The OCID of the reference compute instance from which to obtain the attachment details for the volume.
        This reference compute instance is from the peer DR protection group.

        Example: `ocid1.instance.oc1..uniqueID`


        :param volume_attachment_reference_instance_id: The volume_attachment_reference_instance_id of this UpdateBlockVolumeAttachmentDetails.
        :type: str
        """
        self._volume_attachment_reference_instance_id = volume_attachment_reference_instance_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
