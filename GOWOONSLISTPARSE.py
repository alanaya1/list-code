import numpy as np
import pymatgen
from matminer.featurizers.site import CrystalNNFingerprint
from matminer.featurizers.structure import SiteStatsFingerprint
f = open('2ddata_all.txt', 'r')
lines = f.readlines()
f.close()
mpr = pymatgen.MPRester("iUCzg5aBMJ1w30KT")
#the segment below captures the entire list, unfiltered
all_mat_names = []
complete_list = []
for line in lines[1:]:
    if line[0] != "\n":
        parsed = line.split('\t')
        all_mat_names.append(parsed[1])
        complete_list.append(parsed)
#the segment below creates two new identical lists for furhter use, which contain all of the phase change materials
PC_mats = []
chem_formulas = []
for index, list in enumerate(complete_list):
    mat_name = list[1]
    if all_mat_names.count(mat_name) > 1:
        PC_mats.append(list)
        chem_formulas.append(list)

un_red = []
red_pc_mats = []
other_half = []
placeholderred_pc_mats = []
object = []
#below, it picks the highest e hull from each monolayer
for chem in chem_formulas:
    for mat in PC_mats:
        if mat[1] == chem[1] and mat[15] == chem[15] and mat[14] >= chem [14]:
            other_half.append(mat)
for index, row in enumerate(other_half):
    if other_half.count(row) == 1:
        if mat[14] >= chem [14]:
            placeholderred_pc_mats.append(row)
            object.append(row[1])
red_pc_mats = []
for index, name in enumerate(object):
    if object.count(name) > 1:
            red_pc_mats.append(placeholderred_pc_mats[index])
red_pc_mats = sorted(red_pc_mats, key=lambda x: (x[1], x[14]))

Finallist = []
by_name = {}
for line in red_pc_mats:
    name = line[1]
    if name not in by_name:
        by_name[name] = []
    by_name[name].append(line)
for key in by_name:
    ehull = float(by_name[key][0][14])
    for mat in by_name[key][1:]:
        ehull_test = float(mat[14])
        diff = abs(ehull - ehull_test)
        # if 0.007 < diff < 0.1:
        if 0.007 < diff :
            #comment bellow for total list
            lowest = None
            for line in Finallist:
                if line[0][1] == mat[1] and (not lowest or line[2] < lowest):
                    lowest = line[2]
            if lowest == None or lowest > diff:
                Finallist.append([by_name[key][0], mat, diff])
#         print(key, diff, '\n', by_name[key])
# print(len(by_name))
Done = []

for index, line in enumerate(range(len(Finallist))):
    bandgap1 = float(Finallist[line][0][12])
    bandgap2 = float(Finallist[line][1][12])
    difference = abs(float(bandgap1-bandgap2))
    if difference > 1 :
        if bandgap1 <= 0.1 or bandgap2 <= 0.1:
            Done.append(Finallist[index])
            Done.append(difference)


for line in Done:
    print(line)
print(len(Done))
# Finallist = sorted(Finallist, key=lambda x: float(x[2]))
# for index, thing in enumerate(Finallist):
#     mp1 = thing[0][0]
#     mp2 = thing[1][0]
#     try:
#         SnSelow = mpr.get_structure_by_material_id(mp1)
#         SnSehigh = mpr.get_structure_by_material_id(mp2)
#
#         # Calculate structure fingerprints.
#         ssf = SiteStatsFingerprint(CrystalNNFingerprint.from_preset('cn'))
#         v_SnSelow = np.array(ssf.featurize(SnSelow))
#         v_SnSehigh = np.array(ssf.featurize(SnSehigh))
#         v_SnSelow = v_SnSelow / np.linalg.norm(v_SnSelow)
#         v_SnSehigh = v_SnSehigh / np.linalg.norm(v_SnSehigh)
#
#
#         # Print out distance between structures.
#         fish = np.linalg.norm(v_SnSehigh - v_SnSelow)
#     except Exception as e:
#         print('error')
#         fish = 666
#     thing.append(fish)
#
# Finallist = sorted(Finallist, key=lambda x: x[3])

# print(len(Finallist))
# for line in Finallist:
#     print(line)

# file = open("slideslist.csv","w")
# for line in Finallist:
#     if len(line) == 4:
#         print(line)
#         for index, part in enumerate(line[0]):
#             file.write(str(part))
#             if index < len(line[0]) - 1:
#                 file.write(',')
#         # file.write('\n')
#         for index, part in enumerate(line[1]):
#             file.write(str(part))
#             if index < len(line[1]) - 1:
#                 file.write(',')
#         # file.write('\n')
#         file.write('%f\n' % line[2])
#         file.write('%f\n' % line[3])
# file.close()
