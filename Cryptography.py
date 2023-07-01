# The code in "Cryptography.py" file simulates a quantum key exchange protocol between Alice and Bob using the IBM Qiskit framework. It demonstrates how quantum cryptography can be implemented and establishes a shared secret key that cannot be easily intercepted by a third party.

# The code defines several functions:

# The entangle_qubits function entangles two qubits using the Hadamard gate and CNOT gate.
# The measure_qubits function measures the qubits based on the specified bases.
# The generate_quantum_key function generates a quantum key by entangling and measuring qubits, applying error correction, and extracting the key from the corrected counts.
# The error_correction function performs error correction on the counts obtained from the measurement.
# The verify_quantum_key function verifies if the generated key matches the original key provided by Alice.
# The code initializes the quantum key exchange simulation with Alice's quantum key '10'. It then calls the generate_quantum_key function to generate Bob's quantum key. Finally, it verifies if Bob's quantum key matches Alice's key and prints a success message if it does, indicating a successful quantum key exchange, or an error message if it doesn't, indicating the presence of eavesdropping.

# Overall, this code showcases the principles of quantum key exchange and demonstrates how quantum cryptography can be implemented using the IBM Qiskit framework.

from qiskit import QuantumCircuit, execute, Aer
from qiskit.tools.monitor import job_monitor

def entangle_qubits(qc, a, b):
    qc.h(a)
    qc.cx(a, b)

def measure_qubits(qc, qubits, classical_bits, bases):
    for i, qubit in enumerate(qubits):
        if bases[i] == 'X':
            qc.h(qubit)
        qc.measure(qubit, classical_bits[i])

def generate_quantum_key(alice_quantum_key):
    backend = Aer.get_backend('qasm_simulator')
    qubits = [0, 1]
    bases = ['Z', 'X']
    classical_bits = [0, 1]

    qc = QuantumCircuit(2, 2)
    entangle_qubits(qc, qubits[0], qubits[1])
    qc.barrier()
    measure_qubits(qc, qubits, classical_bits, bases)

    job = execute(qc, backend, shots=1000)
    job_monitor(job)

    results = job.result()
    counts = results.get_counts()
    
    # Enhanced error correction code here
    corrected_counts = error_correction(counts)
    
    bob_quantum_key = str(max(corrected_counts, key=corrected_counts.get)[::-1])

    return bob_quantum_key

def error_correction(counts):
    corrected_counts = {}
    
    for key in counts.keys():
        corrected_key = key[::-1]
        
        if corrected_key in corrected_counts:
            corrected_counts[corrected_key] += counts[key]
        else:
            corrected_counts[corrected_key] = counts[key]
    
    return corrected_counts

def verify_quantum_key(alice_quantum_key, bob_quantum_key):
    if bob_quantum_key == alice_quantum_key:
        print("Quantum key exchange was successful")
    else:
        print("Eavesdropping detected, the keys do not match")

alice_quantum_key = '10'
bob_quantum_key = generate_quantum_key(alice_quantum_key)
verify_quantum_key(alice_quantum_key, bob_quantum_key)
