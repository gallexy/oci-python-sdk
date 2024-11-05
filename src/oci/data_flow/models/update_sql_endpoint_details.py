# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200129


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSqlEndpointDetails(object):
    """
    The information about all updatable parameters of a SQL Endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSqlEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSqlEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSqlEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param display_name:
            The value to assign to the display_name property of this UpdateSqlEndpointDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateSqlEndpointDetails.
        :type description: str

        :param driver_shape:
            The value to assign to the driver_shape property of this UpdateSqlEndpointDetails.
        :type driver_shape: str

        :param driver_shape_config:
            The value to assign to the driver_shape_config property of this UpdateSqlEndpointDetails.
        :type driver_shape_config: oci.data_flow.models.ShapeConfig

        :param executor_shape:
            The value to assign to the executor_shape property of this UpdateSqlEndpointDetails.
        :type executor_shape: str

        :param executor_shape_config:
            The value to assign to the executor_shape_config property of this UpdateSqlEndpointDetails.
        :type executor_shape_config: oci.data_flow.models.ShapeConfig

        :param min_executor_count:
            The value to assign to the min_executor_count property of this UpdateSqlEndpointDetails.
        :type min_executor_count: int

        :param max_executor_count:
            The value to assign to the max_executor_count property of this UpdateSqlEndpointDetails.
        :type max_executor_count: int

        :param metastore_id:
            The value to assign to the metastore_id property of this UpdateSqlEndpointDetails.
        :type metastore_id: str

        :param lake_id:
            The value to assign to the lake_id property of this UpdateSqlEndpointDetails.
        :type lake_id: str

        :param spark_advanced_configurations:
            The value to assign to the spark_advanced_configurations property of this UpdateSqlEndpointDetails.
        :type spark_advanced_configurations: dict(str, str)

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'display_name': 'str',
            'description': 'str',
            'driver_shape': 'str',
            'driver_shape_config': 'ShapeConfig',
            'executor_shape': 'str',
            'executor_shape_config': 'ShapeConfig',
            'min_executor_count': 'int',
            'max_executor_count': 'int',
            'metastore_id': 'str',
            'lake_id': 'str',
            'spark_advanced_configurations': 'dict(str, str)'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'display_name': 'displayName',
            'description': 'description',
            'driver_shape': 'driverShape',
            'driver_shape_config': 'driverShapeConfig',
            'executor_shape': 'executorShape',
            'executor_shape_config': 'executorShapeConfig',
            'min_executor_count': 'minExecutorCount',
            'max_executor_count': 'maxExecutorCount',
            'metastore_id': 'metastoreId',
            'lake_id': 'lakeId',
            'spark_advanced_configurations': 'sparkAdvancedConfigurations'
        }

        self._defined_tags = None
        self._freeform_tags = None
        self._display_name = None
        self._description = None
        self._driver_shape = None
        self._driver_shape_config = None
        self._executor_shape = None
        self._executor_shape_config = None
        self._min_executor_count = None
        self._max_executor_count = None
        self._metastore_id = None
        self._lake_id = None
        self._spark_advanced_configurations = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSqlEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateSqlEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSqlEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateSqlEndpointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSqlEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateSqlEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSqlEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateSqlEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateSqlEndpointDetails.
        The SQL Endpoint name, which can be changed.


        :return: The display_name of this UpdateSqlEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateSqlEndpointDetails.
        The SQL Endpoint name, which can be changed.


        :param display_name: The display_name of this UpdateSqlEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateSqlEndpointDetails.
        The description of CreateSQLEndpointDetails.


        :return: The description of this UpdateSqlEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateSqlEndpointDetails.
        The description of CreateSQLEndpointDetails.


        :param description: The description of this UpdateSqlEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def driver_shape(self):
        """
        Gets the driver_shape of this UpdateSqlEndpointDetails.
        The shape of the SQL Endpoint driver instance.


        :return: The driver_shape of this UpdateSqlEndpointDetails.
        :rtype: str
        """
        return self._driver_shape

    @driver_shape.setter
    def driver_shape(self, driver_shape):
        """
        Sets the driver_shape of this UpdateSqlEndpointDetails.
        The shape of the SQL Endpoint driver instance.


        :param driver_shape: The driver_shape of this UpdateSqlEndpointDetails.
        :type: str
        """
        self._driver_shape = driver_shape

    @property
    def driver_shape_config(self):
        """
        Gets the driver_shape_config of this UpdateSqlEndpointDetails.

        :return: The driver_shape_config of this UpdateSqlEndpointDetails.
        :rtype: oci.data_flow.models.ShapeConfig
        """
        return self._driver_shape_config

    @driver_shape_config.setter
    def driver_shape_config(self, driver_shape_config):
        """
        Sets the driver_shape_config of this UpdateSqlEndpointDetails.

        :param driver_shape_config: The driver_shape_config of this UpdateSqlEndpointDetails.
        :type: oci.data_flow.models.ShapeConfig
        """
        self._driver_shape_config = driver_shape_config

    @property
    def executor_shape(self):
        """
        Gets the executor_shape of this UpdateSqlEndpointDetails.
        The shape of the SQL Endpoint worker instance.


        :return: The executor_shape of this UpdateSqlEndpointDetails.
        :rtype: str
        """
        return self._executor_shape

    @executor_shape.setter
    def executor_shape(self, executor_shape):
        """
        Sets the executor_shape of this UpdateSqlEndpointDetails.
        The shape of the SQL Endpoint worker instance.


        :param executor_shape: The executor_shape of this UpdateSqlEndpointDetails.
        :type: str
        """
        self._executor_shape = executor_shape

    @property
    def executor_shape_config(self):
        """
        Gets the executor_shape_config of this UpdateSqlEndpointDetails.

        :return: The executor_shape_config of this UpdateSqlEndpointDetails.
        :rtype: oci.data_flow.models.ShapeConfig
        """
        return self._executor_shape_config

    @executor_shape_config.setter
    def executor_shape_config(self, executor_shape_config):
        """
        Sets the executor_shape_config of this UpdateSqlEndpointDetails.

        :param executor_shape_config: The executor_shape_config of this UpdateSqlEndpointDetails.
        :type: oci.data_flow.models.ShapeConfig
        """
        self._executor_shape_config = executor_shape_config

    @property
    def min_executor_count(self):
        """
        Gets the min_executor_count of this UpdateSqlEndpointDetails.
        The minimum number of executors.


        :return: The min_executor_count of this UpdateSqlEndpointDetails.
        :rtype: int
        """
        return self._min_executor_count

    @min_executor_count.setter
    def min_executor_count(self, min_executor_count):
        """
        Sets the min_executor_count of this UpdateSqlEndpointDetails.
        The minimum number of executors.


        :param min_executor_count: The min_executor_count of this UpdateSqlEndpointDetails.
        :type: int
        """
        self._min_executor_count = min_executor_count

    @property
    def max_executor_count(self):
        """
        Gets the max_executor_count of this UpdateSqlEndpointDetails.
        The maximum number of executors.


        :return: The max_executor_count of this UpdateSqlEndpointDetails.
        :rtype: int
        """
        return self._max_executor_count

    @max_executor_count.setter
    def max_executor_count(self, max_executor_count):
        """
        Sets the max_executor_count of this UpdateSqlEndpointDetails.
        The maximum number of executors.


        :param max_executor_count: The max_executor_count of this UpdateSqlEndpointDetails.
        :type: int
        """
        self._max_executor_count = max_executor_count

    @property
    def metastore_id(self):
        """
        Gets the metastore_id of this UpdateSqlEndpointDetails.
        Metastore OCID


        :return: The metastore_id of this UpdateSqlEndpointDetails.
        :rtype: str
        """
        return self._metastore_id

    @metastore_id.setter
    def metastore_id(self, metastore_id):
        """
        Sets the metastore_id of this UpdateSqlEndpointDetails.
        Metastore OCID


        :param metastore_id: The metastore_id of this UpdateSqlEndpointDetails.
        :type: str
        """
        self._metastore_id = metastore_id

    @property
    def lake_id(self):
        """
        Gets the lake_id of this UpdateSqlEndpointDetails.
        OCI lake OCID


        :return: The lake_id of this UpdateSqlEndpointDetails.
        :rtype: str
        """
        return self._lake_id

    @lake_id.setter
    def lake_id(self, lake_id):
        """
        Sets the lake_id of this UpdateSqlEndpointDetails.
        OCI lake OCID


        :param lake_id: The lake_id of this UpdateSqlEndpointDetails.
        :type: str
        """
        self._lake_id = lake_id

    @property
    def spark_advanced_configurations(self):
        """
        Gets the spark_advanced_configurations of this UpdateSqlEndpointDetails.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties.
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :return: The spark_advanced_configurations of this UpdateSqlEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._spark_advanced_configurations

    @spark_advanced_configurations.setter
    def spark_advanced_configurations(self, spark_advanced_configurations):
        """
        Sets the spark_advanced_configurations of this UpdateSqlEndpointDetails.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties.
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :param spark_advanced_configurations: The spark_advanced_configurations of this UpdateSqlEndpointDetails.
        :type: dict(str, str)
        """
        self._spark_advanced_configurations = spark_advanced_configurations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
