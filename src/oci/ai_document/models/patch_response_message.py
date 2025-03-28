# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221109


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchResponseMessage(object):
    """
    The response containing the details of the patch operation status.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PatchResponseMessage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this PatchResponseMessage.
        :type message: str

        :param model_id:
            The value to assign to the model_id property of this PatchResponseMessage.
        :type model_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PatchResponseMessage.
        :type compartment_id: str

        """
        self.swagger_types = {
            'message': 'str',
            'model_id': 'str',
            'compartment_id': 'str'
        }
        self.attribute_map = {
            'message': 'message',
            'model_id': 'modelId',
            'compartment_id': 'compartmentId'
        }
        self._message = None
        self._model_id = None
        self._compartment_id = None

    @property
    def message(self):
        """
        **[Required]** Gets the message of this PatchResponseMessage.
        The response message containing details of operation.


        :return: The message of this PatchResponseMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this PatchResponseMessage.
        The response message containing details of operation.


        :param message: The message of this PatchResponseMessage.
        :type: str
        """
        self._message = message

    @property
    def model_id(self):
        """
        Gets the model_id of this PatchResponseMessage.
        Model ID representing the conflicting patch operation.


        :return: The model_id of this PatchResponseMessage.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """
        Sets the model_id of this PatchResponseMessage.
        Model ID representing the conflicting patch operation.


        :param model_id: The model_id of this PatchResponseMessage.
        :type: str
        """
        self._model_id = model_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this PatchResponseMessage.
        Compartment ID representing the conflicting Model Compartment.


        :return: The compartment_id of this PatchResponseMessage.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PatchResponseMessage.
        Compartment ID representing the conflicting Model Compartment.


        :param compartment_id: The compartment_id of this PatchResponseMessage.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
