# Quantum Echo Simulation

import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# 1. Forward Evolution Unitary U(θ)

def forward_circuit(theta):
    """
    Create a simple 1-qubit forward evolution circuit U(θ).
    We'll use Rx and Rz rotations to model time evolution.
    """
    qc = QuantumCircuit(1)
    qc.rx(theta, 0)
    qc.rz(theta/2, 0)
    qc.rx(theta/2, 0)
    return qc

# 2. Perturbation Operator V(δ)

def perturbation(delta):
    """
    Small Z-rotation represents the perturbation V(δ).
    """
    qc = QuantumCircuit(1)
    qc.rz(delta, 0)
    return qc


# 3. Full Echo Circuit: U† * V * U

def build_echo_circuit(theta, delta):
    """
    Build a full circuit:
        |0> → U → V → U†
    """
    U = forward_circuit(theta)
    V = perturbation(delta)
    U_dagger = U.inverse()

    qc = QuantumCircuit(1)
    qc.append(U, [0])
    qc.append(V, [0])
    qc.append(U_dagger, [0])

    return qc


# 4. Compute Echo Amplitude

def echo_amplitude(theta, delta):
    """
    Compute P_echo = |⟨0| U† V U |0⟩|^2
    """
    qc = build_echo_circuit(theta, delta)
    sv = Statevector.from_instruction(qc)
    amp = np.abs(sv.data[0])**2   # probability of returning to |0>
    return amp


# 5. Sweep Perturbation δ and Plot Echo Decay

theta = np.pi/3
deltas = np.linspace(0, np.pi, 50)
echoes = [echo_amplitude(theta, d) for d in deltas]

plt.figure(figsize=(8,5))
plt.plot(deltas, echoes, marker='o')
plt.title("Quantum Echo Amplitude vs Perturbation δ", fontsize=14)
plt.xlabel("Perturbation δ (radians)")
plt.ylabel("Echo Amplitude  |⟨0|U† V U|0⟩|²")
plt.grid(True)
plt.show()