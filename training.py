import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Data Parsing: Read the pdb file and extract only the C3' atoms"""

df = pd.read_table("7shx.pdb")
lst = np.array(df.iloc[:, 0])
c3 = []
for elem in lst:
    if "C3'" in elem:
        c3.append(elem)
print("C3' Atoms:", c3)

"""Calculate 10 distance distributions for the 10 base pairs"""

nucl_pairs = []
distance = []
for i in range(94):
    for j in range(i, 94):
        if (int(c3[j].split()[5]) - int(c3[i].split()[5])) >= 4:
            nucl_pairs.append([c3[i].split()[3], c3[j].split()[3]])
            dist_x = (float(c3[j].split()[6]) - float(c3[i].split()[6])) ** 2
            dist_y = (float(c3[j].split()[7]) - float(c3[i].split()[7])) ** 2
            dist_z = (float(c3[j].split()[8]) - float(c3[i].split()[8])) ** 2
            distance.append((dist_x + dist_y + dist_z) ** 0.5)

print("\nNucl_pairs:", nucl_pairs)
print("\nDistances:", distance)

def distance_nucleotide_pairs(n1, n2, ln):
    NN = []
    for i in range(ln):
        if (nucl_pairs[i][0] == n1 and nucl_pairs[i][1] == n2) or (
                nucl_pairs[i][0] == n1 and nucl_pairs[i][1] == n2):
            if distance[i] <= 20:
                NN.append(distance[i])
    return NN

ln = len(nucl_pairs)
AA = distance_nucleotide_pairs("A", "A", ln)
AU = distance_nucleotide_pairs("A", "U", ln)
AC = distance_nucleotide_pairs("A", "C", ln)
AG = distance_nucleotide_pairs("A", "G", ln)
CC = distance_nucleotide_pairs("C", "C", ln)
CG = distance_nucleotide_pairs("C", "G", ln)
CU = distance_nucleotide_pairs("C", "U", ln)
GG = distance_nucleotide_pairs("G", "G", ln)
GU = distance_nucleotide_pairs("G", "U", ln)
UU = distance_nucleotide_pairs("U", "U", ln)

print("\nAA Distances:", AA)
print("AU Distances:", AU)
print("AC Distances:", AC)
print("AG Distances:", AG)
print("CC Distances:", CC)
print("CG Distances:", CG)
print("CU Distances:", CU)
print("GG Distances:", GG)
print("GU Distances:", GU)
print("UU Distances:", UU)

"""Compute the observed frequencies"""

freq_all = []

def calculate_freq(NN, name):
    global freq_all
    for i in range(20):
        count = 0
        for elem in NN:
            if elem <= (i + 1) and elem >= i:
                count += 1
        freq = count / len(NN)
        freq_all.append(freq)
        print(f"{name} Frequency for Distance {i + 1}-{i + 2}: {freq}")

calculate_freq(AA, "AA")
calculate_freq(AU, "AU")
calculate_freq(AC, "AC")
calculate_freq(AG, "AG")
calculate_freq(CC, "CC")
calculate_freq(CG, "CG")
calculate_freq(CU, "CU")
calculate_freq(GG, "GG")
calculate_freq(GU, "GU")
calculate_freq(UU, "UU")

print("\nTotal Observed Frequencies:", freq_all)

plt.hist(AC)

"""Compute the reference frequency"""

freq_ref = []
distance_20 = list(filter(lambda x: x <= 20, distance))

for i in range(20):
    count = 0
    for elem in distance_20:
        if elem <= (i + 1) and elem >= i:
            count += 1
    freq = count / len(distance_20)
    freq_ref.append(freq)
    print(f"Reference Frequency for Distance {i + 1}-{i + 2}: {freq}")

print("\nTotal Reference Frequencies:", freq_ref)

"""Compute the log-ratio of the two frequencies"""

pseudo_energy = []
for i in range(200):
    obs = freq_all[i]
    ref = freq_ref[(i % 20)]
    if ref != 0 and obs != 0:
        pseudo_energy.append((-1) * np.log(obs / ref))
    else:
        pseudo_energy.append(10)

print("\nPseudo Energies:", pseudo_energy)
