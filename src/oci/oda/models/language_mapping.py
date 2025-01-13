# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LanguageMapping(object):
    """
    A natural language mapping.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LanguageMapping object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param language_tag:
            The value to assign to the language_tag property of this LanguageMapping.
        :type language_tag: str

        :param primary_name:
            The value to assign to the primary_name property of this LanguageMapping.
        :type primary_name: str

        :param names:
            The value to assign to the names property of this LanguageMapping.
        :type names: list[oci.oda.models.NameMapping]

        """
        self.swagger_types = {
            'language_tag': 'str',
            'primary_name': 'str',
            'names': 'list[NameMapping]'
        }

        self.attribute_map = {
            'language_tag': 'languageTag',
            'primary_name': 'primaryName',
            'names': 'names'
        }

        self._language_tag = None
        self._primary_name = None
        self._names = None

    @property
    def language_tag(self):
        """
        **[Required]** Gets the language_tag of this LanguageMapping.
        Language tag of mapping.


        :return: The language_tag of this LanguageMapping.
        :rtype: str
        """
        return self._language_tag

    @language_tag.setter
    def language_tag(self, language_tag):
        """
        Sets the language_tag of this LanguageMapping.
        Language tag of mapping.


        :param language_tag: The language_tag of this LanguageMapping.
        :type: str
        """
        self._language_tag = language_tag

    @property
    def primary_name(self):
        """
        **[Required]** Gets the primary_name of this LanguageMapping.
        Primary name of mapping.


        :return: The primary_name of this LanguageMapping.
        :rtype: str
        """
        return self._primary_name

    @primary_name.setter
    def primary_name(self, primary_name):
        """
        Sets the primary_name of this LanguageMapping.
        Primary name of mapping.


        :param primary_name: The primary_name of this LanguageMapping.
        :type: str
        """
        self._primary_name = primary_name

    @property
    def names(self):
        """
        **[Required]** Gets the names of this LanguageMapping.
        List of named values for mapping.


        :return: The names of this LanguageMapping.
        :rtype: list[oci.oda.models.NameMapping]
        """
        return self._names

    @names.setter
    def names(self, names):
        """
        Sets the names of this LanguageMapping.
        List of named values for mapping.


        :param names: The names of this LanguageMapping.
        :type: list[oci.oda.models.NameMapping]
        """
        self._names = names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
