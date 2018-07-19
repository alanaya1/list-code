from pymatgen import MPRester
from pprint import pprint

with MPRester("iUCzg5aBMJ1w30KT") as m:
    data = m.query(criteria={}, properties=["pretty_formula", "material_id","e_above_hull","spacegroup"])
all_names = [d['pretty_formula'] for d in data]
print('retrieval complete')

chem_formulas = []
PC_mats = []
for index, a in enumerate(all_names):
    if all_names.count(a) > 1:
        PC_mats.append([ data[index]['material_id'], data[index]['pretty_formula'], data[index]['e_above_hull'], data[index]['spacegroup']['symbol'] ])
        chem_formulas.append([ data[index]['material_id'], data[index]['pretty_formula'], data[index]['e_above_hull'], data[index]['spacegroup']['symbol'] ])
PC_mats = sorted(PC_mats, key=lambda x: (x[1]))
print('PC_mats is now sorted')

other_half = []
placeholderred_pc_mats = []
object = []

for chem in chem_formulas:
    for mat in PC_mats:
        if mat[1] == chem[1] and mat[3] == chem[3] and mat[2] >= chem [2]:
            other_half.append(mat)
for index, row in enumerate(other_half):
    if other_half.count(row) == 1:
        placeholderred_pc_mats.append(row)
        object.append(row[1])
print('your almost there')
red_pc_mats = []
for index, name in enumerate(object):
    if object.count(name) > 1:
        red_pc_mats.append(placeholderred_pc_mats[index])
red_pc_mats = sorted(red_pc_mats, key=lambda x: (x[1], x[2]))
print('congrats you are done')


for line in red_pc_mats:
    print(line)
print(len(red_pc_mats))
#for red_pc_mats
file = open("largelist.csv","w")
for line in red_pc_mats:
    for part in line:
        file.write(str(part) + ',')
    file.write('\n')
file.close()
#for final list
file = open("Finallargelist.csv","w")
for line in Finallist:
    for part in line[0]:
        file.write(str(part) + ',')
    file.write('\n')
    for part in line[1]:
        file.write(str(part) + ',')
    file.write('\n')
file.close()
