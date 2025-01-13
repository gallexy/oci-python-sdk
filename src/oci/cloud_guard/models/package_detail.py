# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PackageDetail(object):
    """
    details of package causing vulnerabilities
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PackageDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this PackageDetail.
        :type name: str

        :param package_type:
            The value to assign to the package_type property of this PackageDetail.
        :type package_type: str

        :param version:
            The value to assign to the version property of this PackageDetail.
        :type version: str

        :param cause:
            The value to assign to the cause property of this PackageDetail.
        :type cause: str

        :param location:
            The value to assign to the location property of this PackageDetail.
        :type location: str

        :param remediation:
            The value to assign to the remediation property of this PackageDetail.
        :type remediation: str

        """
        self.swagger_types = {
            'name': 'str',
            'package_type': 'str',
            'version': 'str',
            'cause': 'str',
            'location': 'str',
            'remediation': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'package_type': 'packageType',
            'version': 'version',
            'cause': 'cause',
            'location': 'location',
            'remediation': 'remediation'
        }

        self._name = None
        self._package_type = None
        self._version = None
        self._cause = None
        self._location = None
        self._remediation = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PackageDetail.
        name of the package


        :return: The name of this PackageDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PackageDetail.
        name of the package


        :param name: The name of this PackageDetail.
        :type: str
        """
        self._name = name

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this PackageDetail.
        type of the package


        :return: The package_type of this PackageDetail.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this PackageDetail.
        type of the package


        :param package_type: The package_type of this PackageDetail.
        :type: str
        """
        self._package_type = package_type

    @property
    def version(self):
        """
        **[Required]** Gets the version of this PackageDetail.
        version of the package


        :return: The version of this PackageDetail.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PackageDetail.
        version of the package


        :param version: The version of this PackageDetail.
        :type: str
        """
        self._version = version

    @property
    def cause(self):
        """
        Gets the cause of this PackageDetail.
        cause of the vulnerability in the package


        :return: The cause of this PackageDetail.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """
        Sets the cause of this PackageDetail.
        cause of the vulnerability in the package


        :param cause: The cause of this PackageDetail.
        :type: str
        """
        self._cause = cause

    @property
    def location(self):
        """
        Gets the location of this PackageDetail.
        location of the package


        :return: The location of this PackageDetail.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this PackageDetail.
        location of the package


        :param location: The location of this PackageDetail.
        :type: str
        """
        self._location = location

    @property
    def remediation(self):
        """
        Gets the remediation of this PackageDetail.
        remediation for vulnerability


        :return: The remediation of this PackageDetail.
        :rtype: str
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        """
        Sets the remediation of this PackageDetail.
        remediation for vulnerability


        :param remediation: The remediation of this PackageDetail.
        :type: str
        """
        self._remediation = remediation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
