f = open('2ddata_all.txt', 'r')
lines = f.readlines()
f.close()
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
#the segment below does multiple things, first it filters through the previous list of PC materials and
#selects the material with the lowest E_hull from a set of materials with the same monolayer space group, leaving one value for each monolayer
#the next loop further removes phase change materials which now only have one entry due to previous filtering
#the following loop then filters the list further by E_hull, leaving only two copies of each material
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
    # print(line)
    name = line[1]
    if name not in by_name:
        by_name[name] = []
    by_name[name].append(line)
# print(len(red_pc_mats))
for key in by_name:
    ehull = float(by_name[key][0][14])
    for mat in by_name[key][1:]:
        ehull_test = float(mat[14])
        diff = abs(ehull - ehull_test)
        if diff > 0.007:
            lowest = None
            for line in Finallist:
                if line[0][1] == mat[1] and (not lowest or line[2] < lowest):
                    lowest = line[2]
            if lowest == None or lowest > diff:
                Finallist.append([by_name[key][0], mat, diff])
#         print(key, diff, '\n', by_name[key])
# print(len(by_name))

Finallist = sorted(Finallist, key=lambda x: float(x[2]))

for line in Finallist:
    print(line[0])
    print(line[1])
    print(line[2])
print(len(Finallist))

file = open("slideslist.csv","w")
for line in Finallist:
    for part in line[0]:
        file.write(part + ',')
    file.write('\n')
    for part in line[1]:
        file.write(part + ',')
    file.write('\n')
file.close()
