import random
import Heuristic

IterMAX = 1000000
proba = 10

def lirefichierDimacs(fichierDimacs): #WORKS
    f = open(fichierDimacs, "r")                                            #opens the dimacs file corresponding to the instance of the problem

    liste_clauses = []                                                      #creates an empty list for the set of clauses

    init = f.readline()
    nbClauses = int((init.split(" ")[len(init.split(" ")) - 1]).strip())    #reads the number of clauses in the header
    nbVar = int(init.split(" ")[len(init.split(" ")) - 2])                  #reads the number of variables in the header

    for i in range(nbClauses):                                              #for each clause of the file,
        ligne = f.readline()                                                #reads a line of the file representing a clause
        clause = []                                                         #creates a list representing a clause (empty at the beginning)
        splitted = ligne.split(" ")                                         #splitted is the list containing the variables of the clause of the file
        del splitted[len(splitted)-1]                                       #deletes the '0\n' representing the end of the clause
        for variable in splitted:                                           #for each variable in the clause of the file,
            clause.append(int(variable))                                    #adds the variable to the new clause
        liste_clauses.append(clause)                                        #adds the new clause to the set of clauses

    f.close()                                                               #closes the dimacs file corresponding to the instance of the problem

    return nbVar,nbClauses, liste_clauses

def creationAssignationRandom(nbVar): #WORKS
    assignation = []                                    #creates an empty list (representing an assignation, empty at the beginning)
    for i in range(1,nbVar+1):                          #for each variable,
        x = random.randint(0,1)                         #takes randomly x=0 or x=1

        if x==0:                                        #if x=0,
            assignation.append(-i)                      #the value of the variable in the assignation is False
        else:                                           #if x=1,
            assignation.append(i)                       #the value of the variable in the assignation is True
    return assignation

def isTrue(clause,assignation): #FINISHED
    for variable in clause:                             #for each variable of the clause,
        index = abs(variable)-1
        if assignation[index]*variable > 0:             #if the variable in the context of the assignation is True ( i.e. [var]_assignation = True )
            return True                                 #then the clause is True
    return False                                        #if none of the variables in the context of the assignation is True, then the clause is False


def isModel(assignation,liste_clauses): #FINISHED
    for clause in liste_clauses:                        #for each clause of the set of clauses
        if isTrue(clause,assignation) == False:         #if the clause is false,
            return False                                #then the assignation is not a model
    return True                                         #if none of the clauses is False, then the assignation is a model


def choisirClauseFausse(liste_clauses,assignation): #FINISHED
    listeChoix = []                                     #creates an empty list
    for clause in liste_clauses:                        #for each clause of the set of clauses,
        if not isTrue(clause,assignation):              #if the clause in the context of the assignation is False ( i.e. [clause]_assignation = False )
            listeChoix.append(clause)                   #then adds the clause to the list
    return listeChoix[random.randint(0,len(listeChoix)-1)]      #return a random clause of the list of clauses that are false in the assignation


def choisirVariableRandom(clause): #FINISHED
    return abs(clause[random.randint(0,len(clause)-1)])         #returns a random variable of the clause


def choisirVariableDeterministe(heuristic,clause,assignation,glob_counter_jw,glob_counter_moms,glob_counter_4): #FINISHED
    var = 0
    if int(heuristic)==1:
        var = Heuristic.methode1(clause,glob_counter_moms)

    if int(heuristic)==2:
        var = Heuristic.methode2(clause,glob_counter_jw)

    if int(heuristic)==3:
        var = Heuristic.methode3(clause,assignation)

    if int(heuristic)==4:
        var = Heuristic.methode4(clause,glob_counter_4)

    return var

def inverserDansAssignation(variable,assignation): #WORKS
    var2 = abs(variable) - 1
    assignation[var2] =  (-1)*assignation[var2]           #negates the value of the variable in the assignation
    return assignation

def main(heuristic,fichierDimacs,ResSat): #FINISHED
    f = open(ResSat,"w")                                                                    #opens a file in writing mode (this file will contain the result of the SAT-Solver)
    nbVar, nbClauses, liste_clauses = lirefichierDimacs(fichierDimacs)                      #reads the number of variables, the number of clauses and the set of clauses in the dimacs file

    assignation = creationAssignationRandom(nbVar)                                          #creates a random assignation
    compteurIteration = 0

    glob_counter_moms = []                                                                  #creates an empty counter for moms
    glob_counter_jw = []                                                                    #creates an empty counter for jw
    glob_counter_4 = []                                                                     #creates an empty counter for the forth heuristic

    for i in range(nbVar):                                                                  #nbVar times
        glob_counter_jw.append(0)                                                           #initialises the values at 0
        glob_counter_moms.append(0)                                                         #initialises the values at 0
        glob_counter_4.append(0)                                                            #initialises the values at 0

    for clause in liste_clauses:                                                            #for each clause C' in the set of clauses
        for var in clause:                                                                  #for each variable V' in the clause C'
            if len(clause)==1 or len(clause)==2:                                            #if the clause is short (arbitrarily, a short clause is a clause of size 1 or 2)
                glob_counter_moms[abs(var)-1] += 1                                          #adds 1 to the weight of the litteral corresponding to V'
            glob_counter_jw[abs(var)-1] += len(clause)                                      #adds the size of the clause to the weight of the litteral corresponding to V'


    while isModel(assignation,liste_clauses)==False and compteurIteration < IterMAX:        #while the assignation is not model and the counter of iteration is lesser than the maximum that we defined
        clause = choisirClauseFausse(liste_clauses,assignation)                             #chooses a clause (that is false in the assignation) in the set of clauses
        rand = random.randint(0,100)                                                        #takes a random integer in [0,100]
        if rand<=proba:                                                                     #if this random integer is lesser than our chosen value of P
            var = choisirVariableRandom(clause)                                             #chooses uniformly a random variable of the clause
        else:                                                                               #if this random integer is strictly greater than our chosen value of P
            # chooses deterministically a variable of the clause with the chosen heuristic
            var = choisirVariableDeterministe(heuristic,clause,assignation,glob_counter_jw,glob_counter_moms,glob_counter_4)

        assignation = inverserDansAssignation(var,assignation)                              #negates the value of the variable in the assignation
        compteurIteration += 1                                                              #iteration of the counter

    if isModel(assignation,liste_clauses)==True:                                            #if the assignation is a model of the instance of the problem
        f.write("SAT\n")                                                                    #then writes the header meaning "satisfiable" in the final result file
        for variable in assignation:                                                        #and for each variable in the assignation
            f.write(str(variable) + " ")                                                    #writes the variable in the final result file
        f.write(" 0")                                                                       #format

    else:                                                                                   #if the assignation is not a model of the instance of the problem
        f.write("UNSAT")                                                                    #then writes the header meaning "unsatisfiable" in the final result file
    print("Iteration count : " + str(compteurIteration) + ".\n")                            #prints the iteration count
    f.close()                                                                               #closes the file

    return compteurIteration
