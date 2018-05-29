# -*- coding: utf-8 -*-
from flask import Blueprint

tenser_test_blueprint = Blueprint('tenser_test_blueprint', __name__)

from . import view
