# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateSummary(object):
    """
    Summary of the Certificates.
    """

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CertificateSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CertificateSummary.
        :type key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CertificateSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param subject:
            The value to assign to the subject property of this CertificateSummary.
        :type subject: str

        :param is_self_signed:
            The value to assign to the is_self_signed property of this CertificateSummary.
        :type is_self_signed: bool

        :param time_valid_to:
            The value to assign to the time_valid_to property of this CertificateSummary.
        :type time_valid_to: datetime

        :param time_created:
            The value to assign to the time_created property of this CertificateSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'key': 'str',
            'lifecycle_state': 'str',
            'subject': 'str',
            'is_self_signed': 'bool',
            'time_valid_to': 'datetime',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'key': 'key',
            'lifecycle_state': 'lifecycleState',
            'subject': 'subject',
            'is_self_signed': 'isSelfSigned',
            'time_valid_to': 'timeValidTo',
            'time_created': 'timeCreated'
        }

        self._key = None
        self._lifecycle_state = None
        self._subject = None
        self._is_self_signed = None
        self._time_valid_to = None
        self._time_created = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this CertificateSummary.
        The identifier key (unique name in the scope of the deployment) of the certificate being referenced.
        It must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.


        :return: The key of this CertificateSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CertificateSummary.
        The identifier key (unique name in the scope of the deployment) of the certificate being referenced.
        It must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.


        :param key: The key of this CertificateSummary.
        :type: str
        """
        self._key = key

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CertificateSummary.
        Possible certificate lifecycle states.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CertificateSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CertificateSummary.
        Possible certificate lifecycle states.


        :param lifecycle_state: The lifecycle_state of this CertificateSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def subject(self):
        """
        **[Required]** Gets the subject of this CertificateSummary.
        The Certificate subject.


        :return: The subject of this CertificateSummary.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this CertificateSummary.
        The Certificate subject.


        :param subject: The subject of this CertificateSummary.
        :type: str
        """
        self._subject = subject

    @property
    def is_self_signed(self):
        """
        **[Required]** Gets the is_self_signed of this CertificateSummary.
        Indicates if the certificate is self signed.


        :return: The is_self_signed of this CertificateSummary.
        :rtype: bool
        """
        return self._is_self_signed

    @is_self_signed.setter
    def is_self_signed(self, is_self_signed):
        """
        Sets the is_self_signed of this CertificateSummary.
        Indicates if the certificate is self signed.


        :param is_self_signed: The is_self_signed of this CertificateSummary.
        :type: bool
        """
        self._is_self_signed = is_self_signed

    @property
    def time_valid_to(self):
        """
        **[Required]** Gets the time_valid_to of this CertificateSummary.
        The time the certificate is valid to. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_valid_to of this CertificateSummary.
        :rtype: datetime
        """
        return self._time_valid_to

    @time_valid_to.setter
    def time_valid_to(self, time_valid_to):
        """
        Sets the time_valid_to of this CertificateSummary.
        The time the certificate is valid to. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_valid_to: The time_valid_to of this CertificateSummary.
        :type: datetime
        """
        self._time_valid_to = time_valid_to

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this CertificateSummary.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CertificateSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CertificateSummary.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CertificateSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
