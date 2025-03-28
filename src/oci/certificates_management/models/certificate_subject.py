# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210224


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateSubject(object):
    """
    The subject of the certificate, which is a distinguished name that identifies the entity that owns the public key in the certificate.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateSubject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param common_name:
            The value to assign to the common_name property of this CertificateSubject.
        :type common_name: str

        :param country:
            The value to assign to the country property of this CertificateSubject.
        :type country: str

        :param domain_component:
            The value to assign to the domain_component property of this CertificateSubject.
        :type domain_component: str

        :param distinguished_name_qualifier:
            The value to assign to the distinguished_name_qualifier property of this CertificateSubject.
        :type distinguished_name_qualifier: str

        :param generation_qualifier:
            The value to assign to the generation_qualifier property of this CertificateSubject.
        :type generation_qualifier: str

        :param given_name:
            The value to assign to the given_name property of this CertificateSubject.
        :type given_name: str

        :param initials:
            The value to assign to the initials property of this CertificateSubject.
        :type initials: str

        :param locality_name:
            The value to assign to the locality_name property of this CertificateSubject.
        :type locality_name: str

        :param organization:
            The value to assign to the organization property of this CertificateSubject.
        :type organization: str

        :param organizational_unit:
            The value to assign to the organizational_unit property of this CertificateSubject.
        :type organizational_unit: str

        :param pseudonym:
            The value to assign to the pseudonym property of this CertificateSubject.
        :type pseudonym: str

        :param serial_number:
            The value to assign to the serial_number property of this CertificateSubject.
        :type serial_number: str

        :param state_or_province_name:
            The value to assign to the state_or_province_name property of this CertificateSubject.
        :type state_or_province_name: str

        :param street:
            The value to assign to the street property of this CertificateSubject.
        :type street: str

        :param surname:
            The value to assign to the surname property of this CertificateSubject.
        :type surname: str

        :param title:
            The value to assign to the title property of this CertificateSubject.
        :type title: str

        :param user_id:
            The value to assign to the user_id property of this CertificateSubject.
        :type user_id: str

        """
        self.swagger_types = {
            'common_name': 'str',
            'country': 'str',
            'domain_component': 'str',
            'distinguished_name_qualifier': 'str',
            'generation_qualifier': 'str',
            'given_name': 'str',
            'initials': 'str',
            'locality_name': 'str',
            'organization': 'str',
            'organizational_unit': 'str',
            'pseudonym': 'str',
            'serial_number': 'str',
            'state_or_province_name': 'str',
            'street': 'str',
            'surname': 'str',
            'title': 'str',
            'user_id': 'str'
        }
        self.attribute_map = {
            'common_name': 'commonName',
            'country': 'country',
            'domain_component': 'domainComponent',
            'distinguished_name_qualifier': 'distinguishedNameQualifier',
            'generation_qualifier': 'generationQualifier',
            'given_name': 'givenName',
            'initials': 'initials',
            'locality_name': 'localityName',
            'organization': 'organization',
            'organizational_unit': 'organizationalUnit',
            'pseudonym': 'pseudonym',
            'serial_number': 'serialNumber',
            'state_or_province_name': 'stateOrProvinceName',
            'street': 'street',
            'surname': 'surname',
            'title': 'title',
            'user_id': 'userId'
        }
        self._common_name = None
        self._country = None
        self._domain_component = None
        self._distinguished_name_qualifier = None
        self._generation_qualifier = None
        self._given_name = None
        self._initials = None
        self._locality_name = None
        self._organization = None
        self._organizational_unit = None
        self._pseudonym = None
        self._serial_number = None
        self._state_or_province_name = None
        self._street = None
        self._surname = None
        self._title = None
        self._user_id = None

    @property
    def common_name(self):
        """
        **[Required]** Gets the common_name of this CertificateSubject.
        Common name or fully-qualified domain name (RDN CN).


        :return: The common_name of this CertificateSubject.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """
        Sets the common_name of this CertificateSubject.
        Common name or fully-qualified domain name (RDN CN).


        :param common_name: The common_name of this CertificateSubject.
        :type: str
        """
        self._common_name = common_name

    @property
    def country(self):
        """
        Gets the country of this CertificateSubject.
        Country name (RDN C).


        :return: The country of this CertificateSubject.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this CertificateSubject.
        Country name (RDN C).


        :param country: The country of this CertificateSubject.
        :type: str
        """
        self._country = country

    @property
    def domain_component(self):
        """
        Gets the domain_component of this CertificateSubject.
        Domain component (RDN DC).


        :return: The domain_component of this CertificateSubject.
        :rtype: str
        """
        return self._domain_component

    @domain_component.setter
    def domain_component(self, domain_component):
        """
        Sets the domain_component of this CertificateSubject.
        Domain component (RDN DC).


        :param domain_component: The domain_component of this CertificateSubject.
        :type: str
        """
        self._domain_component = domain_component

    @property
    def distinguished_name_qualifier(self):
        """
        Gets the distinguished_name_qualifier of this CertificateSubject.
        Distinguished name qualifier(RDN DNQ).


        :return: The distinguished_name_qualifier of this CertificateSubject.
        :rtype: str
        """
        return self._distinguished_name_qualifier

    @distinguished_name_qualifier.setter
    def distinguished_name_qualifier(self, distinguished_name_qualifier):
        """
        Sets the distinguished_name_qualifier of this CertificateSubject.
        Distinguished name qualifier(RDN DNQ).


        :param distinguished_name_qualifier: The distinguished_name_qualifier of this CertificateSubject.
        :type: str
        """
        self._distinguished_name_qualifier = distinguished_name_qualifier

    @property
    def generation_qualifier(self):
        """
        Gets the generation_qualifier of this CertificateSubject.
        Personal generational qualifier (for example, Sr., Jr. 3rd, or IV).


        :return: The generation_qualifier of this CertificateSubject.
        :rtype: str
        """
        return self._generation_qualifier

    @generation_qualifier.setter
    def generation_qualifier(self, generation_qualifier):
        """
        Sets the generation_qualifier of this CertificateSubject.
        Personal generational qualifier (for example, Sr., Jr. 3rd, or IV).


        :param generation_qualifier: The generation_qualifier of this CertificateSubject.
        :type: str
        """
        self._generation_qualifier = generation_qualifier

    @property
    def given_name(self):
        """
        Gets the given_name of this CertificateSubject.
        Personal given name (RDN G or GN).


        :return: The given_name of this CertificateSubject.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """
        Sets the given_name of this CertificateSubject.
        Personal given name (RDN G or GN).


        :param given_name: The given_name of this CertificateSubject.
        :type: str
        """
        self._given_name = given_name

    @property
    def initials(self):
        """
        Gets the initials of this CertificateSubject.
        Personal initials.


        :return: The initials of this CertificateSubject.
        :rtype: str
        """
        return self._initials

    @initials.setter
    def initials(self, initials):
        """
        Sets the initials of this CertificateSubject.
        Personal initials.


        :param initials: The initials of this CertificateSubject.
        :type: str
        """
        self._initials = initials

    @property
    def locality_name(self):
        """
        Gets the locality_name of this CertificateSubject.
        Locality (RDN L).


        :return: The locality_name of this CertificateSubject.
        :rtype: str
        """
        return self._locality_name

    @locality_name.setter
    def locality_name(self, locality_name):
        """
        Sets the locality_name of this CertificateSubject.
        Locality (RDN L).


        :param locality_name: The locality_name of this CertificateSubject.
        :type: str
        """
        self._locality_name = locality_name

    @property
    def organization(self):
        """
        Gets the organization of this CertificateSubject.
        Organization (RDN O).


        :return: The organization of this CertificateSubject.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this CertificateSubject.
        Organization (RDN O).


        :param organization: The organization of this CertificateSubject.
        :type: str
        """
        self._organization = organization

    @property
    def organizational_unit(self):
        """
        Gets the organizational_unit of this CertificateSubject.
        Organizational unit (RDN OU).


        :return: The organizational_unit of this CertificateSubject.
        :rtype: str
        """
        return self._organizational_unit

    @organizational_unit.setter
    def organizational_unit(self, organizational_unit):
        """
        Sets the organizational_unit of this CertificateSubject.
        Organizational unit (RDN OU).


        :param organizational_unit: The organizational_unit of this CertificateSubject.
        :type: str
        """
        self._organizational_unit = organizational_unit

    @property
    def pseudonym(self):
        """
        Gets the pseudonym of this CertificateSubject.
        Subject pseudonym.


        :return: The pseudonym of this CertificateSubject.
        :rtype: str
        """
        return self._pseudonym

    @pseudonym.setter
    def pseudonym(self, pseudonym):
        """
        Sets the pseudonym of this CertificateSubject.
        Subject pseudonym.


        :param pseudonym: The pseudonym of this CertificateSubject.
        :type: str
        """
        self._pseudonym = pseudonym

    @property
    def serial_number(self):
        """
        Gets the serial_number of this CertificateSubject.
        Unique subject identifier, which is not the same as the certificate serial number (RDN SERIALNUMBER).


        :return: The serial_number of this CertificateSubject.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this CertificateSubject.
        Unique subject identifier, which is not the same as the certificate serial number (RDN SERIALNUMBER).


        :param serial_number: The serial_number of this CertificateSubject.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def state_or_province_name(self):
        """
        Gets the state_or_province_name of this CertificateSubject.
        State or province name (RDN ST or S).


        :return: The state_or_province_name of this CertificateSubject.
        :rtype: str
        """
        return self._state_or_province_name

    @state_or_province_name.setter
    def state_or_province_name(self, state_or_province_name):
        """
        Sets the state_or_province_name of this CertificateSubject.
        State or province name (RDN ST or S).


        :param state_or_province_name: The state_or_province_name of this CertificateSubject.
        :type: str
        """
        self._state_or_province_name = state_or_province_name

    @property
    def street(self):
        """
        Gets the street of this CertificateSubject.
        Street address (RDN STREET).


        :return: The street of this CertificateSubject.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """
        Sets the street of this CertificateSubject.
        Street address (RDN STREET).


        :param street: The street of this CertificateSubject.
        :type: str
        """
        self._street = street

    @property
    def surname(self):
        """
        Gets the surname of this CertificateSubject.
        Personal surname (RDN SN).


        :return: The surname of this CertificateSubject.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """
        Sets the surname of this CertificateSubject.
        Personal surname (RDN SN).


        :param surname: The surname of this CertificateSubject.
        :type: str
        """
        self._surname = surname

    @property
    def title(self):
        """
        Gets the title of this CertificateSubject.
        Title (RDN T or TITLE).


        :return: The title of this CertificateSubject.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CertificateSubject.
        Title (RDN T or TITLE).


        :param title: The title of this CertificateSubject.
        :type: str
        """
        self._title = title

    @property
    def user_id(self):
        """
        Gets the user_id of this CertificateSubject.
        User ID (RDN UID).


        :return: The user_id of this CertificateSubject.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this CertificateSubject.
        User ID (RDN UID).


        :param user_id: The user_id of this CertificateSubject.
        :type: str
        """
        self._user_id = user_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
