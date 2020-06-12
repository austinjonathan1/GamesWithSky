import random

# KUN (welcome() & easy()):
def welcome(): #ask the user's name and introduce the game
    print("""
 ----------------------------------------------------------
|                                                          |
|                                                          |
|                     GAMES WITH SKY                       |
|                                                          |
|                                                          |
 ----------------------------------------------------------""")
    name = input("Hello! My name is Sky, what's yours?\nName: ") #Sky, short for Skynet
    print("Hi " + str(name) + """.
I want to play a game.
One of us is going to think of a number within a known range and the other will try to guess it.
But don't worry. We'll tell each other whether the guess is too low or high. Let's see who can keep their guesses the lowest. Let's have a go!
Press enter to continue...
""", end="")
    input()
    return(name)

def easy(): #easy mode
    g = 0 #number of guesses
    G = [] #guesses
    a = "Would you like to choose the number range (Default Range: 1 - 100)?\n"
    b = "(y/n/x): "
    c = ["y", "n", "x"]
    option = check1(a, b, c) #offer the user option to choose range or default to 1 - 100
    if option == "x":
        return(g, G, False, True)
    elif option == "y": #ask the user to input the number range
        temp = check3() # [5, 10]
        if (temp == "x"):
            return(g, G, False, True)
        num1 = temp[0]
        num2 = temp[1]
        n1 = random.randint(num1, num2)
        #print("Answer:", n1) #REMOVED IN FINAL VERSION (only for testing)
    elif option == "n":
        n2 = random.randint(1,100)
        #print("Answer:", n2) #REMOVED IN FINAL VERSION (only for testing)
    done = False
    while not done: #if the guess is wrong, the loop keeps running
        a = ""
        b = "Take a guess: "
        guess = check2(a, b)
        if (guess == "x"):
            return(g, G, False, True)
        g+=1
        G.append(guess)
        if option == "y":
            if guess < n1:
                print("Your guess is too low!")
            elif guess > n1:
                print("Your guess is too high!")
            else:
                done = True #end the loop
        elif option == "n":
            if guess < n2:
                print("Your guess is too low!")
            elif guess > n2:
                print("Your guess is too high!")
            else:
                done = True #end the loop
    print("Congrats! You guessed it!")
    return(g, G, True, True)

# GUADALUPE (difficult() & MAIN):
def difficult(): #difficult mode is when user has a limited number of guesses
    guessCount = 0 #keeps track of how many guesses
    guessList = [] #list of guesses
    a = """Would you like to choose the number range (Default Range: 1 - 100)? Or enter "x" to exit.\n"""
    b = "(y/n/x): "
    c = ["y", "n", "x"]
    answer = check1(a, b, c) #setting the range for the number to guess
    if answer == "y": #user-set range
        temp = check3()
        if (temp == "x"):
            return(guessCount, guessList, False, True)
        num1 = temp[0]
        num2 = temp[1]
    elif answer == "n": #default range
        num1 = 1
        num2 = 100
    else:
        return(guessCount, guessList, False, True)
    guessNum = random.randint(num1, num2) #selecting the number to guess
    #print("Answer:", guessNum) #REMOVED IN FINAL VERSION (only for testing)
    while (guessCount < 5):
        a = ""
        b = """Take a guess (or enter "x" to exit): """
        guessUser = check2(a, b)
        if (guessUser == "x"):
            return(guessCount, guessList, False, True)
        guessCount = guessCount+1
        guessList.append(guessUser)
        if (guessUser == guessNum):
            print("Congrats! You guessed it!")
            return(guessCount, guessList, True, True)
        elif (guessUser > guessNum):
            print("Your guess is too high!")
        elif (guessUser < guessNum):
            print("Your guess is too low!")
    print("I'm sorry but you are out of guesses. :( The number I was thinking of was " + str(guessNum) + ".")
    return(guessCount, guessList, False, True)

