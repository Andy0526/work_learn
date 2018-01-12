#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'


@app.route('/hello')
def hello_world():
    return 'hello world'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'welcome {}'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post {}'.format(post_id)


@app.route('/post/<path:s_path>')
def show_path(s_path):
    return 'path:{}'.format(s_path)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


def do_the_login():
    pass


def show_the_login_form():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()


if __name__ == '__main__':
    app.run(debug=True)
