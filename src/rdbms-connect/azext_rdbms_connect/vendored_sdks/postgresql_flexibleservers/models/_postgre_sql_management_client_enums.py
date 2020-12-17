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

from enum import Enum


class ServerVersion(str, Enum):

    one_two = "12"
    one_one = "11"


class ServerState(str, Enum):

    ready = "Ready"
    dropping = "Dropping"
    disabled = "Disabled"
    starting = "Starting"
    stopping = "Stopping"
    stopped = "Stopped"
    updating = "Updating"


class ServerHAState(str, Enum):

    not_enabled = "NotEnabled"
    creating_standby = "CreatingStandby"
    replicating_data = "ReplicatingData"
    failing_over = "FailingOver"
    healthy = "Healthy"
    removing_standby = "RemovingStandby"


class ServerPublicNetworkAccessState(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class HAEnabledEnum(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class CreateMode(str, Enum):

    default = "Default"
    point_in_time_restore = "PointInTimeRestore"


class ResourceIdentityType(str, Enum):

    system_assigned = "SystemAssigned"


class SkuTier(str, Enum):

    burstable = "Burstable"
    general_purpose = "GeneralPurpose"
    memory_optimized = "MemoryOptimized"


class ConfigurationDataType(str, Enum):

    boolean = "Boolean"
    numeric = "Numeric"
    integer = "Integer"
    enumeration = "Enumeration"


class OperationOrigin(str, Enum):

    not_specified = "NotSpecified"
    user = "user"
    system = "system"
