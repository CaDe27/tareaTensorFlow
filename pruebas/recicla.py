#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
model = tf.keras.models.load_model('saved_model/my_model')
(x_train, train_labels), (x_test, test_labels) = tf.keras.datasets.mnist.load_data()

x_train_reshaped = np.reshape(x_train, (60000, 784))
x_test_reshaped = np.reshape(x_test, (10000, 784))

x_mean = np.mean(x_train_reshaped)
x_std = np.std(x_train_reshaped)

epsilon = 1e-10
x_test_norm = (x_test_reshaped - x_mean)/(x_std + epsilon)

pred = np.argmax(model.predict(x_test_norm)[0])
print('actual: ', test_labels[0])
print('prediction: ', pred)

