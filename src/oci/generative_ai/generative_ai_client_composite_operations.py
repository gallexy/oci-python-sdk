# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class GenerativeAiClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.generative_ai.GenerativeAiClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new GenerativeAiClientCompositeOperations object

        :param GenerativeAiClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def create_dedicated_ai_cluster_and_wait_for_state(self, create_dedicated_ai_cluster_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.generative_ai.GenerativeAiClient.create_dedicated_ai_cluster` and waits for the :py:class:`~oci.generative_ai.models.WorkRequest`
        to enter the given state(s).

        :param oci.generative_ai.models.CreateDedicatedAiClusterDetails create_dedicated_ai_cluster_details: (required)
            Details for the new dedicated AI cluster.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.generative_ai.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.generative_ai.GenerativeAiClient.create_dedicated_ai_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_dedicated_ai_cluster(create_dedicated_ai_cluster_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_endpoint_and_wait_for_state(self, create_endpoint_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.generative_ai.GenerativeAiClient.create_endpoint` and waits for the :py:class:`~oci.generative_ai.models.WorkRequest`
        to enter the given state(s).

        :param oci.generative_ai.models.CreateEndpointDetails create_endpoint_details: (required)
            Details for the new endpoint.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.generative_ai.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.generative_ai.GenerativeAiClient.create_endpoint`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_endpoint(create_endpoint_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_model_and_wait_for_state(self, create_model_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.generative_ai.GenerativeAiClient.create_model` and waits for the :py:class:`~oci.generative_ai.models.WorkRequest`
        to enter the given state(s).

        :param oci.generative_ai.models.CreateModelDetails create_model_details: (required)
            Details for the new model.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.generative_ai.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.generative_ai.GenerativeAiClient.create_model`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_model(create_model_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_dedicated_ai_cluster_and_wait_for_state(self, dedicated_ai_cluster_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.generative_ai.GenerativeAiClient.delete_dedicated_ai_cluster` and waits for the :py:class:`~oci.generative_ai.models.WorkRequest`
        to enter the given state(s).

        :param str dedicated_ai_cluster_id: (required)
            The `OCID`__ of the dedicated AI cluster.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.generative_ai.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.generative_ai.GenerativeAiClient.delete_dedicated_ai_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_dedicated_ai_cluster(dedicated_ai_cluster_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_endpoint_and_wait_for_state(self, endpoint_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.generative_ai.GenerativeAiClient.delete_endpoint` and waits for the :py:class:`~oci.generative_ai.models.WorkRequest`
        to enter the given state(s).

        :param str endpoint_id: (required)
            The `OCID`__ of the endpoint.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.generative_ai.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.generative_ai.GenerativeAiClient.delete_endpoint`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_endpoint(endpoint_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_model_and_wait_for_state(self, model_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.generative_ai.GenerativeAiClient.delete_model` and waits for the :py:class:`~oci.generative_ai.models.WorkRequest`
        to enter the given state(s).

        :param str model_id: (required)
            The model OCID

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.generative_ai.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.generative_ai.GenerativeAiClient.delete_model`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_model(model_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_dedicated_ai_cluster_and_wait_for_state(self, dedicated_ai_cluster_id, update_dedicated_ai_cluster_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.generative_ai.GenerativeAiClient.update_dedicated_ai_cluster` and waits for the :py:class:`~oci.generative_ai.models.WorkRequest`
        to enter the given state(s).

        :param str dedicated_ai_cluster_id: (required)
            The `OCID`__ of the dedicated AI cluster.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.generative_ai.models.UpdateDedicatedAiClusterDetails update_dedicated_ai_cluster_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.generative_ai.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.generative_ai.GenerativeAiClient.update_dedicated_ai_cluster`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_dedicated_ai_cluster(dedicated_ai_cluster_id, update_dedicated_ai_cluster_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_endpoint_and_wait_for_state(self, endpoint_id, update_endpoint_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.generative_ai.GenerativeAiClient.update_endpoint` and waits for the :py:class:`~oci.generative_ai.models.WorkRequest`
        to enter the given state(s).

        :param str endpoint_id: (required)
            The `OCID`__ of the endpoint.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.generative_ai.models.UpdateEndpointDetails update_endpoint_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.generative_ai.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.generative_ai.GenerativeAiClient.update_endpoint`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_endpoint(endpoint_id, update_endpoint_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_model_and_wait_for_state(self, model_id, update_model_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.generative_ai.GenerativeAiClient.update_model` and waits for the :py:class:`~oci.generative_ai.models.Model` acted upon
        to enter the given state(s).

        :param str model_id: (required)
            The model OCID

        :param oci.generative_ai.models.UpdateModelDetails update_model_details: (required)
            The model information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.generative_ai.models.Model.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.generative_ai.GenerativeAiClient.update_model`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_model(model_id, update_model_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        model_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_model(model_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)