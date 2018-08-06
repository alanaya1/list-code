from pymatgen import MPRester
from pprint import pprint
with MPRester("iUCzg5aBMJ1w30KT") as mpr:
    data = mpr.query(criteria={}, properties=["pretty_formula", "material_id","e_above_hull","spacegroup", "band_gap"])
    all_names = [d['pretty_formula'] for d in data]
print('retrieval complete')

chem_formulas = []
PC_mats = []
for index, a in enumerate(all_names):
    if all_names.count(a) > 1:
        PC_mats.append([ data[index]['material_id'], data[index]['pretty_formula'], data[index]['e_above_hull'], data[index]['spacegroup']['symbol'], data[index]['band_gap'] ])
        chem_formulas.append([ data[index]['material_id'], data[index]['pretty_formula'], data[index]['e_above_hull'], data[index]['spacegroup']['symbol'], data[index]['band_gap']])
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

print('one more long step to go')

Finallist = []
by_name = {}
for line in red_pc_mats:
    name = line[1]
    if name not in by_name:
        by_name[name] = []
    by_name[name].append(line)
for key in by_name:
    ehull = float(by_name[key][0][2])
    for mat in by_name[key][1:]:
        ehull_test = float(mat[2])
        diff = abs(ehull - ehull_test)
        if diff > 0.007:
            #comment bellow for total list
            lowest = None
            for line in Finallist:
                if line[0][1] == mat[1] and (not lowest or line[2] < lowest):
                    lowest = line[2]
            if lowest == None or lowest > diff:
                Finallist.append([by_name[key][0], mat, diff])
#         print(key, diff, '\n', by_name[key])
# print(len(by_name))
print('even more to go')
Finallist = sorted(Finallist, key=lambda x: float(x[2]))
Done = []

for index, line in enumerate(range(len(Finallist))):
    bandgap1 = float(Finallist[line][0][4])
    bandgap2 = float(Finallist[line][1][4])
    difference = abs(float(bandgap1-bandgap2))
    if difference > 1 :
        if bandgap1 <= 0.1 or bandgap2 <= 0.1:
            Done.append(Finallist[index])
            Done.append(difference)


for line in Done:
    print(line)
print(len(Done))

# Finallist = sorted(Finallist, key=lambda x: float(x[2]))

# for line in Finallist:
#     print(line)

# Finallist = sorted(Finallist, key=lambda x: float(x[2]))
#
# for thing in Done:
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



file = open("slideslist.csv","w")
for line in Done:
    file.write(str(line))
    file.write(',')
    file.write('\n')
file.close()
