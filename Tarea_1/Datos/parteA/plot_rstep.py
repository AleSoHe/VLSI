import numpy as np
from matplotlib import pyplot as plt

filename = 'parteA_NMOS_rstep'

class system():
	def __init__(self, name, filepath):
		self.name = name
		self.filepath = filepath
		self.measures = []
	
	def add_measure(self, measure):
		self.measures.append(measure)

	def subplot_measures(self):
		fig, ax = plt.subplot(nrows=len(self.measures),ncols=1)
		for measure in self.measures:
			measure.subplot_measure()
		plt.show()

class measure():
	def __init__(self, name, system):
		self.name = name
		self.system = system
		self.data = []
		self.time = []

	def plot_measure(self):
		plt.plot(self.time,self.data)
		plt.show()
		
	def subplot_measure(self):
		plt.plot(self.time, self.data)
		
# System 
system_name = 'NMOS_Rstep'		

# Measures
time = measure('Time', system_name)
Idrain = measure('Id', system_name)
Vdrain = measure('Vdrain', system_name)

# Read file
with open(filename, 'r') as f:
	lines = f.readlines()[2:]
	for line in lines:
		words = line.split()
		print(words)
		time.data.append(float(words[0]))
		Idrain.data.append(float(words[1]))
		Vdrain.data.append(float(words[2]))
	f.close()
	
# Assign time vectors
Idrain.time = time.data
Vdrain.time = time.data
del time

#Idrain.plot_measure()
#Vdrain.plot_measure()

Rstep_nmos = system('Rstep', filename)
Rstep_nmos.add_measure(Idrain)
Rstep_nmos.add_measure(Vdrain)

Rstep_nmos.subplot_measures()
