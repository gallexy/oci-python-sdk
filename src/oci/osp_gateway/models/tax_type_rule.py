# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20191001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaxTypeRule(object):
    """
    Tax type rule information
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TaxTypeRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param fields:
            The value to assign to the fields property of this TaxTypeRule.
        :type fields: list[oci.osp_gateway.models.Field]

        :param value_set:
            The value to assign to the value_set property of this TaxTypeRule.
        :type value_set: list[oci.osp_gateway.models.ValueSetEntity]

        """
        self.swagger_types = {
            'fields': 'list[Field]',
            'value_set': 'list[ValueSetEntity]'
        }

        self.attribute_map = {
            'fields': 'fields',
            'value_set': 'valueSet'
        }

        self._fields = None
        self._value_set = None

    @property
    def fields(self):
        """
        **[Required]** Gets the fields of this TaxTypeRule.
        Tax type rule fields


        :return: The fields of this TaxTypeRule.
        :rtype: list[oci.osp_gateway.models.Field]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this TaxTypeRule.
        Tax type rule fields


        :param fields: The fields of this TaxTypeRule.
        :type: list[oci.osp_gateway.models.Field]
        """
        self._fields = fields

    @property
    def value_set(self):
        """
        Gets the value_set of this TaxTypeRule.
        Label value pair for allowed values. Used for GIRO


        :return: The value_set of this TaxTypeRule.
        :rtype: list[oci.osp_gateway.models.ValueSetEntity]
        """
        return self._value_set

    @value_set.setter
    def value_set(self, value_set):
        """
        Sets the value_set of this TaxTypeRule.
        Label value pair for allowed values. Used for GIRO


        :param value_set: The value_set of this TaxTypeRule.
        :type: list[oci.osp_gateway.models.ValueSetEntity]
        """
        self._value_set = value_set

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other