# Plot interaction profiles
import numpy as np
import matplotlib.pyplot as plt


fig, axs = plt.subplots(nrows=2, ncols=5, figsize=(18, 12))
names={0:"AA", 1:"AU", 2:"AC", 3:"AG", 4:"CC", 5:"CG", 6:"CU", 7:"GG", 8:"GU", 9:"UU"}

for i in range(10):
    if i<5:
      axs[0, i].plot(pseudo_energy[20*i:20*(i+1)], label=f'{names[i]}')
      axs[0, i].set_title(f'Pseudo-energy of {names[i]}')
      axs[0, i].set_xlabel('Distance')
      axs[0, i].set_ylabel('Energy')
      axs[0, i].legend()
    else:
      axs[1, i%5].plot(pseudo_energy[20*i:20*(i+1)], label=f'{names[i]}')
      axs[1, i%5].set_title(f'Pseudo-energy of {names[i]}')
      axs[1, i%5].set_xlabel('Distance')
      axs[1, i%5].set_ylabel('Energy')
      axs[1, i%5].legend()

plt.show()

plt.figure(figsize=(12,8))
for i in range(10):
  plt.plot(pseudo_energy[20*i:20*(i+1)], label=f'{names[i]}')
  plt.legend()
plt.xlabel("Distance")
plt.ylabel("Pseudo-energy")
plt.show()