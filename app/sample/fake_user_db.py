#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.sample.user.blogger import Blogger


_user_db = [
    {'id': 1, 'name': 'rain', 'password': '123456', 'age': 16},
    {'id': 2, 'name': 'kevin', 'password': '123456', 'age': 40},
    {'id': 3, 'name': 'James', 'password': '123456', 'age': 33}
]


def load_user_by_id(uid):
    for data in _user_db:
        if str(uid) == str(data['id']):
            return Blogger(data['id'], data['name'], data['password'], data['age'])
    return None


def load_user_by_name(name):
    for data in _user_db:
        if name == data['name']:
            return Blogger(data['id'], data['name'], data['password'], data['age'])
    return None
