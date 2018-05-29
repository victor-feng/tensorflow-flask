# -*- coding: utf-8 -*-

from flask_restful import Api, Resource
from tensor_mnist.tenser_test import tenser_test_blueprint
import numpy as np
from flask import Flask, jsonify, render_template, request
from tensor_mnist.tenser_test.handler import regression, convolutional
tenser_test_api = Api(tenser_test_blueprint)


class Mnist(Resource):

    def get(self):
        input = ((255 - np.array(request.json, dtype=np.uint8)) / 255.0).reshape(1, 784)
        output1 = regression(input)
        output2 = convolutional(input)

        return jsonify(results=[output1, output2])


class Page(Resource):

    def get(self):

        return render_template('index.html')


tenser_test_api.add_resource(Mnist, '/mnist')
tenser_test_api.add_resource(Page, '/')

