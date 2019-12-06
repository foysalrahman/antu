import numpy as np
import turtle
def print_headers(headers):
    heads = headers.split(",")
    print("*" * 50)
    print("%-10s %-25s %-12s" % (heads[0], heads[1], heads[2][:-1]))
    print("*" * 50)
    return


def read_details():
    infile = open("movie_a.txt", "r")
    lines = infile.readlines()
    infile.close()
    print_headers(lines[0])
    genres = []
    for line in lines:
        if line == lines[0]:
            continue
        details = line.split(",")
        genre = details[1]
        genres.append(genre)
        print("%-10s %-25s %-12s" % (details[0], genre, details[2]))
    return genres
#genres = []
genresReturned = read_details()
#genreList = ["War", "Spy", "Action"]
genreList = ["Roamnce", "Romcom", "Action", "War", "Spy", "si-fi", "horror", "history", "fantacy", "Animated"]
for genre in genreList:
    print(genre, genresReturned.count(genre))
    a=(genre, genresReturned.count(genre))
#    f = open('output.txt', 'a')
#    f.write(str(a))
#    f.close()
if a == 0:
    print("\nYour database is empty. Please add few movies first to see the report.")
else:
    maxHeight = max(read_details.genres)     # starts drawing the graph
    maxLength = len(read_details.genres)
    border = 10

    wn = turtle.Screen()  # Set up the window and its attributes
    wn.setworldcoordinates(0 - border, 0 - border, 40 * maxLength + border, maxHeight + border)
    wn.bgcolor("lightblue")

    tess = turtle.Turtle()  # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)

    for i in range(len(genreList)):
        toWrite = genreList[i]
        value = read_details.genres[i]
        tess.begin_fill()  # start filling this shape
        tess.left(90)
        tess.forward(value)
        tess.right(90)
        tess.forward(2)
        tess.write(toWrite)
        tess.forward(38)
        tess.right(90)
        tess.forward(value)
        tess.left(90)
        tess.end_fill()
        wn.exitonclick()
        turtle.TurtleScreen._RUNNING = True