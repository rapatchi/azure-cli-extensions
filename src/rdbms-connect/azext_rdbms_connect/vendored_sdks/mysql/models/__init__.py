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

try:
    from ._models_py3 import Advisor
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import Configuration
    from ._models_py3 import Database
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorResponse
    from ._models_py3 import FirewallRule
    from ._models_py3 import LogFile
    from ._models_py3 import NameAvailability
    from ._models_py3 import NameAvailabilityRequest
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import PerformanceTierProperties
    from ._models_py3 import PerformanceTierServiceLevelObjectives
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointProperty
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceProperties
    from ._models_py3 import PrivateLinkServiceConnectionStateProperty
    from ._models_py3 import ProxyResource
    from ._models_py3 import QueryStatistic
    from ._models_py3 import QueryText
    from ._models_py3 import RecommendationAction
    from ._models_py3 import RecommendationActionsResultList
    from ._models_py3 import RecommendedActionSessionsOperationStatus
    from ._models_py3 import Resource
    from ._models_py3 import ResourceIdentity
    from ._models_py3 import Server
    from ._models_py3 import ServerAdministratorResource
    from ._models_py3 import ServerForCreate
    from ._models_py3 import ServerKey
    from ._models_py3 import ServerPrivateEndpointConnection
    from ._models_py3 import ServerPrivateEndpointConnectionProperties
    from ._models_py3 import ServerPrivateLinkServiceConnectionStateProperty
    from ._models_py3 import ServerPropertiesForCreate
    from ._models_py3 import ServerPropertiesForDefaultCreate
    from ._models_py3 import ServerPropertiesForGeoRestore
    from ._models_py3 import ServerPropertiesForReplica
    from ._models_py3 import ServerPropertiesForRestore
    from ._models_py3 import ServerSecurityAlertPolicy
    from ._models_py3 import ServerUpdateParameters
    from ._models_py3 import ServerUpgradeParameters
    from ._models_py3 import Sku
    from ._models_py3 import StorageProfile
    from ._models_py3 import TagsObject
    from ._models_py3 import TopQueryStatisticsInput
    from ._models_py3 import TrackedResource
    from ._models_py3 import VirtualNetworkRule
    from ._models_py3 import WaitStatistic
    from ._models_py3 import WaitStatisticsInput
except (SyntaxError, ImportError):
    from ._models import Advisor
    from ._models import AzureEntityResource
    from ._models import Configuration
    from ._models import Database
    from ._models import ErrorAdditionalInfo
    from ._models import ErrorResponse
    from ._models import FirewallRule
    from ._models import LogFile
    from ._models import NameAvailability
    from ._models import NameAvailabilityRequest
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import OperationListResult
    from ._models import PerformanceTierProperties
    from ._models import PerformanceTierServiceLevelObjectives
    from ._models import PrivateEndpointConnection
    from ._models import PrivateEndpointProperty
    from ._models import PrivateLinkResource
    from ._models import PrivateLinkResourceProperties
    from ._models import PrivateLinkServiceConnectionStateProperty
    from ._models import ProxyResource
    from ._models import QueryStatistic
    from ._models import QueryText
    from ._models import RecommendationAction
    from ._models import RecommendationActionsResultList
    from ._models import RecommendedActionSessionsOperationStatus
    from ._models import Resource
    from ._models import ResourceIdentity
    from ._models import Server
    from ._models import ServerAdministratorResource
    from ._models import ServerForCreate
    from ._models import ServerKey
    from ._models import ServerPrivateEndpointConnection
    from ._models import ServerPrivateEndpointConnectionProperties
    from ._models import ServerPrivateLinkServiceConnectionStateProperty
    from ._models import ServerPropertiesForCreate
    from ._models import ServerPropertiesForDefaultCreate
    from ._models import ServerPropertiesForGeoRestore
    from ._models import ServerPropertiesForReplica
    from ._models import ServerPropertiesForRestore
    from ._models import ServerSecurityAlertPolicy
    from ._models import ServerUpdateParameters
    from ._models import ServerUpgradeParameters
    from ._models import Sku
    from ._models import StorageProfile
    from ._models import TagsObject
    from ._models import TopQueryStatisticsInput
    from ._models import TrackedResource
    from ._models import VirtualNetworkRule
    from ._models import WaitStatistic
    from ._models import WaitStatisticsInput
