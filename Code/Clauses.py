
from itertools import combinations

def isANumber(element):
    #if the element is a character corresponding to an integer in [0,9], returns True, otherwise returns False
    if element!="0" and element!="1" and element!="2" and element!="3" and element!="4" and element!="5" and element!="6" and element!="7" and element!="8" and element!="9":
        return False
    return True

def isCorrect(nomFichier):
    f = open(nomFichier,"r")                        #opens the file where the input of the instance of the problem is of the defined format

    #verification of the size of the grid
    cote = 0
    ligne_cote = f.readline()
    liste_cote = ligne_cote.split()
    if len(liste_cote) != 1:                        #if there is not exactly one element for the size of the grid
        print("\nERROR : The size of the grid is incorrect (it must be ONE strictly positive integer, not " + str(len(liste_cote)) + ").\n")
        return False                                #returns the boolean False
    val = liste_cote[0]                             #val is the string containing the size of the grid written in the file
    for index in range(len(val)):                   #for each character of the string
        if not isANumber(val[index]):               #if the character is not an integer in [0,9]
            print("\nERROR : The size of the grid is incorrect (it must be a strictly positive integer).\n")
            return False                            #returns the boolean False
        cote = 10*cote + int(val[index])            #computes the value of the size of the grid
    if cote == 0:                                   #if the size of the grid is 0
        print("\nERROR : The size of the grid must be a STRICTLY positive integer (not 0).\n")
        return False                                #returns the boolean False

    # verification of the total number of trees in the grid
    nbArbres = 0
    ligne_nbArbres = f.readline()
    liste_nbArbres = ligne_nbArbres.split()
    if len(liste_nbArbres) != 1:                    #if there is not exactly one element for the size of the grid
        print("\nERROR : The number of trees in the grid is incorrect (it must be ONE strictly positive integer, not " + str(len(liste_nbArbres)) + ").\n")
        return False                                #returns the boolean False
    val = liste_nbArbres[0]                         #val is the string containing the number of trees in the grid written in the file
    for index in range(len(val)):                   #for each character of the string
        if not isANumber(val[index]):               #if the character is not an integer in [0,9]
            print("\nERROR : The number of trees in the grid is incorrect (it must be a strictly positive integer).\n")
            return False                            #returns the boolean False
        nbArbres = 10 * nbArbres + int(val[index])  #computes the value of the number of trees in the grid
    if nbArbres == 0:                               #if the number of trees in the grid is 0
        print("\nERROR : The number of trees in the grid must be a strictly positive integer (not 0).\n")
        return False                                #returns the boolean False

    #verification of the number of trees of each column
    ligne_abscisse = f.readline()
    liste_abscisse = ligne_abscisse.split()
    sum = 0                                         #initialises the sum at 0
    for elem in liste_abscisse:                     #for each element of the line
        for index in range(len(elem)):              #for each character of the element
            if not isANumber(elem[index]):          #if the character is not an integer in [0,9]
                print("\nERROR : The line representing the number of trees of each column is incorrect (it must be only positive integers).\n")
                return False                        #returns the boolean False
            sum += int(elem)                        #adds the element to the sum

    if len(liste_abscisse)!=cote:                   #if the number of elements of the line is different than the size of the grid
        print("\nERROR : The line representing the number of trees of each column is incorrect (there must be " + str(cote) + " elements, not " + str(len(liste_abscisse)) + ").\n")
        return False                                #returns the boolean False

    if sum!=nbArbres:                               #if the sum of elements of the line is different than the total number of trees
        print("\nThe sum of the number of trees in each column (" + str(sum) + ") is different than the total number of trees (" + str(nbArbres) + ").\nTherefore, the grid is unsatisfiable.\n")
        return False                                #returns the boolean False

    # verification of the number of trees of each column
    ligne_ordonnee = f.readline()
    liste_ordonnee = ligne_ordonnee.split()
    sum = 0                                         #initialises the sum at 0
    for elem in liste_ordonnee:                     #for each element of the line
        for index in range(len(elem)):              #for each character of the element
            if not isANumber(elem[index]):          #if the character is not an integer in [0,9]
                print("\nERROR : The line representing the number of trees of each row is incorrect (it must be only positive integers).\n")
                return False                        #returns the boolean False
            sum += int(elem)                        #adds the element to the sum

    if len(liste_ordonnee) != cote:                 #if the number of elements of the line is different than the size of the grid
        print("\nERROR : The line representing the number of trees of each row is incorrect (there must be " + str(cote) + " elements, not " + str(len(liste_ordonnee)) + ").\n")
        return False                                #returns the boolean False

    if sum!=nbArbres:                               #if the sum of elements of the line is different than the total number of trees
        print("\nThe sum of the number of trees in each row (" + str(sum) + ") is different than the total number of trees (" + str(nbArbres) + ").\nTherefore, the grid is unsatisfiable.\n")
        return False

    #verification of the values of the grid
    for i in range(cote):                           #for each line of the grid
        ligne_grille = f.readline()
        liste_grille = ligne_grille.split()
        for elem in liste_grille:                   #for each element of the line
            if elem != "0" and elem != "1":         #if the element is not 0 or 1
                print("\nError at the line " + str(i+1) + " of the grid. Every element of the grid should be a 0 or a 1.\n")
                return False                        #returns the boolean False

        if len(liste_grille) != cote :              #if the number of elements of the line is different than the size of the grid
            print("\nERROR : There is the wrong number of elements in the line " + str(i+1) + " of the grid (there must be " + str(cote) + " elements, not " + str(len(liste_grille)) + ").\n")
            return False                            #returns the boolean False

    return True                                     #returns the boolean True

