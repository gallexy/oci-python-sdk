# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActionGroup(object):
    """
    Action Group.
    """

    #: A constant which can be used with the type property of a ActionGroup.
    #: This constant has a value of "PRODUCT"
    TYPE_PRODUCT = "PRODUCT"

    #: A constant which can be used with the type property of a ActionGroup.
    #: This constant has a value of "ENVIRONMENT"
    TYPE_ENVIRONMENT = "ENVIRONMENT"

    def __init__(self, **kwargs):
        """
        Initializes a new ActionGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this ActionGroup.
        :type resource_id: str

        :param type:
            The value to assign to the type property of this ActionGroup.
            Allowed values for this property are: "PRODUCT", "ENVIRONMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param application_type:
            The value to assign to the application_type property of this ActionGroup.
        :type application_type: str

        :param product:
            The value to assign to the product property of this ActionGroup.
        :type product: str

        :param lifecycle_operation:
            The value to assign to the lifecycle_operation property of this ActionGroup.
        :type lifecycle_operation: str

        :param runbook_id:
            The value to assign to the runbook_id property of this ActionGroup.
        :type runbook_id: str

        :param target_id:
            The value to assign to the target_id property of this ActionGroup.
        :type target_id: str

        :param subjects:
            The value to assign to the subjects property of this ActionGroup.
        :type subjects: list[str]

        """
        self.swagger_types = {
            'resource_id': 'str',
            'type': 'str',
            'application_type': 'str',
            'product': 'str',
            'lifecycle_operation': 'str',
            'runbook_id': 'str',
            'target_id': 'str',
            'subjects': 'list[str]'
        }

        self.attribute_map = {
            'resource_id': 'resourceId',
            'type': 'type',
            'application_type': 'applicationType',
            'product': 'product',
            'lifecycle_operation': 'lifecycleOperation',
            'runbook_id': 'runbookId',
            'target_id': 'targetId',
            'subjects': 'subjects'
        }

        self._resource_id = None
        self._type = None
        self._application_type = None
        self._product = None
        self._lifecycle_operation = None
        self._runbook_id = None
        self._target_id = None
        self._subjects = None

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this ActionGroup.
        Provide the ID of the resource. Example fleet ID.


        :return: The resource_id of this ActionGroup.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this ActionGroup.
        Provide the ID of the resource. Example fleet ID.


        :param resource_id: The resource_id of this ActionGroup.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def type(self):
        """
        Gets the type of this ActionGroup.
        ActionGroup Type associated.

        Allowed values for this property are: "PRODUCT", "ENVIRONMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ActionGroup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ActionGroup.
        ActionGroup Type associated.


        :param type: The type of this ActionGroup.
        :type: str
        """
        allowed_values = ["PRODUCT", "ENVIRONMENT"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def application_type(self):
        """
        Gets the application_type of this ActionGroup.
        Application Type associated.
        Only applicable if type is ENVIRONMENT.


        :return: The application_type of this ActionGroup.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """
        Sets the application_type of this ActionGroup.
        Application Type associated.
        Only applicable if type is ENVIRONMENT.


        :param application_type: The application_type of this ActionGroup.
        :type: str
        """
        self._application_type = application_type

    @property
    def product(self):
        """
        Gets the product of this ActionGroup.
        Product associated.
        Only applicable if type is PRODUCT.


        :return: The product of this ActionGroup.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this ActionGroup.
        Product associated.
        Only applicable if type is PRODUCT.


        :param product: The product of this ActionGroup.
        :type: str
        """
        self._product = product

    @property
    def lifecycle_operation(self):
        """
        Gets the lifecycle_operation of this ActionGroup.
        LifeCycle Operation


        :return: The lifecycle_operation of this ActionGroup.
        :rtype: str
        """
        return self._lifecycle_operation

    @lifecycle_operation.setter
    def lifecycle_operation(self, lifecycle_operation):
        """
        Sets the lifecycle_operation of this ActionGroup.
        LifeCycle Operation


        :param lifecycle_operation: The lifecycle_operation of this ActionGroup.
        :type: str
        """
        self._lifecycle_operation = lifecycle_operation

    @property
    def runbook_id(self):
        """
        **[Required]** Gets the runbook_id of this ActionGroup.
        ID of the runbook


        :return: The runbook_id of this ActionGroup.
        :rtype: str
        """
        return self._runbook_id

    @runbook_id.setter
    def runbook_id(self, runbook_id):
        """
        Sets the runbook_id of this ActionGroup.
        ID of the runbook


        :param runbook_id: The runbook_id of this ActionGroup.
        :type: str
        """
        self._runbook_id = runbook_id

    @property
    def target_id(self):
        """
        Gets the target_id of this ActionGroup.
        Provide the target if schedule is created against the target


        :return: The target_id of this ActionGroup.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this ActionGroup.
        Provide the target if schedule is created against the target


        :param target_id: The target_id of this ActionGroup.
        :type: str
        """
        self._target_id = target_id

    @property
    def subjects(self):
        """
        Gets the subjects of this ActionGroup.
        Provide subjects that need to be considered for the schedule.


        :return: The subjects of this ActionGroup.
        :rtype: list[str]
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """
        Sets the subjects of this ActionGroup.
        Provide subjects that need to be considered for the schedule.


        :param subjects: The subjects of this ActionGroup.
        :type: list[str]
        """
        self._subjects = subjects

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
