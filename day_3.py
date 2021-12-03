from utils import get_input_file, inputfile_to_array

get_input_file(3)

binary_list = inputfile_to_array("inputs/input_day_3.txt")

def flip_bits(binary_string):
    '''
    Returns at string of flipped bits
    '''
    return ''.join('1' if x == '0' else '0' for x in binary_string)

def get_gamma_epsilon_rate(binary_list, debug=False):
    length_of_binary_string = len(binary_list[0])
    gamma_rate_array = []
    for i in range(length_of_binary_string):
        zero_counter = 0
        one_counter  = 0
        for element in binary_list:
            if element[i] == "0":
                zero_counter += 1
            else:
                one_counter  += 1
        gamma_rate_array.append(str(int(one_counter > zero_counter)))
    gamma_rate_binary = "".join(gamma_rate_array)
    epsilon_rate_binary = flip_bits(gamma_rate_binary)
    gamma_rate_decimal = int(gamma_rate_binary, 2)
    epsilon_rate_decimal = int(epsilon_rate_binary, 2)
    if debug:
        print("Zeroes in index", i, ": ", zero_counter)
        print("Ones in index", i, ": ", one_counter)
        print("gamma_rate_array at index ", i, ": ", gamma_rate_array)
        print("gamma rate at index ", i, " binary: ", gamma_rate_binary)
        print("decimal gamma rate at index ", i, ": ", gamma_rate_decimal)
    return gamma_rate_decimal, epsilon_rate_decimal

def power_consumpsion(binary_list):
    gamma_rate, epsilon_rate = get_gamma_epsilon_rate(binary_list)
    return gamma_rate * epsilon_rate


print ("First answer: ", power_consumpsion(binary_list))
