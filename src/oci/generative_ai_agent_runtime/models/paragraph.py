# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Paragraph(object):
    """
    The paragraph of the generated message that contains a citation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Paragraph object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param text:
            The value to assign to the text property of this Paragraph.
        :type text: str

        :param start:
            The value to assign to the start property of this Paragraph.
        :type start: int

        :param end:
            The value to assign to the end property of this Paragraph.
        :type end: int

        """
        self.swagger_types = {
            'text': 'str',
            'start': 'int',
            'end': 'int'
        }
        self.attribute_map = {
            'text': 'text',
            'start': 'start',
            'end': 'end'
        }
        self._text = None
        self._start = None
        self._end = None

    @property
    def text(self):
        """
        **[Required]** Gets the text of this Paragraph.
        The part of the generated message that contains a citation.


        :return: The text of this Paragraph.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Paragraph.
        The part of the generated message that contains a citation.


        :param text: The text of this Paragraph.
        :type: str
        """
        self._text = text

    @property
    def start(self):
        """
        **[Required]** Gets the start of this Paragraph.
        Where the text with a citation starts in the generated message.


        :return: The start of this Paragraph.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this Paragraph.
        Where the text with a citation starts in the generated message.


        :param start: The start of this Paragraph.
        :type: int
        """
        self._start = start

    @property
    def end(self):
        """
        **[Required]** Gets the end of this Paragraph.
        Where the text with a citation ends in the generated message.


        :return: The end of this Paragraph.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this Paragraph.
        Where the text with a citation ends in the generated message.


        :param end: The end of this Paragraph.
        :type: int
        """
        self._end = end

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
