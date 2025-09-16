# motif-entropy-nfkb

Compute the entropy of an NF-κB motif from a small DNA set and show how entropy reflects column-wise conservation.

## Project goals
- Tiny, readable, reproducible example an admissions reader can scan in ~2 minutes.
- Clear structure (`data/`, `src/`, `notebooks/`) and one-command run.

## How it works
Given short NF-κB sites (consensus ~ GGGRNNYYCC), we compute motif entropy as the sum of per-column entropies:

\[
H = \sum_{i=1}^{L} \left( -\sum_{b \in \{A,C,G,T\}} p_{i,b}\log_2 p_{i,b} \right)
\]

Lower entropy → more conservation.

## Quick start (Windows)

### Option 1 — One-click run  
Double-click `run_entropy.bat` (or run it from a terminal). It will use the `motif-entropy` conda environment and print the total motif entropy.  

### Option 2 — Manual run with Conda  
```bat
conda activate motif-entropy
cd src
python motif_entropy.py



