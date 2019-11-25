# Author: Cenk Tüysüz
# Date: 19.11.2019
# 4 qubit Deutsch-Jozsa implementation
from qiskit import *

if __name__ == "__main__":
	backend = Aer.get_backend('qasm_simulator')
	q = QuantumRegister(4)
	c = ClassicalRegister(3)
	circuit = QuantumCircuit(q, c)

	# Create superpostion |+>|->
	circuit.h(q[0])
	circuit.h(q[1])
	circuit.h(q[2])
	circuit.x(q[3])
	circuit.h(q[3])
	## Implement the function here
	circuit.cx(q[0],q[3])
	circuit.cx(q[1],q[3])
	circuit.cx(q[2],q[3])
	# e.g. balanced function f(x) = x
	# e.g. constant function f(x) = 0
	## Apply another hadamard
	circuit.h(q[0])
	circuit.measure(q[0], c[0])
	job = execute(circuit,backend,shots=1)
	counts = job.result().get_counts(circuit)
	# If the function is balanced the output will be 1
	# If the function is constant the output will be 0
	
	if '000' in counts.keys():
		print('Constant Function')
	else:
		print('Balanced Function')

