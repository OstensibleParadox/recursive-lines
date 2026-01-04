import sys
import re
import os
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import warnings
import torch

# --- 1. SILENCE COMPATIBILITY WARNINGS ---
warnings.filterwarnings("ignore")

# --- 2. FORCE CPU MODE (LITE VERSION) ---
# DOCUMENTATION: This forces the scanner to run on standard CPU architecture,
# fulfilling the "Democratization of Auditing" requirement for FAccT/AIES.
device = "cpu"
print(f"--- HARDWARE DETECTED: FORCE CPU (Lite Mode) ---")

# --- CONFIGURATION ---
OUTPUT_DIR = "nps4_results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- 3. LOAD NEURAL ENGINE (CPU) ---
try:
    from sentence_transformers import SentenceTransformer, util
    print("Loading Neural Model (CPU)...")
    # Load to CPU to save RAM
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2', device="cpu")
    USE_NEURAL = True
except Exception as e:
    print(f"Warning: Neural engine unavailable ({e}). Switching to Logic-Overlap Mode.")
    USE_NEURAL = False

class NarrativeGraphBuilder:
    def __init__(self, similarity_threshold=0.6):
        self.sim_threshold = similarity_threshold

    def split_sentences(self, text):
        text = re.sub(r'([.!?;。！？\?])', r"\1\n", text)
        lines = [s.strip() for s in text.splitlines() if len(s.strip()) > 5]

        # --- LITE LIMIT: 100 NODES ---
        # Optimization for rapid auditing on consumer hardware
        limit = 100
        print(f"Limiting scan to first {limit} nodes for performance.")
        return lines[:limit]

    def extract_label(self, text):
        words = re.findall(r'\b\w+\b', text)
        if not words:
            return "..."
        caps = [w for w in words if w[0].isupper() and len(w) > 1]
        if caps:
            return caps[0]
        return max(words, key=len)

    def build(self, text):
        sentences = self.split_sentences(text)
        G = nx.DiGraph()
        nodes = []

        # A. BATCH EMBEDDING
        sim_matrix = None
        if USE_NEURAL:
            embeddings = embedding_model.encode(sentences, convert_to_tensor=True, device="cpu")
            print("Computing Topology Matrix...")
            cosine_scores = util.cos_sim(embeddings, embeddings)
            sim_matrix = cosine_scores.numpy()

        for i, sent in enumerate(sentences):
            node_id = f"N{i}"
            label = self.extract_label(sent)
            G.add_node(node_id, text=sent, label=label)
            nodes.append({'id': node_id, 'idx': i})

        # C. GRAPH CONSTRUCTION
        print("Linking Neural Pathways...")
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i == j: continue

                weight = 0
                if USE_NEURAL and sim_matrix is not None:
                    weight = float(sim_matrix[i][j])
                else:
                    words_i = set(nodes[i]['text'].lower().split())
                    words_j = set(nodes[j]['text'].lower().split())
                    if len(words_i | words_j) > 0:
                         weight = len(words_i & words_j) / len(words_i | words_j)

                if weight > self.sim_threshold:
                    G.add_edge(nodes[i]['id'], nodes[j]['id'], weight=weight, type="semantic")

        for i in range(len(nodes) - 1):
            G.add_edge(nodes[i]['id'], nodes[i+1]['id'], weight=0.5, type="sequence")

        return G

class PathologyMetrics:
    """
    Calculates the 3 Governance Signals:
    1. CMI (Core Monopoly Index) -> Centralization
    2. SRD (Self-Referential Density) -> Circular Logic
    3. EIT (External Information Throughput) -> Input Metabolism
    """
    def calculate_all(self, G):
        if len(G.nodes) == 0:
            return {"total_score": 0, "CMI": 0, "SRD": 0, "EIT": 0}

        # 1. CMI
        try:
            centrality = nx.eigenvector_centrality(G, max_iter=500, weight='weight')
        except:
            centrality = nx.degree_centrality(G)

        sorted_nodes = sorted(centrality, key=centrality.get, reverse=True)
        top_node = sorted_nodes[0]
        cmi = sum(centrality[n] for n in sorted_nodes[:3]) / sum(centrality.values())

        # 2. SRD
        try:
            srd = 0
            cycles = 0
            components = list(nx.strongly_connected_components(G))
            for comp in components:
                if len(comp) > 1:
                    subgraph = G.subgraph(comp)
                    if len(subgraph.nodes) < 30:
                        sub_cycles = list(nx.simple_cycles(subgraph))
                        short_cycles = [c for c in sub_cycles if len(c) <= 4]
                        cycles += len(short_cycles)

            if len(G.nodes) > 0:
                srd = cycles / len(G.nodes)
        except:
            srd = 0
            cycles = 0

        # 3. EIT
        external_nodes = [n for n, d in G.in_degree() if d == 0]
        if not external_nodes:
            eit = 0.0
        else:
            paths = []
            for ext in external_nodes:
                try:
                    l = nx.shortest_path_length(G, source=ext, target=top_node)
                    paths.append(l)
                except:
                    continue
            eit = 1 / (np.mean(paths) + 1e-5) if paths else 0.0

        total_score = (0.4 * cmi) + (0.4 * min(srd, 1.0)) + (0.2 * (1.0 - min(eit, 1.0)))

        return {
            "CMI": cmi,
            "SRD": srd,
            "EIT": eit,
            "total_score": total_score,
            "top_core_node": G.nodes[top_node]['label'],
            "cycle_count": cycles
        }

def analyze_file(filepath):
    print(f"\n--- ANALYZING: {filepath} ---")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print("File not found.")
        return

    builder = NarrativeGraphBuilder()
    G = builder.build(text)
    metrics = PathologyMetrics().calculate_all(G)

    # Visualization
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=0.6, seed=42)

    d = dict(G.degree)
    sizes = [v * 50 + 50 for v in d.values()]
    nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color='#ff2a6d', alpha=0.8)
    nx.draw_networkx_edges(G, pos, alpha=0.1, edge_color='gray')
    labels = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)

    filename = os.path.basename(filepath)
    plt.title(f"Pathology Map: {filename}\nCMI: {metrics['CMI']:.2f} | SRD: {metrics['SRD']:.2f} | EIT: {metrics['EIT']:.2f}", fontsize=10)
    plt.axis('off')

    out_path = f"{OUTPUT_DIR}/{filename}.png"
    plt.savefig(out_path, dpi=150)
    plt.close()

    print(f"""
    [GOVERNANCE AUDIT RESULTS]
    File: {filename}
    Composite Risk Score: {metrics['total_score']:.2f}
    --------------------------------------------------
    1. CMI (Centralization): {metrics['CMI']:.2f}
    2. SRD (Loops): {metrics['SRD']:.2f}
    3. EIT (Throughput): {metrics['EIT']:.2f}
    --------------------------------------------------
    Core Obsession: '{metrics['top_core_node']}'
    Graph Artifact: {out_path}
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nps4_scanner.py <file>")
    else:
        analyze_file(sys.argv[1])
