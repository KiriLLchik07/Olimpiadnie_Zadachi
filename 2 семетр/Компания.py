def add_individual_to_dict(num, name, individuals_dict):
    individuals_dict[num] = name

def find_dependents(master_id, base_list):
    dependents = set()
    for idx in range(len(base_list) - 1):
        if idx % 2 == 0 and base_list[idx][0] == master_id:
            dependents.add(base_list[idx + 1][0])
    return dependents

individuals = {}
file_lines = open("input_s1_01.txt").readlines()
IDs = set([line[:4] for line in file_lines][:-2])
individual_list = []

for idx in range(len(file_lines) - 2):
    individual_list.append([file_lines[idx][:4], file_lines[idx][5:-1]])

for i in IDs:
    add_individual_to_dict(i, 'Unknown Name', individuals)
    for individual in individual_list:
        if i == individual[0] and individual[1] != '':
            add_individual_to_dict(i, individual[1], individuals)

main_person_id = file_lines[-1]
if not (main_person_id.isdigit()):
    for individual in individual_list:
        if individual[1] == main_person_id:
            main_person_id = individual[0]
            break

main_person_dependents = find_dependents(main_person_id, individual_list)

new_dependents = set()
while True:
    length = len(main_person_dependents)
    for individual in main_person_dependents:
        new_dependents = new_dependents.union(find_dependents(individual, individual_list))
    main_person_dependents = main_person_dependents.union(new_dependents)
    if len(main_person_dependents) == length:
        break

main_person_dependents = sorted(main_person_dependents)
if main_person_dependents == set():
    print("NO")
else:
    for dependent_id in main_person_dependents:
        print(dependent_id, individuals[dependent_id])
