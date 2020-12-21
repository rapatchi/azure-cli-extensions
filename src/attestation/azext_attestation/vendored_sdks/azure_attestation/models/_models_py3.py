# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class AttestationPolicy(Model):

    _attribute_map = {
        'token': {'key': 'token', 'type': 'str'},
    }

    def __init__(self, *, token: str=None, **kwargs) -> None:
        super(AttestationPolicy, self).__init__(**kwargs)
        self.token = token


class AttestSgxEnclaveRequest(Model):
    """Attestation request for SGX-IntelSDK enclaves.
    """

    _attribute_map = {
        'quote': {'key': 'quote', 'type': 'str'},
        'runtime_data': {'key': 'runtimeData', 'type': 'RuntimeData'},
        'init_time_data': {'key': 'initTimeData', 'type': 'InitTimeData'},
        'draft_policy_for_attestation': {'key': 'draftPolicyForAttestation', 'type': 'str'}
    }

    def __init__(self, quoto=None, runtime_data=None, init_time_data=None, draft_policy_for_attestation=None, **kwargs):
        super(AttestSgxEnclaveRequest, self).__init__(**kwargs)
        self.quoto = quoto
        self.runtime_data = runtime_data
        self.init_time_data = init_time_data
        self.draft_policy_for_attestation = draft_policy_for_attestation


class AttestOpenEnclaveRequest(Model):
    """Attestation request for SGX-OpenEnclaveSDK enclaves.
    """

    _attribute_map = {
        'report': {'key': 'report', 'type': 'str'},
        'runtime_data': {'key': 'runtimeData', 'type': 'RuntimeData'},
        'init_time_data': {'key': 'initTimeData', 'type': 'InitTimeData'},
        'draft_policy_for_attestation': {'key': 'draftPolicyForAttestation', 'type': 'str'}
    }

    def __init__(self, report=None, runtime_data=None, init_time_data=None, draft_policy_for_attestation=None, **kwargs):
        super(AttestOpenEnclaveRequest, self).__init__(**kwargs)
        self.report = report
        self.runtime_data = runtime_data
        self.init_time_data = init_time_data
        self.draft_policy_for_attestation = draft_policy_for_attestation


class TPMOpenEnclaveRequest(Model):
    """Attestation request for Trusted Platform Module (TPM) attestation.
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'str'}
    }

    def __init__(self, data=None, **kwargs):
        super(TPMOpenEnclaveRequest, self).__init__(**kwargs)
        self.data = data


class RuntimeData(Model):
    """Defines the \"run time data\" provided by the attestation target for use by the MAA
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'str'},
        'data_type': {'key': 'dataType', 'type': 'DataType'}
    }

    def __init__(self, data=None, data_type=None, **kwargs):
        super(RuntimeData, self).__init__(**kwargs)
        self.data = data
        self.data_type = data_type


class InitTimeData(Model):
    """Defines the \"initialization time data\" used to provision the attestation target for use by the MAA
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'str'},
        'data_type': {'key': 'dataType', 'type': 'DataType'}
    }

    def __init__(self, data=None, data_type=None, **kwargs):
        super(InitTimeData, self).__init__(**kwargs)
        self.data = data
        self.data_type = data_type


class CloudError(Model):
    """An error response from Attestation.

    :param error:
    :type error: ~azure.attestation.models.CloudErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CloudErrorBody'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(CloudError, self).__init__(**kwargs)
        self.error = error


class CloudErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CloudErrorException, self).__init__(deserialize, response, 'CloudError', *args)


class CloudErrorBody(Model):
    """An error response from Attestation.

    :param code: An identifier for the error. Codes are invariant and are
     intended to be consumed programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable
     for displaying in a user interface.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, **kwargs) -> None:
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
