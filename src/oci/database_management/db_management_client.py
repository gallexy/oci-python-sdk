# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from .models import database_management_type_mapping
missing = Sentinel("Missing")


class DbManagementClient(object):
    """
    Use the Database Management API to perform tasks such as obtaining performance and resource usage metrics
    for a fleet of Managed Databases or a specific Managed Database, creating Managed Database Groups, and
    running a SQL job on a Managed Database or Managed Database Group.
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default values are connection timeout 10 seconds and read timeout 60 seconds. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.
        """
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']

        elif AUTHENTICATION_TYPE_FIELD_NAME in config:
            signer = get_signer_from_authentication_type(config)

        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'base_path': '/20201101',
            'service_endpoint_template': 'https://dbmgmt.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        self.base_client = BaseClient("db_management", config, signer, database_management_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def add_managed_database_to_managed_database_group(self, managed_database_group_id, add_managed_database_to_managed_database_group_details, **kwargs):
        """
        Adds a Managed Database to a specific Managed Database Group.
        After the database is added, it will be included in the
        management activities performed on the Managed Database Group.


        :param str managed_database_group_id: (required)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_management.models.AddManagedDatabaseToManagedDatabaseGroupDetails add_managed_database_to_managed_database_group_details: (required)
            The Managed Database details required to add the Managed Database to a Managed Database Group.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/add_managed_database_to_managed_database_group.py.html>`__ to see an example of how to use add_managed_database_to_managed_database_group API.
        """
        resource_path = "/managedDatabaseGroups/{managedDatabaseGroupId}/actions/addManagedDatabase"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "add_managed_database_to_managed_database_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseGroupId": managed_database_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=add_managed_database_to_managed_database_group_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=add_managed_database_to_managed_database_group_details)

    def change_database_parameters(self, managed_database_id, change_database_parameters_details, **kwargs):
        """
        Changes database parameter values. There are two kinds of database
        parameters:

        - Dynamic parameters: They can be changed for the current Oracle
        Database instance. The changes take effect immediately.
        - Static parameters: They cannot be changed for the current instance.
        You must change these parameters and then restart the database before
        changes take effect.

        **Note:** If the instance is started using a text initialization
        parameter file, the parameter changes are applicable only for the
        current instance. You must update them manually to be passed to
        a future instance.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_management.models.ChangeDatabaseParametersDetails change_database_parameters_details: (required)
            The details required to change database parameter values.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.UpdateDatabaseParametersResult`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/change_database_parameters.py.html>`__ to see an example of how to use change_database_parameters API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/actions/changeDatabaseParameters"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_database_parameters got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_database_parameters_details,
                response_type="UpdateDatabaseParametersResult")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_database_parameters_details,
                response_type="UpdateDatabaseParametersResult")

    def change_job_compartment(self, job_id, change_job_compartment_details, **kwargs):
        """
        Moves a job.


        :param str job_id: (required)
            The identifier of the job.

        :param oci.database_management.models.ChangeJobCompartmentDetails change_job_compartment_details: (required)
            The `OCID`__ of the compartment to move the job to.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/change_job_compartment.py.html>`__ to see an example of how to use change_job_compartment API.
        """
        resource_path = "/jobs/{jobId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_job_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobId": job_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_job_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_job_compartment_details)

    def change_managed_database_group_compartment(self, managed_database_group_id, change_managed_database_group_compartment_details, **kwargs):
        """
        Moves a Managed Database Group to a different compartment.
        The destination compartment must not have a Managed Database Group
        with the same name.


        :param str managed_database_group_id: (required)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_management.models.ChangeManagedDatabaseGroupCompartmentDetails change_managed_database_group_compartment_details: (required)
            The `OCID`__ of the compartment to move the Managed Database Group to.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/change_managed_database_group_compartment.py.html>`__ to see an example of how to use change_managed_database_group_compartment API.
        """
        resource_path = "/managedDatabaseGroups/{managedDatabaseGroupId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_managed_database_group_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseGroupId": managed_database_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_managed_database_group_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_managed_database_group_compartment_details)

    def create_job(self, create_job_details, **kwargs):
        """
        Creates a job to be executed on a Managed Database or Managed Database Group. Only one
        of the parameters, managedDatabaseId or managedDatabaseGroupId should be provided as
        input in CreateJobDetails resource in request body.


        :param oci.database_management.models.CreateJobDetails create_job_details: (required)
            The details required to create a job.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.Job`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/create_job.py.html>`__ to see an example of how to use create_job API.
        """
        resource_path = "/jobs"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_job got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_job_details,
                response_type="Job")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_job_details,
                response_type="Job")

    def create_managed_database_group(self, create_managed_database_group_details, **kwargs):
        """
        Creates a Managed Database Group. The group does not contain any
        Managed Databases when it is created, and they must be added later.


        :param oci.database_management.models.CreateManagedDatabaseGroupDetails create_managed_database_group_details: (required)
            The details required to create a Managed Database Group.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.ManagedDatabaseGroup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/create_managed_database_group.py.html>`__ to see an example of how to use create_managed_database_group API.
        """
        resource_path = "/managedDatabaseGroups"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_managed_database_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_managed_database_group_details,
                response_type="ManagedDatabaseGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_managed_database_group_details,
                response_type="ManagedDatabaseGroup")

    def delete_job(self, job_id, **kwargs):
        """
        Deletes the job specified by jobId.


        :param str job_id: (required)
            The identifier of the job.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/delete_job.py.html>`__ to see an example of how to use delete_job API.
        """
        resource_path = "/jobs/{jobId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_job got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobId": job_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_managed_database_group(self, managed_database_group_id, **kwargs):
        """
        Deletes the Managed Database Group specified by managedDatabaseGroupId.
        If the group contains Managed Databases, then it cannot be deleted.


        :param str managed_database_group_id: (required)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/delete_managed_database_group.py.html>`__ to see an example of how to use delete_managed_database_group API.
        """
        resource_path = "/managedDatabaseGroups/{managedDatabaseGroupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_managed_database_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseGroupId": managed_database_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def get_awr_db_report(self, managed_database_id, awr_db_id, **kwargs):
        """
        Gets the AWR report for the specified Managed Database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str awr_db_id: (required)
            The parameter to filter the database by internal ID.
            Note that the internal ID of the database can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbs:

        :param list[int] inst_nums: (optional)
            The optional multiple value query parameter to filter the database instance numbers.

        :param int begin_sn_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_sn_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot ID.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param str report_type: (optional)
            The query parameter to filter the AWR report types.

            Allowed values are: "AWR", "ASH"

        :param int container_id: (optional)
            The optional query parameter to filter the database container by an exact ID value.
            Note that the database container ID can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

        :param str report_format: (optional)
            The format of the AWR report.

            Allowed values are: "HTML", "TEXT"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbReport`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_awr_db_report.py.html>`__ to see an example of how to use get_awr_db_report API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbReport"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "inst_nums",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "report_type",
            "container_id",
            "report_format",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_awr_db_report got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "awrDbId": awr_db_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'report_type' in kwargs:
            report_type_allowed_values = ["AWR", "ASH"]
            if kwargs['report_type'] not in report_type_allowed_values:
                raise ValueError(
                    "Invalid value for `report_type`, must be one of {0}".format(report_type_allowed_values)
                )

        if 'report_format' in kwargs:
            report_format_allowed_values = ["HTML", "TEXT"]
            if kwargs['report_format'] not in report_format_allowed_values:
                raise ValueError(
                    "Invalid value for `report_format`, must be one of {0}".format(report_format_allowed_values)
                )

        query_params = {
            "instNums": self.base_client.generate_collection_format_param(kwargs.get("inst_nums", missing), 'csv'),
            "beginSnIdGreaterThanOrEqualTo": kwargs.get("begin_sn_id_greater_than_or_equal_to", missing),
            "endSnIdLessThanOrEqualTo": kwargs.get("end_sn_id_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "reportType": kwargs.get("report_type", missing),
            "containerId": kwargs.get("container_id", missing),
            "reportFormat": kwargs.get("report_format", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbReport")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbReport")

    def get_awr_db_sql_report(self, managed_database_id, awr_db_id, sql_id, **kwargs):
        """
        Get a AWR SQL report for one SQL.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str awr_db_id: (required)
            The parameter to filter the database by internal ID.
            Note that the internal ID of the database can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbs:

        :param str sql_id: (required)
            The parameter to filter SQL by ID. Note that the SQL ID is generated internally by Oracle for each SQL statement and can be retrieved from AWR Report API (/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbReport) or Performance Hub API (/internal/managedDatabases/{managedDatabaseId}/actions/retrievePerformanceData)

        :param str inst_num: (optional)
            The optional single value query parameter to filter the database instance number.

        :param int begin_sn_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_sn_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot ID.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param str report_format: (optional)
            The format of the AWR report.

            Allowed values are: "HTML", "TEXT"

        :param int container_id: (optional)
            The optional query parameter to filter the database container by an exact ID value.
            Note that the database container ID can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbSqlReport`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_awr_db_sql_report.py.html>`__ to see an example of how to use get_awr_db_sql_report API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSqlReport"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "report_format",
            "container_id",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_awr_db_sql_report got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "awrDbId": awr_db_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'report_format' in kwargs:
            report_format_allowed_values = ["HTML", "TEXT"]
            if kwargs['report_format'] not in report_format_allowed_values:
                raise ValueError(
                    "Invalid value for `report_format`, must be one of {0}".format(report_format_allowed_values)
                )

        query_params = {
            "instNum": kwargs.get("inst_num", missing),
            "beginSnIdGreaterThanOrEqualTo": kwargs.get("begin_sn_id_greater_than_or_equal_to", missing),
            "endSnIdLessThanOrEqualTo": kwargs.get("end_sn_id_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "sqlId": sql_id,
            "reportFormat": kwargs.get("report_format", missing),
            "containerId": kwargs.get("container_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbSqlReport")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbSqlReport")

    def get_cluster_cache_metric(self, managed_database_id, start_time, end_time, **kwargs):
        """
        Gets the metrics related to cluster cache for the Oracle
        Real Application Clusters (Oracle RAC) database specified
        by managedDatabaseId.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str start_time: (required)
            The start time for the time range to retrieve the health metrics of a Managed Database
            in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

        :param str end_time: (required)
            The end time for the time range to retrieve the health metrics of a Managed Database
            in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.ClusterCacheMetric`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_cluster_cache_metric.py.html>`__ to see an example of how to use get_cluster_cache_metric API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/clusterCacheMetrics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_cluster_cache_metric got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "startTime": start_time,
            "endTime": end_time
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ClusterCacheMetric")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ClusterCacheMetric")

    def get_database_fleet_health_metrics(self, compare_baseline_time, compare_target_time, **kwargs):
        """
        Gets the health metrics for a fleet of databases in a compartment or in a Managed Database Group.
        Either the CompartmentId or the ManagedDatabaseGroupId query parameters must be provided to retrieve the health metrics.


        :param str compare_baseline_time: (required)
            The baseline time for metrics comparison.

        :param str compare_target_time: (required)
            The target time for metrics comparison.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str managed_database_group_id: (optional)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str compare_type: (optional)
            The time window used for metrics comparison.

            Allowed values are: "HOUR", "DAY"

        :param str filter_by_metric_names: (optional)
            The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the service returns all supported metrics.

        :param str filter_by_database_type: (optional)
            The filter used to filter the databases in the fleet by a specific Oracle Database type.

        :param str filter_by_database_sub_type: (optional)
            The filter used to filter the databases in the fleet by a specific Oracle Database subtype.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.DatabaseFleetHealthMetrics`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_database_fleet_health_metrics.py.html>`__ to see an example of how to use get_database_fleet_health_metrics API.
        """
        resource_path = "/fleetMetrics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "managed_database_group_id",
            "compartment_id",
            "compare_type",
            "filter_by_metric_names",
            "filter_by_database_type",
            "filter_by_database_sub_type"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_database_fleet_health_metrics got unknown kwargs: {!r}".format(extra_kwargs))

        if 'compare_type' in kwargs:
            compare_type_allowed_values = ["HOUR", "DAY"]
            if kwargs['compare_type'] not in compare_type_allowed_values:
                raise ValueError(
                    "Invalid value for `compare_type`, must be one of {0}".format(compare_type_allowed_values)
                )

        query_params = {
            "managedDatabaseGroupId": kwargs.get("managed_database_group_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "compareBaselineTime": compare_baseline_time,
            "compareTargetTime": compare_target_time,
            "compareType": kwargs.get("compare_type", missing),
            "filterByMetricNames": kwargs.get("filter_by_metric_names", missing),
            "filterByDatabaseType": kwargs.get("filter_by_database_type", missing),
            "filterByDatabaseSubType": kwargs.get("filter_by_database_sub_type", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="DatabaseFleetHealthMetrics")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="DatabaseFleetHealthMetrics")

    def get_database_home_metrics(self, managed_database_id, start_time, end_time, **kwargs):
        """
        Gets a summary of the activity and resource usage metrics like DB Time, CPU, User I/O, Wait, Storage, and Memory for a Managed Database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str start_time: (required)
            The start time for the time range to retrieve the health metrics of a Managed Database
            in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

        :param str end_time: (required)
            The end time for the time range to retrieve the health metrics of a Managed Database
            in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.DatabaseHomeMetrics`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_database_home_metrics.py.html>`__ to see an example of how to use get_database_home_metrics API.
        """
        resource_path = "/databaseHomeMetrics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_database_home_metrics got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "managedDatabaseId": managed_database_id,
            "startTime": start_time,
            "endTime": end_time
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="DatabaseHomeMetrics")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="DatabaseHomeMetrics")

    def get_job(self, job_id, **kwargs):
        """
        Gets the details for the job specified by jobId.


        :param str job_id: (required)
            The identifier of the job.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.Job`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_job.py.html>`__ to see an example of how to use get_job API.
        """
        resource_path = "/jobs/{jobId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_job got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobId": job_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Job")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Job")

    def get_job_execution(self, job_execution_id, **kwargs):
        """
        Gets the details for the job execution specified by jobExecutionId.


        :param str job_execution_id: (required)
            The identifier of the job execution.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.JobExecution`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_job_execution.py.html>`__ to see an example of how to use get_job_execution API.
        """
        resource_path = "/jobExecutions/{jobExecutionId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_job_execution got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobExecutionId": job_execution_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="JobExecution")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="JobExecution")

    def get_job_run(self, job_run_id, **kwargs):
        """
        Gets the details for the job run specified by jobRunId.


        :param str job_run_id: (required)
            The identifier of the job run.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.JobRun`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_job_run.py.html>`__ to see an example of how to use get_job_run API.
        """
        resource_path = "/jobRuns/{jobRunId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_job_run got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobRunId": job_run_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="JobRun")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="JobRun")

    def get_managed_database(self, managed_database_id, **kwargs):
        """
        Gets the details for the Managed Database specified by managedDatabaseId.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.ManagedDatabase`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_managed_database.py.html>`__ to see an example of how to use get_managed_database API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_managed_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ManagedDatabase")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ManagedDatabase")

    def get_managed_database_group(self, managed_database_group_id, **kwargs):
        """
        Gets the details for the Managed Database Group specified by managedDatabaseGroupId.


        :param str managed_database_group_id: (required)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.ManagedDatabaseGroup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_managed_database_group.py.html>`__ to see an example of how to use get_managed_database_group API.
        """
        resource_path = "/managedDatabaseGroups/{managedDatabaseGroupId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_managed_database_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseGroupId": managed_database_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ManagedDatabaseGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ManagedDatabaseGroup")

    def list_awr_db_snapshots(self, managed_database_id, awr_db_id, **kwargs):
        """
        Lists AWR snapshots for the specified database in the AWR.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str awr_db_id: (required)
            The parameter to filter the database by internal ID.
            Note that the internal ID of the database can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbs:

        :param str inst_num: (optional)
            The optional single value query parameter to filter the database instance number.

        :param int begin_sn_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_sn_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot ID.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param int container_id: (optional)
            The optional query parameter to filter the database container by an exact ID value.
            Note that the database container ID can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in paginated response.

        :param str sort_by: (optional)
            The option to sort the AWR snapshot summary data.

            Allowed values are: "TIME_BEGIN", "SNAPSHOT_ID"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbSnapshotCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_awr_db_snapshots.py.html>`__ to see an example of how to use list_awr_db_snapshots API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "container_id",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_awr_db_snapshots got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "awrDbId": awr_db_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_BEGIN", "SNAPSHOT_ID"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "instNum": kwargs.get("inst_num", missing),
            "beginSnIdGreaterThanOrEqualTo": kwargs.get("begin_sn_id_greater_than_or_equal_to", missing),
            "endSnIdLessThanOrEqualTo": kwargs.get("end_sn_id_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "containerId": kwargs.get("container_id", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbSnapshotCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbSnapshotCollection")

    def list_awr_dbs(self, managed_database_id, **kwargs):
        """
        Gets the list of databases and their snapshot summary details available in the AWR of the specified Managed Database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str name: (optional)
            The optional single value query parameter to filter the entity name.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in paginated response.

        :param str sort_by: (optional)
            The option to sort the AWR summary data.

            Allowed values are: "END_INTERVAL_TIME", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_awr_dbs.py.html>`__ to see an example of how to use list_awr_dbs API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "name",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_awr_dbs got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["END_INTERVAL_TIME", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "name": kwargs.get("name", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbCollection")

    def list_database_parameters(self, managed_database_id, **kwargs):
        """
        Gets the list of database parameters for the specified Managed Database. The parameters are listed in alphabetical order, along with their current values.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str source: (optional)
            The source used to list database parameters. `CURRENT` is used to get the
            database parameters that are currently in effect for the database
            instance. `SPFILE` is used to list parameters from the server parameter
            file. Default is `CURRENT`.

            Allowed values are: "CURRENT", "SPFILE"

        :param str name: (optional)
            A filter to return all parameters that have the text given in their names.

        :param bool is_allowed_values_included: (optional)
            When true, results include a list of valid values for parameters (if applicable).

        :param str sort_by: (optional)
            The field to sort information by. Only one sortOrder can be used. The
            default sort order for `NAME` is ascending and it is case-sensitive.

            Allowed values are: "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.DatabaseParametersCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_database_parameters.py.html>`__ to see an example of how to use list_database_parameters API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/databaseParameters"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "source",
            "name",
            "is_allowed_values_included",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_database_parameters got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'source' in kwargs:
            source_allowed_values = ["CURRENT", "SPFILE"]
            if kwargs['source'] not in source_allowed_values:
                raise ValueError(
                    "Invalid value for `source`, must be one of {0}".format(source_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "source": kwargs.get("source", missing),
            "name": kwargs.get("name", missing),
            "isAllowedValuesIncluded": kwargs.get("is_allowed_values_included", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DatabaseParametersCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DatabaseParametersCollection")

    def list_job_executions(self, compartment_id, **kwargs):
        """
        Gets the job execution for a specific ID or the list of job executions for a job, Managed Database or Managed Database Group
        in a specific compartment. Only one of the parameters, ID, jobId, managedDatabaseId or managedDatabaseGroupId should be provided.
        If none of these parameters is provided, all the job executions in the compartment are listed. Job executions can also be filtered
        based on the name and status parameters.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str id: (optional)
            The identifier of the resource.

        :param str job_id: (optional)
            The identifier of the job.

        :param str managed_database_id: (optional)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str managed_database_group_id: (optional)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str status: (optional)
            The status of the job execution.

        :param str name: (optional)
            A filter to return only resources that match the entire name.

        :param int limit: (optional)
            The maximum number of records returned in paginated response.

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param str sort_by: (optional)
            The field to sort information by. Only one sortOrder can be used. The default sort order
            for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending.
            The \u2018NAME\u2019 sort order is case-sensitive.

            Allowed values are: "TIMECREATED", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.JobExecutionCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_job_executions.py.html>`__ to see an example of how to use list_job_executions API.
        """
        resource_path = "/jobExecutions"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "id",
            "job_id",
            "managed_database_id",
            "managed_database_group_id",
            "status",
            "name",
            "limit",
            "page",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_job_executions got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "id": kwargs.get("id", missing),
            "jobId": kwargs.get("job_id", missing),
            "managedDatabaseId": kwargs.get("managed_database_id", missing),
            "managedDatabaseGroupId": kwargs.get("managed_database_group_id", missing),
            "status": kwargs.get("status", missing),
            "name": kwargs.get("name", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="JobExecutionCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="JobExecutionCollection")

    def list_job_runs(self, compartment_id, **kwargs):
        """
        Gets the job run for a specific ID or the list of job runs for a job, Managed Database or Managed Database Group
        in a specific compartment. Only one of the parameters, ID, jobId, managedDatabaseId, or managedDatabaseGroupId
        should be provided. If none of these parameters is provided, all the job runs in the compartment are listed.
        Job runs can also be filtered based on name and runStatus parameters.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str id: (optional)
            The identifier of the resource.

        :param str job_id: (optional)
            The identifier of the job.

        :param str managed_database_id: (optional)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str managed_database_group_id: (optional)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str run_status: (optional)
            The status of the job run.

        :param str name: (optional)
            A filter to return only resources that match the entire name.

        :param int limit: (optional)
            The maximum number of records returned in paginated response.

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param str sort_by: (optional)
            The field to sort information by. Only one sortOrder can be used. The default sort order
            for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending.
            The \u2018NAME\u2019 sort order is case-sensitive.

            Allowed values are: "TIMECREATED", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.JobRunCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_job_runs.py.html>`__ to see an example of how to use list_job_runs API.
        """
        resource_path = "/jobRuns"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "id",
            "job_id",
            "managed_database_id",
            "managed_database_group_id",
            "run_status",
            "name",
            "limit",
            "page",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_job_runs got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "id": kwargs.get("id", missing),
            "jobId": kwargs.get("job_id", missing),
            "managedDatabaseId": kwargs.get("managed_database_id", missing),
            "managedDatabaseGroupId": kwargs.get("managed_database_group_id", missing),
            "runStatus": kwargs.get("run_status", missing),
            "name": kwargs.get("name", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="JobRunCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="JobRunCollection")

    def list_jobs(self, compartment_id, **kwargs):
        """
        Gets the job for a specific ID or the list of jobs for a Managed Database or Managed Database Group
        in a specific compartment. Only one of the parameters, ID, managedDatabaseId or managedDatabaseGroupId,
        should be provided. If none of these parameters is provided, all the jobs in the compartment are listed.
        Jobs can also be filtered based on the name and lifecycleState parameters.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str id: (optional)
            The identifier of the resource.

        :param str managed_database_group_id: (optional)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str managed_database_id: (optional)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str name: (optional)
            A filter to return only resources that match the entire name.

        :param str lifecycle_state: (optional)
            The lifecycle state of the job.

            Allowed values are: "ACTIVE", "INACTIVE"

        :param int limit: (optional)
            The maximum number of records returned in paginated response.

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param str sort_by: (optional)
            The field to sort information by. Only one sortOrder can be used. The default sort order
            for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending.
            The \u2018NAME\u2019 sort order is case-sensitive.

            Allowed values are: "TIMECREATED", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.JobCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_jobs.py.html>`__ to see an example of how to use list_jobs API.
        """
        resource_path = "/jobs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "id",
            "managed_database_group_id",
            "managed_database_id",
            "name",
            "lifecycle_state",
            "limit",
            "page",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_jobs got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "INACTIVE"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "id": kwargs.get("id", missing),
            "managedDatabaseGroupId": kwargs.get("managed_database_group_id", missing),
            "managedDatabaseId": kwargs.get("managed_database_id", missing),
            "name": kwargs.get("name", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="JobCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="JobCollection")

    def list_managed_database_groups(self, compartment_id, **kwargs):
        """
        Gets the Managed Database Group for a specific ID or the list of Managed Database Groups in
        a specific compartment. Managed Database Groups can also be filtered based on the name parameter.
        Only one of the parameters, ID or name should be provided. If none of these parameters is provided,
        all the Managed Database Groups in the compartment are listed.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str id: (optional)
            The identifier of the resource.

        :param str name: (optional)
            A filter to return only resources that match the entire name.

        :param str lifecycle_state: (optional)
            The lifecycle state of a resource.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in paginated response.

        :param str sort_by: (optional)
            The field to sort information by. Only one sortOrder can be used. The default sort order
            for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending.
            The \u2018NAME\u2019 sort order is case-sensitive.

            Allowed values are: "TIMECREATED", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.ManagedDatabaseGroupCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_managed_database_groups.py.html>`__ to see an example of how to use list_managed_database_groups API.
        """
        resource_path = "/managedDatabaseGroups"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "id",
            "name",
            "lifecycle_state",
            "page",
            "limit",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_managed_database_groups got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "id": kwargs.get("id", missing),
            "name": kwargs.get("name", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ManagedDatabaseGroupCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ManagedDatabaseGroupCollection")

    def list_managed_databases(self, compartment_id, **kwargs):
        """
        Gets the Managed Database for a specific ID or the list of Managed Databases in a specific compartment.
        Managed Databases can also be filtered based on the name parameter. Only one of the parameters, ID or name
        should be provided. If none of these parameters is provided, all the Managed Databases in the compartment are listed.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str id: (optional)
            The identifier of the resource.

        :param str name: (optional)
            A filter to return only resources that match the entire name.

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in paginated response.

        :param str sort_by: (optional)
            The field to sort information by. Only one sortOrder can be used. The default sort order
            for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending.
            The \u2018NAME\u2019 sort order is case-sensitive.

            Allowed values are: "TIMECREATED", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.ManagedDatabaseCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_managed_databases.py.html>`__ to see an example of how to use list_managed_databases API.
        """
        resource_path = "/managedDatabases"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "id",
            "name",
            "page",
            "limit",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_managed_databases got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "id": kwargs.get("id", missing),
            "name": kwargs.get("name", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ManagedDatabaseCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ManagedDatabaseCollection")

    def list_tablespaces(self, managed_database_id, **kwargs):
        """
        Gets the list of tablespaces for the specified managedDatabaseId.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str name: (optional)
            A filter to return only resources that match the entire name.

        :param str sort_by: (optional)
            The field to sort information by. Only one sortOrder can be used. The default sort order
            for \u2018TIMECREATED\u2019 is descending and the default sort order for \u2018NAME\u2019 is ascending.
            The \u2018NAME\u2019 sort order is case-sensitive.

            Allowed values are: "TIMECREATED", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in paginated response.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.TablespaceCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_tablespaces.py.html>`__ to see an example of how to use list_tablespaces API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/tablespaces"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "name",
            "sort_by",
            "sort_order",
            "page",
            "limit"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_tablespaces got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "name": kwargs.get("name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="TablespaceCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="TablespaceCollection")

    def remove_managed_database_from_managed_database_group(self, managed_database_group_id, remove_managed_database_from_managed_database_group_details, **kwargs):
        """
        Removes a Managed Database from a Managed Database Group. Any management
        activities that are currently running on this database will continue to
        run to completion. However, any activities scheduled to run in the future
        will not be performed on this database.


        :param str managed_database_group_id: (required)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_management.models.RemoveManagedDatabaseFromManagedDatabaseGroupDetails remove_managed_database_from_managed_database_group_details: (required)
            The Managed Database details required to remove the Managed Database from a Managed Database Group.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/remove_managed_database_from_managed_database_group.py.html>`__ to see an example of how to use remove_managed_database_from_managed_database_group API.
        """
        resource_path = "/managedDatabaseGroups/{managedDatabaseGroupId}/actions/removeManagedDatabase"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "remove_managed_database_from_managed_database_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseGroupId": managed_database_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=remove_managed_database_from_managed_database_group_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=remove_managed_database_from_managed_database_group_details)

    def reset_database_parameters(self, managed_database_id, reset_database_parameters_details, **kwargs):
        """
        Resets database parameter values to their default or startup values.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_management.models.ResetDatabaseParametersDetails reset_database_parameters_details: (required)
            The details required to reset database parameters.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.UpdateDatabaseParametersResult`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/reset_database_parameters.py.html>`__ to see an example of how to use reset_database_parameters API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/actions/resetDatabaseParameters"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "reset_database_parameters got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=reset_database_parameters_details,
                response_type="UpdateDatabaseParametersResult")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=reset_database_parameters_details,
                response_type="UpdateDatabaseParametersResult")

    def summarize_awr_db_cpu_usages(self, managed_database_id, awr_db_id, **kwargs):
        """
        Summarizes the AWR CPU resource limits and metrics for the specified database in AWR.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str awr_db_id: (required)
            The parameter to filter the database by internal ID.
            Note that the internal ID of the database can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbs:

        :param str inst_num: (optional)
            The optional single value query parameter to filter the database instance number.

        :param int begin_sn_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_sn_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot ID.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param str session_type: (optional)
            The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.

            Allowed values are: "FOREGROUND", "BACKGROUND", "ALL"

        :param int container_id: (optional)
            The optional query parameter to filter the database container by an exact ID value.
            Note that the database container ID can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in large paginated response.

        :param str sort_by: (optional)
            The option to sort the AWR CPU usage summary data.

            Allowed values are: "TIME_SAMPLED", "AVG_VALUE"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbCpuUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/summarize_awr_db_cpu_usages.py.html>`__ to see an example of how to use summarize_awr_db_cpu_usages API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbCpuUsages"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "session_type",
            "container_id",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_awr_db_cpu_usages got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "awrDbId": awr_db_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'session_type' in kwargs:
            session_type_allowed_values = ["FOREGROUND", "BACKGROUND", "ALL"]
            if kwargs['session_type'] not in session_type_allowed_values:
                raise ValueError(
                    "Invalid value for `session_type`, must be one of {0}".format(session_type_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_SAMPLED", "AVG_VALUE"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "instNum": kwargs.get("inst_num", missing),
            "beginSnIdGreaterThanOrEqualTo": kwargs.get("begin_sn_id_greater_than_or_equal_to", missing),
            "endSnIdLessThanOrEqualTo": kwargs.get("end_sn_id_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "sessionType": kwargs.get("session_type", missing),
            "containerId": kwargs.get("container_id", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbCpuUsageCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbCpuUsageCollection")

    def summarize_awr_db_metrics(self, managed_database_id, awr_db_id, name, **kwargs):
        """
        Summarizes the metric samples for the specified database in the AWR. The metric samples are summarized based on the Time dimension for each metric.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str awr_db_id: (required)
            The parameter to filter the database by internal ID.
            Note that the internal ID of the database can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbs:

        :param oci.database_management.models.list[str] name: (required)
            The required multiple value query parameter to filter the entity name.

        :param str inst_num: (optional)
            The optional single value query parameter to filter the database instance number.

        :param int begin_sn_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_sn_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot ID.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param int container_id: (optional)
            The optional query parameter to filter the database container by an exact ID value.
            Note that the database container ID can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in large paginated response.

        :param str sort_by: (optional)
            The option to sort the AWR time series summary data.

            Allowed values are: "TIMESTAMP", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbMetricCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/summarize_awr_db_metrics.py.html>`__ to see an example of how to use summarize_awr_db_metrics API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbMetrics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "container_id",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_awr_db_metrics got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "awrDbId": awr_db_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMESTAMP", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "instNum": kwargs.get("inst_num", missing),
            "beginSnIdGreaterThanOrEqualTo": kwargs.get("begin_sn_id_greater_than_or_equal_to", missing),
            "endSnIdLessThanOrEqualTo": kwargs.get("end_sn_id_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "name": self.base_client.generate_collection_format_param(name, 'multi'),
            "containerId": kwargs.get("container_id", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbMetricCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbMetricCollection")

    def summarize_awr_db_parameter_changes(self, managed_database_id, awr_db_id, name, **kwargs):
        """
        Summarizes the AWR database parameter change history for one database parameter of the specified Managed Database. One change history record contains
        the previous value, the changed value, and the corresponding time range. If the database parameter value was changed multiple times within the time range, then multiple change history records are created for the same parameter.
        Note that this API only returns information on change history details for one database parameter.
        To get a list of all the database parameters whose values were changed during a specified time range, use the following API endpoint:
        /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameters


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str awr_db_id: (required)
            The parameter to filter the database by internal ID.
            Note that the internal ID of the database can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbs:

        :param str name: (required)
            The required single value query parameter to filter the entity name.

        :param str inst_num: (optional)
            The optional single value query parameter to filter the database instance number.

        :param int begin_sn_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_sn_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot ID.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param int container_id: (optional)
            The optional query parameter to filter the database container by an exact ID value.
            Note that the database container ID can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in large paginated response.

        :param str sort_by: (optional)
            The option to sort the AWR database parameter change history data.

            Allowed values are: "IS_CHANGED", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbParameterChangeCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/summarize_awr_db_parameter_changes.py.html>`__ to see an example of how to use summarize_awr_db_parameter_changes API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameterChanges"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "container_id",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_awr_db_parameter_changes got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "awrDbId": awr_db_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["IS_CHANGED", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "instNum": kwargs.get("inst_num", missing),
            "beginSnIdGreaterThanOrEqualTo": kwargs.get("begin_sn_id_greater_than_or_equal_to", missing),
            "endSnIdLessThanOrEqualTo": kwargs.get("end_sn_id_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "containerId": kwargs.get("container_id", missing),
            "name": name,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbParameterChangeCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbParameterChangeCollection")

    def summarize_awr_db_parameters(self, managed_database_id, awr_db_id, **kwargs):
        """
        Summarizes the AWR database parameter history for the specified Managed Database. This includes the list of database
        parameters, with information on whether the parameter values were modified within the query time range. Note that
        each database parameter is only listed once. The returned summary gets all the database parameters, which include:
         -Each parameter whose value was changed during the time range: AwrDbParameterValueOptionalQueryParam (valueChanged =\"Y\")
         -Each parameter whose value was unchanged during the time range: AwrDbParameterValueOptionalQueryParam (valueChanged =\"N\")
         -Each parameter whose value was changed at the system level during the time range: (valueChanged =\"Y\"  and valueModified = \"SYSTEM_MOD\").
         -Each parameter whose value was unchanged during the time range, however, the value is not the default value: (valueChanged =\"N\" and  valueDefault = \"FALSE\")
        Note that this API does not return information on the number of times each database parameter has been changed within the time range. To get the database parameter value change history for a specific parameter, use the following API endpoint:
        /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameterChanges


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str awr_db_id: (required)
            The parameter to filter the database by internal ID.
            Note that the internal ID of the database can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbs:

        :param str inst_num: (optional)
            The optional single value query parameter to filter the database instance number.

        :param int begin_sn_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_sn_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot ID.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param int container_id: (optional)
            The optional query parameter to filter the database container by an exact ID value.
            Note that the database container ID can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

        :param list[str] name: (optional)
            The optional multiple value query parameter to filter the entity name.

        :param str name_contains: (optional)
            The optional contains query parameter to filter the entity name by any part of the name.

        :param str value_changed: (optional)
            The optional query parameter to filter database parameters whose values were changed.

            Allowed values are: "Y", "N"

        :param str value_default: (optional)
            The optional query parameter to filter the database parameters that had the default value in the last snapshot.

            Allowed values are: "TRUE", "FALSE"

        :param str value_modified: (optional)
            The optional query parameter to filter the database parameters that had a modified value in the last snapshot.

            Allowed values are: "MODIFIED", "SYSTEM_MOD", "FALSE"

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in large paginated response.

        :param str sort_by: (optional)
            The option to sort the AWR database parameter change history data.

            Allowed values are: "IS_CHANGED", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbParameterCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/summarize_awr_db_parameters.py.html>`__ to see an example of how to use summarize_awr_db_parameters API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameters"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "container_id",
            "name",
            "name_contains",
            "value_changed",
            "value_default",
            "value_modified",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_awr_db_parameters got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "awrDbId": awr_db_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'value_changed' in kwargs:
            value_changed_allowed_values = ["Y", "N"]
            if kwargs['value_changed'] not in value_changed_allowed_values:
                raise ValueError(
                    "Invalid value for `value_changed`, must be one of {0}".format(value_changed_allowed_values)
                )

        if 'value_default' in kwargs:
            value_default_allowed_values = ["TRUE", "FALSE"]
            if kwargs['value_default'] not in value_default_allowed_values:
                raise ValueError(
                    "Invalid value for `value_default`, must be one of {0}".format(value_default_allowed_values)
                )

        if 'value_modified' in kwargs:
            value_modified_allowed_values = ["MODIFIED", "SYSTEM_MOD", "FALSE"]
            if kwargs['value_modified'] not in value_modified_allowed_values:
                raise ValueError(
                    "Invalid value for `value_modified`, must be one of {0}".format(value_modified_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["IS_CHANGED", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "instNum": kwargs.get("inst_num", missing),
            "beginSnIdGreaterThanOrEqualTo": kwargs.get("begin_sn_id_greater_than_or_equal_to", missing),
            "endSnIdLessThanOrEqualTo": kwargs.get("end_sn_id_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "containerId": kwargs.get("container_id", missing),
            "name": self.base_client.generate_collection_format_param(kwargs.get("name", missing), 'multi'),
            "nameContains": kwargs.get("name_contains", missing),
            "valueChanged": kwargs.get("value_changed", missing),
            "valueDefault": kwargs.get("value_default", missing),
            "valueModified": kwargs.get("value_modified", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbParameterCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbParameterCollection")

    def summarize_awr_db_snapshot_ranges(self, managed_database_id, **kwargs):
        """
        Summarizes the AWR snapshot ranges that contain continuous snapshots, for the specified Managed Database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str name: (optional)
            The optional single value query parameter to filter the entity name.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in paginated response.

        :param str sort_by: (optional)
            The option to sort the AWR summary data.

            Allowed values are: "END_INTERVAL_TIME", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbSnapshotRangeCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/summarize_awr_db_snapshot_ranges.py.html>`__ to see an example of how to use summarize_awr_db_snapshot_ranges API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "name",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_awr_db_snapshot_ranges got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["END_INTERVAL_TIME", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "name": kwargs.get("name", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbSnapshotRangeCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbSnapshotRangeCollection")

    def summarize_awr_db_sysstats(self, managed_database_id, awr_db_id, name, **kwargs):
        """
        Summarizes the AWR SYSSTAT sample data for the specified database in AWR. The statistical data is summarized based on the Time dimension for each statistic.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str awr_db_id: (required)
            The parameter to filter the database by internal ID.
            Note that the internal ID of the database can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbs:

        :param oci.database_management.models.list[str] name: (required)
            The required multiple value query parameter to filter the entity name.

        :param str inst_num: (optional)
            The optional single value query parameter to filter the database instance number.

        :param int begin_sn_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_sn_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot ID.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param int container_id: (optional)
            The optional query parameter to filter the database container by an exact ID value.
            Note that the database container ID can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in large paginated response.

        :param str sort_by: (optional)
            The option to sort the data within a time period.

            Allowed values are: "TIME_BEGIN", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbSysstatCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/summarize_awr_db_sysstats.py.html>`__ to see an example of how to use summarize_awr_db_sysstats API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSysstats"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "container_id",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_awr_db_sysstats got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "awrDbId": awr_db_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_BEGIN", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "instNum": kwargs.get("inst_num", missing),
            "beginSnIdGreaterThanOrEqualTo": kwargs.get("begin_sn_id_greater_than_or_equal_to", missing),
            "endSnIdLessThanOrEqualTo": kwargs.get("end_sn_id_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "name": self.base_client.generate_collection_format_param(name, 'multi'),
            "containerId": kwargs.get("container_id", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbSysstatCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbSysstatCollection")

    def summarize_awr_db_top_wait_events(self, managed_database_id, awr_db_id, **kwargs):
        """
        Summarizes the AWR top wait events.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str awr_db_id: (required)
            The parameter to filter the database by internal ID.
            Note that the internal ID of the database can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbs:

        :param str inst_num: (optional)
            The optional single value query parameter to filter the database instance number.

        :param int begin_sn_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_sn_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot ID.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param str session_type: (optional)
            The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.

            Allowed values are: "FOREGROUND", "BACKGROUND", "ALL"

        :param int container_id: (optional)
            The optional query parameter to filter the database container by an exact ID value.
            Note that the database container ID can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

        :param int top_n: (optional)
            The optional query parameter to filter the number of top categories to be returned.

        :param str sort_by: (optional)
            The option to sort the AWR top event summary data.

            Allowed values are: "WAITS_PERSEC", "AVG_WAIT_TIME_PERSEC"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbTopWaitEventCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/summarize_awr_db_top_wait_events.py.html>`__ to see an example of how to use summarize_awr_db_top_wait_events API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbTopWaitEvents"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "session_type",
            "container_id",
            "top_n",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_awr_db_top_wait_events got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "awrDbId": awr_db_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'session_type' in kwargs:
            session_type_allowed_values = ["FOREGROUND", "BACKGROUND", "ALL"]
            if kwargs['session_type'] not in session_type_allowed_values:
                raise ValueError(
                    "Invalid value for `session_type`, must be one of {0}".format(session_type_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["WAITS_PERSEC", "AVG_WAIT_TIME_PERSEC"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "instNum": kwargs.get("inst_num", missing),
            "beginSnIdGreaterThanOrEqualTo": kwargs.get("begin_sn_id_greater_than_or_equal_to", missing),
            "endSnIdLessThanOrEqualTo": kwargs.get("end_sn_id_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "sessionType": kwargs.get("session_type", missing),
            "containerId": kwargs.get("container_id", missing),
            "topN": kwargs.get("top_n", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbTopWaitEventCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbTopWaitEventCollection")

    def summarize_awr_db_wait_event_buckets(self, managed_database_id, awr_db_id, name, **kwargs):
        """
        Summarizes AWR wait event data into value buckets and frequency, for the specified database in the AWR.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str awr_db_id: (required)
            The parameter to filter the database by internal ID.
            Note that the internal ID of the database can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbs:

        :param str name: (required)
            The required single value query parameter to filter the entity name.

        :param str inst_num: (optional)
            The optional single value query parameter to filter the database instance number.

        :param int begin_sn_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_sn_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot ID.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param int num_bucket: (optional)
            The number of buckets within the histogram.

        :param float min_value: (optional)
            The minimum value of the histogram.

        :param float max_value: (optional)
            The maximum value of the histogram.

        :param int container_id: (optional)
            The optional query parameter to filter the database container by an exact ID value.
            Note that the database container ID can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in large paginated response.

        :param str sort_by: (optional)
            The option to sort distribution data.

            Allowed values are: "CATEGORY", "PERCENTAGE"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbWaitEventBucketCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/summarize_awr_db_wait_event_buckets.py.html>`__ to see an example of how to use summarize_awr_db_wait_event_buckets API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbWaitEventBuckets"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "num_bucket",
            "min_value",
            "max_value",
            "container_id",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_awr_db_wait_event_buckets got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "awrDbId": awr_db_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["CATEGORY", "PERCENTAGE"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "instNum": kwargs.get("inst_num", missing),
            "beginSnIdGreaterThanOrEqualTo": kwargs.get("begin_sn_id_greater_than_or_equal_to", missing),
            "endSnIdLessThanOrEqualTo": kwargs.get("end_sn_id_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "name": name,
            "numBucket": kwargs.get("num_bucket", missing),
            "minValue": kwargs.get("min_value", missing),
            "maxValue": kwargs.get("max_value", missing),
            "containerId": kwargs.get("container_id", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbWaitEventBucketCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbWaitEventBucketCollection")

    def summarize_awr_db_wait_events(self, managed_database_id, awr_db_id, **kwargs):
        """
        Summarizes the AWR wait event sample data for the specified database in the AWR. The event data is summarized based on the Time dimension for each event.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str awr_db_id: (required)
            The parameter to filter the database by internal ID.
            Note that the internal ID of the database can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbs:

        :param str inst_num: (optional)
            The optional single value query parameter to filter the database instance number.

        :param int begin_sn_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_sn_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot ID.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param list[str] name: (optional)
            The optional multiple value query parameter to filter the entity name.

        :param str session_type: (optional)
            The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.

            Allowed values are: "FOREGROUND", "BACKGROUND", "ALL"

        :param int container_id: (optional)
            The optional query parameter to filter the database container by an exact ID value.
            Note that the database container ID can be retrieved from the following endpoint:
            /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

        :param str page: (optional)
            The page token representing the page, from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in large paginated response.

        :param str sort_by: (optional)
            The option to sort the data within a time period.

            Allowed values are: "TIME_BEGIN", "NAME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the the default order.

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AwrDbWaitEventCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/summarize_awr_db_wait_events.py.html>`__ to see an example of how to use summarize_awr_db_wait_events API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbWaitEvents"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "name",
            "session_type",
            "container_id",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_awr_db_wait_events got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "awrDbId": awr_db_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'session_type' in kwargs:
            session_type_allowed_values = ["FOREGROUND", "BACKGROUND", "ALL"]
            if kwargs['session_type'] not in session_type_allowed_values:
                raise ValueError(
                    "Invalid value for `session_type`, must be one of {0}".format(session_type_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_BEGIN", "NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "instNum": kwargs.get("inst_num", missing),
            "beginSnIdGreaterThanOrEqualTo": kwargs.get("begin_sn_id_greater_than_or_equal_to", missing),
            "endSnIdLessThanOrEqualTo": kwargs.get("end_sn_id_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "name": self.base_client.generate_collection_format_param(kwargs.get("name", missing), 'multi'),
            "sessionType": kwargs.get("session_type", missing),
            "containerId": kwargs.get("container_id", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbWaitEventCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrDbWaitEventCollection")

    def update_managed_database_group(self, managed_database_group_id, update_managed_database_group_details, **kwargs):
        """
        Updates the Managed Database Group specified by managedDatabaseGroupId.


        :param str managed_database_group_id: (required)
            The `OCID`__ of the Managed Database Group.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_management.models.UpdateManagedDatabaseGroupDetails update_managed_database_group_details: (required)
            The details required to update a Managed Database Group.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.ManagedDatabaseGroup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/update_managed_database_group.py.html>`__ to see an example of how to use update_managed_database_group API.
        """
        resource_path = "/managedDatabaseGroups/{managedDatabaseGroupId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_managed_database_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseGroupId": managed_database_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_managed_database_group_details,
                response_type="ManagedDatabaseGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_managed_database_group_details,
                response_type="ManagedDatabaseGroup")
