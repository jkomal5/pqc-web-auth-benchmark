import json
import os
import matplotlib.pyplot as plt

def generate_benchmark_plots():
    json_path = "data/processed/protocol_benchmarks.json"
    if not os.path.exists(json_path):
        print(f"[-] Error: Telemetry file not found at {json_path}")
        return

    with open(json_path, "r") as f:
        data = json.load(f)

    names = [d["name"] for d in data]
    pub_key_sizes = [d["pub_key_bytes"] for d in data]
    latencies = [d["simulated_latency_ms"] for d in data]

    os.makedirs("results/plots", exist_ok=True)

    # Figure 1: Public Key Sizes Comparison
    plt.figure(figsize=(10, 5))
    bars = plt.barh(names, pub_key_sizes, color='skyblue', edgecolor='black')
    plt.xlabel('Public Key Size (Bytes)')
    plt.title('PQC vs Classical Cryptography: Public Key Sizes')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 20, bar.get_y() + bar.get_height()/2, f'{int(width)} B', 
                 va='center', ha='left', fontsize=9)

    plt.tight_layout()
    plot_path_1 = "results/plots/public_key_sizes.png"
    plt.savefig(plot_path_1, dpi=300)
    plt.close()
    print(f"[+] Saved plot: {plot_path_1}")

    # Figure 2: Execution Latency Comparison
    plt.figure(figsize=(10, 5))
    bars = plt.barh(names, latencies, color='salmon', edgecolor='black')
    plt.xlabel('Execution Time (ms)')
    plt.title('PQC vs Classical Cryptography: Execution Latency')
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.02, bar.get_y() + bar.get_height()/2, f'{width:.2f} ms', 
                 va='center', ha='left', fontsize=9)

    plt.tight_layout()
    plot_path_2 = "results/plots/execution_latency.png"
    plt.savefig(plot_path_2, dpi=300)
    plt.close()
    print(f"[+] Saved plot: {plot_path_2}")

if __name__ == "__main__":
    generate_benchmark_plots()