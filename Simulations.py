# In this example, we define a small quantum circuit that applies a Hadamard gate and a CNOT gate to two qubits, and then measures the result. We then perform a quantum simulation using the qasm_simulator backend on the IBM Qiskit framework, and output the counts of the different measurement outcomes. This demonstrates how quantum simulations can be performed on classical computers.

import qiskit 

circuit = qiskit.QuantumCircuit(2, 2) 
circuit.h(0) 
circuit.cx(0,1) 
circuit.measure([0,1],[0,1]) 
backend = qiskit.Aer.get_backend('qasm_simulator') 
job = qiskit.execute(circuit, backend, shots=1000) 
result = job.result() 
counts = result.get_counts(circuit) 
print(counts)
  
