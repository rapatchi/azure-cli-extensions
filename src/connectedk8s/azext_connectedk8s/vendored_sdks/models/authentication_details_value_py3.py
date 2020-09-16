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


class AuthenticationDetailsValue(Model):
    """AuthenticationDetailsValue.

    :param token: Authentication token.
    :type token: str
    :param client_certificate:
    :type client_certificate:
     ~azure.mgmt.hybridkubernetes.models.AuthenticationCertificateDetails
    """

    _attribute_map = {
        'token': {'key': 'token', 'type': 'str'},
        'client_certificate': {'key': 'clientCertificate', 'type': 'AuthenticationCertificateDetails'},
    }

    def __init__(self, *, token: str=None, client_certificate=None, **kwargs) -> None:
        super(AuthenticationDetailsValue, self).__init__(**kwargs)
        self.token = token
        self.client_certificate = client_certificate
