# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .function_provisioned_concurrency_config import FunctionProvisionedConcurrencyConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NoneProvisionedConcurrencyConfig(FunctionProvisionedConcurrencyConfig):
    """
    Configuration specifying no provisioned concurrency
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NoneProvisionedConcurrencyConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.functions.models.NoneProvisionedConcurrencyConfig.strategy` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param strategy:
            The value to assign to the strategy property of this NoneProvisionedConcurrencyConfig.
            Allowed values for this property are: "CONSTANT", "NONE"
        :type strategy: str

        """
        self.swagger_types = {
            'strategy': 'str'
        }

        self.attribute_map = {
            'strategy': 'strategy'
        }

        self._strategy = None
        self._strategy = 'NONE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other