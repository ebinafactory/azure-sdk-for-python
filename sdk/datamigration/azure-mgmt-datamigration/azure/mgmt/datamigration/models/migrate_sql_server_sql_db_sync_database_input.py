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


class MigrateSqlServerSqlDbSyncDatabaseInput(Model):
    """Database specific information for SQL to Azure SQL DB sync migration task
    inputs.

    :param id: Unique identifier for database
    :type id: str
    :param name: Name of database
    :type name: str
    :param target_database_name: Target database name
    :type target_database_name: str
    :param schema_name: Schema name to be migrated
    :type schema_name: str
    :param table_map: Mapping of source to target tables
    :type table_map: dict[str, str]
    :param migration_setting: Migration settings which tune the migration
     behavior
    :type migration_setting: dict[str, str]
    :param source_setting: Source settings to tune source endpoint migration
     behavior
    :type source_setting: dict[str, str]
    :param target_setting: Target settings to tune target endpoint migration
     behavior
    :type target_setting: dict[str, str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'target_database_name': {'key': 'targetDatabaseName', 'type': 'str'},
        'schema_name': {'key': 'schemaName', 'type': 'str'},
        'table_map': {'key': 'tableMap', 'type': '{str}'},
        'migration_setting': {'key': 'migrationSetting', 'type': '{str}'},
        'source_setting': {'key': 'sourceSetting', 'type': '{str}'},
        'target_setting': {'key': 'targetSetting', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(MigrateSqlServerSqlDbSyncDatabaseInput, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.target_database_name = kwargs.get('target_database_name', None)
        self.schema_name = kwargs.get('schema_name', None)
        self.table_map = kwargs.get('table_map', None)
        self.migration_setting = kwargs.get('migration_setting', None)
        self.source_setting = kwargs.get('source_setting', None)
        self.target_setting = kwargs.get('target_setting', None)