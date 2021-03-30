# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsMetric(object):
    """
    LogAnalyticsMetric
    """

    #: A constant which can be used with the metric_type property of a LogAnalyticsMetric.
    #: This constant has a value of "COUNT"
    METRIC_TYPE_COUNT = "COUNT"

    #: A constant which can be used with the metric_type property of a LogAnalyticsMetric.
    #: This constant has a value of "SUM"
    METRIC_TYPE_SUM = "SUM"

    #: A constant which can be used with the metric_type property of a LogAnalyticsMetric.
    #: This constant has a value of "AVERAGE"
    METRIC_TYPE_AVERAGE = "AVERAGE"

    #: A constant which can be used with the metric_type property of a LogAnalyticsMetric.
    #: This constant has a value of "COUNT_DISTRIBUTION"
    METRIC_TYPE_COUNT_DISTRIBUTION = "COUNT_DISTRIBUTION"

    #: A constant which can be used with the metric_type property of a LogAnalyticsMetric.
    #: This constant has a value of "SUM_DISTRIBUTION"
    METRIC_TYPE_SUM_DISTRIBUTION = "SUM_DISTRIBUTION"

    #: A constant which can be used with the metric_type property of a LogAnalyticsMetric.
    #: This constant has a value of "AVERAGE_DISTRIBUTION"
    METRIC_TYPE_AVERAGE_DISTRIBUTION = "AVERAGE_DISTRIBUTION"

    #: A constant which can be used with the operator property of a LogAnalyticsMetric.
    #: This constant has a value of "CONTAINS_IGNORE_CASE"
    OPERATOR_CONTAINS_IGNORE_CASE = "CONTAINS_IGNORE_CASE"

    #: A constant which can be used with the operator property of a LogAnalyticsMetric.
    #: This constant has a value of "IN_IGNORE_CASE"
    OPERATOR_IN_IGNORE_CASE = "IN_IGNORE_CASE"

    #: A constant which can be used with the operator property of a LogAnalyticsMetric.
    #: This constant has a value of "EQUAL_IGNORE_CASE"
    OPERATOR_EQUAL_IGNORE_CASE = "EQUAL_IGNORE_CASE"

    #: A constant which can be used with the operator property of a LogAnalyticsMetric.
    #: This constant has a value of "NOT_NULL"
    OPERATOR_NOT_NULL = "NOT_NULL"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsMetric object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param aggregation_field:
            The value to assign to the aggregation_field property of this LogAnalyticsMetric.
        :type aggregation_field: str

        :param bucket_metadata:
            The value to assign to the bucket_metadata property of this LogAnalyticsMetric.
        :type bucket_metadata: str

        :param clock_period:
            The value to assign to the clock_period property of this LogAnalyticsMetric.
        :type clock_period: str

        :param description:
            The value to assign to the description property of this LogAnalyticsMetric.
        :type description: str

        :param edit_version:
            The value to assign to the edit_version property of this LogAnalyticsMetric.
        :type edit_version: int

        :param field_name:
            The value to assign to the field_name property of this LogAnalyticsMetric.
        :type field_name: str

        :param field_values:
            The value to assign to the field_values property of this LogAnalyticsMetric.
        :type field_values: list[str]

        :param grouping_field:
            The value to assign to the grouping_field property of this LogAnalyticsMetric.
        :type grouping_field: str

        :param is_enabled:
            The value to assign to the is_enabled property of this LogAnalyticsMetric.
        :type is_enabled: bool

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsMetric.
        :type is_system: bool

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsMetric.
        :type display_name: str

        :param metric_reference:
            The value to assign to the metric_reference property of this LogAnalyticsMetric.
        :type metric_reference: int

        :param name:
            The value to assign to the name property of this LogAnalyticsMetric.
        :type name: str

        :param metric_type:
            The value to assign to the metric_type property of this LogAnalyticsMetric.
            Allowed values for this property are: "COUNT", "SUM", "AVERAGE", "COUNT_DISTRIBUTION", "SUM_DISTRIBUTION", "AVERAGE_DISTRIBUTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_type: str

        :param is_metric_source_enabled:
            The value to assign to the is_metric_source_enabled property of this LogAnalyticsMetric.
        :type is_metric_source_enabled: bool

        :param operator:
            The value to assign to the operator property of this LogAnalyticsMetric.
            Allowed values for this property are: "CONTAINS_IGNORE_CASE", "IN_IGNORE_CASE", "EQUAL_IGNORE_CASE", "NOT_NULL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operator: str

        :param sources:
            The value to assign to the sources property of this LogAnalyticsMetric.
        :type sources: list[oci.log_analytics.models.LogAnalyticsSource]

        :param entity_type:
            The value to assign to the entity_type property of this LogAnalyticsMetric.
        :type entity_type: str

        :param time_updated:
            The value to assign to the time_updated property of this LogAnalyticsMetric.
        :type time_updated: datetime

        :param unit_type:
            The value to assign to the unit_type property of this LogAnalyticsMetric.
        :type unit_type: str

        :param is_user_customized:
            The value to assign to the is_user_customized property of this LogAnalyticsMetric.
        :type is_user_customized: bool

        """
        self.swagger_types = {
            'aggregation_field': 'str',
            'bucket_metadata': 'str',
            'clock_period': 'str',
            'description': 'str',
            'edit_version': 'int',
            'field_name': 'str',
            'field_values': 'list[str]',
            'grouping_field': 'str',
            'is_enabled': 'bool',
            'is_system': 'bool',
            'display_name': 'str',
            'metric_reference': 'int',
            'name': 'str',
            'metric_type': 'str',
            'is_metric_source_enabled': 'bool',
            'operator': 'str',
            'sources': 'list[LogAnalyticsSource]',
            'entity_type': 'str',
            'time_updated': 'datetime',
            'unit_type': 'str',
            'is_user_customized': 'bool'
        }

        self.attribute_map = {
            'aggregation_field': 'aggregationField',
            'bucket_metadata': 'bucketMetadata',
            'clock_period': 'clockPeriod',
            'description': 'description',
            'edit_version': 'editVersion',
            'field_name': 'fieldName',
            'field_values': 'fieldValues',
            'grouping_field': 'groupingField',
            'is_enabled': 'isEnabled',
            'is_system': 'isSystem',
            'display_name': 'displayName',
            'metric_reference': 'metricReference',
            'name': 'name',
            'metric_type': 'metricType',
            'is_metric_source_enabled': 'isMetricSourceEnabled',
            'operator': 'operator',
            'sources': 'sources',
            'entity_type': 'entityType',
            'time_updated': 'timeUpdated',
            'unit_type': 'unitType',
            'is_user_customized': 'isUserCustomized'
        }

        self._aggregation_field = None
        self._bucket_metadata = None
        self._clock_period = None
        self._description = None
        self._edit_version = None
        self._field_name = None
        self._field_values = None
        self._grouping_field = None
        self._is_enabled = None
        self._is_system = None
        self._display_name = None
        self._metric_reference = None
        self._name = None
        self._metric_type = None
        self._is_metric_source_enabled = None
        self._operator = None
        self._sources = None
        self._entity_type = None
        self._time_updated = None
        self._unit_type = None
        self._is_user_customized = None

    @property
    def aggregation_field(self):
        """
        Gets the aggregation_field of this LogAnalyticsMetric.
        The aggregation field.


        :return: The aggregation_field of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._aggregation_field

    @aggregation_field.setter
    def aggregation_field(self, aggregation_field):
        """
        Sets the aggregation_field of this LogAnalyticsMetric.
        The aggregation field.


        :param aggregation_field: The aggregation_field of this LogAnalyticsMetric.
        :type: str
        """
        self._aggregation_field = aggregation_field

    @property
    def bucket_metadata(self):
        """
        Gets the bucket_metadata of this LogAnalyticsMetric.
        The bucket metadata.


        :return: The bucket_metadata of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._bucket_metadata

    @bucket_metadata.setter
    def bucket_metadata(self, bucket_metadata):
        """
        Sets the bucket_metadata of this LogAnalyticsMetric.
        The bucket metadata.


        :param bucket_metadata: The bucket_metadata of this LogAnalyticsMetric.
        :type: str
        """
        self._bucket_metadata = bucket_metadata

    @property
    def clock_period(self):
        """
        Gets the clock_period of this LogAnalyticsMetric.
        The clock period.


        :return: The clock_period of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._clock_period

    @clock_period.setter
    def clock_period(self, clock_period):
        """
        Sets the clock_period of this LogAnalyticsMetric.
        The clock period.


        :param clock_period: The clock_period of this LogAnalyticsMetric.
        :type: str
        """
        self._clock_period = clock_period

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsMetric.
        The metric description.


        :return: The description of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsMetric.
        The metric description.


        :param description: The description of this LogAnalyticsMetric.
        :type: str
        """
        self._description = description

    @property
    def edit_version(self):
        """
        Gets the edit_version of this LogAnalyticsMetric.
        The metric edit version.


        :return: The edit_version of this LogAnalyticsMetric.
        :rtype: int
        """
        return self._edit_version

    @edit_version.setter
    def edit_version(self, edit_version):
        """
        Sets the edit_version of this LogAnalyticsMetric.
        The metric edit version.


        :param edit_version: The edit_version of this LogAnalyticsMetric.
        :type: int
        """
        self._edit_version = edit_version

    @property
    def field_name(self):
        """
        Gets the field_name of this LogAnalyticsMetric.
        The field name.


        :return: The field_name of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this LogAnalyticsMetric.
        The field name.


        :param field_name: The field_name of this LogAnalyticsMetric.
        :type: str
        """
        self._field_name = field_name

    @property
    def field_values(self):
        """
        Gets the field_values of this LogAnalyticsMetric.
        The field values.


        :return: The field_values of this LogAnalyticsMetric.
        :rtype: list[str]
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this LogAnalyticsMetric.
        The field values.


        :param field_values: The field_values of this LogAnalyticsMetric.
        :type: list[str]
        """
        self._field_values = field_values

    @property
    def grouping_field(self):
        """
        Gets the grouping_field of this LogAnalyticsMetric.
        The grouping fields.


        :return: The grouping_field of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._grouping_field

    @grouping_field.setter
    def grouping_field(self, grouping_field):
        """
        Sets the grouping_field of this LogAnalyticsMetric.
        The grouping fields.


        :param grouping_field: The grouping_field of this LogAnalyticsMetric.
        :type: str
        """
        self._grouping_field = grouping_field

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this LogAnalyticsMetric.
        A flag inidcating whether or not the metric is enabled.


        :return: The is_enabled of this LogAnalyticsMetric.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this LogAnalyticsMetric.
        A flag inidcating whether or not the metric is enabled.


        :param is_enabled: The is_enabled of this LogAnalyticsMetric.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsMetric.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :return: The is_system of this LogAnalyticsMetric.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsMetric.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :param is_system: The is_system of this LogAnalyticsMetric.
        :type: bool
        """
        self._is_system = is_system

    @property
    def display_name(self):
        """
        Gets the display_name of this LogAnalyticsMetric.
        The metric display name.


        :return: The display_name of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsMetric.
        The metric display name.


        :param display_name: The display_name of this LogAnalyticsMetric.
        :type: str
        """
        self._display_name = display_name

    @property
    def metric_reference(self):
        """
        Gets the metric_reference of this LogAnalyticsMetric.
        The metric unique identifier.


        :return: The metric_reference of this LogAnalyticsMetric.
        :rtype: int
        """
        return self._metric_reference

    @metric_reference.setter
    def metric_reference(self, metric_reference):
        """
        Sets the metric_reference of this LogAnalyticsMetric.
        The metric unique identifier.


        :param metric_reference: The metric_reference of this LogAnalyticsMetric.
        :type: int
        """
        self._metric_reference = metric_reference

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsMetric.
        The metric name.


        :return: The name of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsMetric.
        The metric name.


        :param name: The name of this LogAnalyticsMetric.
        :type: str
        """
        self._name = name

    @property
    def metric_type(self):
        """
        Gets the metric_type of this LogAnalyticsMetric.
        The metric type, specifying the type of aggreation to perform.  Default value
        is COUNT.

        Allowed values for this property are: "COUNT", "SUM", "AVERAGE", "COUNT_DISTRIBUTION", "SUM_DISTRIBUTION", "AVERAGE_DISTRIBUTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metric_type of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """
        Sets the metric_type of this LogAnalyticsMetric.
        The metric type, specifying the type of aggreation to perform.  Default value
        is COUNT.


        :param metric_type: The metric_type of this LogAnalyticsMetric.
        :type: str
        """
        allowed_values = ["COUNT", "SUM", "AVERAGE", "COUNT_DISTRIBUTION", "SUM_DISTRIBUTION", "AVERAGE_DISTRIBUTION"]
        if not value_allowed_none_or_none_sentinel(metric_type, allowed_values):
            metric_type = 'UNKNOWN_ENUM_VALUE'
        self._metric_type = metric_type

    @property
    def is_metric_source_enabled(self):
        """
        Gets the is_metric_source_enabled of this LogAnalyticsMetric.
        A flag specifying whether or not the metric source is enabled.


        :return: The is_metric_source_enabled of this LogAnalyticsMetric.
        :rtype: bool
        """
        return self._is_metric_source_enabled

    @is_metric_source_enabled.setter
    def is_metric_source_enabled(self, is_metric_source_enabled):
        """
        Sets the is_metric_source_enabled of this LogAnalyticsMetric.
        A flag specifying whether or not the metric source is enabled.


        :param is_metric_source_enabled: The is_metric_source_enabled of this LogAnalyticsMetric.
        :type: bool
        """
        self._is_metric_source_enabled = is_metric_source_enabled

    @property
    def operator(self):
        """
        Gets the operator of this LogAnalyticsMetric.
        The metric operator.

        Allowed values for this property are: "CONTAINS_IGNORE_CASE", "IN_IGNORE_CASE", "EQUAL_IGNORE_CASE", "NOT_NULL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operator of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this LogAnalyticsMetric.
        The metric operator.


        :param operator: The operator of this LogAnalyticsMetric.
        :type: str
        """
        allowed_values = ["CONTAINS_IGNORE_CASE", "IN_IGNORE_CASE", "EQUAL_IGNORE_CASE", "NOT_NULL"]
        if not value_allowed_none_or_none_sentinel(operator, allowed_values):
            operator = 'UNKNOWN_ENUM_VALUE'
        self._operator = operator

    @property
    def sources(self):
        """
        Gets the sources of this LogAnalyticsMetric.
        The metric sources.


        :return: The sources of this LogAnalyticsMetric.
        :rtype: list[oci.log_analytics.models.LogAnalyticsSource]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this LogAnalyticsMetric.
        The metric sources.


        :param sources: The sources of this LogAnalyticsMetric.
        :type: list[oci.log_analytics.models.LogAnalyticsSource]
        """
        self._sources = sources

    @property
    def entity_type(self):
        """
        Gets the entity_type of this LogAnalyticsMetric.
        The entity type.


        :return: The entity_type of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this LogAnalyticsMetric.
        The entity type.


        :param entity_type: The entity_type of this LogAnalyticsMetric.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def time_updated(self):
        """
        Gets the time_updated of this LogAnalyticsMetric.
        The last updated date.


        :return: The time_updated of this LogAnalyticsMetric.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LogAnalyticsMetric.
        The last updated date.


        :param time_updated: The time_updated of this LogAnalyticsMetric.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def unit_type(self):
        """
        Gets the unit_type of this LogAnalyticsMetric.
        The unit type.


        :return: The unit_type of this LogAnalyticsMetric.
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """
        Sets the unit_type of this LogAnalyticsMetric.
        The unit type.


        :param unit_type: The unit_type of this LogAnalyticsMetric.
        :type: str
        """
        self._unit_type = unit_type

    @property
    def is_user_customized(self):
        """
        Gets the is_user_customized of this LogAnalyticsMetric.
        A flag specifying whether or not this is a custom (user defined) metric.


        :return: The is_user_customized of this LogAnalyticsMetric.
        :rtype: bool
        """
        return self._is_user_customized

    @is_user_customized.setter
    def is_user_customized(self, is_user_customized):
        """
        Sets the is_user_customized of this LogAnalyticsMetric.
        A flag specifying whether or not this is a custom (user defined) metric.


        :param is_user_customized: The is_user_customized of this LogAnalyticsMetric.
        :type: bool
        """
        self._is_user_customized = is_user_customized

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
