import turtle

def read_coords(file):
    # variable declaration
    data_list = []
    coordinate_tuple = (0, 0)
    coordinates_dictionary = {}
    magnitude_dictionary = {}
    name_dictionary = {}

    # parsing through the file
    for line in file:
        working_string = line
        # stripping the newline and \r
        working_string = working_string.rstrip('\r\n')
        # gathering the data and putting it in a list
        data_list = working_string.split(" ")
        # loading the x and y coordinates
        coordinate_tuple = (data_list[0], data_list[1])
        # adding the coordinates to the dictionary
        coordinates_dictionary.update({data_list[3]: coordinate_tuple})
        # adding the magnitude to the dictionary
        magnitude_dictionary.update({data_list[3]: data_list[4]})
        # holding on to the Henry Draper number
        hd_number = data_list[3]
        # clearing information we no longer need
        del data_list[0:6]
        # if the star has a particular name
        if data_list:
            # making the string easier to manipulate
            name_string = " ".join(data_list)
            data_list = name_string.split(";")
            # if the star has one or two names, the key changes
            if len(data_list) == 1:
                name_dictionary.update({data_list[0]: hd_number})
            elif len(data_list) == 2:
                name_dictionary.update({data_list[1]: None})

    # loading up the dictionaries into a tuple
    coords_tuple = (coordinates_dictionary,
                    magnitude_dictionary, name_dictionary)

    return coords_tuple


def plot_plain_stars(picture_size, coordinates_dict):
    # creating a screensize that is pic_size x pic_size
    # also creating the black background
    turtle.screensize(picture_size, picture_size, "#000")
    # setting the pen color and fill color
    turtle.pencolor("#ffffff")
    turtle.fillcolor("#ffffff")
    # going through the coordinate pairs
    for pair in coordinates_dict:
        # calculating the x and y coordinates to fit on the screen
        x_coordinate = float(coordinates_dict[pair][0]) * picture_size
        y_coordinate = float(coordinates_dict[pair][1]) * picture_size
        # drawing a 2x2 square
        turtle.penup()
        turtle.goto(x_coordinate, y_coordinate)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(2)
        turtle.left(90)
        turtle.forward(2)
        turtle.left(90)
        turtle.forward(2)
        turtle.left(90)
        turtle.forward(2)
        turtle.left(90)
        turtle.end_fill()


def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    # creating a screensize that is pic_size x pic_size
    # also creating the black background
    turtle.screensize(picture_size, picture_size, "#000")
    # setting the pen color and fill color
    turtle.pencolor("#ffffff")
    turtle.fillcolor("#ffffff")
    # going through the coordinate pairs
    # and their magnitudes
    for pair in coordinates_dict:
        # calculating the x and y coordinates to fit on the screen
        x_coordinate = float(coordinates_dict[pair][0]) * picture_size
        y_coordinate = float(coordinates_dict[pair][1]) * picture_size
        # calculating the star size
        star_size = round(10 / (float(magnitudes_dict[pair]) + 2))
        # checking for resizing
        if star_size > 8:
            star_size = 8
        # drawing the appropriately sized square
        turtle.penup()
        turtle.goto(x_coordinate, y_coordinate)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(star_size)
        turtle.left(90)
        turtle.forward(star_size)
        turtle.left(90)
        turtle.forward(star_size)
        turtle.left(90)
        turtle.forward(star_size)
        turtle.left(90)
        turtle.end_fill()


# DRIVER
turtle.tracer(10)  # speeding the tracer up

# opening the txt file
working_file = open("stars.txt", "r")

# getting the data
tuple = read_coords(working_file)

# plotting functions
plot_plain_stars(400, tuple[0])

plot_by_magnitude(400, tuple[0], tuple[1])
