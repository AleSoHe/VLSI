import numpy as np
from matplotlib import pyplot as plt

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
	def __init__(self, name, label, scale, _system):
		self.name = name
		self.label = label
		self.scale = scale
		self.system = _system
		self.data = []
		self.x = None
		
	def plot_measure(self):
		plt.plot(np.array(self.x.data), np.array(self.data)*self.scale)
		plt.xlabel(self.x.label)
		plt.ylabel(self.label)
		g1 = plt.grid(b=True, which='major', color='k', linestyle='-', linewidth=0.2)
		#g2 = plt.grid(b=True, which='minor', color='k', linestyle='-', linewidth=0.05)
		plt.minorticks_on()		
		
	def subplot_measures(measure_list):
		for i,_measure in enumerate(measure_list):
			print(i+1)
			plt.subplot(len(measure_list), 1, i+1)			
			_measure.plot_measure()
		plt.suptitle(measure_list[0].system)
		plt.show()
	
# --------
# --- PMOS
# --------
# DATA filename
filename = 'parteA_PMOS_rstep'
system_name = 'RSTEP'


# Measures
time = measure('Time', 'time [ns]', 1000000000, system_name)
Idrain = measure('Drain current', 'Id [uA]', 1000000, system_name)
Vdrain = measure('Drain Voltage', 'Vd [V]', 1, system_name)


# Read file
with open(filename, 'r') as f:
	lines = f.readlines()[2:]
	for line in lines:
		words = line.split()
		time.data.append(float(words[0]))
		Idrain.data.append(float(words[1])*Idrain.scale)
		Vdrain.data.append(float(words[2])-1.79)
	f.close()


filename = 'rstep_P18'
with open(filename, 'w+') as f:
	f.write('Vds Id_uA\n')
	for v,i in zip(Vdrain.data[0::3], Idrain.data[0::3]):
		f.write(str(v) + ' ' + str(i) + '\n')
	f.close()

# --------
# --- NMOS
# --------			
# DATA filename
filename = 'parteA_NMOS_rstep'

time.data = []
Idrain.data = []
Vdrain.data = []


# Read file
with open(filename, 'r') as f:
	lines = f.readlines()[2:]
	for line in lines:
		words = line.split()
		print(words)
		time.data.append(float(words[0]))
		Idrain.data.append(float(words[1])*Idrain.scale)
		Vdrain.data.append(float(words[2]))
	f.close()

filename = 'rstep_N18'
with open(filename, 'w+') as f:
	f.write('Vds Id_uA\n')
	for v,i in zip(Vdrain.data[0::3], Idrain.data[0::3]):
		f.write(str(v) + ' ' + str(i) + '\n')
	f.close()
		
# Assign X vectors
