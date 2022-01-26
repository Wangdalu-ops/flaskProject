from flask import request

from flask_shop.user import user
from flask_shop.utils.message import to_dict_msg


@user.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@user.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('pwd')
    if not all([name, password]):
        return to_dict_msg(10000)
    if len(name) > 1:
        usr = models
