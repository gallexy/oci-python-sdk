# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531

from .unified_agent_logging_filter import UnifiedAgentLoggingFilter
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentLoggingGrepFilter(UnifiedAgentLoggingFilter):
    """
    Logging grep filter object greps events by the values of specified fields.
    Ref: https://docs.fluentd.org/filter/grep
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentLoggingGrepFilter object with values from keyword arguments. The default value of the :py:attr:`~oci.logging.models.UnifiedAgentLoggingGrepFilter.filter_type` attribute
        of this class is ``GREP_FILTER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UnifiedAgentLoggingGrepFilter.
        :type name: str

        :param filter_type:
            The value to assign to the filter_type property of this UnifiedAgentLoggingGrepFilter.
            Allowed values for this property are: "PARSER_FILTER", "GREP_FILTER", "RECORD_TRANSFORMER_FILTER", "CUSTOM_FILTER"
        :type filter_type: str

        :param allow_list:
            The value to assign to the allow_list property of this UnifiedAgentLoggingGrepFilter.
        :type allow_list: list[oci.logging.models.GrepFilterAllowRule]

        :param deny_list:
            The value to assign to the deny_list property of this UnifiedAgentLoggingGrepFilter.
        :type deny_list: list[oci.logging.models.GrepFilterDenyRule]

        """
        self.swagger_types = {
            'name': 'str',
            'filter_type': 'str',
            'allow_list': 'list[GrepFilterAllowRule]',
            'deny_list': 'list[GrepFilterDenyRule]'
        }

        self.attribute_map = {
            'name': 'name',
            'filter_type': 'filterType',
            'allow_list': 'allowList',
            'deny_list': 'denyList'
        }

        self._name = None
        self._filter_type = None
        self._allow_list = None
        self._deny_list = None
        self._filter_type = 'GREP_FILTER'

    @property
    def allow_list(self):
        """
        Gets the allow_list of this UnifiedAgentLoggingGrepFilter.
        A list of filtering rules to include logs


        :return: The allow_list of this UnifiedAgentLoggingGrepFilter.
        :rtype: list[oci.logging.models.GrepFilterAllowRule]
        """
        return self._allow_list

    @allow_list.setter
    def allow_list(self, allow_list):
        """
        Sets the allow_list of this UnifiedAgentLoggingGrepFilter.
        A list of filtering rules to include logs


        :param allow_list: The allow_list of this UnifiedAgentLoggingGrepFilter.
        :type: list[oci.logging.models.GrepFilterAllowRule]
        """
        self._allow_list = allow_list

    @property
    def deny_list(self):
        """
        Gets the deny_list of this UnifiedAgentLoggingGrepFilter.
        A list of filtering rules to reject logs


        :return: The deny_list of this UnifiedAgentLoggingGrepFilter.
        :rtype: list[oci.logging.models.GrepFilterDenyRule]
        """
        return self._deny_list

    @deny_list.setter
    def deny_list(self, deny_list):
        """
        Sets the deny_list of this UnifiedAgentLoggingGrepFilter.
        A list of filtering rules to reject logs


        :param deny_list: The deny_list of this UnifiedAgentLoggingGrepFilter.
        :type: list[oci.logging.models.GrepFilterDenyRule]
        """
        self._deny_list = deny_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
