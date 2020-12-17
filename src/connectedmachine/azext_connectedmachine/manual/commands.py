# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from collections import OrderedDict
from azure.cli.core.commands import CliCommandType


def transform_machine(result):
    return OrderedDict([('Name', result['name']),
                        ('ResourceGroup', result['resourceGroup']),
                        ('Location', result['location']),
                        ('Status', result.get('status'))])


def transform_machine_list(result):
    return [transform_machine(machine) for machine in result]


def load_command_table(self, _):

    from azext_connectedmachine.generated._client_factory import cf_machine
    connectedmachine_machine = CliCommandType(
        operations_tmpl='azext_connectedmachine.vendored_sdks.connectedmachine.operations._machine_operations#MachineOp'
        'erations.{}',
        client_factory=cf_machine)
    with self.command_group('connectedmachine', connectedmachine_machine, client_factory=cf_machine) as g:
        g.custom_command('list', 'connectedmachine_list', table_transformer=transform_machine_list)
