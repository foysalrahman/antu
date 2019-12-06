import turtle

open("movieDB.txt", "a+").close()       # creates the empty database file in case its not present
selection = input("###############################\n#  Welcome to Movie database  #\n###############################. "
                  "\n0. Exit program \n1. Enter details \n2. Reports \nPlease enter your selection number: ")
genreList = ['Romance', 'Rom-com', 'War', 'Spy', 'Si-fi', 'Horror', 'Historic', 'Fantasy', 'Animated']      # can add
# new genres if needed
while selection != "0":         # starts here
    if selection == "1":
        outfile = open("movieDB.txt", "a+")
        sentinel = "y"  # sentinel for movie input loop
        while sentinel == "y":
            name = input("Movie name: ")
            print("Please select the genre.")
            for i in range(0, len(genreList)):      # generates the genre list
                print("{}. ".format(i) + genreList[i])
            genre = input("Enter your selection number: ")
            while True:         # validate the genre selection input is valid and within range
                if genre.isdigit() and int(genre) in [n for n in range(len(genreList))]:
                    break
                else:
                    genre = input("Enter your selection number: ")
            rating = input("Rate the movie from 1 to 10: ")     # validate the rating selection input is valid and
            # within range
            while True:
                if rating.isdigit() and int(rating) in [m for m in range(1, 11)]:
                    break
                else:
                    rating = input("Rate the movie from 1 to 10: ")
            outfile.write(name+','+genreList[int(genre)]+','+rating+'\n')       # writes to file
            sentinel = input("Do you want to add more? y/n : ")
        outfile.close()
    elif selection == "2":
        selection = input("#############\n#  Reports  #\n############# \n0. Return to previous menu \n1. List all "
                          "movies and draw bar graph \nPlease enter your selection number: ")
        if selection == "1":
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
    selection = input("\n###############################\n#  Welcome to Movie database  "
                      "#\n###############################. \n0. Exit program \n1. Enter details \n2. Reports \nPlease "
                      "enter your selection number: ")
print('Goodbye!')
