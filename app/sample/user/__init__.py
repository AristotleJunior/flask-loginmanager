#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, Blueprint
from app.sample.user.blogger import Blogger
from app.sample.user.forms import BloggerLoginForm
from app.flask_loginmanager import LoginManager


bp_user = Blueprint('user', __name__)
user_manager = LoginManager(bp_user, 'blogger', expires=1800, salt='eiuenko')


@bp_user.route('/', methods=['GET', 'POST'])
def index():
    form = BloggerLoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        from app.sample.fake_user_db import load_user_by_name
        
        user = load_user_by_name(username)
        
        if user is not None:
            if user.password == password:
                user_manager.login(user)
                return redirect(url_for('user.index'))
        
    return render_template('user_index.html', form=form)


@bp_user.route('/logout')
@user_manager.login_required()
def logout():
    user_manager.logout()
    return redirect(url_for('user.index'))


@bp_user.route('/profile')
@user_manager.login_required()
def profile():
    return 'Hello, this is the normal user profile page'


@bp_user.route('/secret')
@user_manager.login_required()
def secret():
    return 'Now you can see this secret page'


@user_manager.user_loader
def user_loader(uid):
    
    if uid is None:
        return None
    
    try:
        from app.sample.fake_user_db import load_user_by_id
        
        return load_user_by_id(uid=uid)
        
    except TypeError:
        return None
    except ValueError:
        return None


@user_manager.failure_handler
def failure_handler():
    return 'You should login first'


@user_manager.hash_generator
def hash_generator(user):
    
    from app.sample.utils import generate_user_hash
    
    return generate_user_hash(user.get_id(), user.password, user_manager.expires, user_manager.salt)
