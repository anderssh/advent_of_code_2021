from utils import get_input_file, inputfile_to_array

get_input_file(8)

input_list = inputfile_to_array("inputs/input_day_8_test.txt")

def get_input_and_output_signal(input_list):
    input_signal = []
    output_signal = []
    for i in input_list:
        single_signal = i.split(" | ")
        input_signal.append(single_signal[0])
        output_signal.append(single_signal[1])
    return input_signal, output_signal

def identify_digit(single_input_signal, digit_to_identify=4):
    phrases = single_input_signal.split()
    digit_to_length_mapping = {
        0:6,
        1:2,
        2:5,
        3:5,
        4:4,
        5:5,
        6:6,
        7:3,
        8:7,
        9:6,
    }
    length_to_look_for = digit_to_length_mapping[digit_to_identify]
    candidates = []
    for phrase in phrases:
        if len(phrase) == length_to_look_for:
            candidates.append(phrase)
    return candidates

def identify_digits(single_input_signal):
    one = identify_digit(single_input_signal, digit_to_identify=1)
    two_candidates = identify_digit(single_input_signal, digit_to_identify=2)
    three_candidates = identify_digit(single_input_signal, digit_to_identify=3)
    four = identify_digit(single_input_signal, digit_to_identify=4)
    five_candidates = identify_digit(single_input_signal, digit_to_identify=5)
    six_candidates = identify_digit(single_input_signal, digit_to_identify=6)
    seven = identify_digit(single_input_signal, digit_to_identify=7)
    eight = identify_digit(single_input_signal, digit_to_identify=8)
    nine_candidates = identify_digit(single_input_signal, digit_to_identify=9)
    zero_candidates = identify_digit(single_input_signal, digit_to_identify=0)
    middle_row_candidates = get_middle_row_candidates(four[0],seven[0])
    top_left_col_candidates = get_middle_row_candidates(four[0],seven[0])
    two_candidates, last_one_with_five_segments = remove_if_both_there(two_candidates, middle_row_candidates)
    three_candidates, _ = remove_if_both_there(three_candidates, middle_row_candidates)
    five = last_one_with_five_segments[0]
    right_top_col = get_right_top_col(five, two_candidates)
    six = get_six(six_candidates, right_top_col)
    nine_candidates.remove(six)
    zero_candidates.remove(six)
    top_left_col = get_top_left_col_based_on_nine_and_six_candidates(nine_candidates, middle_row_candidates)
    middle_row_candidates.remove(top_left_col)
    middle_row = middle_row_candidates[0]
    nine = get_nine(nine_candidates, middle_row)
    zero_candidates.remove(nine)
    zero = zero_candidates[0]
    bottom_left_col = get_bottom_left_col(eight[0], nine)
    two = get_two(two_candidates, bottom_left_col)
    three_candidates.remove(two)
    three = three_candidates[0]
    one = "".join(sorted(one[0]))
    two = "".join(sorted(two))
    three = "".join(sorted(three))
    four = "".join(sorted(four[0]))
    five = "".join(sorted(five))
    six = "".join(sorted(six))
    seven = "".join(sorted(seven[0]))
    eight = "".join(sorted(eight[0]))
    nine = "".join(sorted(nine))
    zero = "".join(sorted(zero))
    list_of_digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    return list_of_digits

    
def get_two(two_candidates, bottom_left_col):
    for i in two_candidates:
        if bottom_left_col in i:
            return i
    
def get_bottom_left_col(eight, nine):
    for i in eight:
        if i not in nine:
            return i

def get_nine(nine_candidates, middle_row):
    for candidate in nine_candidates:
        if middle_row in candidate:
            return candidate
    

def get_six(six_candidates, right_top_col):
    for candidate in six_candidates:
        if right_top_col not in candidate:
            return candidate

    
def get_right_top_col(five, two_candidates):
    common_chars = ''.join(set(two_candidates[0]).intersection(two_candidates[1]))
    for char in common_chars:
        if char not in five:
            return char

def get_top_left_col_based_on_nine_and_six_candidates(nine_candidates, middle_row_candidates):
    ''' The one of the middle_row_candidates that are only in one of them gives a middle row
    '''
    for middle_row_candidate in middle_row_candidates:
        for nine_candidate in nine_candidates:
            if middle_row_candidate not in nine_candidates:
                return middle_row_candidate

def remove_if_both_there(candidate_list, char_list):
    '''
    Removes candidate from candidate_list, if all char in char_list are present in candidate
    returns updatede candidate_list
    '''
    to_be_removed = []
    for i in candidate_list:
        both_there = True
        for j in char_list:
            if j not in i:
                both_there = False
        if both_there:
            to_be_removed.append(i)
    for i in to_be_removed:
        candidate_list.remove(i)
    return candidate_list, to_be_removed
    



def get_top_row(one, seven):
    for i in seven:
        if i not in one:
            return i

def get_middle_row_candidates(four, seven):
    candidates = []
    for i in four:
        if i not in seven:
            candidates.append(i)
    return candidates

def get_top_row_candidates(four, seven):
    candidates = []
    for i in four:
        if i not in seven:
            candidates.append(i)
    return candidates

def count_unique_digits_in_output(input_list):
    input_signal, output_signal = get_input_and_output_signal(input_list)
    relevant_lengths = [2,4,3,7] # corresponding to 1,4,7,8
    count  = 0
    for singel_output_signal in output_signal:
        phrases = singel_output_signal.split()
        for phrase in phrases:
            if len(phrase) in relevant_lengths:
                count += 1
    return count

def calculate_number(digits, single_output_signal):
    phrases = single_output_signal.split()
    number_as_string = ''
    for seq in phrases:
        sorted_seq = "".join(sorted(seq))
        for i,val in enumerate(digits):
            if val == sorted_seq:
                #print(str(i))
                number_as_string += str(i)
    print(number_as_string)
    return int(number_as_string)

input_list = ["fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb"]
#input_list = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
#print("First answer: ", count_unique_digits_in_output(input_list))
input_signal, output_signal = get_input_and_output_signal(input_list)
sum = 0

for i in range(len(input_signal)):
    digits = identify_digits(input_signal[i])
    print(digits)
    sum += calculate_number(digits, output_signal[i])
print("lengde", len(input_signal))
print (sum)
