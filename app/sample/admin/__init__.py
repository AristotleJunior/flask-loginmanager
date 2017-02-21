#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, Blueprint
from app.sample.admin.forms import ManagerLoginForm
from app.sample.admin.manager import Manager
from app.flask_loginmanager import LoginManager


bp_admin = Blueprint('admin', __name__)
admin_manager = LoginManager(bp_admin, 'manager', expires=3600, salt='ioejklj')


@bp_admin.route('/', methods=['GET', 'POST'])
def index():
    form = ManagerLoginForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        from app.sample.fake_admin_db import load_admin_by_name
        
        user = load_admin_by_name(username)
        
        if user is not None:
            if user.password == password:
                admin_manager.login(user)
                return redirect(url_for('admin.index'))

    print("form errors:", form.errors)
    
    return render_template('admin_index.html', form=form)


@bp_admin.route('/logout')
@admin_manager.login_required()
def logout():
    admin_manager.logout()
    return redirect(url_for('admin.index'))


@bp_admin.route('/secret')
@admin_manager.login_required()
def secret():
    return 'Now you can see this secret page'


@admin_manager.user_loader
def user_loader(uid):
    
    if uid is None:
        return None
    
    try:
        from app.sample.fake_admin_db import load_admin_by_id
    
        return load_admin_by_id(uid=uid)
        
    except TypeError:
        return None
    except ValueError:
        return None


@admin_manager.failure_handler
def failure_handler():
    return 'You are not admin'


@admin_manager.hash_generator
def hash_generator(user):
    
    from app.sample.utils import generate_user_hash
    
    return generate_user_hash(user.get_id(), user.password, admin_manager.expires, admin_manager.salt)
