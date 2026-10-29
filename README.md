# Post-Quantum Cryptography (PQC) Web Authentication Benchmark

I am building this repository to evaluate and document the protocol-level performance overhead of migrating web authentication workflows from classical cryptography to NIST-standardized Post-Quantum Cryptography (PQC). 

## Project Motivation & Objectives

As quantum computing threatens traditional public-key infrastructure (such as ECC and RSA), transitioning web standards to post-quantum algorithms introduces significant trade-offs—particularly regarding larger public key dimensions, ciphertext sizes, and packet fragmentation over network layers. 

Through this project, I am establishing a rigorous benchmarking pipeline to:
* **Quantify Performance Trade-offs:** Measure execution latencies, public key sizes, and payload overheads comparing classical primitives (X25519/Ed25519) against NIST standards (ML-KEM and ML-DSA).
* **Document Technical Competency:** Provide reproducible, protocol-level telemetry data and automated evaluation scripts to study PQC integration challenges for secure web applications.

## Algorithms Evaluated

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
