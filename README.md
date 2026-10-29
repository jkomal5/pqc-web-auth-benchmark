# Post-Quantum Cryptography (PQC) Web Authentication Benchmark

This repository contains protocol-level benchmarking scripts and empirical data comparing classical cryptographic primitives against NIST-standardized Post-Quantum Cryptography (PQC) algorithms.

## Project Overview

As quantum computing threatens traditional public-key infrastructure, evaluating the real-world overhead of PQC migration in web authentication workflows is critical. This benchmark evaluates payload sizes, public key dimensions, and execution latencies across:

* **Key Encapsulation Mechanisms (KEM):** X25519 (Classical) vs. ML-KEM-512 / ML-KEM-768 / ML-KEM-1024 (NIST Standards)
* **Digital Signatures (SIG):** Ed25519 (Classical) vs. ML-DSA-65 (NIST Standard)

## Repository Structure

```text
pqc-web-auth-benchmark/
├── data/
│   └── processed/
│       └── protocol_benchmarks.json  # Raw telemetry data from benchmark runs
├── results/
│   └── plots/                      # Visualization outputs
└── scripts/
    └── run_benchmarks.py           # Phase 1 protocol benchmark execution script
