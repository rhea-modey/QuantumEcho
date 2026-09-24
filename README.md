# Quantum Echo Simulation

A one-qubit Qiskit simulation of a quantum echo experiment.

The circuit applies a forward unitary `U`, a small perturbation `V`, and the inverse evolution `U†`, then measures the probability of returning to the initial state:

`|0> → U → V → U†`

The script sweeps the perturbation strength and plots the resulting echo amplitude.

## Tech

Python · Qiskit · NumPy · Matplotlib

## Run

```bash
python quantum_echo.py
```

## Implementation

- Forward evolution is modeled with `Rx` and `Rz` rotations.
- The perturbation is a small `Rz` rotation.
- `Statevector` simulation computes `|<0|U†VU|0>|²`.
- A perturbation sweep visualizes how the echo changes as the perturbation grows.
