import os, sys, time, random
import numpy as np
from pathlib import Path

from Utilities.Parser import *


random.seed(os.urandom(10))  # Best Random seed

''' I am trying to automize everything. Let's Hope it is faster '''
''' Using many parts from SimpleBool package '''
'''I am using Class which makes I think makes my life a lot easier. Let's See'''
''' Using Class for these operations is a terible Idea. Never do it!!! '''
'''I hope Iron Man is with me throughout the Journey'''

# global variables. Nodes record names of all nodes. InterMat record edge
# weights of all the interactions
global NODES, INTERMAT

if __name__ == '__main__':
    #sys.argv is the list of all arguments you give in the terminal, i.e., command line, like python 'name of the file' 'other args'
    #so sys.argv is list of 'name of the file' and 'other args'
    #sys.argv[0] is the name of the program.
    if sys.argv[1]:
        in_file = sys.argv[1] #Either you can give the name of the file (Remember, not zero as zero means name of python file)
    else:
        in_file = 'bool.in' #Or it takes in the default file

    Rand_weigh = [False,True]; Runs_num = 10

    for run_num in range(1,Runs_num+1):
        print(f'Run No.:{run_num}')
        for rand_weigh in Rand_weigh:
            #takes the sim params from the input file 
            INPUT = InputParser(in_file)
            #spits out the initial nodes and inter_mat 
            NODES, INTERMAT = ReadRules(INPUT['network'], INPUT['model'],rand_weigh=rand_weigh)
            #self-explanatory
            IniState, FixedState, TurnState = PreDefine(INPUT, NODES)

            output_file = INPUT['network'] #Create a folder with network name

            if INPUT['mode'] == 'Sync':
                from Methods.Sync import SummarySync
                SummarySync(
                    NODES, INTERMAT,
                    INPUT, IniState,
                    FixedState, TurnState,
                    folder=output_file,rand_weigh=rand_weigh)
                print("All the analysis is done. Bye ;)")
            elif INPUT['mode'] == 'Async':
                from Methods.Async import SummaryAsync
                SummaryAsync(
                    NODES, INTERMAT,
                    INPUT, IniState,
                    FixedState, TurnState,
                    folder=output_file,rand_weigh=rand_weigh,run_num=run_num)
                print("All the analysis is done. Bye ;)")
