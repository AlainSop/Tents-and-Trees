#unused function
def wannaQuit():
    x = input("You have two choices. Press c to continue your instantiation, q to quit :\n")
    while x.lower() != "c" and x.lower() != "q" :
        x = input("Please press c or q")

    if x == "q":
        exit(1)
    if x == "c":
        return

def calculArbresMax(cote):
    if cote%2 == 1:         #if the size of the side of the grid is odd
        cote += 1           #then we add 1 to it
    return (cote//2)**2

def entreeAbscisse(cote,nbArbres):
    print("Now, you will have to enter the number of tents that you want for each column.\n"
          "Remember that for the instance to have a chance to be satisfiable, the sum of these numbers have to be equal to " + str(nbArbres) + ", the number of trees.")
    liste_abscisse = []     #list of number representing the number of tents of each column

    #this loop takes an input from the user, representing the number of tents, for every column (this input has to be a strictly positive integer)
    for i in range(cote):
        val = int(input("Column " + str(i + 1) + " : "))       #takes the input
        while val<0 and val<cote:        #checks if the input is a strictly postive integer, and while not, takes a new input
            val = int(input("Enter a positive integer in [0," + str(cote) + "] : "))
        liste_abscisse.append(val)      #adds the correct input to the list

    return liste_abscisse

def entreeOrdonnee(cote,nbArbres):
    print("Now, you will have to enter the number of tents that you want for each row.\n"
          "Remember that for the instance to have a chance to be satisfiable, the sum of these numbers have to be equal to " + str(nbArbres) + ", the number of trees.")
    liste_ordonnee = []     #list of number representing the number of tents of each row

    #this loop takes an input from the user, representing the number of tents, for every row (this input has to be a strictly positive integer)
    for i in range(cote):
        val = int(input("Row " + str(i + 1) + " : "))       #takes the input
        while val<0:        #checks if the input is a strictly postive integer, and while not, takes a new input
            val = int(input("Enter a positive integer in [0," + str(cote) + "] : "))
        liste_ordonnee.append(val)      #adds the correct input to the list

    return liste_ordonnee

def entreeGrille(cote,nbArbres):
    print("Now, you will have to enter the grid.\nRemember that 0 stands for 'there is no tree' and 1 stands for 'there is a tree'.\n"
          "Remember that you wanted " + str(nbArbres) + " trees to be in the grid.")
    grille = {}     #dictionnary representing the grid : keys are tups corresponding to coordinates, and values are 0 or 1

    #this loop takes an input from the user, representing the presence or absence of a tree, for all grid cells
    for i in range(cote):
        for j in range(cote):
            tup = (j,i)
            val = int(input("(" + str(j) + "," + str(i) + ") : "))       #takes the input
            while val!=0 and val!=1:        #checks if the input is 0 or 1, and while not, takes a new input
                val = int(input("Enter 0 or 1 : "))
            grille[tup] = val       #adds the correct input to the dict

    return grille

def ecritureFichier(cote,nbArbres,liste_abscisse,liste_ordonnee,grille,nomFichier):
    f = open(nomFichier,"w")            #opens the file where we want to have the instance of the problem chosen by the user
    f.write(str(cote) + "\n")           #writes, in the file, the size of the side of the grid
    f.write(str(nbArbres) + "\n")       #writes, in the file, the number of trees in the grid

    #this loop writes, in the file, all the values corresponding to the number of tents of each column
    for val_abs in liste_abscisse:
        f.write(str(val_abs) + " ")
    f.write("\n")

    #this loop writes, in the file, all the values corresponding to the number of tents of each row
    for val_ord in liste_ordonnee:
        f.write(str(val_ord) + " ")
    f.write("\n")

    #this loop writes, in the file, all the values of the grid, line by line
    for i in range(cote):
        for j in range(cote):
            tup = (i,j)
            f.write(str(grille[tup]) + " ")
        f.write("\n")

    f.close()       #closes the file

def affichageGrille(cote, liste_abscisse, liste_ordonnee, grille):
    print("Voici la grille que vous avez entrée :\n\n")
    string_abscisse = ""

    #this loop adds all the values corresponding to the number of tents of each column to a string
    for elem in liste_abscisse:
        string_abscisse = string_abscisse + str(elem) + " "

    print(string_abscisse + "\n")       #prints the final string with all the values

    #this loop creates, for each row, a string that will contain all the values of the grid on this row AND the number of trees of this row
    for i in range(cote):
        string = ""     #creates an empty string

        # this loop adds all the values corresponding to the number of tents of each row to a string
        for j in range(cote):
            string = string + str(grille[j,i]) + " "
        string = string + "   " + str(liste_ordonnee[i]) + ""   #adds the number of trees of this row to the string

        print(string)




def EntreeEtVerif(nomFichier):
    print("You chose to enter your own instance of the problem.\nLet's do this together to make sure that there is no error.\n")

    #input of the dimension of the grid
    cote = int(input("Enter the dimension of the grid (enter only one number) : "))
    while cote<1:   #while the side of the grid is not a strictly positive integer, takes a new input
        cote = int(input("Enter a positive integer : "))

    nbArbresMax = calculArbresMax(cote)
    #input of the number of trees in the grid
    nbArbres = int(input("Enter the number of trees that you want on the grid. This number has to be in [0," + str(nbArbresMax) + "] : "))
    while nbArbres<0 or nbArbres>nbArbresMax:
        #while the number of trees in the grid is not a strictly positive integer or is strictly greater than the possible maximum, takes a new input
        nbArbres = int(input("Enter an integer between 0 and " + str(nbArbresMax) + " : "))

    #input of the number of trees of each column
    liste_abscisse = entreeAbscisse(cote,nbArbres)
    #input of the number of trees of each row
    liste_ordonnee = entreeOrdonnee(cote,nbArbres)

    #input of the position of the trees in the grid
    grille = entreeGrille(cote,nbArbres)

    #writes all the inputs in a file
    ecritureFichier(cote, nbArbres, liste_abscisse, liste_ordonnee, grille, nomFichier)
    #writes all the inputs in the system console in an understandable way
    affichageGrille(cote, liste_abscisse, liste_ordonnee, grille)

    return nomFichier

