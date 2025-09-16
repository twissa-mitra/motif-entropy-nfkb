import os
import math
from collections import Counter

def read_fasta(filename):
    sequences = []
    with open(filename) as f:
        seq = ""
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if seq:
                    sequences.append(seq)
                    seq = ""
            else:
                seq += line
        if seq:
            sequences.append(seq)
    return sequences

def column_entropy(column):
    counts = Counter(column)
    total = len(column)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def motif_entropy(sequences):
    if not sequences:
        return 0.0
    length = len(sequences[0])
    total_entropy = 0.0
    for i in range(length):
        column = [seq[i] for seq in sequences]
        total_entropy += column_entropy(column)
    return total_entropy

if __name__ == "__main__":
    data_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "data", "nfkb_example.fasta"))
    seqs = read_fasta(data_path)
    print(f"Loaded {len(seqs)} sequences from {data_path}")
    print("Motif entropy:", motif_entropy(seqs))
