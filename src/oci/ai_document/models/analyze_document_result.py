# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnalyzeDocumentResult(object):
    """
    The document analysis results.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnalyzeDocumentResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param document_metadata:
            The value to assign to the document_metadata property of this AnalyzeDocumentResult.
        :type document_metadata: oci.ai_document.models.DocumentMetadata

        :param pages:
            The value to assign to the pages property of this AnalyzeDocumentResult.
        :type pages: list[oci.ai_document.models.Page]

        :param detected_document_types:
            The value to assign to the detected_document_types property of this AnalyzeDocumentResult.
        :type detected_document_types: list[oci.ai_document.models.DetectedDocumentType]

        :param detected_languages:
            The value to assign to the detected_languages property of this AnalyzeDocumentResult.
        :type detected_languages: list[oci.ai_document.models.DetectedLanguage]

        :param document_classification_model_version:
            The value to assign to the document_classification_model_version property of this AnalyzeDocumentResult.
        :type document_classification_model_version: str

        :param language_classification_model_version:
            The value to assign to the language_classification_model_version property of this AnalyzeDocumentResult.
        :type language_classification_model_version: str

        :param text_extraction_model_version:
            The value to assign to the text_extraction_model_version property of this AnalyzeDocumentResult.
        :type text_extraction_model_version: str

        :param key_value_extraction_model_version:
            The value to assign to the key_value_extraction_model_version property of this AnalyzeDocumentResult.
        :type key_value_extraction_model_version: str

        :param table_extraction_model_version:
            The value to assign to the table_extraction_model_version property of this AnalyzeDocumentResult.
        :type table_extraction_model_version: str

        :param errors:
            The value to assign to the errors property of this AnalyzeDocumentResult.
        :type errors: list[oci.ai_document.models.ProcessingError]

        :param searchable_pdf:
            The value to assign to the searchable_pdf property of this AnalyzeDocumentResult.
        :type searchable_pdf: str

        """
        self.swagger_types = {
            'document_metadata': 'DocumentMetadata',
            'pages': 'list[Page]',
            'detected_document_types': 'list[DetectedDocumentType]',
            'detected_languages': 'list[DetectedLanguage]',
            'document_classification_model_version': 'str',
            'language_classification_model_version': 'str',
            'text_extraction_model_version': 'str',
            'key_value_extraction_model_version': 'str',
            'table_extraction_model_version': 'str',
            'errors': 'list[ProcessingError]',
            'searchable_pdf': 'str'
        }

        self.attribute_map = {
            'document_metadata': 'documentMetadata',
            'pages': 'pages',
            'detected_document_types': 'detectedDocumentTypes',
            'detected_languages': 'detectedLanguages',
            'document_classification_model_version': 'documentClassificationModelVersion',
            'language_classification_model_version': 'languageClassificationModelVersion',
            'text_extraction_model_version': 'textExtractionModelVersion',
            'key_value_extraction_model_version': 'keyValueExtractionModelVersion',
            'table_extraction_model_version': 'tableExtractionModelVersion',
            'errors': 'errors',
            'searchable_pdf': 'searchablePdf'
        }

        self._document_metadata = None
        self._pages = None
        self._detected_document_types = None
        self._detected_languages = None
        self._document_classification_model_version = None
        self._language_classification_model_version = None
        self._text_extraction_model_version = None
        self._key_value_extraction_model_version = None
        self._table_extraction_model_version = None
        self._errors = None
        self._searchable_pdf = None

    @property
    def document_metadata(self):
        """
        **[Required]** Gets the document_metadata of this AnalyzeDocumentResult.

        :return: The document_metadata of this AnalyzeDocumentResult.
        :rtype: oci.ai_document.models.DocumentMetadata
        """
        return self._document_metadata

    @document_metadata.setter
    def document_metadata(self, document_metadata):
        """
        Sets the document_metadata of this AnalyzeDocumentResult.

        :param document_metadata: The document_metadata of this AnalyzeDocumentResult.
        :type: oci.ai_document.models.DocumentMetadata
        """
        self._document_metadata = document_metadata

    @property
    def pages(self):
        """
        **[Required]** Gets the pages of this AnalyzeDocumentResult.
        The array of a Page.


        :return: The pages of this AnalyzeDocumentResult.
        :rtype: list[oci.ai_document.models.Page]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages of this AnalyzeDocumentResult.
        The array of a Page.


        :param pages: The pages of this AnalyzeDocumentResult.
        :type: list[oci.ai_document.models.Page]
        """
        self._pages = pages

    @property
    def detected_document_types(self):
        """
        Gets the detected_document_types of this AnalyzeDocumentResult.
        An array of detected document types.


        :return: The detected_document_types of this AnalyzeDocumentResult.
        :rtype: list[oci.ai_document.models.DetectedDocumentType]
        """
        return self._detected_document_types

    @detected_document_types.setter
    def detected_document_types(self, detected_document_types):
        """
        Sets the detected_document_types of this AnalyzeDocumentResult.
        An array of detected document types.


        :param detected_document_types: The detected_document_types of this AnalyzeDocumentResult.
        :type: list[oci.ai_document.models.DetectedDocumentType]
        """
        self._detected_document_types = detected_document_types

    @property
    def detected_languages(self):
        """
        Gets the detected_languages of this AnalyzeDocumentResult.
        An array of detected languages.


        :return: The detected_languages of this AnalyzeDocumentResult.
        :rtype: list[oci.ai_document.models.DetectedLanguage]
        """
        return self._detected_languages

    @detected_languages.setter
    def detected_languages(self, detected_languages):
        """
        Sets the detected_languages of this AnalyzeDocumentResult.
        An array of detected languages.


        :param detected_languages: The detected_languages of this AnalyzeDocumentResult.
        :type: list[oci.ai_document.models.DetectedLanguage]
        """
        self._detected_languages = detected_languages

    @property
    def document_classification_model_version(self):
        """
        Gets the document_classification_model_version of this AnalyzeDocumentResult.
        The document classification model version.


        :return: The document_classification_model_version of this AnalyzeDocumentResult.
        :rtype: str
        """
        return self._document_classification_model_version

    @document_classification_model_version.setter
    def document_classification_model_version(self, document_classification_model_version):
        """
        Sets the document_classification_model_version of this AnalyzeDocumentResult.
        The document classification model version.


        :param document_classification_model_version: The document_classification_model_version of this AnalyzeDocumentResult.
        :type: str
        """
        self._document_classification_model_version = document_classification_model_version

    @property
    def language_classification_model_version(self):
        """
        Gets the language_classification_model_version of this AnalyzeDocumentResult.
        The document language classification model version.


        :return: The language_classification_model_version of this AnalyzeDocumentResult.
        :rtype: str
        """
        return self._language_classification_model_version

    @language_classification_model_version.setter
    def language_classification_model_version(self, language_classification_model_version):
        """
        Sets the language_classification_model_version of this AnalyzeDocumentResult.
        The document language classification model version.


        :param language_classification_model_version: The language_classification_model_version of this AnalyzeDocumentResult.
        :type: str
        """
        self._language_classification_model_version = language_classification_model_version

    @property
    def text_extraction_model_version(self):
        """
        Gets the text_extraction_model_version of this AnalyzeDocumentResult.
        The document text extraction model version.


        :return: The text_extraction_model_version of this AnalyzeDocumentResult.
        :rtype: str
        """
        return self._text_extraction_model_version

    @text_extraction_model_version.setter
    def text_extraction_model_version(self, text_extraction_model_version):
        """
        Sets the text_extraction_model_version of this AnalyzeDocumentResult.
        The document text extraction model version.


        :param text_extraction_model_version: The text_extraction_model_version of this AnalyzeDocumentResult.
        :type: str
        """
        self._text_extraction_model_version = text_extraction_model_version

    @property
    def key_value_extraction_model_version(self):
        """
        Gets the key_value_extraction_model_version of this AnalyzeDocumentResult.
        The document keyValue extraction model version.


        :return: The key_value_extraction_model_version of this AnalyzeDocumentResult.
        :rtype: str
        """
        return self._key_value_extraction_model_version

    @key_value_extraction_model_version.setter
    def key_value_extraction_model_version(self, key_value_extraction_model_version):
        """
        Sets the key_value_extraction_model_version of this AnalyzeDocumentResult.
        The document keyValue extraction model version.


        :param key_value_extraction_model_version: The key_value_extraction_model_version of this AnalyzeDocumentResult.
        :type: str
        """
        self._key_value_extraction_model_version = key_value_extraction_model_version

    @property
    def table_extraction_model_version(self):
        """
        Gets the table_extraction_model_version of this AnalyzeDocumentResult.
        The document table extraction model version.


        :return: The table_extraction_model_version of this AnalyzeDocumentResult.
        :rtype: str
        """
        return self._table_extraction_model_version

    @table_extraction_model_version.setter
    def table_extraction_model_version(self, table_extraction_model_version):
        """
        Sets the table_extraction_model_version of this AnalyzeDocumentResult.
        The document table extraction model version.


        :param table_extraction_model_version: The table_extraction_model_version of this AnalyzeDocumentResult.
        :type: str
        """
        self._table_extraction_model_version = table_extraction_model_version

    @property
    def errors(self):
        """
        Gets the errors of this AnalyzeDocumentResult.
        The errors encountered during document analysis.


        :return: The errors of this AnalyzeDocumentResult.
        :rtype: list[oci.ai_document.models.ProcessingError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this AnalyzeDocumentResult.
        The errors encountered during document analysis.


        :param errors: The errors of this AnalyzeDocumentResult.
        :type: list[oci.ai_document.models.ProcessingError]
        """
        self._errors = errors

    @property
    def searchable_pdf(self):
        """
        Gets the searchable_pdf of this AnalyzeDocumentResult.
        The searchable PDF file that was generated.


        :return: The searchable_pdf of this AnalyzeDocumentResult.
        :rtype: str
        """
        return self._searchable_pdf

    @searchable_pdf.setter
    def searchable_pdf(self, searchable_pdf):
        """
        Sets the searchable_pdf of this AnalyzeDocumentResult.
        The searchable PDF file that was generated.


        :param searchable_pdf: The searchable_pdf of this AnalyzeDocumentResult.
        :type: str
        """
        self._searchable_pdf = searchable_pdf

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other