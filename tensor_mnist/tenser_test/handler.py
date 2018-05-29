# -*- coding: utf-8 -*-
import tensorflow as tf
from tensor_mnist import models
x = tf.placeholder("float", [None, 784])

sess = tf.Session()

with tf.variable_scope("regression"):
    y1, variables = models.regression(x)
saver = tf.train.Saver(variables)
saver.restore(sess, "tensor_mnist/data/regression.ckpt")


with tf.variable_scope("convolutional"):
    keep_prob = tf.placeholder("float")
    y2, variables = models.convolutional(x, keep_prob)
saver = tf.train.Saver(variables)
saver.restore(sess, "tensor_mnist/data/convolutional.ckpt")


def regression(input):
    return sess.run(y1, feed_dict={x: input}).flatten().tolist()


def convolutional(input):
    return sess.run(y2, feed_dict={x: input, keep_prob: 1.0}).flatten().tolist()