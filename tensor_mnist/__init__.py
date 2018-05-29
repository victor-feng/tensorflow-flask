from flask import Flask
from tenser_test import tenser_test_blueprint

app = Flask(__name__)

app.register_blueprint(tenser_test_blueprint, url_prefix='/api/tensor')
