# VID-Framework

Implementation of Valamontes Interaction Diagrams (VID) from the paper "From Feynman Diagrams to Valamontes Interaction Diagrams (VID): A Nonperturbative Diagrammatic Framework for Geometry, Coherence, and ∞-Algebraic Dynamics" by Antonios Valamontes (v15, Dec 2025).

VID is a diagrammatic tool for nonperturbative QFT, using a dodecahedral lattice (DLSFH), coherence dynamics (SGCV+MC), and graded-infinite operators (Infinity Algebra). This repo provides prototypes based on the paper and Dr. Gregg Tyler Milligan's review suggestions.

## Features
- Discrete dodecahedral graph simulations.
- Convergence checks for ∞-algebra propagators.
- Path pruning and amplitude calculations with admissibility rules.
- Coherence curl for emergent curvature.
- Toy three-node chain example with explicit computations.

## Structure
- **notebooks/**: Jupyter notebooks for key modules.
  - convergence.ipynb: ∞-Algebra sector convergence (review 3.2, Prop. 2.3).
  - path_amplitude.ipynb: Admissible path pruning and VID amplitude sum (review 3.4).
  - coherence_curvature.ipynb: SGCV coherence calculus and discrete curl (Sec. 3, Lemma 3.1).
  - three_node_example.ipynb: Minimal three-node chain with explicit Laplacian pseudoinverse and weights (review praise for concrete examples).
- **src/**: Utility scripts.
  - vid_utils.py: Common functions (graph building, L+ computation).

## Setup
```bash
pip install -r requirements.txt
jupyter notebook
