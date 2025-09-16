# Motif Entropy Analysis – NF-κB Example

This project computes and visualizes the entropy of NF-κB DNA binding motifs using Python and Jupyter.  
It demonstrates how entropy reflects column-wise conservation in sequence motifs and provides a reproducible pipeline for motif analysis.

---

## Problem

Transcription factors such as NF-κB regulate gene expression by binding to specific DNA motifs. These binding sites are typically short (8–12 bp) and contain a mixture of highly conserved and variable positions.  

Accurately quantifying motif conservation is critical for understanding:  
- **DNA–protein interactions** — which bases are essential for recognition versus those that tolerate substitutions.  
- **Regulatory logic** — how sequence variation influences binding strength and downstream gene regulation.  
- **Comparative genomics** — distinguishing true binding sites from background sequence.  

Traditional consensus sequences (e.g., `GGGRNNYYCC` for NF-κB) provide a qualitative description but fail to capture positional variability. **Entropy-based scoring** offers a principled, quantitative alternative. By measuring the uncertainty at each motif position, entropy reveals which sites are strongly constrained and which allow flexibility.  

The goal of this project is to implement an **entropy-based framework for motif analysis** that:  
1. Reads aligned sequences (FASTA).  
2. Constructs position probability matrices (PPMs).  
3. Computes per-column entropy and information content.  
4. Visualizes results using bar plots and sequence logos.  

This approach produces interpretable metrics and figures that connect raw sequence data to biological insight about conservation within transcription factor motifs.

---

## Methods

Our workflow was designed to be fully reproducible and transparent. Each step moves from raw DNA sequences to interpretable measures of motif conservation:

1. **Data Loading**  
   NF-κB binding site sequences were provided in FASTA format (`data/nfkb_example.fasta`). A parser was implemented to handle sequence headers, validate characters (A, C, G, T), and ensure equal sequence lengths.

2. **Dataset Validation**  
   Quality checks confirmed that all sequences were aligned and consistent in length. Any invalid characters or malformed entries would raise errors early in the workflow.

3. **PPM Construction**  
   A **position probability matrix (PPM)** was built by counting nucleotides at each column, adding pseudocounts (α = 1) to avoid zeros, and normalizing by column totals.

4. **Entropy and Information Content**  
   For each position, per-column entropy was calculated:  
   \[
   H_i = - \sum_{b \in \{A,C,G,T\}} p_{i,b}\,\log_2 p_{i,b}
   \]  
   Information content was then derived relative to a uniform background (2 bits):  
   \[
   I_i = H_{bg} - H_i
   \]

5. **Visualization**  
   - Bar plots of per-column information (matplotlib).  
   - Sequence logos using `logomaker`: both **frequency-scaled** and **information-weighted**.  
   These figures highlight conserved vs. variable regions.

6. **Results Export**  
   All intermediate tables (counts, PPM, per-position metrics) and summary statistics were saved to `results/`, with publication-ready figures written to `docs/figs/`.

This structured pipeline links sequence-level data to interpretable entropy and conservation measures, with clear outputs for downstream use or inclusion in publications.

---

## Results

Using the **real NF-κB dataset** (12 sequences, length 10), we quantified motif conservation using entropy and information content:

- **Total entropy**: ~11.86 bits  
- **Total information**: ~8.14 bits  
- **Conserved positions** (1–3, 8–10) show low entropy (~1.0) and high information (~1.0).  
- **Variable positions** (4–7) have higher entropy (~1.5–1.6).  

These metrics confirm the expected NF-κB consensus, where the flanking regions are strongly conserved while the central region is more flexible.

---

### Visual Outputs

**Per-column information bar chart**  
This plot shows the information content (in bits) at each motif position. Peaks correspond to conserved columns, while valleys highlight variable positions.  

![NF-κB motif information bar](docs/figs/nfkb_info_bar_real.png)

---

**Frequency sequence logo**  
This logo represents the relative frequency of each nucleotide at every position. Tall letters indicate dominant bases (e.g., G at positions 1–3), while mixed stacks reveal variable sites.  

![NF-κB motif frequency logo](docs/figs/nfkb_logo_freq_real.png)

---

**Information-weighted sequence logo**  
This logo scales nucleotide frequencies by information content, making conserved positions appear taller. It emphasizes the GGG start and C/C-rich ending, consistent with NF-κB’s canonical binding motif.  

![NF-κB motif information-weighted logo](docs/figs/nfkb_logo_info_real.png)


---

## Quick Start

**Option 1 — Run notebook interactively**
```bash
conda activate motif-entropy
jupyter notebook notebooks/01_motif_entropy_demo.ipynb

run_entropy.bat

motif-entropy-nfkb/
│
├── data/          # Example FASTA input
├── notebooks/     # Main Jupyter workflow
├── results/       # CSV outputs + summary
├── docs/figs/     # Saved figures for README/paper
└── src/           # Python scripts (optional)



