# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Service(object):
    """
    A Service which can be used to identify the running service. It uses port & protocol information.
    """

    #: A constant which can be used with the type property of a Service.
    #: This constant has a value of "TCP_SERVICE"
    TYPE_TCP_SERVICE = "TCP_SERVICE"

    #: A constant which can be used with the type property of a Service.
    #: This constant has a value of "UDP_SERVICE"
    TYPE_UDP_SERVICE = "UDP_SERVICE"

    def __init__(self, **kwargs):
        """
        Initializes a new Service object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.network_firewall.models.TcpService`
        * :class:`~oci.network_firewall.models.UdpService`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Service.
            Allowed values for this property are: "TCP_SERVICE", "UDP_SERVICE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param name:
            The value to assign to the name property of this Service.
        :type name: str

        :param parent_resource_id:
            The value to assign to the parent_resource_id property of this Service.
        :type parent_resource_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'parent_resource_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'parent_resource_id': 'parentResourceId'
        }

        self._type = None
        self._name = None
        self._parent_resource_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'TCP_SERVICE':
            return 'TcpService'

        if type == 'UDP_SERVICE':
            return 'UdpService'
        else:
            return 'Service'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Service.
        Describes the type of Service.

        Allowed values for this property are: "TCP_SERVICE", "UDP_SERVICE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Service.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Service.
        Describes the type of Service.


        :param type: The type of this Service.
        :type: str
        """
        allowed_values = ["TCP_SERVICE", "UDP_SERVICE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Service.
        Name of the service.


        :return: The name of this Service.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Service.
        Name of the service.


        :param name: The name of this Service.
        :type: str
        """
        self._name = name

    @property
    def parent_resource_id(self):
        """
        **[Required]** Gets the parent_resource_id of this Service.
        OCID of the Network Firewall Policy this service belongs to.


        :return: The parent_resource_id of this Service.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """
        Sets the parent_resource_id of this Service.
        OCID of the Network Firewall Policy this service belongs to.


        :param parent_resource_id: The parent_resource_id of this Service.
        :type: str
        """
        self._parent_resource_id = parent_resource_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
