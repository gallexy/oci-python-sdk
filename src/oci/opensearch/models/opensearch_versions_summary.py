# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpensearchVersionsSummary(object):
    """
    A description of Opensearch versions
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OpensearchVersionsSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this OpensearchVersionsSummary.
        :type version: str

        """
        self.swagger_types = {
            'version': 'str'
        }

        self.attribute_map = {
            'version': 'version'
        }

        self._version = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this OpensearchVersionsSummary.
        The version of OpenSearch.


        :return: The version of this OpensearchVersionsSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this OpensearchVersionsSummary.
        The version of OpenSearch.


        :param version: The version of this OpensearchVersionsSummary.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
