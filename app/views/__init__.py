# -*- coding: utf-8 -*-
from flask import Blueprint

test_flask = Blueprint('test', __name__)

from . import views
