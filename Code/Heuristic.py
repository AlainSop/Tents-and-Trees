import random

def methode1(clause,glob_counter_moms):
    counter = []                                        #creates an empty list of counters for weight of litterals
    for i in range(len(clause)):
        counter.append(0)                               #initialises the list of counters with zeros

    #computations of occurences of litterals in short clauses
    index = 0
    for variable in clause:                                     #for each variable V of the given clause C
        counter[index] += glob_counter_moms[abs(variable) - 1]  #adds the size of the clause to the weight of the litteral corresponding to V
        index += 1                                              #iterates the index to go through the given clause C

    #computation of the litteral with the highest number of occurences in short clauses
    max = 0                                             #initialises the heaviest weight at 0
    indexMax = 0                                        #initialises the index corresponding to the heaviest weight at 0

    for i in range(len(counter)):                       #for each index of the counter
        if counter[i] > max:                            #if the weight at this index is heavier than the current highest number of occurences in short clauses
            max = counter[i]                            #updates the highest number of occurences in short clauses
            indexMax = i                                #updates the index

    return clause[indexMax]                             #returns the litteral with the highest number of occurences in short clauses

def methode2(clause,glob_counter_jw):
    counter = []                                        #creates an empty list of counters for weight of litterals
    for i in range(len(clause)):
        counter.append(0)                               #initialises the list of counters with zeros

    #computations of weight of litterals
    index = 0
    for variable in clause:                                 #for each variable V of the given clause C
        counter[index] += glob_counter_jw[abs(variable)-1]  #adds the size of the clause to the weight of the litteral corresponding to V
        index += 1                                          #iterates the index to go through the given clause C

    min = 1000000
    indexMin = 0

    for id in range(len(counter)):                      #for each index of the counter
        curr = random.randint(0,counter[id])            #computes a random number in [0, weight of the variable]
        if curr < min :                                 #if the value at this index is smaller than the current smallest value
            min = curr                                  #updates the smallest value
            indexMin = id                               #updates the index

    return abs(clause[indexMin])                        #returns the litteral corresponding to the smallest value

def methode3(clause,assignation): #FINISHED
    listeChoix = []                                     #creates an empty list
    for variable in clause:                             #for each variable of the clause,
        index = abs(variable)-1
        if assignation[index]*variable < 0:             #if the variable in the context of the assignation is False ( i.e. [var]_assignation = False )
            listeChoix.append(variable)                 #adds the variable to the list

    return abs(listeChoix[random.randint(0, len(listeChoix) - 1)])  #returns a random variable of the list of variables that are false in the assignation

def methode4(clause,glob_counter_4):
    min = 1000000
    indexMin = 0
    for variable in clause:                             #for each variable of the clause,
        index = abs(variable)-1
        if glob_counter_4[index]<min:                   #if the value of the counter at this index is smaller than the current smallest value
            min = glob_counter_4[index]                 #updates the smallest value
            indexMin = clause.index(variable)           #updates the index

    glob_counter_4[abs(clause[indexMin])-1] += 1        #updates the number of switches of the variable that has been picked

    return abs(clause[indexMin])                        #returns the litteral corresponding to the smallest value