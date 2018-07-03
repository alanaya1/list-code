f = open('2ddata_all.txt', 'r')
lines = f.readlines()
f.close()
#the segment below captures the entire list, unfiltered  (checked in test)
all_mat_names = []
complete_list = []
for line in lines[1:]:
    if line[0] != "\n":
        parsed = line.split('\t')
        all_mat_names.append(parsed[1])
        complete_list.append(parsed)
#the segment below creates two new identical lists for furhter use, which contain all of the phase change materials    (checked in test)
PC_mats = []
chem_formulas = []
for index, list in enumerate(complete_list):
    mat_name = list[1]
    if all_mat_names.count(mat_name) > 1:
        PC_mats.append(list)
        chem_formulas.append(list)
#the segment below does multiple things, first it filters through the previous list of PC materials and
#removes all materials with identical monolayer space, but highest E_hull, leaving one value for each monolayer
#the last for loop further removes phase change materials which now only have one entry due to previous filtering
#the final folder with our filters applied is     red_pc_mats   all the others are used as placehodlers
un_red = []
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

un_red_names = []
object = sorted(object)
placeholderred_pc_mats = sorted(placeholderred_pc_mats, key=lambda x: x[1])
for index, name in enumerate(object):
    if object.count(name) == 2:
            red_pc_mats.append(placeholderred_pc_mats[index])
    else:
        if object.count(name) > 2 and un_red_names.count(name) == 0:
            un_red_names.append(name)
            un_red.append(placeholderred_pc_mats[index])
for row in un_red:
    indices = [index for index, value in enumerate(object) if value == row[1]]
    indices = sorted(indices, key=lambda x: placeholderred_pc_mats[x][14])
    for index in indices[:2]:

        red_pc_mats.append(placeholderred_pc_mats[index])
#sorts by energy difference in e hull per material, only prints one of the 2; (a,b,c) a = 0 to start from begiinign, b = end of list, c = 2,, abs changes it to the absolute value fo the differences
diffs = []
for x in range(0, len(red_pc_mats), 2):
    diff = abs(float(red_pc_mats[x][14]) - float(red_pc_mats[x + 1][14]))
    # print(red_pc_mats[x][1], red_pc_mats[x + 1][1])
    diffs.append([red_pc_mats[x], red_pc_mats[x + 1], diff])
diffs = sorted(diffs, key=lambda x: float(x[2]))
for line in diffs:
    print('–––––––––––––––––––––––––––––-')
    for part in line:
        print(part)
print(len(diffs))

#this line of code filters the final list by an extra parameter, bandgap, if any value is greater then 0.1, it is appended to Finallist
Finallist = []
for values in diffs:
    if float(values[0][12]) >= 0.1 and float(values[1][12]) >= 0.1:
        Finallist.append(values)

# for line in placeholderred_pc_mats:
#     print(line)
# print(len(diffs))

for line in Finallist:
    print('–––––––––––––––––––––––––––––-')
    for part in line:
        print(part)
print(len(Finallist))
