# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .stage_output import StageOutput
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenericArtifacts(StageOutput):
    """
    Details of artifact generated via pipeline run
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenericArtifacts object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.GenericArtifacts.output_type` attribute
        of this class is ``ARTIFACT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param output_type:
            The value to assign to the output_type property of this GenericArtifacts.
            Allowed values for this property are: "ARTIFACT", "TEST_REPORT"
        :type output_type: str

        :param step_name:
            The value to assign to the step_name property of this GenericArtifacts.
        :type step_name: str

        :param name:
            The value to assign to the name property of this GenericArtifacts.
        :type name: str

        :param location_details:
            The value to assign to the location_details property of this GenericArtifacts.
        :type location_details: oci.devops.models.GenericArtifactLocationDetails

        """
        self.swagger_types = {
            'output_type': 'str',
            'step_name': 'str',
            'name': 'str',
            'location_details': 'GenericArtifactLocationDetails'
        }

        self.attribute_map = {
            'output_type': 'outputType',
            'step_name': 'stepName',
            'name': 'name',
            'location_details': 'locationDetails'
        }

        self._output_type = None
        self._step_name = None
        self._name = None
        self._location_details = None
        self._output_type = 'ARTIFACT'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this GenericArtifacts.
        Name of artifact.


        :return: The name of this GenericArtifacts.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GenericArtifacts.
        Name of artifact.


        :param name: The name of this GenericArtifacts.
        :type: str
        """
        self._name = name

    @property
    def location_details(self):
        """
        **[Required]** Gets the location_details of this GenericArtifacts.

        :return: The location_details of this GenericArtifacts.
        :rtype: oci.devops.models.GenericArtifactLocationDetails
        """
        return self._location_details

    @location_details.setter
    def location_details(self, location_details):
        """
        Sets the location_details of this GenericArtifacts.

        :param location_details: The location_details of this GenericArtifacts.
        :type: oci.devops.models.GenericArtifactLocationDetails
        """
        self._location_details = location_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
