import turtle

working_file = open("stars.txt", "r")

data_list = []
coordinate_tuple = (0, 0)
coordinates_dictionary = {}
magnitude_dictionary = {}
name_dictionary = {}


for line in working_file:
    working_string = line
    working_string = working_string.rstrip('\r\n')
    data_list = working_string.split(" ")
    coordinate_tuple = (data_list[0], data_list[1])
    coordinates_dictionary.update({data_list[3]: coordinate_tuple})
    magnitude_dictionary.update({data_list[3]: data_list[4]})
    hd_number = data_list[3]
    del data_list[0:6]
    if data_list:
        name_string = " ".join(data_list)
        data_list = name_string.split(";")
        if len(data_list) == 1:
            name_dictionary.update({data_list[0]: hd_number})
        elif len(data_list) == 2:
            name_dictionary.update({data_list[1]: hd_number})

turtle.bgcolor("#000000")
turtle.pencolor("#ffffff")
turtle.screensize(500, 500)
turtle.circle(300)
