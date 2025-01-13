# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VideoTrackedObject(object):
    """
    Tracked object in a video.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VideoTrackedObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this VideoTrackedObject.
        :type name: str

        :param object_id:
            The value to assign to the object_id property of this VideoTrackedObject.
        :type object_id: int

        :param properties:
            The value to assign to the properties property of this VideoTrackedObject.
        :type properties: oci.ai_vision.models.VideoTrackedObjectProperties

        :param segments:
            The value to assign to the segments property of this VideoTrackedObject.
        :type segments: list[oci.ai_vision.models.VideoTrackedObjectSegment]

        """
        self.swagger_types = {
            'name': 'str',
            'object_id': 'int',
            'properties': 'VideoTrackedObjectProperties',
            'segments': 'list[VideoTrackedObjectSegment]'
        }

        self.attribute_map = {
            'name': 'name',
            'object_id': 'objectId',
            'properties': 'properties',
            'segments': 'segments'
        }

        self._name = None
        self._object_id = None
        self._properties = None
        self._segments = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this VideoTrackedObject.
        Name of the object category label.


        :return: The name of this VideoTrackedObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VideoTrackedObject.
        Name of the object category label.


        :param name: The name of this VideoTrackedObject.
        :type: str
        """
        self._name = name

    @property
    def object_id(self):
        """
        **[Required]** Gets the object_id of this VideoTrackedObject.
        Unique identifier for the object.


        :return: The object_id of this VideoTrackedObject.
        :rtype: int
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """
        Sets the object_id of this VideoTrackedObject.
        Unique identifier for the object.


        :param object_id: The object_id of this VideoTrackedObject.
        :type: int
        """
        self._object_id = object_id

    @property
    def properties(self):
        """
        Gets the properties of this VideoTrackedObject.

        :return: The properties of this VideoTrackedObject.
        :rtype: oci.ai_vision.models.VideoTrackedObjectProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this VideoTrackedObject.

        :param properties: The properties of this VideoTrackedObject.
        :type: oci.ai_vision.models.VideoTrackedObjectProperties
        """
        self._properties = properties

    @property
    def segments(self):
        """
        **[Required]** Gets the segments of this VideoTrackedObject.
        Segments for the tracked object.


        :return: The segments of this VideoTrackedObject.
        :rtype: list[oci.ai_vision.models.VideoTrackedObjectSegment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """
        Sets the segments of this VideoTrackedObject.
        Segments for the tracked object.


        :param segments: The segments of this VideoTrackedObject.
        :type: list[oci.ai_vision.models.VideoTrackedObjectSegment]
        """
        self._segments = segments

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
