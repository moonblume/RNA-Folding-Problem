import numpy as np
from training import calculate_pseudo_energy, AA

bins = np.arange(0, 20) + 1

# Call the calculate_pseudo_energy function to get the pseudo_energy data
pseudo_energy = calculate_pseudo_energy()

# Perform interpolation using AA and pseudo_energy
interpolation_function = np.interp(AA, bins, pseudo_energy[0:20])

print("Interpolation Function:", interpolation_function)

pseudo_energy_slice = pseudo_energy[0:20]
print("Pseudo Energy (0-19):", pseudo_energy_slice)
