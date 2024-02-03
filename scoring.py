import numpy as np
from training import calculate_pseudo_energy, AA

# Call the calculate_pseudo_energy function to get the pseudo_energy data
pseudo_energy = calculate_pseudo_energy()

bins = np.arange(0, 20) + 1

interpolation_function = np.interp(AA, bins, pseudo_energy[0:20]) #interpolation function based on pseudo-energy of AA pair

print("Distances in AA:", AA)
print("Pseudo-energy of AA for bins:", pseudo_energy[0:20])
print("Results of interpolation:", interpolation_function)
#we can see that the pseudo-energy per each distance in AA list is approximately the same as pseudo-energy according to the bin, to which this particular distance belongs
#the same thing we can do with each nucleotides pair and their pseudo energy



