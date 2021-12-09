from utils import get_input_file, inputfile_to_array

get_input_file(6)

input_list = inputfile_to_array("inputs/input_day_6.txt")
fish_list_as_strings = input_list[0].split(",")
fish_list = map(int, fish_list_as_strings)
fish_list = list(fish_list)


def get_fish_list_after_num_days(fish_list, num_days=80):
    if num_days == 0:
        return fish_list
    for i in range(num_days):
        new_fish_list = []
        for fish in fish_list:
            if fish == 0:
                new_fish_list.append(6)
                new_fish_list.append(8)
            else:
                new_fish_list.append(fish-1)
        fish_list = new_fish_list
    return new_fish_list

def efficient_get_number_of_fish_after_num_days(fish_list, num_days=80):
    smart_fish_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in fish_list:
        smart_fish_list[i] +=1
    for i in range(num_days):
        zeros = smart_fish_list[0] 
        smart_fish_list = smart_fish_list[1:] + smart_fish_list[:1] # Rotate list one place to the left
        smart_fish_list[6] += zeros
    return sum(smart_fish_list)

def get_number_of_fish_after_num_days(fish_list, num_days=80):
    new_fish_list = get_fish_list_after_num_days(fish_list, num_days)
    return(len(new_fish_list))

print ("First answer: ", get_number_of_fish_after_num_days(fish_list))
print ("Second answer: ", efficient_get_number_of_fish_after_num_days(fish_list, 256))