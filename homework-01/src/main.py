#!/usr/bin/env python3

import sys
import pandas

"""
.\program <L> <K> <training-set> <validation-set> <test-set> <to-print>
L: integer (used in the post-pruning algorithm)
K: integer (used in the post-pruning algorithm)
to-print:{yes,no}
"""

# input_string = ['D:/_PROJECTS/machine-learning-class/homework-01/src/main.py', '2', '5', 'training_set.csv', 'validation_set.csv', 'test_set.csv', 'yes']
# print(input_string)
# inputs = input_string.split(" ")

#print(sys.argv)

def initalize():
    L = sys.argv[1]
    K = sys.argv[2]
    training_set_path = sys.argv[3]
    validation_set_path = sys.argv[4]
    test_set_path = sys.argv[5]
    to_print_input = sys.argv[6]

    training_set = pandas.read_csv(training_set_path)
    validation_set = pandas.read_csv(validation_set_path)
    test_set = pandas.read_csv(test_set_path)

    if to_print_input == "yes":
        to_print = True
    elif to_print_input == "no":
        to_print = False
    else:
        print("to-print must be 'yes' or 'no', printing anyway")
        to_print = True

def node_formation(df):
    # recursive function which drills down until a pure node is returned
    # no promises, but I think this recursive structure should work

    count_01 = {}
    for attribute in df.loc[:, df.columns != 'Class']:
        zeros = (df[attribute] == 0).sum()
        ones = (df[attribute] == 1).sum()
        count_01[attribute] = (zeros, ones)

    # Send dictionary for variance comparison
    # That returns the attribute to form a node on ... the lowest value?

    # If value > 0:
    #    branch_0 = node_formation(df[df[returned_attribute] == 0])
    #    branch_1 = node_formation(df[df[returned_attribute] == 1])
    #    return {node: {0: branch_0, 1: branch_1}}
        
    # else: # value was 0, set as pure_node with outcome
    #    return {pure_node: leaf}
        # pure_node is an attribute "X_"
        # leaf is 0 or 1


if __name__=="__main__":
initialize()
node_formation(training_set)

#print("L: {}".format(L))
#print("K: {}".format(K))
#print("Training Set: \n{}".format(training_set))
#print("Validation Set: \n{}".format(validation_set))
#print("Test Set: \n{}".format(test_set))
#print("To Print: {}".format(str(to_print)))
