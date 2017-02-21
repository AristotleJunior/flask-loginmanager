#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.flask_loginmanager.user_mixin import UserMixin


class Blogger(UserMixin):
    def __init__(self, uid, username='', password='', age=0):
        super(Blogger, self).__init__()
        self.__uid = uid
        self.__username = username
        self.__password = password
        self.__age = age
    
    def get_id(self):
        return self.__uid

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__username = username
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password
