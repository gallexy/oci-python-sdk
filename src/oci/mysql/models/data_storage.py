# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190415


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataStorage(object):
    """
    Data Storage information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataStorage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param allocated_storage_size_in_gbs:
            The value to assign to the allocated_storage_size_in_gbs property of this DataStorage.
        :type allocated_storage_size_in_gbs: int

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this DataStorage.
        :type data_storage_size_in_gbs: int

        :param data_storage_size_limit_in_gbs:
            The value to assign to the data_storage_size_limit_in_gbs property of this DataStorage.
        :type data_storage_size_limit_in_gbs: int

        :param is_auto_expand_storage_enabled:
            The value to assign to the is_auto_expand_storage_enabled property of this DataStorage.
        :type is_auto_expand_storage_enabled: bool

        :param max_storage_size_in_gbs:
            The value to assign to the max_storage_size_in_gbs property of this DataStorage.
        :type max_storage_size_in_gbs: int

        """
        self.swagger_types = {
            'allocated_storage_size_in_gbs': 'int',
            'data_storage_size_in_gbs': 'int',
            'data_storage_size_limit_in_gbs': 'int',
            'is_auto_expand_storage_enabled': 'bool',
            'max_storage_size_in_gbs': 'int'
        }

        self.attribute_map = {
            'allocated_storage_size_in_gbs': 'allocatedStorageSizeInGBs',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'data_storage_size_limit_in_gbs': 'dataStorageSizeLimitInGBs',
            'is_auto_expand_storage_enabled': 'isAutoExpandStorageEnabled',
            'max_storage_size_in_gbs': 'maxStorageSizeInGBs'
        }

        self._allocated_storage_size_in_gbs = None
        self._data_storage_size_in_gbs = None
        self._data_storage_size_limit_in_gbs = None
        self._is_auto_expand_storage_enabled = None
        self._max_storage_size_in_gbs = None

    @property
    def allocated_storage_size_in_gbs(self):
        """
        Gets the allocated_storage_size_in_gbs of this DataStorage.
        The actual allocated storage size for the DB System. This may be higher than dataStorageSizeInGBs
        if an automatic storage expansion has occurred.


        :return: The allocated_storage_size_in_gbs of this DataStorage.
        :rtype: int
        """
        return self._allocated_storage_size_in_gbs

    @allocated_storage_size_in_gbs.setter
    def allocated_storage_size_in_gbs(self, allocated_storage_size_in_gbs):
        """
        Sets the allocated_storage_size_in_gbs of this DataStorage.
        The actual allocated storage size for the DB System. This may be higher than dataStorageSizeInGBs
        if an automatic storage expansion has occurred.


        :param allocated_storage_size_in_gbs: The allocated_storage_size_in_gbs of this DataStorage.
        :type: int
        """
        self._allocated_storage_size_in_gbs = allocated_storage_size_in_gbs

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this DataStorage.
        User specified size of the data volume. May be less than current allocatedStorageSizeInGBs.


        :return: The data_storage_size_in_gbs of this DataStorage.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this DataStorage.
        User specified size of the data volume. May be less than current allocatedStorageSizeInGBs.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this DataStorage.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def data_storage_size_limit_in_gbs(self):
        """
        Gets the data_storage_size_limit_in_gbs of this DataStorage.
        The absolute limit the DB System's storage size may ever expand to, either manually or automatically.
        This limit is based based on the initial dataStorageSizeInGBs when the DB System was first created.
        Both dataStorageSizeInGBs and maxDataStorageSizeInGBs can not exceed this value.

        DB Systems with an initial storage size of 400 GB or less can be expanded up to 32 TB.
        DB Systems with an initial storage size between 401-800 GB can be expanded up to 64 TB.
        DB Systems with an initial storage size between 801-1200 GB can be expanded up to 96 TB.
        DB Systems with an initial storage size of 1201 GB or more can be expanded up to 128 TB.


        :return: The data_storage_size_limit_in_gbs of this DataStorage.
        :rtype: int
        """
        return self._data_storage_size_limit_in_gbs

    @data_storage_size_limit_in_gbs.setter
    def data_storage_size_limit_in_gbs(self, data_storage_size_limit_in_gbs):
        """
        Sets the data_storage_size_limit_in_gbs of this DataStorage.
        The absolute limit the DB System's storage size may ever expand to, either manually or automatically.
        This limit is based based on the initial dataStorageSizeInGBs when the DB System was first created.
        Both dataStorageSizeInGBs and maxDataStorageSizeInGBs can not exceed this value.

        DB Systems with an initial storage size of 400 GB or less can be expanded up to 32 TB.
        DB Systems with an initial storage size between 401-800 GB can be expanded up to 64 TB.
        DB Systems with an initial storage size between 801-1200 GB can be expanded up to 96 TB.
        DB Systems with an initial storage size of 1201 GB or more can be expanded up to 128 TB.


        :param data_storage_size_limit_in_gbs: The data_storage_size_limit_in_gbs of this DataStorage.
        :type: int
        """
        self._data_storage_size_limit_in_gbs = data_storage_size_limit_in_gbs

    @property
    def is_auto_expand_storage_enabled(self):
        """
        Gets the is_auto_expand_storage_enabled of this DataStorage.
        Enable/disable automatic storage expansion. When set to true, the DB System will automatically
        add storage incrementally up to the value specified in maxStorageSizeInGBs.


        :return: The is_auto_expand_storage_enabled of this DataStorage.
        :rtype: bool
        """
        return self._is_auto_expand_storage_enabled

    @is_auto_expand_storage_enabled.setter
    def is_auto_expand_storage_enabled(self, is_auto_expand_storage_enabled):
        """
        Sets the is_auto_expand_storage_enabled of this DataStorage.
        Enable/disable automatic storage expansion. When set to true, the DB System will automatically
        add storage incrementally up to the value specified in maxStorageSizeInGBs.


        :param is_auto_expand_storage_enabled: The is_auto_expand_storage_enabled of this DataStorage.
        :type: bool
        """
        self._is_auto_expand_storage_enabled = is_auto_expand_storage_enabled

    @property
    def max_storage_size_in_gbs(self):
        """
        Gets the max_storage_size_in_gbs of this DataStorage.
        Maximum storage size this DB System can expand to. When isAutoExpandStorageEnabled
        is set to true, the DB System will add storage incrementally up to this value.

        DB Systems with an initial storage size of 400 GB or less can be expanded up to 32 TB.
        DB Systems with an initial storage size between 401-800 GB can be expanded up to 64 TB.
        DB Systems with an initial storage size between 801-1200 GB can be expanded up to 96 TB.
        DB Systems with an initial storage size of 1201 GB or more can be expanded up to 128 TB.

        It is not possible to decrease data storage size. You cannot set the maximum data storage size to less
        than either current DB System dataStorageSizeInGBs or allocatedStorageSizeInGBs.


        :return: The max_storage_size_in_gbs of this DataStorage.
        :rtype: int
        """
        return self._max_storage_size_in_gbs

    @max_storage_size_in_gbs.setter
    def max_storage_size_in_gbs(self, max_storage_size_in_gbs):
        """
        Sets the max_storage_size_in_gbs of this DataStorage.
        Maximum storage size this DB System can expand to. When isAutoExpandStorageEnabled
        is set to true, the DB System will add storage incrementally up to this value.

        DB Systems with an initial storage size of 400 GB or less can be expanded up to 32 TB.
        DB Systems with an initial storage size between 401-800 GB can be expanded up to 64 TB.
        DB Systems with an initial storage size between 801-1200 GB can be expanded up to 96 TB.
        DB Systems with an initial storage size of 1201 GB or more can be expanded up to 128 TB.

        It is not possible to decrease data storage size. You cannot set the maximum data storage size to less
        than either current DB System dataStorageSizeInGBs or allocatedStorageSizeInGBs.


        :param max_storage_size_in_gbs: The max_storage_size_in_gbs of this DataStorage.
        :type: int
        """
        self._max_storage_size_in_gbs = max_storage_size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
