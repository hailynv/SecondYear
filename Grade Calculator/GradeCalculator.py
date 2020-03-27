from __future__ import division

def average(total_score, points_possible):
    average = (float)(total_score / points_possible)
    return average


def letter_grade(percent):
    letter = "Z"
    if percent >= .9:
        letter = "A"
    elif percent >= .8:
        letter = "B"
    elif percent >= .7:
        letter = "C"
    elif percent >= .6:
        letter = "D"
    else:
        letter = "F"

    return letter


def average_weighted(points_earned, points_possible, weight):
    total_score = (float)(points_earned / points_possible)
    weighted_score = total_score * float(weight)
    return weighted_score


def read_grade_data(filehandle):
    # creating a string to work with
    working_string = ""
    # creating a list to hold the information
    information_list = []

    # adding the different categories to the information list
    for line in filehandle:
        working_string = line
        # stripping the end parts
        working_string = working_string.rstrip('\r\n')
        # adding the information to the list
        information_list.append(working_string)

    return information_list


def write_grade_report(filehandle, data):
    # creating a working string
    working_string = ""
    # creating a string to hold the catgeory
    subject = ""
    # the weight of each category
    weight = ""
    # total points earned
    class_points_earned = 0
    # total points possible in the category
    total_class_points = 0

    # data is the information list
    # EXTRACTING INFORMATION PART
    for category in data:
        # creating a list of scores
        scores = []
        # points earned for the assignment
        points_earned = 0
        # points possible for the assignment
        points_possible = 0
        working_string = category
        # replacing the commas with spaces
        working_string = working_string.replace(",", " ")
        # splitting the string to seperate the information
        sublist = working_string.split(" ")

        # removing empty values from the sublist
        for item in sublist:
            if item == "":
                sublist.remove(item)

        # getting the subject
        subject = sublist[0]

        # getting the weight
        weight = sublist[1]

        # removing the % sign
        weight = weight.split("%")

        # converting the weight to a percentage
        weight = "." + weight[0]

        # adding the scores to the score list
        for score in sublist[2:]:
            scores.append(score)

        # adding up points
        for score in scores:
            # seperating the points earned vs points possible
            temp = score.split("/")
            # adding the points earned for the assignment
            points_earned += int(temp[0])
            # adding the points possible for the assignment
            points_possible += int(temp[1])

            # adding the total points earned
            class_points_earned += int(temp[0])
            # adding the total points possible
            total_class_points += int(temp[1])

        # calculating the average score
        average_score = average(points_earned, points_possible)
        # calculating the letter grade
        actual_letter_grade = letter_grade(average_score)
        # calculating the grade contribution
        grade_contribution = average_weighted(
            points_earned, points_possible, weight)

        # WRITING TO THE HTML FILE PART
        # writing the heading part
        filehandle.write("<h1>{} Statistics ({}.0)</h1>".format(
            subject, weight.strip(".")))
        # creating an unordered list
        filehandle.write("<ul>")
        # writing the average
        filehandle.write("<li><b>Average:</b> {:.2f}</li>".format(
            average_score))
        # writing the letter grade
        filehandle.write("<li><b>Letter Grade:</b> {}</li>".format(
            actual_letter_grade))
        # writing the overall grade contribution
        filehandle.write(
            "<li><b>Overall Grade Contribution:</b> {:.3f}</li>".format(
                grade_contribution))
        # closing the unordered list
        filehandle.write("</ul>")

    # cumulative grade and letter using total points earned and total
    # points possible
    cumulative_grade = average(class_points_earned, total_class_points)
    cumulative_letter = letter_grade(cumulative_grade)

    # writing the cumulative grade part
    filehandle.write("<h1>Cumulative Grade</h1>")
    filehandle.write("<ul>")
    filehandle.write("<li><b>Average:</b> {:.2f}</li>".format(
        cumulative_grade))
    filehandle.write("<li><b>Letter Grade:</b> {}</li>".format(
        cumulative_letter))
    filehandle.write("</ul>")

# DRIVER PART


# opening the input file
working_file = open("lab8input.txt", "r")
# opening / creating the html file
written_file = open("lab8output.html", "w+")

# calling read_grade_data to load the information to a list
data = read_grade_data(working_file)

# writing the html file
write_grade_report(written_file, data)

# closing the files
written_file.close
working_file.close
