#coding: utf-8

import numpy as np

def convert(voltage):
	force = 0.649 * np.log(voltage) - 1.1306
	print (force)



