# Flask-Login

Flask-Loginmanager supports multiple roles and permissions for Flask, inspired by Flask-Login.

## Installation

Install this extension with pip:

```sh
$ pip install flask-loginmanager
```

## Usage
```python
from flask_loginmanager import LoginManager

user_manager = LoginManager(blueprint_user, 'blogger', expires=1800, salt='''ExI^u0YQ`_,E1j/<''')
admin_manager = LoginManager(blueprint_admin, 'manager', expires=3600, salt='''Xv5OY\:Fj}4:7!$U''')

