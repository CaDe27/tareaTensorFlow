#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#modifica index y xquery
import tensorflow as tf
import numpy as np

index = 13
modelPath = 'modelos/modelo{}'.format(index)
model = tf.keras.models.load_model(modelPath)

x_query = [0]*13
meanstdFile = open(modelPath+"/mean_std.txt", "r")

x_mean = float(meanstdFile.readline())
x_std = float(meanstdFile.readline())

meanstdFile.close()

epsilon = 1e-10

x_test = []
for i in range(13):
	x_query[i] = (x_query[i] - x_mean)/(x_std + epsilon)
x_test.append(x_query)
pred = np.argmax(model.predict(x_test)[0])
respQuery = open('respQuery.txt','w')
respQuery.write(str(pred))


