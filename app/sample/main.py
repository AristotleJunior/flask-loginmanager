#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask


instance = Flask(__name__)
instance.config['SECRET_KEY'] = '84j548f&$32l54f(*&^kjlfd(893^'
instance.config['CSRF_ENABLED'] = True
instance.config['DEBUG'] = True


from app.sample.admin import bp_admin
from app.sample.user import bp_user


instance.register_blueprint(bp_admin, url_prefix='/admin')
instance.register_blueprint(bp_user, url_prefix='/user')


@instance.route('/')
def index():
    return 'Hello, This is the index page'


if __name__ == '__main__':
    instance.run()
