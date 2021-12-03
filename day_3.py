from utils import get_input_file, inputfile_to_array

get_input_file(3)

binary_list = inputfile_to_array("inputs/input_day_3.txt")

def flip_bits(binary_string):
    '''
    Returns at string of flipped bits
    '''
    return ''.join('1' if x == '0' else '0' for x in binary_string)

def counter(binary_list, i):
    zero_counter = 0
    one_counter  = 0
    for element in binary_list:
        if element[i] == "0":
            zero_counter += 1
        else:
            one_counter  += 1
    return zero_counter,one_counter

def get_most_common_bit(binary_list, i, value_if_equal=1):
    num_zeros, num_ones = counter(binary_list,i)
    if num_zeros == num_ones:
        return value_if_equal
    else:
        return int(num_ones > num_zeros)

def get_least_common_bit(binary_list, i, value_if_equal=0):
    num_zeros, num_ones = counter(binary_list,i)
    if num_zeros == num_ones:
        return value_if_equal
    else:
        return int(num_ones < num_zeros)

def get_gamma_epsilon_rate(binary_list):
    length_of_binary_string = len(binary_list[0])
    gamma_rate_list = []
    for i in range(length_of_binary_string):
        gamma_rate_list.append(str(get_most_common_bit(binary_list, i)))    
    gamma_rate_binary = "".join(gamma_rate_list)
    epsilon_rate_binary = flip_bits(gamma_rate_binary)
    gamma_rate_decimal = int(gamma_rate_binary, 2)
    epsilon_rate_decimal = int(epsilon_rate_binary, 2)
    return gamma_rate_decimal, epsilon_rate_decimal    

def power_consumpsion(binary_list):
    gamma_rate, epsilon_rate = get_gamma_epsilon_rate(binary_list)
    return gamma_rate * epsilon_rate

def get_oxygen_generator_rating(binary_list):
    length_of_binary_string = len(binary_list[0])
    for i in range(length_of_binary_string):
        contestants = []
        most_common_bit = get_most_common_bit(binary_list, i)
        for idx, val in enumerate(binary_list):
            if val[i] == str(most_common_bit):
                contestants.append(val)
        if len(contestants) == 1:
            return (int(contestants[0], 2))
        binary_list = contestants

def get_co2_scrubber_rating(binary_list):
    length_of_binary_string = len(binary_list[0])
    for i in range(length_of_binary_string):
        contestants = []
        least_common_bit = get_least_common_bit(binary_list, i)
        for idx, val in enumerate(binary_list):
            if val[i] == str(least_common_bit):
                contestants.append(val)
        if len(contestants) == 1:
            return (int(contestants[0], 2))
        binary_list = contestants

def get_life_support_rating(binary_list):
    return (get_oxygen_generator_rating(binary_list) * get_co2_scrubber_rating(binary_list))

print ("First answer: ", power_consumpsion(binary_list))
print ("Second answer: ", get_life_support_rating(binary_list))