def lireFichierEnonce(nomFichier): #WORKS

    f = open(nomFichier,"r")      #opens the file where the input of the instance of the problem is of the defined format

    #retrieval of the size of the side of the grid
    ligne = f.readline()
    cote = int(ligne)

    #retrieval of the number of trees in the grid
    ligne = f.readline()
    nbArbres = int(ligne)

    #retrieval of the number of trees of each column
    ligne_abscisse = f.readline()
    liste_abscisse = ligne_abscisse.split()

    #retrieval of the number of trees of each column
    ligne_ordonnee = f.readline()
    liste_ordonnee = ligne_ordonnee.split()

    #retrieval of the values of the grid (position of the trees)
    grille_arbres = {}
    for u in range(cote):
        ligne_grille = f.readline()
        liste_grille = ligne_grille.split()
        for v in range(cote):
            grille_arbres[v,u] = liste_grille[v]

    f.close()

    return cote,nbArbres, liste_abscisse,liste_ordonnee,grille_arbres

def regle1(cote,grille_arbres,liste_clauses): #WORKS
    for i in range(cote):
        for j in range(cote):
            if grille_arbres[i,j] == "1":       #if the cell contains a tree
                dico = {}                       #creates an empty dictionnary (representing an empty clause)
                dico[i,j] = False               #adds the equivalent of "there is no tent in this grid cell" to the clause
                liste_clauses.append(dico)      #adds the clause to the set of clauses


def regle2(cote,grille_arbres,liste_clauses): #WORKS
    for i in range(cote):
        for j in range(cote):
            if grille_arbres[i,j] == "1":       #if the cell contains a tree
                dico = {}                       #creates an empty dictionnary (representing an empty clause)

                if i>0:                         #if the cell of coordinates (j-1,i) is in the grid,
                    dico[i-1,j] = True          #then we add to the clause a value True for this cell
                    regle3(cote,i-1,j,liste_clauses)

                if j>0:                         #if the cell of coordinates (j,i-1) is in the grid,
                    dico[i,j-1] = True          #then we add to the clause a value True for this cell
                    regle3(cote,i,j-1,liste_clauses)

                if i<cote-1:                    #if the cell of coordinates (j+1,i) is in the grid,
                    dico[i+1,j] = True          #then we add to the clause a value True for this cell
                    regle3(cote,i+1,j,liste_clauses)

                if j<cote-1:                    #if the cell of coordinates (j,i+1) is in the grid,
                    dico[i,j+1] = True          #then we add to the clause a value True for this cell
                    regle3(cote,i,j+1,liste_clauses)

                liste_clauses.append(dico)      #adds the clause to the set of clauses




