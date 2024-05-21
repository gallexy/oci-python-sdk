# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220926

from __future__ import absolute_import

from .email_address import EmailAddress
from .email_submitted_response import EmailSubmittedResponse
from .recipients import Recipients
from .sender import Sender
from .submit_email_details import SubmitEmailDetails

# Maps type names to classes for email_data_plane services.
email_data_plane_type_mapping = {
    "EmailAddress": EmailAddress,
    "EmailSubmittedResponse": EmailSubmittedResponse,
    "Recipients": Recipients,
    "Sender": Sender,
    "SubmitEmailDetails": SubmitEmailDetails
}