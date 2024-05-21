# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

from .base_chat_request import BaseChatRequest
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CohereChatRequest(BaseChatRequest):
    """
    Details for the chat request for Cohere models.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CohereChatRequest object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_inference.models.CohereChatRequest.api_format` attribute
        of this class is ``COHERE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param api_format:
            The value to assign to the api_format property of this CohereChatRequest.
            Allowed values for this property are: "COHERE", "GENERIC"
        :type api_format: str

        :param message:
            The value to assign to the message property of this CohereChatRequest.
        :type message: str

        :param chat_history:
            The value to assign to the chat_history property of this CohereChatRequest.
        :type chat_history: list[oci.generative_ai_inference.models.CohereMessage]

        :param documents:
            The value to assign to the documents property of this CohereChatRequest.
        :type documents: list[object]

        :param is_search_queries_only:
            The value to assign to the is_search_queries_only property of this CohereChatRequest.
        :type is_search_queries_only: bool

        :param preamble_override:
            The value to assign to the preamble_override property of this CohereChatRequest.
        :type preamble_override: str

        :param is_stream:
            The value to assign to the is_stream property of this CohereChatRequest.
        :type is_stream: bool

        :param max_tokens:
            The value to assign to the max_tokens property of this CohereChatRequest.
        :type max_tokens: int

        :param temperature:
            The value to assign to the temperature property of this CohereChatRequest.
        :type temperature: float

        :param top_k:
            The value to assign to the top_k property of this CohereChatRequest.
        :type top_k: int

        :param top_p:
            The value to assign to the top_p property of this CohereChatRequest.
        :type top_p: float

        :param frequency_penalty:
            The value to assign to the frequency_penalty property of this CohereChatRequest.
        :type frequency_penalty: float

        :param presence_penalty:
            The value to assign to the presence_penalty property of this CohereChatRequest.
        :type presence_penalty: float

        """
        self.swagger_types = {
            'api_format': 'str',
            'message': 'str',
            'chat_history': 'list[CohereMessage]',
            'documents': 'list[object]',
            'is_search_queries_only': 'bool',
            'preamble_override': 'str',
            'is_stream': 'bool',
            'max_tokens': 'int',
            'temperature': 'float',
            'top_k': 'int',
            'top_p': 'float',
            'frequency_penalty': 'float',
            'presence_penalty': 'float'
        }

        self.attribute_map = {
            'api_format': 'apiFormat',
            'message': 'message',
            'chat_history': 'chatHistory',
            'documents': 'documents',
            'is_search_queries_only': 'isSearchQueriesOnly',
            'preamble_override': 'preambleOverride',
            'is_stream': 'isStream',
            'max_tokens': 'maxTokens',
            'temperature': 'temperature',
            'top_k': 'topK',
            'top_p': 'topP',
            'frequency_penalty': 'frequencyPenalty',
            'presence_penalty': 'presencePenalty'
        }

        self._api_format = None
        self._message = None
        self._chat_history = None
        self._documents = None
        self._is_search_queries_only = None
        self._preamble_override = None
        self._is_stream = None
        self._max_tokens = None
        self._temperature = None
        self._top_k = None
        self._top_p = None
        self._frequency_penalty = None
        self._presence_penalty = None
        self._api_format = 'COHERE'

    @property
    def message(self):
        """
        **[Required]** Gets the message of this CohereChatRequest.
        Text input for the model to respond to.


        :return: The message of this CohereChatRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CohereChatRequest.
        Text input for the model to respond to.


        :param message: The message of this CohereChatRequest.
        :type: str
        """
        self._message = message

    @property
    def chat_history(self):
        """
        Gets the chat_history of this CohereChatRequest.
        A list of previous messages between the user and the model, meant to give the model conversational context for responding to the user's message.


        :return: The chat_history of this CohereChatRequest.
        :rtype: list[oci.generative_ai_inference.models.CohereMessage]
        """
        return self._chat_history

    @chat_history.setter
    def chat_history(self, chat_history):
        """
        Sets the chat_history of this CohereChatRequest.
        A list of previous messages between the user and the model, meant to give the model conversational context for responding to the user's message.


        :param chat_history: The chat_history of this CohereChatRequest.
        :type: list[oci.generative_ai_inference.models.CohereMessage]
        """
        self._chat_history = chat_history

    @property
    def documents(self):
        """
        Gets the documents of this CohereChatRequest.
        list of relevant documents that the model can cite to generate a more accurate reply.
        Some suggested keys are \"text\", \"author\", and \"date\". For better generation quality, it is
        recommended to keep the total word count of the strings in the dictionary to under 300
        words.


        :return: The documents of this CohereChatRequest.
        :rtype: list[object]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this CohereChatRequest.
        list of relevant documents that the model can cite to generate a more accurate reply.
        Some suggested keys are \"text\", \"author\", and \"date\". For better generation quality, it is
        recommended to keep the total word count of the strings in the dictionary to under 300
        words.


        :param documents: The documents of this CohereChatRequest.
        :type: list[object]
        """
        self._documents = documents

    @property
    def is_search_queries_only(self):
        """
        Gets the is_search_queries_only of this CohereChatRequest.
        When true, the response will only contain a list of generated search queries, but no search will take place, and no reply from the model to the user's message will be generated.


        :return: The is_search_queries_only of this CohereChatRequest.
        :rtype: bool
        """
        return self._is_search_queries_only

    @is_search_queries_only.setter
    def is_search_queries_only(self, is_search_queries_only):
        """
        Sets the is_search_queries_only of this CohereChatRequest.
        When true, the response will only contain a list of generated search queries, but no search will take place, and no reply from the model to the user's message will be generated.


        :param is_search_queries_only: The is_search_queries_only of this CohereChatRequest.
        :type: bool
        """
        self._is_search_queries_only = is_search_queries_only

    @property
    def preamble_override(self):
        """
        Gets the preamble_override of this CohereChatRequest.
        When specified, the default Cohere preamble will be replaced with the provided one. Preambles are a part of the prompt used to adjust the model's overall behavior and conversation style. Default preambles vary for different models.


        :return: The preamble_override of this CohereChatRequest.
        :rtype: str
        """
        return self._preamble_override

    @preamble_override.setter
    def preamble_override(self, preamble_override):
        """
        Sets the preamble_override of this CohereChatRequest.
        When specified, the default Cohere preamble will be replaced with the provided one. Preambles are a part of the prompt used to adjust the model's overall behavior and conversation style. Default preambles vary for different models.


        :param preamble_override: The preamble_override of this CohereChatRequest.
        :type: str
        """
        self._preamble_override = preamble_override

    @property
    def is_stream(self):
        """
        Gets the is_stream of this CohereChatRequest.
        Whether to stream back partial progress. If set, tokens are sent as data-only server-sent events as they become available.


        :return: The is_stream of this CohereChatRequest.
        :rtype: bool
        """
        return self._is_stream

    @is_stream.setter
    def is_stream(self, is_stream):
        """
        Sets the is_stream of this CohereChatRequest.
        Whether to stream back partial progress. If set, tokens are sent as data-only server-sent events as they become available.


        :param is_stream: The is_stream of this CohereChatRequest.
        :type: bool
        """
        self._is_stream = is_stream

    @property
    def max_tokens(self):
        """
        Gets the max_tokens of this CohereChatRequest.
        The maximum number of tokens to predict for each response. Includes input plus output tokens.


        :return: The max_tokens of this CohereChatRequest.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        """
        Sets the max_tokens of this CohereChatRequest.
        The maximum number of tokens to predict for each response. Includes input plus output tokens.


        :param max_tokens: The max_tokens of this CohereChatRequest.
        :type: int
        """
        self._max_tokens = max_tokens

    @property
    def temperature(self):
        """
        Gets the temperature of this CohereChatRequest.
        A number that sets the randomness of the generated output. A lower temperature means a less random generations.
        Use lower numbers for tasks with a correct answer such as question answering or summarizing. High temperatures can generate hallucinations or factually incorrect information. Start with temperatures lower than 1.0 and increase the temperature for more creative outputs, as you regenerate the prompts to refine the outputs.


        :return: The temperature of this CohereChatRequest.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """
        Sets the temperature of this CohereChatRequest.
        A number that sets the randomness of the generated output. A lower temperature means a less random generations.
        Use lower numbers for tasks with a correct answer such as question answering or summarizing. High temperatures can generate hallucinations or factually incorrect information. Start with temperatures lower than 1.0 and increase the temperature for more creative outputs, as you regenerate the prompts to refine the outputs.


        :param temperature: The temperature of this CohereChatRequest.
        :type: float
        """
        self._temperature = temperature

    @property
    def top_k(self):
        """
        Gets the top_k of this CohereChatRequest.
        An integer that sets up the model to use only the top k most likely tokens in the generated output. A higher k introduces more randomness into the output making the output text sound more natural. Default value is 0 which disables this method and considers all tokens. To set a number for the likely tokens, choose an integer between 1 and 500.

        If also using top p, then the model considers only the top tokens whose probabilities add up to p percent and ignores the rest of the k tokens. For example, if k is 20, but the probabilities of the top 10 add up to .75, then only the top 10 tokens are chosen.


        :return: The top_k of this CohereChatRequest.
        :rtype: int
        """
        return self._top_k

    @top_k.setter
    def top_k(self, top_k):
        """
        Sets the top_k of this CohereChatRequest.
        An integer that sets up the model to use only the top k most likely tokens in the generated output. A higher k introduces more randomness into the output making the output text sound more natural. Default value is 0 which disables this method and considers all tokens. To set a number for the likely tokens, choose an integer between 1 and 500.

        If also using top p, then the model considers only the top tokens whose probabilities add up to p percent and ignores the rest of the k tokens. For example, if k is 20, but the probabilities of the top 10 add up to .75, then only the top 10 tokens are chosen.


        :param top_k: The top_k of this CohereChatRequest.
        :type: int
        """
        self._top_k = top_k

    @property
    def top_p(self):
        """
        Gets the top_p of this CohereChatRequest.
        If set to a probability 0.0 < p < 1.0, it ensures that only the most likely tokens, with total probability mass of p, are considered for generation at each step.

        To eliminate tokens with low likelihood, assign p a minimum percentage for the next token's likelihood. For example, when p is set to 0.75, the model eliminates the bottom 25 percent for the next token. Set to 1.0 to consider all tokens and set to 0 to disable. If both k and p are enabled, p acts after k.


        :return: The top_p of this CohereChatRequest.
        :rtype: float
        """
        return self._top_p

    @top_p.setter
    def top_p(self, top_p):
        """
        Sets the top_p of this CohereChatRequest.
        If set to a probability 0.0 < p < 1.0, it ensures that only the most likely tokens, with total probability mass of p, are considered for generation at each step.

        To eliminate tokens with low likelihood, assign p a minimum percentage for the next token's likelihood. For example, when p is set to 0.75, the model eliminates the bottom 25 percent for the next token. Set to 1.0 to consider all tokens and set to 0 to disable. If both k and p are enabled, p acts after k.


        :param top_p: The top_p of this CohereChatRequest.
        :type: float
        """
        self._top_p = top_p

    @property
    def frequency_penalty(self):
        """
        Gets the frequency_penalty of this CohereChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on their frequency in the generated text so far. Greater numbers encourage the model to use new tokens, while lower numbers encourage the model to repeat the tokens. Set to 0 to disable.


        :return: The frequency_penalty of this CohereChatRequest.
        :rtype: float
        """
        return self._frequency_penalty

    @frequency_penalty.setter
    def frequency_penalty(self, frequency_penalty):
        """
        Sets the frequency_penalty of this CohereChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on their frequency in the generated text so far. Greater numbers encourage the model to use new tokens, while lower numbers encourage the model to repeat the tokens. Set to 0 to disable.


        :param frequency_penalty: The frequency_penalty of this CohereChatRequest.
        :type: float
        """
        self._frequency_penalty = frequency_penalty

    @property
    def presence_penalty(self):
        """
        Gets the presence_penalty of this CohereChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on whether they've appeared in the generated text so far. Greater numbers encourage the model to use new tokens, while lower numbers encourage the model to repeat the tokens.

        Similar to frequency penalty, a penalty is applied to previously present tokens, except that this penalty is applied equally to all tokens that have already appeared, regardless of how many times they've appeared. Set to 0 to disable.


        :return: The presence_penalty of this CohereChatRequest.
        :rtype: float
        """
        return self._presence_penalty

    @presence_penalty.setter
    def presence_penalty(self, presence_penalty):
        """
        Sets the presence_penalty of this CohereChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on whether they've appeared in the generated text so far. Greater numbers encourage the model to use new tokens, while lower numbers encourage the model to repeat the tokens.

        Similar to frequency penalty, a penalty is applied to previously present tokens, except that this penalty is applied equally to all tokens that have already appeared, regardless of how many times they've appeared. Set to 0 to disable.


        :param presence_penalty: The presence_penalty of this CohereChatRequest.
        :type: float
        """
        self._presence_penalty = presence_penalty

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other