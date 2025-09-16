# motif-entropy-nfkb

Compute the entropy of an NF-κB motif from a small DNA set and show how entropy reflects column-wise conservation.

---

## Project goals

- Formalize the NF-κB motif as a position probability matrix (PPM) by estimating per-position nucleotide frequencies from the input sequences.  
- Compute per-column entropy  
  \[
  H_i = -\sum_{b \in \{A,C,G,T\}} p_{i,b}\log_2 p_{i,b}
  \]  
  and total motif entropy  
  \[
  H = \sum_i H_i
  \].  
- Expose configurable parameters: pseudocount size, background nucleotide frequencies, and choice of log base.  
- Quantify motif conservation by comparing entropy to information content and PWM logo height; visualize both across motif positions.  
- Assess statistical significance of observed entropy using permutation or bootstrap resampling of the input sequences, with empirical \(p\)-values reported.  
- Provide a one-command reproducible run: input FASTA/CSV → frequency tables → per-position entropy → total entropy → figures.  
- Package a small curated dataset with documented provenance and a GC-matched synthetic control set.  
- Include unit tests for frequency estimation, entropy calculation, and CLI input/output, along with linting and type checks.  
- Capture environment details in `environment.yml` and lockfile, with workflow steps automated by `Makefile` for deterministic builds.  
- Deliver a concise, methods-driven Jupyter notebook that documents assumptions, shows key outputs, and interprets results in the context of motif conservation.

---

## How it works

Given short NF-κB sites (consensus ~ **GGGRNNYYCC**), we compute motif entropy as the sum of per-column entropies:

\[
H = \sum_{i=1}^{L} \left( -\sum_{b \in \{A,C,G,T\}} p_{i,b}\log_2 p_{i,b} \right)
\]

Lower entropy → more conservation.

---

## Quick start (Windows)

### Option 1 — One-click run
Double-click `run_entropy.bat` (or run it from a terminal). It will use the `motif-entropy` conda environment and print the total motif entropy.

### Option 2 — Manual run with Conda
```bash
conda activate motif-entropy
cd src
python motif_entropy.py



