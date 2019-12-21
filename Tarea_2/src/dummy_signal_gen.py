import numpy as np

''' Forma de fuentes
VSX X gnd PWL(
+ 0ps 'SUPPLY'
+ 180ps 'SUPPLY'
+ 200ps 0
) 
'''

N = 4 # Number of inputs
num_transitions = 1000

class source:
	def __init__(self, name, tmin, t_transition, folder):
		self.name = name
		self.tmin = tmin
		self.t_transition = t_transition 
		self.folder = folder
		# First state: 0 or 1, with normal distribution
		first_state = 1 if (np.random.uniform(0,1)>0.5) else 0
		self.states = [0]
		
	def new_state(self):
		last_state = self.states[-1]
		self.states.append(int(not last_state)) # Transition

	def states_to_sources(self):
		time = 0
		header = 'VS'+self.name + ' ' + self.name + ' gnd PWL('
		initial_supply = '\'SUPPLY\'' if (self.states[0]) else '0'
		initial_state = '+ 0ps ' + initial_supply
		footer = ')'
		
		src_states = [initial_state]
		for state in self.states:
			if state: # if state == 1
				src_states.append('+ ' + str(time + t_transition) + 'ps ' + '\'SUPPLY\'')
				src_states.append('+ ' + str(time + tmin) + 'ps ' + '\'SUPPLY\'')
			else:
				src_states.append('+ ' + str(time + t_transition) + 'ps ' + '0')
				src_states.append('+ ' + str(time + tmin) + 'ps ' + '0')
			time += tmin
		
		with open('./sources/dummy/' + self.folder + self.name, 'w+') as f:
			f.write('%s\n' %header)
			f.write('%s\n' %initial_state)
			for state in src_states:
				f.write('%s\n' %state)
			f.write('%s\n' %footer)
			

t_transition = 20

# Tiempos mínimos en picosegundos
tmins = [479, 517, 434, 465]

# Nombres de las celdas
cells = ['simple_sch/', 'simple_layout/', 'complex_sch/','complex_layout/']

for tmin,cell in zip(tmins,cells):
	# Init sources
	A = source('A', tmin, t_transition, cell)
	B = source('B', tmin, t_transition, cell)
	C = source('C', tmin, t_transition, cell)
	D = source('D', tmin, t_transition, cell)

	# Generate states with normal distribution
	for i in range(num_transitions):
		A.new_state()
		B.new_state()
		C.new_state()
		D.new_state()

	# Create states files
	A.states_to_sources()
	B.states_to_sources()
	C.states_to_sources()
	D.states_to_sources()

