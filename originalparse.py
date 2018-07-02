f = open('2ddata_all.txt', 'r')
lines = f.readlines()
f.close()

all_mat_names = []
complete_list = []
for line in lines[1:]:
    if line[0] != "\n":
        parsed = line.split('\t')
        all_mat_names.append(parsed[1])
        complete_list.append(parsed)

PC_mats = []
chem_formulas = []
for index, list in enumerate(complete_list):
    mat_name = list[1]
    if all_mat_names.count(mat_name) > 1:
        PC_mats.append(list)
        chem_formulas.append(list)

red_pc_mats = []
other_half = []
placeholderred_pc_mats = []
object = []
for chem in chem_formulas:
    for mat in PC_mats:
        if mat[1] == chem[1] and mat[15] == chem[15] and mat[14] >= chem [14]:
            other_half.append(mat)
for index, row in enumerate(other_half):
    if other_half.count(row) == 1:
        if mat[14] >= chem [14]:
            placeholderred_pc_mats.append(row)
            object.append(row[1])
for index, name in enumerate(object):
    if object.count(name) > 1:
            red_pc_mats.append(placeholderred_pc_mats[index])

length_red = []
for index, length in enumerate(red_pc_mats):
    mat_name = length[1]
    if length_red.count(mat_name) == 0:
        length_red.append(mat_name)

for line in red_pc_mats:
    print(line)
print(len(red_pc_mats))
print(length_red)
print(len(length_red))
