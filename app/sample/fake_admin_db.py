#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.sample.admin.manager import Manager

_admin_db = [
    {'id': 1, 'name': 'susan', 'password': '111111', 'dept': 'IT'},
    {'id': 2, 'name': 'Jane', 'password': '222222', 'dept': 'HR'},
    {'id': 3, 'name': 'Tracy', 'password': '333333', 'dept': 'Marketing'}
]


def load_admin_by_id(uid):
    for data in _admin_db:
        if str(uid) == str(data['id']):
            return Manager(data['id'], data['name'], data['password'], data['dept'])
    return None


def load_admin_by_name(name):
    for data in _admin_db:
        if name == data['name']:
            return Manager(data['id'], data['name'], data['password'], data['dept'])
    return None
