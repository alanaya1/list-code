import sys

def getFullList(filename):
    f = open(filename, 'r')
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

    return all_mat_names, complete_list

def getPossiblePCMats(all_mat_names, complete_list):
    #the segment below creates two new identical lists for furhter use, which contain all of the phase change materials
    PC_mats = []
    chem_formulas = []
    chem_names = []
    for index, mylist in enumerate(complete_list):
        mat_name = mylist[1]
        if all_mat_names.count(mat_name) > 1:
            PC_mats.append(mylist)
            chem_formulas.append(mylist)
            chem_names.append(mat_name)

    return PC_mats, chem_formulas, chem_names


def filterLowestMonoSpace(chem_formulas, PC_mats):
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

    red_chem_form = []
    for index, name in enumerate(object):
        if object.count(name) > 1:
            red_pc_mats.append(placeholderred_pc_mats[index])
            red_chem_form.append(placeholderred_pc_mats[index][1])
    red_pc_mats = sorted(red_pc_mats, key=lambda x: (x[1], x[14]))


    return red_pc_mats, red_chem_form

def filterEnergy(red_pc_mats):
    Finallist = []
    final_chem_names = []
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
            if diff > 0.007:
                lowest = None
                for line in Finallist:
                    if line[0][1] == mat[1] and (not lowest or line[2] < lowest):
                        lowest = line[2]
                if lowest == None or lowest > diff:
                    Finallist.append([by_name[key][0], mat, diff])
                    final_chem_names.append(mat[1])
    Finallist = sorted(Finallist, key=lambda x: float(x[2]))

    return Finallist, final_chem_names


if __name__ == '__main__':
    filename = '2ddata_all.txt'

    all_mat_names, complete_list = getFullList(filename)
    print('Original list')
    print('# chem formulas', len(set(all_mat_names)), ', # mpids in list', len(complete_list))

    PC_mats, chem_formulas, chem_names = getPossiblePCMats(all_mat_names, complete_list)
    print('\nFilter by chem name > 1')
    print('# chem formulas', len(set(chem_names)), ', # mpids in list', len(PC_mats))

    red_pc_mats, red_chem_form = filterLowestMonoSpace(chem_formulas, PC_mats)
    print('\nFilter by mono space group')
    print('#chem formulas', len(set(red_chem_form)), '# mpids in list', len(red_pc_mats))

    final_list, final_chem_names = filterEnergy(red_pc_mats)
    print('\nFilter by dE > 0.007')
    print('#chem formulas', len(set(final_chem_names)), '# mpids in list', 2*len(final_list))
    
    # for line in Finallist:
    #     print(line[0])
    #     print(line[1])
    #     print(line[2])
    # print(len(Finallist))
    
    # file = open("slideslist.csv","w")
    # for line in Finallist:
    #     for part in line[0]:
    #         file.write(part + ',')
    #     file.write('\n')
    #     for part in line[1]:
    #         file.write(part + ',')
    #     file.write('\n')
    # file.close()
