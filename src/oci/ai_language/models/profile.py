# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Profile(object):
    """
    Documents profile
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Profile object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param domain:
            The value to assign to the domain property of this Profile.
        :type domain: str

        :param document_type:
            The value to assign to the document_type property of this Profile.
        :type document_type: str

        :param speciality:
            The value to assign to the speciality property of this Profile.
        :type speciality: str

        """
        self.swagger_types = {
            'domain': 'str',
            'document_type': 'str',
            'speciality': 'str'
        }

        self.attribute_map = {
            'domain': 'domain',
            'document_type': 'documentType',
            'speciality': 'speciality'
        }

        self._domain = None
        self._document_type = None
        self._speciality = None

    @property
    def domain(self):
        """
        Gets the domain of this Profile.
        For PHI API this field can be PII/PHI/ALL and by default PII will be used. For other APIs Healthcare or Financial etc.


        :return: The domain of this Profile.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this Profile.
        For PHI API this field can be PII/PHI/ALL and by default PII will be used. For other APIs Healthcare or Financial etc.


        :param domain: The domain of this Profile.
        :type: str
        """
        self._domain = domain

    @property
    def document_type(self):
        """
        Gets the document_type of this Profile.
        Document type EHR Or Utterance


        :return: The document_type of this Profile.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """
        Sets the document_type of this Profile.
        Document type EHR Or Utterance


        :param document_type: The document_type of this Profile.
        :type: str
        """
        self._document_type = document_type

    @property
    def speciality(self):
        """
        Gets the speciality of this Profile.
        Document speciality like paediatrics, internal medicine etc.


        :return: The speciality of this Profile.
        :rtype: str
        """
        return self._speciality

    @speciality.setter
    def speciality(self, speciality):
        """
        Sets the speciality of this Profile.
        Document speciality like paediatrics, internal medicine etc.


        :param speciality: The speciality of this Profile.
        :type: str
        """
        self._speciality = speciality

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
