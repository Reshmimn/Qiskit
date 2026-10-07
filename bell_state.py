from qiskit import QuantumCircuit

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Put qubit 0 into superposition
qc.h(0)

# Entangle qubit 0 and qubit 1
qc.cx(0, 1)

# Measure both qubits
pc.measure([0, 1], [0, 1])

# Print the circuit
print(qc)
