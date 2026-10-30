import json
import os

def simulate_packet_fragmentation():
    # Standard Ethernet MTU = 1500 bytes, minus 20B IP header and 20B TCP header = 1460 bytes MSS
    MSS = 1460
    
    # Define cryptographic payload sizes (Combining Public Keys, Ciphertexts/Signatures) for handshakes
    protocols = [
        {
            "name": "Classical Baseline (X25519 + Ed25519)", 
            "pub_key": 32, 
            "sig_or_ciphertext": 64, 
            "total_bytes": 32 + 32 + 64  # Key exchange + signature overhead
        },
        {
            "name": "Hybrid Mode (X25519 + ML-KEM-768)", 
            "pub_key": 32 + 1184, 
            "sig_or_ciphertext": 64 + 1088, 
            "total_bytes": 32 + 1184 + 1088
        },
        {
            "name": "Pure PQC (ML-KEM-1024 + ML-DSA-65)", 
            "pub_key": 1568 + 1952, 
            "sig_or_ciphertext": 1568 + 3309, 
            "total_bytes": 1568 + 1568 + 1952 + 3309
        }
    ]

    results = []
    print("=== WebAuthn / TLS 1.3 PQC Fragmentation & Overhead Simulation ===\n")
    
    for proto in protocols:
        total_bytes = proto["total_bytes"]
        # Calculate how many TCP segments are required based on Maximum Segment Size
        segments = (total_bytes + MSS - 1) // MSS
        
        # Simulate network latency impact (assuming a 15ms regional RTT per extra packet fragment)
        simulated_extra_rtt_ms = (segments - 1) * 15.0 
        
        entry = {
            "protocol": proto["name"],
            "total_payload_bytes": total_bytes,
            "tcp_segments_required": segments,
            "simulated_extra_handshake_delay_ms": simulated_extra_rtt_ms
        }
        results.append(entry)
        
        print(f"Protocol: {proto['name']}")
        print(f"  - Total Crypto Payload: {total_bytes:,} bytes")
        print(f"  - TCP Segments Required (MSS = {MSS}B): {segments}")
        print(f"  - Estimated Handshake Delay Penalty: {simulated_extra_rtt_ms:.1f} ms\n")

    # Save output to data directory
    os.makedirs("data/processed", exist_ok=True)
    out_path = "data/processed/fragmentation_simulation.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=4)
    print(f"[+] Simulation telemetry saved to {out_path}")

if __name__ == "__main__":
    simulate_packet_fragmentation()