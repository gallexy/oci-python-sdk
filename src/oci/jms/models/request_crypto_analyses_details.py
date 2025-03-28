# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestCryptoAnalysesDetails(object):
    """
    Details of the request to start a JFR crypto event analysis.
    When the targets aren't specified, then all managed instances currently in the fleet are selected.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestCryptoAnalysesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param targets:
            The value to assign to the targets property of this RequestCryptoAnalysesDetails.
        :type targets: list[oci.jms.models.JfrAttachmentTarget]

        :param recording_duration_in_minutes:
            The value to assign to the recording_duration_in_minutes property of this RequestCryptoAnalysesDetails.
        :type recording_duration_in_minutes: int

        :param waiting_period_in_minutes:
            The value to assign to the waiting_period_in_minutes property of this RequestCryptoAnalysesDetails.
        :type waiting_period_in_minutes: int

        """
        self.swagger_types = {
            'targets': 'list[JfrAttachmentTarget]',
            'recording_duration_in_minutes': 'int',
            'waiting_period_in_minutes': 'int'
        }
        self.attribute_map = {
            'targets': 'targets',
            'recording_duration_in_minutes': 'recordingDurationInMinutes',
            'waiting_period_in_minutes': 'waitingPeriodInMinutes'
        }
        self._targets = None
        self._recording_duration_in_minutes = None
        self._waiting_period_in_minutes = None

    @property
    def targets(self):
        """
        Gets the targets of this RequestCryptoAnalysesDetails.
        The attachment targets to start JFR.


        :return: The targets of this RequestCryptoAnalysesDetails.
        :rtype: list[oci.jms.models.JfrAttachmentTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this RequestCryptoAnalysesDetails.
        The attachment targets to start JFR.


        :param targets: The targets of this RequestCryptoAnalysesDetails.
        :type: list[oci.jms.models.JfrAttachmentTarget]
        """
        self._targets = targets

    @property
    def recording_duration_in_minutes(self):
        """
        Gets the recording_duration_in_minutes of this RequestCryptoAnalysesDetails.
        Duration of the JFR recording in minutes.


        :return: The recording_duration_in_minutes of this RequestCryptoAnalysesDetails.
        :rtype: int
        """
        return self._recording_duration_in_minutes

    @recording_duration_in_minutes.setter
    def recording_duration_in_minutes(self, recording_duration_in_minutes):
        """
        Sets the recording_duration_in_minutes of this RequestCryptoAnalysesDetails.
        Duration of the JFR recording in minutes.


        :param recording_duration_in_minutes: The recording_duration_in_minutes of this RequestCryptoAnalysesDetails.
        :type: int
        """
        self._recording_duration_in_minutes = recording_duration_in_minutes

    @property
    def waiting_period_in_minutes(self):
        """
        Gets the waiting_period_in_minutes of this RequestCryptoAnalysesDetails.
        Period to looking for JVMs. In addition to attach to running JVMs when given the command,
        JVM started within the waiting period will also be attached for JFR. The value should be
        larger than the agent polling interval setting for the fleet to ensure agent can get the
        instructions. If not specified, the agent polling interval for the fleet is used.


        :return: The waiting_period_in_minutes of this RequestCryptoAnalysesDetails.
        :rtype: int
        """
        return self._waiting_period_in_minutes

    @waiting_period_in_minutes.setter
    def waiting_period_in_minutes(self, waiting_period_in_minutes):
        """
        Sets the waiting_period_in_minutes of this RequestCryptoAnalysesDetails.
        Period to looking for JVMs. In addition to attach to running JVMs when given the command,
        JVM started within the waiting period will also be attached for JFR. The value should be
        larger than the agent polling interval setting for the fleet to ensure agent can get the
        instructions. If not specified, the agent polling interval for the fleet is used.


        :param waiting_period_in_minutes: The waiting_period_in_minutes of this RequestCryptoAnalysesDetails.
        :type: int
        """
        self._waiting_period_in_minutes = waiting_period_in_minutes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
