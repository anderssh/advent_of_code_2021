import sys
import requests
import os.path


def inputfile_to_array(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
    lines_as_array = [(line) for line in lines]
    return lines_as_array

number_list = [int(item) for item in inputfile_to_array("input_1")]

def calculate_num_increases(number_list):
  num_increases = 0
  prev_num = 9999999999999
  for element in number_list:
    if element > prev_num:
      num_increases += 1
    prev_num = element
  return num_increases
  
def calculate_sliding_window(number_list):
  i = 0
  sliding_window_list = []
  for idx, val in enumerate(number_list):
    if idx < (len(number_list) - 2):
      window_sum = val + number_list[idx +1] + number_list[idx +2]
      sliding_window_list.append(window_sum)
  return sliding_window_list

print (calculate_num_increases(calculate_sliding_window(number_list)))
