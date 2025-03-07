import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT #EMT - Effective Medium Theory - used as a reference for interatomic potentials
from ase.neighborlist import NeighborList

def compute_descriptors(atoms):
    positions = atoms.get_positions()
    atomic_numbers = atoms.get_atomic_numbers()
    nl = NeighborList([1.5]*len(atoms),self_interaction=False,bothways=True)
    nl.update(atoms)

    descriptors = []
    for i,atoms in enumerate(atoms):
        indices = nl.get_neighbors(i)
        distances = np.linalg.norm(positions[indices] - positions[i], axis=1)
        feature_vector = [atomic_numbers[i]+list(distances[:5])]
        descriptors.append(feature_vector)
    return np.array(descriptors)