from ._paged_models import AdvisorPaged
from ._paged_models import ConfigurationPaged
from ._paged_models import DatabasePaged
from ._paged_models import FirewallRulePaged
from ._paged_models import LogFilePaged
from ._paged_models import PerformanceTierPropertiesPaged
from ._paged_models import PrivateEndpointConnectionPaged
from ._paged_models import PrivateLinkResourcePaged
from ._paged_models import QueryStatisticPaged
from ._paged_models import QueryTextPaged
from ._paged_models import RecommendationActionPaged
from ._paged_models import ServerAdministratorResourcePaged
from ._paged_models import ServerKeyPaged
from ._paged_models import ServerPaged
from ._paged_models import VirtualNetworkRulePaged
from ._paged_models import WaitStatisticPaged
from ._my_sql_management_client_enums import (
    ServerVersion,
    SslEnforcementEnum,
    MinimalTlsVersionEnum,
    InfrastructureEncryption,
    PublicNetworkAccessEnum,
    PrivateLinkServiceConnectionStateStatus,
    PrivateLinkServiceConnectionStateActionsRequire,
    PrivateEndpointProvisioningState,
    ServerState,
    GeoRedundantBackup,
    StorageAutogrow,
    SkuTier,
    IdentityType,
    VirtualNetworkRuleState,
    OperationOrigin,
    ServerSecurityAlertPolicyState,
)

__all__ = [
    'Advisor',
    'AzureEntityResource',
    'Configuration',
    'Database',
    'ErrorAdditionalInfo',
    'ErrorResponse',
    'FirewallRule',
    'LogFile',
    'NameAvailability',
    'NameAvailabilityRequest',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'PerformanceTierProperties',
    'PerformanceTierServiceLevelObjectives',
    'PrivateEndpointConnection',
    'PrivateEndpointProperty',
    'PrivateLinkResource',
    'PrivateLinkResourceProperties',
    'PrivateLinkServiceConnectionStateProperty',
    'ProxyResource',
    'QueryStatistic',
    'QueryText',
    'RecommendationAction',
    'RecommendationActionsResultList',
    'RecommendedActionSessionsOperationStatus',
    'Resource',
    'ResourceIdentity',
    'Server',
    'ServerAdministratorResource',
    'ServerForCreate',
    'ServerKey',
    'ServerPrivateEndpointConnection',
    'ServerPrivateEndpointConnectionProperties',
    'ServerPrivateLinkServiceConnectionStateProperty',
    'ServerPropertiesForCreate',
    'ServerPropertiesForDefaultCreate',
    'ServerPropertiesForGeoRestore',
    'ServerPropertiesForReplica',
    'ServerPropertiesForRestore',
    'ServerSecurityAlertPolicy',
    'ServerUpdateParameters',
    'ServerUpgradeParameters',
    'Sku',
    'StorageProfile',
    'TagsObject',
    'TopQueryStatisticsInput',
    'TrackedResource',
    'VirtualNetworkRule',
    'WaitStatistic',
    'WaitStatisticsInput',
    'ServerPaged',
    'FirewallRulePaged',
    'VirtualNetworkRulePaged',
    'DatabasePaged',
    'ConfigurationPaged',
    'LogFilePaged',
    'ServerAdministratorResourcePaged',
    'PerformanceTierPropertiesPaged',
    'QueryTextPaged',
    'QueryStatisticPaged',
    'WaitStatisticPaged',
    'AdvisorPaged',
    'RecommendationActionPaged',
    'PrivateEndpointConnectionPaged',
    'PrivateLinkResourcePaged',
    'ServerKeyPaged',
    'ServerVersion',
    'SslEnforcementEnum',
    'MinimalTlsVersionEnum',
    'InfrastructureEncryption',
    'PublicNetworkAccessEnum',
    'PrivateLinkServiceConnectionStateStatus',
    'PrivateLinkServiceConnectionStateActionsRequire',
    'PrivateEndpointProvisioningState',
    'ServerState',
    'GeoRedundantBackup',
    'StorageAutogrow',
    'SkuTier',
    'IdentityType',
    'VirtualNetworkRuleState',
    'OperationOrigin',
    'ServerSecurityAlertPolicyState',
]
