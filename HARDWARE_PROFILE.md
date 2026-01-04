# Hardware Profile & Benchmarking

In alignment with **AIES Empirical Standards**, this benchmark was designed to be reproducible on consumer-grade hardware to ensure the democratization of AI governance tools.

## System Specifications (Reference Run)
*   **Chipset:** Apple M4 Max
*   **Memory:** 64GB Unified Memory
*   **Storage:** 2TB SSD
*   **OS:** macOS Sequoia 15.1

## Performance Metrics

| Process | Avg. Time | Resource Load |
| :--- | :--- | :--- |
| **NPS4 Scan (CPU Mode)** | < 1.2s per file | Single Core |
| **Agency Simulation (v2)** | 280ms per epoch | Multi-threaded |
| **Full Suite Regression** | < 45s | Low (<1GB RAM) |

## CPU vs. GPU Logic
The `nps4_scanner.py` script includes a "Force CPU / Lite Mode" switch.
*   **Why:** To allow auditors running on standard laptops (e.g., MacBook Air, Dell XPS) to verify agency metrics without requiring NVIDIA H100/A100 clusters.
*   **Validation:** Neural embeddings utilize `all-MiniLM-L6-v2` optimized for CPU inference, maintaining 96% correlation with larger GPU-bound models for this specific topology task.
