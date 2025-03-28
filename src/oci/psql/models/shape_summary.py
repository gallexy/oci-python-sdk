# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeSummary(object):
    """
    Summary of the database system shape.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ShapeSummary.
        :type id: str

        :param shape:
            The value to assign to the shape property of this ShapeSummary.
        :type shape: str

        :param is_flexible:
            The value to assign to the is_flexible property of this ShapeSummary.
        :type is_flexible: bool

        :param ocpu_count:
            The value to assign to the ocpu_count property of this ShapeSummary.
        :type ocpu_count: int

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this ShapeSummary.
        :type memory_size_in_gbs: int

        :param shape_ocpu_options:
            The value to assign to the shape_ocpu_options property of this ShapeSummary.
        :type shape_ocpu_options: oci.psql.models.ShapeOcpuOptions

        :param shape_memory_options:
            The value to assign to the shape_memory_options property of this ShapeSummary.
        :type shape_memory_options: oci.psql.models.ShapeMemoryOptions

        """
        self.swagger_types = {
            'id': 'str',
            'shape': 'str',
            'is_flexible': 'bool',
            'ocpu_count': 'int',
            'memory_size_in_gbs': 'int',
            'shape_ocpu_options': 'ShapeOcpuOptions',
            'shape_memory_options': 'ShapeMemoryOptions'
        }
        self.attribute_map = {
            'id': 'id',
            'shape': 'shape',
            'is_flexible': 'isFlexible',
            'ocpu_count': 'ocpuCount',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'shape_ocpu_options': 'shapeOcpuOptions',
            'shape_memory_options': 'shapeMemoryOptions'
        }
        self._id = None
        self._shape = None
        self._is_flexible = None
        self._ocpu_count = None
        self._memory_size_in_gbs = None
        self._shape_ocpu_options = None
        self._shape_memory_options = None

    @property
    def id(self):
        """
        Gets the id of this ShapeSummary.
        A unique identifier for the shape.


        :return: The id of this ShapeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ShapeSummary.
        A unique identifier for the shape.


        :param id: The id of this ShapeSummary.
        :type: str
        """
        self._id = id

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this ShapeSummary.
        The name of the Compute VM shape.
        Example: `VM.Standard.E4.Flex`


        :return: The shape of this ShapeSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this ShapeSummary.
        The name of the Compute VM shape.
        Example: `VM.Standard.E4.Flex`


        :param shape: The shape of this ShapeSummary.
        :type: str
        """
        self._shape = shape

    @property
    def is_flexible(self):
        """
        Gets the is_flexible of this ShapeSummary.
        Indicates if the shape is a flex shape.


        :return: The is_flexible of this ShapeSummary.
        :rtype: bool
        """
        return self._is_flexible

    @is_flexible.setter
    def is_flexible(self, is_flexible):
        """
        Sets the is_flexible of this ShapeSummary.
        Indicates if the shape is a flex shape.


        :param is_flexible: The is_flexible of this ShapeSummary.
        :type: bool
        """
        self._is_flexible = is_flexible

    @property
    def ocpu_count(self):
        """
        **[Required]** Gets the ocpu_count of this ShapeSummary.
        The number of OCPUs.


        :return: The ocpu_count of this ShapeSummary.
        :rtype: int
        """
        return self._ocpu_count

    @ocpu_count.setter
    def ocpu_count(self, ocpu_count):
        """
        Sets the ocpu_count of this ShapeSummary.
        The number of OCPUs.


        :param ocpu_count: The ocpu_count of this ShapeSummary.
        :type: int
        """
        self._ocpu_count = ocpu_count

    @property
    def memory_size_in_gbs(self):
        """
        **[Required]** Gets the memory_size_in_gbs of this ShapeSummary.
        The amount of memory in gigabytes.


        :return: The memory_size_in_gbs of this ShapeSummary.
        :rtype: int
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this ShapeSummary.
        The amount of memory in gigabytes.


        :param memory_size_in_gbs: The memory_size_in_gbs of this ShapeSummary.
        :type: int
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def shape_ocpu_options(self):
        """
        Gets the shape_ocpu_options of this ShapeSummary.

        :return: The shape_ocpu_options of this ShapeSummary.
        :rtype: oci.psql.models.ShapeOcpuOptions
        """
        return self._shape_ocpu_options

    @shape_ocpu_options.setter
    def shape_ocpu_options(self, shape_ocpu_options):
        """
        Sets the shape_ocpu_options of this ShapeSummary.

        :param shape_ocpu_options: The shape_ocpu_options of this ShapeSummary.
        :type: oci.psql.models.ShapeOcpuOptions
        """
        self._shape_ocpu_options = shape_ocpu_options

    @property
    def shape_memory_options(self):
        """
        Gets the shape_memory_options of this ShapeSummary.

        :return: The shape_memory_options of this ShapeSummary.
        :rtype: oci.psql.models.ShapeMemoryOptions
        """
        return self._shape_memory_options

    @shape_memory_options.setter
    def shape_memory_options(self, shape_memory_options):
        """
        Sets the shape_memory_options of this ShapeSummary.

        :param shape_memory_options: The shape_memory_options of this ShapeSummary.
        :type: oci.psql.models.ShapeMemoryOptions
        """
        self._shape_memory_options = shape_memory_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
