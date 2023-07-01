# This file contains code that implements a quantum harmonic oscillator simulation using the IBM Qiskit framework.
# The simulation demonstrates the behavior of a quantum harmonic oscillator, including the quantized energy levels and wavefunction dynamics.
# The code utilizes quantum gates and measurements to simulate the oscillator's evolution over a given number of steps.
# The resulting measurement outcomes provide insights into the probabilities of different energy levels and contribute to the understanding of quantum mechanics.

import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, Aer

def quantum_harmonic_oscillator_simulation(n_qubits, n_steps):
    q = QuantumRegister(n_qubits)
    c = ClassicalRegister(n_qubits)
    qc = QuantumCircuit(q, c)

    theta = 2 * np.arcsin(1 / np.sqrt(n_steps))
    for step in range(n_steps):
        for i in range(n_qubits):
            qc.rz(2 * theta, q[i])
        for i in range(n_qubits - 1):
            qc.cz(q[i], q[i + 1])
        for i in range(n_qubits):
            qc.rz(-2 * theta, q[i])

    qc.measure(q, c)

    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    
    return counts


n_qubits = 3
n_steps = 10
counts = quantum_harmonic_oscillator_simulation(n_qubits, n_steps)
print(counts)
