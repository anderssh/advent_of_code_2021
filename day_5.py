from utils import get_input_file, inputfile_to_array, pretty_print_table

get_input_file(5)

input_list = inputfile_to_array("inputs/input_day_5.txt")

def get_endpoints_from_vent_line(vent_line):
    x_string,y_string = vent_line.split(" -> ")
    x1, y1 = x_string.split(",")
    x2, y2 = y_string.split(",")
    x = (int(x1),int(x2))
    y = (int(y1),int(y2))
    return x,y
def get_covered_coordinates(vent_line, only_use_vertical_and_horizontal_lines=True):
    x,y = get_endpoints_from_vent_line(vent_line)
    point_list = []
    is_vertical = x[0] == x[1]
    is_horizontal = y[0] == y[1]
    if is_vertical:
        for i in range(min(y[0],y[1]),max(y[0],y[1])+1):
            point_list.append((x[0], i))
    elif is_horizontal:
        for i in range(min(x[0],x[1]),max(x[0],x[1])+1):
            point_list.append((i, y[0]))
    else:
        if not only_use_vertical_and_horizontal_lines:
            if x[1] > x[0]:
                x_list = [i for i in range(x[0],x[1]+1)]
            else:
                x_list = [i for i in range(x[0],x[1]-1,-1)]
            if y[1] > y[0]:
                y_list = [i for i in range(y[0],y[1]+1)]
            else:
                y_list = [i for i in range(y[0],y[1]-1,-1)]
            for i in range(len(x_list)):
                point_list.append((x_list[i], y_list[i]))
    return(point_list)

def add_points_to_diagram(diagram, point_list):
    for index, points in enumerate(point_list):
        x,y = points
        diagram[y][x] += 1
    return diagram

def make_diagram(input_list):
    max_x = 0
    max_y = 0
    for vent_line in input_list:
        x,y = get_endpoints_from_vent_line(vent_line)
        if max(x) > max_x:
            max_x = max(x)
        if max(y) > max_y:
            max_y = max(y)
    diagram = [[0 for i in range(max_x+1)] for j in range(max_y+1)]
    return diagram

def fill_diagram_with_info(input_list, only_use_vertical_and_horizontal_lines=True):
    diagram = make_diagram(input_list)
    for vent_line in input_list:
        point_list = get_covered_coordinates(vent_line, only_use_vertical_and_horizontal_lines)
        diagram = add_points_to_diagram(diagram, point_list)
    return diagram

def count_points_where_number_is_larger_than(diagram, relevant_number=2):
    number_of_points = 0
    for row in diagram:
        for point in row:
            if point >= relevant_number:
                number_of_points += 1
    return number_of_points


diagram1 = fill_diagram_with_info(input_list)
diagram2 = fill_diagram_with_info(input_list, False)
print ("First answer: ", count_points_where_number_is_larger_than(diagram1))
print ("Second answer: ", count_points_where_number_is_larger_than(diagram2))