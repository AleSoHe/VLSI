import numpy as np
from matplotlib import pyplot as plt

filename = 'parteA_NMOS_rstep'

class measure():
	def __init__(self, name, system):
		self.name = name
		self.system = system
		self.data = []
		self.time = []

	def plot_measure(self):
		plt.plot(self.time,self.data)
		plt.show()
		
# System 
system = 'NMOS_Rstep'		

# Measures
time = measure('Time', system)
Idrain = measure('Id', system)
Vdrain = measure('Vdrain', system)

# Read file
with open(filename, 'r') as f:
	lines = f.readlines()[2:]
	for line in lines:
		words = line.split()
		print(words)
		time.data.append(words[0])
		Idrain.data.append(words[1])
		Vdrain.data.append(words[2])
	f.close()
	
# Subsample
time.data = np.array(time.data[1::7])*0.0000001
Idrain.data = Idrain.data[1::7]
Vdrain.data = Vdrain.data[1::7]
	
# Assign time vectors
Idrain.time = time.data
Vdrain.time = time.data
del time

Idrain.plot_measure()
Vdrain.plot_measure()
