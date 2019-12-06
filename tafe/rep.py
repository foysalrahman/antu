import turtle
genreList = ['Romance', 'Rom-com', 'War', 'Spy', 'Si-fi', 'Horror', 'Historic', 'Fantasy', 'Animated']
sx = []  # graph coordinate list
print("%-80s %-20s %-2s" % ("Name", "Genre", "Rating"))     # starts printing report
for i in range(0, 108):
    print("=", end='')
    print('')
    with open("movieDB.txt") as readfile:
        for lines in readfile:
            items = lines.rstrip().split(',')
            print("%-80s %-20s %6s" % (items[0], items[1], items[2]))
    for i in range(0, 108):
        print("=", end='')      # ends printing report
    for i in range(len(genreList)):     # counts number of movies each genre and puts in the coordinate list
        with open("movieDB.txt") as readfile:
            numberOfLines = 0
            count = 0
            for lines in readfile:
                numberOfLines += 1
                items = lines.rstrip().split(',')
                if genreList[i] in items:
                    count += 1
            sx.append(count)
        if numberOfLines == 0:
            print("\nYour database is empty. Please add few movies first to see the report.")
        else:
            maxHeight = max(sx)     # starts drawing the graph
            maxLength = len(sx)
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
                value = sx[i]
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
