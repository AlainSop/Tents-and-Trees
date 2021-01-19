#!/usr/bin/env python3

#imports all the files and elements of the system needed
import sys
import subprocess
import Clauses
import Transformation3Sat
import Walksat
import Entree

def my_main(my_args):
    trys = 1

    nomFichier = my_args[1]                                             #stores the first argument as the file representing the instance of the problem
    if nomFichier.lower()=="input":                                     #if the first argument is "input",
        nomFichier = Entree.EntreeEtVerif("Input.txt")                  #guides the user through the input of a file and stores this file

    fichierDimacs = Clauses.main(nomFichier)                            #creates the dimacs file corresponding to the instance of the problem

    ResSat = "ResSat.sat"                                               #names the file that will contain the result of the SAT-Solver
    if len(my_args)!=4 and len(my_args)!=5:                             #if there are not 3 or 4 arguments,
        print("\nUse of the program :\n./main.py <problem-file> <final-result-file> <sat-solver> <sat-To-3-Sat>\n"
              "The <SAT-solver> can be 'minisat' or 'walksat'.\nIf <sat-To-3-Sat> is not empty, all the clauses will be of length 3.\n")
        return exit(1)                                                  #exits the program

    iterations = 0
    if my_args[3].lower() == "walksat":                                 #if the third argument is walksat
        #choice of the heuristic
        heuristic = input("Choice of heuristic for Walksat:\n1 : MOMS\n2 : JW\n3 : based on the value of variables in assignation\n4 : based on the number of switches of every variable\nEnter 1,2,3 or 4 : ")
        while heuristic != "1" and heuristic != "2" and heuristic != "3" and heuristic != "4":
            heuristic = input("You have to enter 1,2,3 or 4 : ")

    for i in range(trys):
        if len(my_args)==5:                                                 #if there are 4 arguments (i.e. <sat-To-3-Sat> is not empty)
            Transformation3Sat.satTo3sat(fichierDimacs, "dimacs3Sat.txt")   #then transforms the set of clauses into set of clauses of length 3

            if my_args[3].lower() == "minisat":                             #if the third argument is minisat
                subprocess.run([my_args[3], "dimacs3Sat.txt", ResSat])      #runs minisat on the 3-clauses dimacs file, the input is stored in the file "ResSat.sat"

            elif my_args[3].lower() == "walksat":                           #if the third argument is walksat

                iterations += Walksat.main(heuristic,"dimacs3Sat.txt", ResSat)            #runs walksat on the 3-clauses dimacs file, the input is stored in the file "ResSat.sat"

            Clauses.afficherResultat(nomFichier,ResSat,my_args[2])          #writes a model of the instance of the problem found by the SAT-Solver in an understandable way
                                                                            #(in the file chosen by the user for <final-result-file>)

        else:                                                               #if there are not 4 arguments (i.e. there are 3)
            if my_args[3].lower() == "minisat":                             #if the third argument is minisat
                subprocess.run([my_args[3], fichierDimacs, ResSat])         #runs minisat on the dimacs file, the input is stored in the file "ResSat.sat"

            elif my_args[3].lower() == "walksat":                           #if the third argument is walksat

                iterations += Walksat.main(heuristic,fichierDimacs, ResSat)               #runs walksat on the dimacs file, the input is stored in the file "ResSat.sat"

            Clauses.afficherResultat(nomFichier,ResSat,my_args[2])          #writes a model of the instance of the problem found by the SAT-Solver in an understandable way
                                                                            #(in the file chosen by the user for <final-result-file>)

    mean = float(iterations)/float(trys)
    print("Total iterations on " + str(trys) + " trys : " + str(iterations) + ".\nMean = " + str(mean) + ".\n")

if __name__ == '__main__' :                                             #macro that allows the user to execute ./main.py
    my_main(sys.argv)