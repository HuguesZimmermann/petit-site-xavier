#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time

from google.appengine.api import users

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify
from werkzeug.exceptions import InternalServerError, Forbidden


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')