def creationTup(compteur,i,j,cote): #WORKS
    dico = {}                                   #creates an empty dictionnary (representing an empty clause)
    dico[i,j] = False                           #adds the equivalent of "there is no tent in this grid cell" to the clause

    #the value of "compteur", which is in [0,7] represents the eight grid cells around the cell of coordinates (i,j)

    if compteur == 0 and j>0 and i>0:           #if the cell of coordinates (i-1,j-1) is in the grid,
        dico[i - 1,j - 1] = False               #then adds to the clause a value False for this cell

    if compteur == 1 and j>0:                   #if the cell of coordinates (i,j-1) is in the grid,
        dico[i, j - 1] = False                  #then adds to the clause a value False for this cell

    if compteur == 2 and j>0 and i<cote-1:      #if the cell of coordinates (i+1,j-1) is in the grid,
        dico[i+1,j - 1] = False                 #then adds to the clause a value False for this cell

    if compteur == 3 and i>0:                   #if the cell of coordinates (i-1,j) is in the grid,
        dico[i - 1,j] = False                   #then adds to the clause a value False for this cell

    if compteur == 4 and i<cote-1:              #if the cell of coordinates (i+1,j) is in the grid,
        dico[i + 1,j] = False                   #then adds to the clause a value False for this cell

    if compteur == 5 and j<cote-1 and i>0:      #if the cell of coordinates (i-1,j+1) is in the grid,
        dico[i - 1,j + 1] = False               #then adds to the clause a value False for this cell

    if compteur == 6 and j<cote-1:              #if the cell of coordinates (i,j+1) is in the grid,
        dico[i,j + 1] = False                   #then adds to the clause a value False for this cell

    if compteur == 7 and j<cote-1 and i<cote-1: #if the cell of coordinates (i+1,j+1) is in the grid,
        dico[i + 1,j + 1] = False               #then adds to the clause a value False for this cell

    return dico                                 #returns the created dictionnary


def regle3(cote,i,j,liste_clauses): #WORKS
    #for all the cells around each grid cell,
    for compteur in range(8):                           #8 corresponds to the maximal number of cells around a cell of coordinates (i,j)
        dico3 = creationTup(compteur,i,j,cote)          #creates a clause by calling the function above
        if len(dico3)>1:                                #if the size of this clause is strictly greater than 1
            liste_clauses.append(dico3)                 #then adds this clause to the set of clauses


def regle4abscisse(cote,ligne_abscisse,liste_clauses): #FALSE

    for i in range(int(cote)):                                  #for each column
        if ligne_abscisse[i] == "0":                            #if there no tree in the column,
            for j in range(cote):                               #then for each cell of the column,
                dico0 = {}                                      #creates an empty dictionnary (representing an empty clause)
                dico0[i,j] = False                              #then adds to the clause a value False for this cell
                liste_clauses.append(dico0)                     #finally adds the clause to the set of clauses

        else:                                                   #if there is at least one tree in the column,

            #creates a list containing all the integers in [0,cote-1]
            liste_comb = []
            for nb in range(cote):
                liste_comb.append(nb)

            val_pos = int(cote) - int(ligne_abscisse[i]) + 1    #corresponds to y-x+1 (see report)
            val_neg = int(ligne_abscisse[i]) + 1                #corresponds to x+1 (see report)

            comb_pos = []                                       #creates an empty list for the positive literals
            comb_neg = []                                       #creates an empty list for the negative literals

            for elem_pos in combinations(liste_comb, val_pos):  #for each set of numbers in ((val_pos) among (size of the grid))
                comb_pos.append(elem_pos)                       #adds in comb_pos the values of the set of numbers

            for elem_neg in combinations(liste_comb, val_neg):  #for each set of numbers in ((val_neg) among (size of the grid))
                comb_neg.append(elem_neg)                       #adds in comb_neg the values of the set of numbers

            dico = {}                                           #initialises an empty dictionnary that will contain the clauses

            for comb in comb_pos:                               #for each element in comb_pos (which are set of numbers)
                for index in range(len(comb)):                  #for each index of the element
                    j = comb[index]                             #saves in j the value of the element at the index
                    dico[i, j] = True                           #adds a value True for the tup (i,j) in the dictionnary
                liste_clauses.append(dico)                      #adds the dictionnary (representing a clause) to the set of clauses
                dico = {}                                       #empties the dictionnary

            for comb in comb_neg:                               #for each set of numbers in comb_neg
                for index in range(len(comb)):                  #for each index of the element
                    j = comb[index]                             #saves in j the value of the element at the index
                    dico[i, j] = False                          #adds a value False for the tup (i,j) in the dictionnary
                liste_clauses.append(dico)                      #adds the dictionnary (representing a clause) to the set of clauses
                dico = {}                                       #empties the dictionnary

