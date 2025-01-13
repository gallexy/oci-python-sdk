# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Indicator(object):
    """
    A data signature observed on a network or host that indicates a potential security threat. Indicators can be plain text or computed (hashed) values.
    """

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "DOMAIN_NAME"
    TYPE_DOMAIN_NAME = "DOMAIN_NAME"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "FILE_NAME"
    TYPE_FILE_NAME = "FILE_NAME"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "MD5_HASH"
    TYPE_MD5_HASH = "MD5_HASH"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "SHA1_HASH"
    TYPE_SHA1_HASH = "SHA1_HASH"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "SHA256_HASH"
    TYPE_SHA256_HASH = "SHA256_HASH"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "IP_ADDRESS"
    TYPE_IP_ADDRESS = "IP_ADDRESS"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "URL"
    TYPE_URL = "URL"

    #: A constant which can be used with the lifecycle_state property of a Indicator.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Indicator.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Indicator object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Indicator.
        :type id: str

        :param type:
            The value to assign to the type property of this Indicator.
            Allowed values for this property are: "DOMAIN_NAME", "FILE_NAME", "MD5_HASH", "SHA1_HASH", "SHA256_HASH", "IP_ADDRESS", "URL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param value:
            The value to assign to the value property of this Indicator.
        :type value: str

        :param confidence:
            The value to assign to the confidence property of this Indicator.
        :type confidence: int

        :param compartment_id:
            The value to assign to the compartment_id property of this Indicator.
        :type compartment_id: str

        :param threat_types:
            The value to assign to the threat_types property of this Indicator.
        :type threat_types: list[oci.threat_intelligence.models.ThreatType]

        :param attributes:
            The value to assign to the attributes property of this Indicator.
        :type attributes: list[oci.threat_intelligence.models.IndicatorAttribute]

        :param relationships:
            The value to assign to the relationships property of this Indicator.
        :type relationships: list[oci.threat_intelligence.models.IndicatorRelationship]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Indicator.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Indicator.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Indicator.
        :type time_updated: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this Indicator.
        :type time_last_seen: datetime

        :param geodata:
            The value to assign to the geodata property of this Indicator.
        :type geodata: oci.threat_intelligence.models.GeodataDetails

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'value': 'str',
            'confidence': 'int',
            'compartment_id': 'str',
            'threat_types': 'list[ThreatType]',
            'attributes': 'list[IndicatorAttribute]',
            'relationships': 'list[IndicatorRelationship]',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_last_seen': 'datetime',
            'geodata': 'GeodataDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'value': 'value',
            'confidence': 'confidence',
            'compartment_id': 'compartmentId',
            'threat_types': 'threatTypes',
            'attributes': 'attributes',
            'relationships': 'relationships',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_last_seen': 'timeLastSeen',
            'geodata': 'geodata'
        }

        self._id = None
        self._type = None
        self._value = None
        self._confidence = None
        self._compartment_id = None
        self._threat_types = None
        self._attributes = None
        self._relationships = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._time_last_seen = None
        self._geodata = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Indicator.
        The OCID of the indicator.


        :return: The id of this Indicator.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Indicator.
        The OCID of the indicator.


        :param id: The id of this Indicator.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Indicator.
        The type of indicator.

        Allowed values for this property are: "DOMAIN_NAME", "FILE_NAME", "MD5_HASH", "SHA1_HASH", "SHA256_HASH", "IP_ADDRESS", "URL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Indicator.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Indicator.
        The type of indicator.


        :param type: The type of this Indicator.
        :type: str
        """
        allowed_values = ["DOMAIN_NAME", "FILE_NAME", "MD5_HASH", "SHA1_HASH", "SHA256_HASH", "IP_ADDRESS", "URL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this Indicator.
        The value for this indicator.
        The value's format is dependent upon its `type`. Examples:

        DOMAIN_NAME \"evil.example.com\"

        MD5_HASH \"44d88612fea8a8f36de82e1278abb02f\"

        IP_ADDRESS \"2001:db8::1\"


        :return: The value of this Indicator.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Indicator.
        The value for this indicator.
        The value's format is dependent upon its `type`. Examples:

        DOMAIN_NAME \"evil.example.com\"

        MD5_HASH \"44d88612fea8a8f36de82e1278abb02f\"

        IP_ADDRESS \"2001:db8::1\"


        :param value: The value of this Indicator.
        :type: str
        """
        self._value = value

    @property
    def confidence(self):
        """
        Gets the confidence of this Indicator.
        An integer from 0 to 100 that represents how certain we are that the indicator is malicious and a potential threat if it is detected communicating with your cloud resources. This confidence value is aggregated from the confidence in the threat types, attributes, and relationships to create an overall value for the indicator.


        :return: The confidence of this Indicator.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this Indicator.
        An integer from 0 to 100 that represents how certain we are that the indicator is malicious and a potential threat if it is detected communicating with your cloud resources. This confidence value is aggregated from the confidence in the threat types, attributes, and relationships to create an overall value for the indicator.


        :param confidence: The confidence of this Indicator.
        :type: int
        """
        self._confidence = confidence

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Indicator.
        The OCID of the compartment that contains this indicator.


        :return: The compartment_id of this Indicator.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Indicator.
        The OCID of the compartment that contains this indicator.


        :param compartment_id: The compartment_id of this Indicator.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def threat_types(self):
        """
        **[Required]** Gets the threat_types of this Indicator.
        Characteristics of the threat indicator based on previous observations or behavior. May include related tactics, techniques, and procedures.


        :return: The threat_types of this Indicator.
        :rtype: list[oci.threat_intelligence.models.ThreatType]
        """
        return self._threat_types

    @threat_types.setter
    def threat_types(self, threat_types):
        """
        Sets the threat_types of this Indicator.
        Characteristics of the threat indicator based on previous observations or behavior. May include related tactics, techniques, and procedures.


        :param threat_types: The threat_types of this Indicator.
        :type: list[oci.threat_intelligence.models.ThreatType]
        """
        self._threat_types = threat_types

    @property
    def attributes(self):
        """
        **[Required]** Gets the attributes of this Indicator.
        A map of attributes with additional information about the indicator.
        Each attribute has a name (string), value (string), and attribution (supporting data).


        :return: The attributes of this Indicator.
        :rtype: list[oci.threat_intelligence.models.IndicatorAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this Indicator.
        A map of attributes with additional information about the indicator.
        Each attribute has a name (string), value (string), and attribution (supporting data).


        :param attributes: The attributes of this Indicator.
        :type: list[oci.threat_intelligence.models.IndicatorAttribute]
        """
        self._attributes = attributes

    @property
    def relationships(self):
        """
        **[Required]** Gets the relationships of this Indicator.
        A map of relationships between the indicator and other entities.
        Each relationship has a name (string), related entity, and attribution (supporting data).


        :return: The relationships of this Indicator.
        :rtype: list[oci.threat_intelligence.models.IndicatorRelationship]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """
        Sets the relationships of this Indicator.
        A map of relationships between the indicator and other entities.
        Each relationship has a name (string), related entity, and attribution (supporting data).


        :param relationships: The relationships of this Indicator.
        :type: list[oci.threat_intelligence.models.IndicatorRelationship]
        """
        self._relationships = relationships

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Indicator.
        The state of the indicator. It will always be `ACTIVE`.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Indicator.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Indicator.
        The state of the indicator. It will always be `ACTIVE`.


        :param lifecycle_state: The lifecycle_state of this Indicator.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Indicator.
        The date and time that the indicator was first detected. An RFC3339 formatted string.


        :return: The time_created of this Indicator.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Indicator.
        The date and time that the indicator was first detected. An RFC3339 formatted string.


        :param time_created: The time_created of this Indicator.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Indicator.
        The date and time that this indicator was last updated. The value is the same as `timeCreated` for a new indicator. An RFC3339 formatted string.


        :return: The time_updated of this Indicator.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Indicator.
        The date and time that this indicator was last updated. The value is the same as `timeCreated` for a new indicator. An RFC3339 formatted string.


        :param time_updated: The time_updated of this Indicator.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_last_seen(self):
        """
        **[Required]** Gets the time_last_seen of this Indicator.
        The date and time that this indicator was last seen. The value is the same as `timeCreated` for a new indicator. An RFC3339 formatted string.


        :return: The time_last_seen of this Indicator.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this Indicator.
        The date and time that this indicator was last seen. The value is the same as `timeCreated` for a new indicator. An RFC3339 formatted string.


        :param time_last_seen: The time_last_seen of this Indicator.
        :type: datetime
        """
        self._time_last_seen = time_last_seen

    @property
    def geodata(self):
        """
        **[Required]** Gets the geodata of this Indicator.

        :return: The geodata of this Indicator.
        :rtype: oci.threat_intelligence.models.GeodataDetails
        """
        return self._geodata

    @geodata.setter
    def geodata(self, geodata):
        """
        Sets the geodata of this Indicator.

        :param geodata: The geodata of this Indicator.
        :type: oci.threat_intelligence.models.GeodataDetails
        """
        self._geodata = geodata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
