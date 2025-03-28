# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentMonitoringUrlSource(object):
    """
    Kubernetes source object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentMonitoringUrlSource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UnifiedAgentMonitoringUrlSource.
        :type name: str

        :param scrape_targets:
            The value to assign to the scrape_targets property of this UnifiedAgentMonitoringUrlSource.
        :type scrape_targets: list[oci.logging.models.UnifiedAgentUrlScrapeTarget]

        """
        self.swagger_types = {
            'name': 'str',
            'scrape_targets': 'list[UnifiedAgentUrlScrapeTarget]'
        }
        self.attribute_map = {
            'name': 'name',
            'scrape_targets': 'scrapeTargets'
        }
        self._name = None
        self._scrape_targets = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this UnifiedAgentMonitoringUrlSource.
        Unique name for the source.


        :return: The name of this UnifiedAgentMonitoringUrlSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UnifiedAgentMonitoringUrlSource.
        Unique name for the source.


        :param name: The name of this UnifiedAgentMonitoringUrlSource.
        :type: str
        """
        self._name = name

    @property
    def scrape_targets(self):
        """
        **[Required]** Gets the scrape_targets of this UnifiedAgentMonitoringUrlSource.
        List of UnifiedAgentKubernetesScrapeTarget.


        :return: The scrape_targets of this UnifiedAgentMonitoringUrlSource.
        :rtype: list[oci.logging.models.UnifiedAgentUrlScrapeTarget]
        """
        return self._scrape_targets

    @scrape_targets.setter
    def scrape_targets(self, scrape_targets):
        """
        Sets the scrape_targets of this UnifiedAgentMonitoringUrlSource.
        List of UnifiedAgentKubernetesScrapeTarget.


        :param scrape_targets: The scrape_targets of this UnifiedAgentMonitoringUrlSource.
        :type: list[oci.logging.models.UnifiedAgentUrlScrapeTarget]
        """
        self._scrape_targets = scrape_targets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
