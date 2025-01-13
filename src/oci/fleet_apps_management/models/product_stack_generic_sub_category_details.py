# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .product_stack_sub_category_details import ProductStackSubCategoryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProductStackGenericSubCategoryDetails(ProductStackSubCategoryDetails):
    """
    Generic Product Stack.Can be used for grouping Products.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProductStackGenericSubCategoryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.ProductStackGenericSubCategoryDetails.sub_category` attribute
        of this class is ``PRODUCT_STACK_GENERIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sub_category:
            The value to assign to the sub_category property of this ProductStackGenericSubCategoryDetails.
            Allowed values for this property are: "PRODUCT_STACK_GENERIC", "PRODUCT_STACK_AS_PRODUCT"
        :type sub_category: str

        """
        self.swagger_types = {
            'sub_category': 'str'
        }

        self.attribute_map = {
            'sub_category': 'subCategory'
        }

        self._sub_category = None
        self._sub_category = 'PRODUCT_STACK_GENERIC'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
