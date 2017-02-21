#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


def generate_user_hash(*args):
    s = ''
    for arg in args:
        s += str(arg)
    
    return hashlib.sha256().hexdigest()
