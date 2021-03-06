from utils import get_input_file, inputfile_to_array

get_input_file(2)

coordinate_list = inputfile_to_array("inputs/input_day_2.txt")
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

def get_new_pos(coordinate_list):
  vert_pos = 0
  horiz_pos = 0
  aim = 0
  for element in coordinate_list:
    dir = element.split()[0]
    num = int(element.split()[1])
    if dir == "forward":
      horiz_pos += num
      vert_pos += aim * num
    elif dir == "up":
      aim -= num
    elif dir == "down":
      aim += num
    else:
      print("Something is wrong")
  return (vert_pos,horiz_pos,aim)
  
vert_pos, horizon_pos = get_pos(coordinate_list)
new_vert_pos, new_horizon_pos, aim = get_new_pos(coordinate_list)
print ("First answer: ", vert_pos * horizon_pos)
print ("Second answer: ", new_vert_pos * new_horizon_pos)
