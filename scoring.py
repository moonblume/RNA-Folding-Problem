import numpy as np

bins = np.arange(0, 20) + 1
interpolation_function = np.interp(AA, bins, pseudo_energy[0:20])

print("Interpolation Function:", interpolation_function)

pseudo_energy_slice = pseudo_energy[0:20]
print("Pseudo Energy (0-19):", pseudo_energy_slice)
