import networkx as nx
import numpy as np
def build_dodeca_graph():
return nx.dodecahedral_graph()
def compute_laplacian_pseudoinverse(G):
L = nx.laplacian_matrix(G).toarray().astype(float)
eigvals, eigvecs = np.linalg.eigh(L)
eigvals[eigvals < 1e-10] = 1.0
return eigvecs @ np.diag(1.0 / eigvals) @ eigvecs.T
