# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityActionNaturalLanguageMapping(object):
    """
    Natural language mapping of an entity action.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntityActionNaturalLanguageMapping object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param languages:
            The value to assign to the languages property of this EntityActionNaturalLanguageMapping.
        :type languages: list[oci.oda.models.LanguageMapping]

        """
        self.swagger_types = {
            'languages': 'list[LanguageMapping]'
        }

        self.attribute_map = {
            'languages': 'languages'
        }

        self._languages = None

    @property
    def languages(self):
        """
        **[Required]** Gets the languages of this EntityActionNaturalLanguageMapping.
        List of natural language mapped values.


        :return: The languages of this EntityActionNaturalLanguageMapping.
        :rtype: list[oci.oda.models.LanguageMapping]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """
        Sets the languages of this EntityActionNaturalLanguageMapping.
        List of natural language mapped values.


        :param languages: The languages of this EntityActionNaturalLanguageMapping.
        :type: list[oci.oda.models.LanguageMapping]
        """
        self._languages = languages

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