# JONATHAN (switch(), end(), & check()):
def switch():
    g = 0 #number of guesses
    G = [] #guesses
    a = """Would you like to choose the number range (Default Range: 1 - 100)? Or enter "x" to exit.\n"""
    b = "(y/n/x): "
    c = ["y", "n", "x"]
    u = check1(a, b, c) #setting the range for the number to guess
    if (u == "y"):
        t = check3() #temporary variable
        if (t == "x"):
            return(g, G, False, True) #user quits
        l = t[0] #lower bound
        h = t[1] #upper bound
    elif (u == "n"):
        l = 1
        h = 100
    else:
        return(g, G, False, True)
    p = [] #possible numbers
    while (l <= h):
        p.append(l)
        l+=1
    x = 0 #beginning index of the scope
    y = len(p) - 1 #ending index of the scope
    while (x <= y):
        m = int((x + y)/2) #middle index of the scope
        print("Is it " + str(p[m]) + '? You may enter "x" to exit.')
        a = ""
        b = "(y/n/x): "
        c = ["y", "n", "x"]
        f = check1(a, b, c) #user feedback
        if (f == "x"):
            return(g, G, False, True) #user quits
        g+=1
        G.append(p[m])
        if (f == "y"):
            print("Yay! I guessed it!")
            return(g, G, True, True) #sky won but player cheated
        else:
            a = """Aw darn! Was I too low or high? You may enter "x" to exit.\n"""
            b = "(l/h/x): "
            c = ["l", "h", "x"]
            f = check1(a, b, c) #user feedback
            if (f == "x"):
                return(g, G, False, True) #user quits
            elif (f == "h"):
                y = m - 1
            else:
                x = m + 1
    print("You're a cheater. I don't like cheaters. From what you told me, the answer must've been " + str(p[m]) + "!")
    return(g, G, True, False) #sky won but player cheated
def end(u, g, G, w, z): #end sequence
    R = "n" #by default assume user does not want to play again
    if (w):
        print(g,"guess(es) were made and the guess(es) were/was: ", end="") #gives user data on game
        for i in range(g):
            print(G[i], end="") #prints each guess out
            if not(i == g - 1):
                print (", ", end="")
            else:
                print(".\n", end="")
    if (not(G == 0)):
        if (z):
            a = "Exiting Game...\n\nWould you like to play again?\n" #offers user option to play again
            b = "(y/n): "
            c = ["y", "n"]
            R = check1(a, b, c)
        else:
            print("Exiting Game...\n\nI don't want to play with you again. Goodbye. >:(\nExiting Program...") #if they are a cheater, exit program
            return(False)
    if (R == "y"):
        print("\nWhoohoo! Here we go again!") #repeat the program
        return(True)
    else:
        print("\nGoodbye, til' next time... :)\nExiting Program...") #exit program
        return(False)
def check1(a, b, c): #checks for given options [a = Initial Message with "\n" at end (displayed once), b = Input Message (repeated if input is invalid), c = valid inputs in list form with each element defined as a string]
    print(a, end="")
    f = True #infinite loop until a valid input is given
    while (f):
        u = str(input(b))
        for i in c: #checks if it is a given option
            if (u == i):
                return(u)
        print("ERROR: unrecognized input")
def check2(a, b): #checks for an integer [a = Initial Message with "\n" at end (displayed once), b = Input Message (repeated if input is invalid)]
    print(a, end="")
    f = True #infinite loop until a valid input is given
    while (f):
        j = 0 #number of integer characters
        u = str(input(b))
        if (not(len(u) < 1)):
            if (u == "x"):
                return(u)
            if (u[0] == "-"):
                t = u[1:] #removes valid integer's negative signs
            else:
                t = u #temporary variable
            for i in range(len(t)): #checks if it is an integer
                if (47 < ord(t[i]) < 58):
                    j+=1
                else:
                    i = len(t)
            if (j == len(t)):
                return(int(u))
        print("ERROR: unrecognized input")
def check3(): #checks for a valid range
    f = True #infinite loop until a valid input is given
    while (f):
        a = """Please enter an integer for the beginning of the range or "x" to exit.\n"""
        b = "Lower Bound: "
        l = check2(a, b) #lower bound
        if (l == "x"):
            return(l)
        a = """Please enter an integer for the end of the range or "x" to exit.\n"""
        b = "Upper Bound: "
        h = check2(a, b) #upper bound
        if (h == "x"):
            return(h)
        if (l <= h): #checks if it is a valid range
            return(l, h)
        else:
            print("ERROR: lower bound greater than upper bound")
# MAIN
n = welcome() #player name
r = True #repeat variable
while (r):
    u = n #player name (re)assigned to username
    a = """Choose an option by typing in the corresponding character.
1: Easy (unlimited number of guesses)
2: Difficult (only five guesses)
3: Switch (Sky guesses your number)
x: Exit
"""
    b = "Gamemode: "
    c = ["1", "2", "3", "x"]
    m = check1(a, b, c) #function allows the user to choose a difficulty mode and routes accordingly, or quits game 
    if m == "1":
        print("You have chosen: EASY MODE")
        t = easy()
    elif m == "2":
        print("You have chosen: DIFFICULT MODE")
        t = difficult()
    elif m == "3":
        print("You have chosen: SWITCH MODE")
        t = switch()
        u = "Sky" #sky's name assigned to username
    else:
        t = [0, 0, False, True] #skips user data feedback and offer to play again in end sequence
    r = end(u, t[0], t[1], t[2], t[3])
