import sys
import requests
import os.path


def inputfile_to_array(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
    lines_as_array = [(line) for line in lines]
    return lines_as_array

coordinate_list = inputfile_to_array("input_2")

def get_pos(coordinate_list):
  vert_pos = 0
  horiz_pos = 0
  for element in coordinate_list:
    dir = element.split()[0]
    num = int(element.split()[1])
    if dir == "forward":
      horiz_pos += num
    elif dir == "up":
      vert_pos -= num
    elif dir == "down":
      vert_pos += num
    else:
      print("Something is wrong")
  return (vert_pos,horiz_pos)

vert_pos, horizon_pos = get_pos(coordinate_list)
print (vert_pos * horizon_pos)

