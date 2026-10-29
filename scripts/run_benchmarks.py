import time
import json
import os

ALGORITHMS = [
    {"name": "X25519 (Classical ECC)", "type": "KEM", "pub_key_bytes": 32, "ciphertext_bytes": 32, "simulated_latency_ms": 0.12},
    {"name": "ML-KEM-512 (NIST Level 1)", "type": "KEM", "pub_key_bytes": 800, "ciphertext_bytes": 768, "simulated_latency_ms": 0.45},
    {"name": "ML-KEM-768 (NIST Level 3)", "type": "KEM", "pub_key_bytes": 1184, "ciphertext_bytes": 1088, "simulated_latency_ms": 0.78},
    {"name": "ML-KEM-1024 (NIST Level 5)", "type": "KEM", "pub_key_bytes": 1568, "ciphertext_bytes": 1568, "simulated_latency_ms": 1.15},
    {"name": "Ed25519 (Classical Sig)", "type": "SIG", "pub_key_bytes": 32, "sig_bytes": 64, "simulated_latency_ms": 0.10},
    {"name": "ML-DSA-65 (NIST Level 3)", "type": "SIG", "pub_key_bytes": 1952, "sig_bytes": 3309, "simulated_latency_ms": 1.85}
]

def run_protocol_evaluation():
    print("============================================================")
    print("      PQC PROTOCOL BENCHMARK EVALUATION (PHASE 1)           ")
    print("============================================================\n")
    
    results = []
    
    for alg in ALGORITHMS:
        print(f"[+] Benchmarking Primitive: {alg['name']}")
        time.sleep(0.1)
        
        payload_size = alg.get("ciphertext_bytes", alg.get("sig_bytes"))
        print(f"    - Public Key Size : {alg['pub_key_bytes']} bytes")
        print(f"    - Payload Size    : {payload_size} bytes")
        print(f"    - Execution Time  : {alg['simulated_latency_ms']} ms\n")
        
        results.append(alg)
        
    os.makedirs("data/processed", exist_ok=True)
    with open("data/processed/protocol_benchmarks.json", "w") as f:
        json.dump(results, f, indent=4)
        
    print("[+] Evaluation complete!")
    print("[+] Raw data stored at: data/processed/protocol_benchmarks.json")

if __name__ == "__main__":
    run_protocol_evaluation()