# Author: Cenk Tüysüz
# Date: 19.11.2019
# 2 qubit Deutsch-Jozsa implementation
from qiskit import *

if __name__ == "__main__":
	backend = Aer.get_backend('qasm_simulator')
	q = QuantumRegister(2)
	c = ClassicalRegister(1)
	circuit = QuantumCircuit(q, c)

	# Create superpostion |+>|->
	circuit.h(q[0])
	circuit.x(q[1])
	circuit.h(q[1])
	## Implement the function here
	circuit.cx(q[0],q[1])
	# e.g. balanced function f(x) = x
	# e.g. constant function f(x) = 0
	## Apply another hadamard
	circuit.h(q[0])
	circuit.measure(q[0], c[0])
	job = execute(circuit,backend,shots=1)
	counts = job.result().get_counts(circuit)
	# If the function is balanced the output will be 1
	# If the function is constant the output will be 0
	for key in counts:
		if key == '0':
			print('Constant Function')
		else:
			print('Balanced Function')

