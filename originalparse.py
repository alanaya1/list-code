f = open('2ddata_all.txt', 'r')
lines = f.readlines()
f.close()

num_lines = len(lines)
all_mat_names = []
complete_list = []

for line in lines[1:]:
    if line[0] != "\n":
        parsed = line.split('\t')
        all_mat_names.append(parsed[1])
        complete_list.append(parsed)

PC_Mats = []
chem_formulas = []

for index, list in enumerate(complete_list):
    mat_name = list[1]
    if all_mat_names.count(mat_name) > 1:
        PC_Mats.append(list)
        chem_formulas.append(list)


red_pc_mats = []
other_half = []

for chem in chem_formulas:
    for mat in PC_Mats:
        if mat[1] == chem[1] and mat[15] == chem[15] and mat[14] >= chem [14]:
            other_half.append(mat)

for index, row in enumerate(other_half):
    if other_half.count(row) == 1:
        if mat[14] >= chem [14]:
            red_pc_mats.append(row)


# for line in PC_Mats:
#     print(line)
# print(len(PC_Mats))
# for line in chem_formulas:
#     print(line)
# print(len(chem_formulas))
# for line in red_pc_mats:
#     print(line)
# print(len(red_pc_mats))
# for line in other_half:
#     print(line)
# print(len(other_half))
for line in red_pc_mats:
    print(line)
print(len(red_pc_mats))
