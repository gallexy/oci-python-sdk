# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FleetTarget(object):
    """
    Description of FleetTarget.
    """

    #: A constant which can be used with the compliance_state property of a FleetTarget.
    #: This constant has a value of "UNKNOWN"
    COMPLIANCE_STATE_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the compliance_state property of a FleetTarget.
    #: This constant has a value of "COMPLIANT"
    COMPLIANCE_STATE_COMPLIANT = "COMPLIANT"

    #: A constant which can be used with the compliance_state property of a FleetTarget.
    #: This constant has a value of "NON_COMPLIANT"
    COMPLIANCE_STATE_NON_COMPLIANT = "NON_COMPLIANT"

    #: A constant which can be used with the compliance_state property of a FleetTarget.
    #: This constant has a value of "WARNING"
    COMPLIANCE_STATE_WARNING = "WARNING"

    #: A constant which can be used with the lifecycle_state property of a FleetTarget.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FleetTarget.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a FleetTarget.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new FleetTarget object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this FleetTarget.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this FleetTarget.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this FleetTarget.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this FleetTarget.
        :type time_created: datetime

        :param version:
            The value to assign to the version property of this FleetTarget.
        :type version: str

        :param product:
            The value to assign to the product property of this FleetTarget.
        :type product: str

        :param resource:
            The value to assign to the resource property of this FleetTarget.
        :type resource: oci.fleet_apps_management.models.TargetResource

        :param compliance_state:
            The value to assign to the compliance_state property of this FleetTarget.
            Allowed values for this property are: "UNKNOWN", "COMPLIANT", "NON_COMPLIANT", "WARNING"
        :type compliance_state: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FleetTarget.
            Allowed values for this property are: "ACTIVE", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param system_tags:
            The value to assign to the system_tags property of this FleetTarget.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'version': 'str',
            'product': 'str',
            'resource': 'TargetResource',
            'compliance_state': 'str',
            'lifecycle_state': 'str',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'version': 'version',
            'product': 'product',
            'resource': 'resource',
            'compliance_state': 'complianceState',
            'lifecycle_state': 'lifecycleState',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._version = None
        self._product = None
        self._resource = None
        self._compliance_state = None
        self._lifecycle_state = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FleetTarget.
        The OCID of the resource.


        :return: The id of this FleetTarget.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FleetTarget.
        The OCID of the resource.


        :param id: The id of this FleetTarget.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this FleetTarget.
        Tenancy OCID


        :return: The compartment_id of this FleetTarget.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FleetTarget.
        Tenancy OCID


        :param compartment_id: The compartment_id of this FleetTarget.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this FleetTarget.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this FleetTarget.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FleetTarget.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this FleetTarget.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this FleetTarget.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this FleetTarget.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FleetTarget.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this FleetTarget.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def version(self):
        """
        Gets the version of this FleetTarget.
        Current version of Target


        :return: The version of this FleetTarget.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this FleetTarget.
        Current version of Target


        :param version: The version of this FleetTarget.
        :type: str
        """
        self._version = version

    @property
    def product(self):
        """
        Gets the product of this FleetTarget.
        Product to which the target belongs to.


        :return: The product of this FleetTarget.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this FleetTarget.
        Product to which the target belongs to.


        :param product: The product of this FleetTarget.
        :type: str
        """
        self._product = product

    @property
    def resource(self):
        """
        Gets the resource of this FleetTarget.

        :return: The resource of this FleetTarget.
        :rtype: oci.fleet_apps_management.models.TargetResource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this FleetTarget.

        :param resource: The resource of this FleetTarget.
        :type: oci.fleet_apps_management.models.TargetResource
        """
        self._resource = resource

    @property
    def compliance_state(self):
        """
        Gets the compliance_state of this FleetTarget.
        Last known compliance state of Target.

        Allowed values for this property are: "UNKNOWN", "COMPLIANT", "NON_COMPLIANT", "WARNING"


        :return: The compliance_state of this FleetTarget.
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        """
        Sets the compliance_state of this FleetTarget.
        Last known compliance state of Target.


        :param compliance_state: The compliance_state of this FleetTarget.
        :type: str
        """
        allowed_values = ["UNKNOWN", "COMPLIANT", "NON_COMPLIANT", "WARNING"]
        if not value_allowed_none_or_none_sentinel(compliance_state, allowed_values):
            raise ValueError(
                f"Invalid value for `compliance_state`, must be None or one of {allowed_values}"
            )
        self._compliance_state = compliance_state

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this FleetTarget.
        The current state of the FleetTarget.

        Allowed values for this property are: "ACTIVE", "DELETED", "FAILED"


        :return: The lifecycle_state of this FleetTarget.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FleetTarget.
        The current state of the FleetTarget.


        :param lifecycle_state: The lifecycle_state of this FleetTarget.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                f"Invalid value for `lifecycle_state`, must be None or one of {allowed_values}"
            )
        self._lifecycle_state = lifecycle_state

    @property
    def system_tags(self):
        """
        Gets the system_tags of this FleetTarget.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this FleetTarget.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this FleetTarget.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this FleetTarget.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