def regle4ordonnee(cote,ligne_ordonnee,liste_clauses): #FALSE

    for i in range(cote):                                       #for each column
        if ligne_ordonnee[i] == "0":                            #if there no tree in the column,
            for j in range(cote):                               #then for each cell of the column,
                dico0 = {}                                      #creates an empty dictionnary (representing an empty clause)
                dico0[j,i] = False                              #then adds to the clause a value False for this cell
                liste_clauses.append(dico0)                     #finally adds the clause to the set of clauses

        else:                                                   #if there is at least one tree in the column,

            # creates a list containing all the integers in [0,cote-1]
            liste_comb = []
            for nb in range(cote):
                liste_comb.append(nb)

            val_pos = int(cote) - int(ligne_ordonnee[i]) + 1    #corresponds to y-x+1 (see report)
            val_neg = int(ligne_ordonnee[i]) + 1                #corresponds to x+1 (see report)

            comb_pos = []                                       #creates an empty list for the positive literals
            comb_neg = []                                       #creates an empty list for the negative literals

            for elem_pos in combinations(liste_comb, val_pos):  #for each set of numbers in ((val_pos) among (size of the grid))
                comb_pos.append(elem_pos)                       #adds in comb_pos the values of the set of numbers

            for elem_neg in combinations(liste_comb, val_neg):  #for each set of numbers in ((val_neg) among (size of the grid))
                comb_neg.append(elem_neg)                       #adds in comb_neg the values of the set of numbers

            dico = {}                                           #initialises an empty dictionnary that will contain the clauses

            for comb in comb_pos:                               #for each element in comb_pos (which are set of numbers)
                for index in range(len(comb)):                  #for each index of the element
                    j = comb[index]                             #saves in j the value of the element at the index
                    dico[j, i] = True                           #adds a value True for the tup (j,i) in the dictionnary
                liste_clauses.append(dico)                      #adds the dictionnary (representing a clause) to the set of clauses
                dico = {}                                       #empties the dictionnary

            for comb in comb_neg:                               #for each set of numbers in comb_neg
                for index in range(len(comb)):                  #for each index of the element
                    j = comb[index]                             #saves in j the value of the element at the index
                    dico[j, i] = False                          #adds a value False for the tup (j,i) in the dictionnary
                liste_clauses.append(dico)                      #adds the dictionnary (representing a clause) to the set of clauses
                dico = {}                                       #empties the dictionnary


def creationClauses(cote,grille_arbres,ligne_abscisse,ligne_ordonnee): #WORKS
    liste_clauses = []                                      #creates an empty list that will represent the set of clauses

    regle1(cote,grille_arbres,liste_clauses)                #adds all the clauses defined by the first rule to the set of clauses
    regle2(cote,grille_arbres,liste_clauses)                #adds all the clauses defined by the second rule to the set of clauses
    regle4abscisse(cote,ligne_abscisse,liste_clauses)       #adds all the clauses defined by the fourth rule to the set of clauses (rows)
    regle4ordonnee(cote,ligne_ordonnee,liste_clauses)       #adds all the clauses defined by the fourth rule to the set of clauses (columns)

    return liste_clauses

