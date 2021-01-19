
def clauseTo3clause(clause,fichierDimacs3SAT,compteurVar,compteurClauses): #WORKS
    g = open(fichierDimacs3SAT, "a")                                                    #open a file in add mode (this file will contain all the clauses converted to size 3)

    taille_clause = len(clause.split(" ")) -1                                           #takes the size of the clause

    if taille_clause == 1:                                                              #if the size of the clause is 1, we need to add two additional variables x and y
        compteurVar +=1
        x = str(compteurVar)
        compteurVar +=1
        y = str(compteurVar)

        #writes the new collection C' in the file : for exemple if the clause is {z1}, C' = {{z1, x, y}, {z1, x, -y}, {z1, -x, y}, {z1, -x, -y}}
        g.write(clause.split()[0] + " " + x + " " + y + " 0\n")                         #writes {z1, x, y} as a clause in the file
        g.write(clause.split()[0] + " " + x + " -" + y + " 0\n")                        #writes {z1, x, -y} as a clause in the file
        g.write(clause.split()[0] + " -" + x + " " + y + " 0\n")                        #writes {z1, -x, y} as a clause in the file
        g.write(clause.split()[0] + " -" + x + " -" + y + " 0\n")                       #writes {z1, -x, -y} as a clause in the file
        compteurClauses += 3                                                            #adds 3 to the number of clauses (one clause is transformed into 4 clauses)

    if taille_clause == 2:                                                              #if the size of the clause is 2, we need to add one additional variable x
        compteurVar += 1
        x = str(compteurVar)

        # writes the new collection C' in the file : for exemple if the clause is {z1,z2}, C' = {{z1, z2, x},{z1, z2, -x}}
        g.write(clause.split()[0] + " " + clause.split()[1] + " " + x + " 0\n")         #writes {z1, z2, x} as a clause in the file
        g.write(clause.split()[0] + " " + clause.split()[1] + " -" + x + " 0\n")        #writes {z1, z2, -x} as a clause in the file
        compteurClauses += 1


    if taille_clause == 3:                                                              #if the size of the clause is 3, no need to add any variable
        g.write(clause.split()[0] + " " + clause.split()[1] + " " + clause.split()[2] + " 0\n")     #writes the (unchanged) clause in the file

    if taille_clause > 3:                                                               #if the size of the clause is k, we need to add k-3 additional variables

        compteurVar += 1
        x = str(compteurVar)
        g.write(clause.split()[0] + " " + clause.split()[1] + " " + x + " 0\n")         #writes {z_1, z_2, y_1} as a clause in the file
        iter = 2

        for i in range(taille_clause-4):                                                #for i in [0,k-5]
            compteurVar += 1
            y = str(compteurVar)                                                        #adds an additional variable

            g.write("-" + x + " " + clause.split()[iter] + " " + y + " 0\n")            #writes {-y_i, z2, y_i+1} as a clause in the file

            x = y
            iter += 1

        g.write("-" + x + " " + clause.split()[iter] + " " + clause.split()[iter+1] + " 0\n")   #finally writes {y_(k-3), z_(k-1), z_k} as a clause in the file

        compteurClauses += taille_clause -3                                             #adds k-3 clauses to the number of clauses

    g.close()                                                                           #closes the file containing all the clauses converted to size 3
    return compteurVar, compteurClauses


def satTo3sat(fichierDimacs,fichierDimacs3SAT): #WORKS
    f = open(fichierDimacs, "r")                                                        #opens the dimacs file containing the clauses representing the instance of the problem
    g = open(fichierDimacs3SAT, "w")                                                    #opens a file to write the dimacs file with clauses of size 3

    init = f.readline()
    nbClauses = int((init.split(" ")[len(init.split(" ")) - 1]).strip())                #takes the initial number of clauses
    compteurVar = int(init.split(" ")[len(init.split(" ")) - 2])                        #takes the initial number of variables
    compteurClauses = nbClauses                                                         #counter of clauses

    for i in range(nbClauses):                                                          #for each clause,
        clause = f.readline()
        compteurVar,compteurClauses = clauseTo3clause(clause,fichierDimacs3SAT,compteurVar,compteurClauses)    #transforms the clause into a clause of size 3

    firstLine = "p cnf " + str(compteurVar) + " " + str(compteurClauses) + "\n"         #defines the header with the new values of number of variables and number of clauses

    fichierTmp = open(fichierDimacs3SAT, "r")                                           #opens the file containing the 3-clauses
    total = firstLine + fichierTmp.read()                                               #merges the header with the 3-clauses
    fichierTmp.close()                                                                  #closes the file containing the 3-clauses

    fichierFinal = open(fichierDimacs3SAT, "w")                                         #opens a file in writing mode
    fichierFinal.write(total)                                                           #writes, in the file, the final 3-clauses dimacs file
    fichierFinal.close()                                                                #closes the final file

    g.close()                                                                           #closes the file
    f.close()                                                                           #closes the file

