from ase import Atoms
from ase.calculators.emt import EMT
import pandas as pd
import numpy as np

data = []

for i in range(1000):
    atoms = Atoms('H2O', positions=np.random.rand(3, 3) * 5)
    atoms.calc = EMT()  
    
    atomic_numbers = atoms.get_atomic_numbers()  # List of  atomic numbers [1, 1, 8] for H2O
    positions = atoms.get_positions().flatten()  # Flatten the 3x3 array to a 1D array
    energy = atoms.get_potential_energy()

    # Append correct numerical data
    data.append(list(atomic_numbers) + list(positions) + [energy])

# Correct column names
columns = ['Atom1', 'Atom2', 'Atom3', 'x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3', 'Energy']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('data/dataset.csv', index=False)
print('Synthetic Data Saved Successfully')
