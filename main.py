import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram

QBIT_NUMBER = 8

simulator = Aer.get_backend('qasm_simulator')

qc = QuantumCircuit(QBIT_NUMBER)

for i in range(0, QBIT_NUMBER):
    qc.h(i)

# qc.cx(0, range(1, 5))
a = qc.measure_all()

job = execute(qc, simulator, shots=255)

result = job.result()

# Returns counts
counts = result.get_counts(qc)
print("\nQubit measurements",counts)