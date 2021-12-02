import sys
import requests
import os.path


def inputfile_to_array(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
    lines_as_array = [(line) for line in lines]
    return lines_as_array

number_list = [int(item) for item in inputfile_to_array("input_1")]

num_increases = 0
prev_num = 999999
for i in number_list:
  if i > prev_num:
    num_increases += 1
  prev_num = i
print(num_increases)
  
