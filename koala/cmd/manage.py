#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2013 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Run storage database migration.
"""
import sys

from oslo.config import cfg
from koala.db import migration

CONF = cfg.CONF

CONF.import_opt('connection',
                'koala.openstack.common.db.sqlalchemy.session',
                group='database')

CONF.import_opt('sqlite_db',
                'koala.openstack.common.db.sqlalchemy.session')


def main():
    version = None
    if 'db_sync' in sys.argv and len(sys.argv) > 2:
        version = sys.argv[2]
    migration.db_sync(version=version)