def creationDimacs(cote,grille_arbres,liste_clauses,fichierDimacs): #WORKS
    f = open(fichierDimacs,"w")                                             #opens a file in writing mode

    f.write("p cnf " + str(cote**2) + " " + str(len(liste_clauses)) + "\n") #writes, in the file, the first line corresponding to the header
    for dico in liste_clauses:                                              #for each clause,
        int_from_tuple = sorted(list(grille_arbres.keys()))                 #int_from_tuple contains the tuples representing the coordinates of all grid cells
        for tup in int_from_tuple:                                          #for each cell
            if tup in dico:                                                 #if the cell (its coordinates) is in the list
                val = int_from_tuple.index(tup) + 1                         #then takes the number of the cell in the grid (not the coordinates) (the "+1" is here to have variables in [1,...] and not [0,...]
                if dico[tup] == False:                                      #if, in the clause, the boolean associated to the cell is False,
                    val = -val                                              #then takes the negative of the value (representing the negation here)
                f.write(str(val) + " ")                                     #and writes the final value in the file

        f.write("0\n")                                                      #writes, in the file, a 0 representing the end of the clause, and goes to a new line, representing the start of another clause
    f.close()                                                               #closes the file

def resultatFinal(cote,RESsat,RESfinal): #WORKS
    f = open(RESsat,"r")                                                    #opens the file containing the output of the SAT-Solver in reading mode

    sat = f.readline()                                                      #reads the first line to know whether the instance of the problem is satisfiable or not

    if sat[0]!="S":                                                         #if unsatisfiable, ...
        print("\nThe grid is unsatisfiable or the maximal number of iteration has been reached.\n")

    else:                                                                   #if satisfiable,
        g = open(RESfinal, "w")                                             #opens a file in writing mode (it will contain a model of the instance of the problem found by the SAT-Solver written in an understandable way)
        g.write("The solution is :\n\n")
        ligne_solution = f.readline()
        index = 0
        grille_solution = [[] for i in range(cote)]                         #initialises a list with 'cote' empty lists
        while ligne_solution.split()[index]!="0" and index<cote**2:         #while the character is not 0 (representing the end of the solution) and is not above the total number of variables,
            ind = (index)%cote                                              #allows the program to invert rows and columns to write the good result (i.e. column by column)
            grille_solution[ind].append(ligne_solution.split()[index])
            index +=1                                                       #iterates index

        for ligne in grille_solution:
            for var in ligne:
                if var[0]=="-":                                             #if the variable is negative,
                    g.write("0 ")                                           #then writes a 0 (meaning "there is no tent")
                else:                                                       #if the variable is not negative,
                    g.write("1 ")                                           #then writes a 1 (meaning "there is a tent")
            g.write("\n")                                                   #format

        g.write("\nRemember:\n0: there is no tent\n1: there is a tent\n\n")
        g.close()                                                           #closes the result file
        print("\nThe grid is satisfiable.\nOpen 'ResSat.sat' to see the model found by the SAT-Solver.\nOpen '"
                + RESfinal + "' to see the corresponding solution of the problem.\n")
    f.close()                                                               #closes the file containing the output of the SAT-Solver


def main(nomFichier): #WORKS

    fichierDimacs= "dimacs.cnf"

    if not isCorrect(nomFichier):
        exit(1)

    cote,nbArbres, ligne_abscisse,ligne_ordonnee,grille_arbres = lireFichierEnonce(nomFichier)

    creationDimacs(cote,grille_arbres,creationClauses(cote,grille_arbres,ligne_abscisse,ligne_ordonnee),fichierDimacs)
    return fichierDimacs

def afficherResultat(nomFichier,ResSat,RESfinal): #WORKS

    cote, nbArbres, ligne_abscisse, ligne_ordonnee, grille_arbres = lireFichierEnonce(nomFichier)
    resultatFinal(cote,ResSat,RESfinal)

